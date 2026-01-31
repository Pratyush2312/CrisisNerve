import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from fastapi import FastAPI
from datetime import datetime
from agents.collector_agent import CollectorAgent
from agents.orchestrator import Orchestrator


app = FastAPI(title="Disaster AI Coordinator")
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "Disaster AI Coordinator Backend is Running 🚨",
        "time": datetime.now()
    }


@app.get("/analyze")
def analyze():
    orch = Orchestrator()
    return orch.run()

@app.get("/health")
def health_check():
    return {"status": "OK"}

# Example dummy endpoint for zones
@app.get("/zones")
def get_zones():
    return [
        {"zone": "Zone A", "risk": "High", "type": "Flood"},
        {"zone": "Zone B", "risk": "Medium", "type": "Fire"},
        {"zone": "Zone C", "risk": "Low", "type": "Normal"}
    ]



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run("backend.app.main:app", host="0.0.0.0", port=port)