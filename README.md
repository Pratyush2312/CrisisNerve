# 🌍 Disaster AI Coordinator

An AI-powered disaster response dashboard that uses live weather data, multi-agent reasoning, and smart resource allocation to help authorities decide **where** and **how** to act during emergencies.

---

## 🚨 Problem

During floods and disasters, authorities are overwhelmed with scattered data but lack **decision clarity**:

- Which area is most critical?
- What action should be taken?
- How should rescue resources be deployed?

---

## 🤖 Our Solution

This system acts as an **AI decision-support co-pilot** that:

- Monitors live rainfall data from weather APIs
- Analyzes risk using multiple environmental factors
- Provides recommended actions (Evacuate / Monitor)
- Allocates rescue resources (boats, ambulances, helicopters)
- Shows **AI reasoning** behind every decision

---

## 🧠 AI Agent Architecture

The backend is designed using multiple AI-style agents:

| Agent | Responsibility |
|------|-----------------|
| Collector Agent | Fetches live rainfall data |
| Risk Analyzer Agent | Computes risk score using rainfall, river level, population |
| Decision Agent | Determines evacuation or monitoring action |
| Resource Planner Agent | Allocates rescue resources |
| Orchestrator | Coordinates all agents |

---

## 🗺 Features

- Interactive disaster risk map
- Live alert sidebar with resource allocation
- AI reasoning panel (why a zone is critical)
- Responsive UI for all screen sizes
- Auto-refreshing real-time analysis
- Live weather API integration

---

## 🛠 Tech Stack

### Frontend
- React
- Tailwind CSS
- React Leaflet (Map)

### Backend
- FastAPI (Python)
- Requests (Weather API)

### Data Source
- Open-Meteo Weather API

---

## ⚙ How to Run Locally

### Backend

```bash
pip install -r requirements.txt
uvicorn backend.app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```
---

## 🌧 Live Data
The system pulls real-time rainfall data from the Open-Meteo API and continuously updates risk calculations.

---
## 🎯Goal
This is not just a dashboard.
This is an AI-powered disaster response assistant to support faster, smarter decisions when every minute matters.

---
## 👨‍💻 Team
- Pratyush Singh
- Aditya Dev
