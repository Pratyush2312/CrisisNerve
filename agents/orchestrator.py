from agents.collector_agent import CollectorAgent
from agents.risk_analyzer_agent import RiskAnalyzerAgent
from agents.decision_agent import DecisionAgent
from agents.resource_planner_agent import ResourcePlannerAgent

class Orchestrator:
    def run(self):
        collector = CollectorAgent()
        zones = collector.collect()
        return self._process(zones)

    def run_with_custom_data(self, zones):
        return self._process(zones)

    def _process(self, zones):
        analyzer = RiskAnalyzerAgent()
        decision = DecisionAgent()
        resource_planner = ResourcePlannerAgent()

        results = []

        for z in zones:
            risk = analyzer.analyze(z)
            action = decision.decide(risk)
            resources = resource_planner.allocate(z, risk)

            results.append({
                "zone": z["zone"],
                "lat": z["lat"],
                "lon": z["lon"],
                "risk": risk,
                "recommended_action": action,
                "resources": resources,
                "rainfall_mm": z["rainfall_mm"],
                "reasoning": risk["reasons"]
            })


        return results
