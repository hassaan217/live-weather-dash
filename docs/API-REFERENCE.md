# API Reference

Base URL: http://localhost:8000

## Endpoints

GET /api/weather
- Query Params: q (string, required) — location query (city name, or "lat,lon")
- 200 Response
```
{
  "location": { "name": "City", "country": "US", "lat": 0, "lon": 0 },
  "current": { "temp": 0, "humidity": 0, "wind": 0, "condition": "Clear", "icon": "01d" },
  "forecast": [ { "dt": 0, "temp": 0, "humidity": 0, "wind": 0, "precipitation": 0 }, ... ],
  "insights": { "riskAlerts": [], "kpis": {} }
}
```
- Errors: 400 (bad input), 502 (upstream), 500 (server)

GET /api/search/recent
- 200 Response: `[ { q, timestamp }, ... ]`

POST /api/export
- Body: `{ format: "csv" | "json", data: any }`
- Response: file download or link

Notes
- See backend/app/routes/weather.py for actual route names and schemas.
- CORS: configured in backend/app/main.py.
