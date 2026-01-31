class ResourcePlannerAgent:
    def allocate(self, zone, risk):
        if risk["risk_level"] == "CRITICAL":
            return {
                "boats": 10,
                "ambulances": 5,
                "helicopters": 2
            }
        elif risk["risk_level"] == "HIGH":
            return {
                "boats": 5,
                "ambulances": 3,
                "helicopters": 1
            }
        else:
            return {
                "boats": 2,
                "ambulances": 1,
                "helicopters": 0
            }
