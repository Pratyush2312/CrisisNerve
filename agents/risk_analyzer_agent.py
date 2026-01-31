class RiskAnalyzerAgent:
    def analyze(self, zone):
        score = 0
        reasons = []

        if zone["rainfall_mm"] > 150:
            score += 3
            reasons.append(f"Heavy rainfall detected: {zone['rainfall_mm']} mm")

        if zone["river_level_m"] > 5:
            score += 4
            reasons.append(f"River level critical: {zone['river_level_m']} m")

        if zone["population_density"] > 20000:
            score += 2
            reasons.append(
                f"High population density: {zone['population_density']} people/km²"
            )

        if score >= 7:
            level, color = "CRITICAL", "RED"
        elif score >= 4:
            level, color = "HIGH", "ORANGE"
        else:
            level, color = "MODERATE", "YELLOW"

        return {
            "risk_score": score,
            "risk_level": level,
            "zone_color": color,
            "reasons": reasons,   # 👈 NEW
        }
