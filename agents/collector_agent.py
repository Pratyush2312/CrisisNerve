import requests

class CollectorAgent:
    def get_rainfall(self, lat, lon):
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=rain"
        try:
            res = requests.get(url, timeout=5).json()
            rain = res["hourly"]["rain"][-1]  # latest value
            return max(rain * 50, 120) # scale for demo visibility
        except:
            return 100  # fallback

    def collect(self):
        zones = [
            {"zone": "Kolkata", "lat": 22.5726, "lon": 88.3639, "river_level_m": 5.3, "population_density": 24000},
            {"zone": "Patna", "lat": 25.5941, "lon": 85.1376, "river_level_m": 4.6, "population_density": 18000},
            {"zone": "Guwahati", "lat": 26.1445, "lon": 91.7362, "river_level_m": 6.1, "population_density": 9000},
        ]

        for z in zones:
            z["rainfall_mm"] = self.get_rainfall(z["lat"], z["lon"])

        return zones
