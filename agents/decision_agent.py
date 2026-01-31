class DecisionAgent:
    def decide(self, risk):
        if risk["risk_level"] == "CRITICAL":
            return "IMMEDIATE EVACUATION"
        elif risk["risk_level"] == "HIGH":
            return "PREPARE RESCUE TEAMS"
        else:
            return "MONITOR SITUATION"
