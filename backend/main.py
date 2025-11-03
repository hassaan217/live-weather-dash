# # app/main.py
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from app.routes import weather
# from app.db.database import connect_to_mongo, close_mongo_connection

# app = FastAPI(title="Weather Insight Dashboard API")

# # Configure CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[
#         "https://weather-live-dashboard.vercel.app",
#         "http://localhost:5173",  # for local dev
#         "*"  # fallback for any other environment
#     ],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Add event handlers for MongoDB connection
# app.add_event_handler("startup", connect_to_mongo)
# app.add_event_handler("shutdown", close_mongo_connection)

# # Include routes
# app.include_router(weather.router, prefix="/api", tags=["weather"])

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to Weather Insight Dashboard API"}



# main.py

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import connect_to_mongo, close_mongo_connection, get_db
import httpx

app = FastAPI(title="Weather Insight Dashboard API")

# Allow frontend (e.g., localhost or Vercel) access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change to specific origin later for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Startup and shutdown
app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_mongo_connection)

# Test route
@app.get("/")
def root():
    return {"message": "Welcome to Weather Insight Dashboard API"}

# Weather route
@app.get("/api/weather/current")
async def get_weather(city: str = Query(..., description="City name to fetch weather for")):
    """Fetch current weather for a given city."""
    try:
        # Example: if you're fetching weather from an external API
        url = f"https://api.open-meteo.com/v1/forecast?latitude=24.8607&longitude=67.0011&current_weather=true"
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            data = response.json()
        
        # Example: store weather in MongoDB
        db = get_db()
        db.weather_data.insert_one({"city": city, "data": data})
        
        return {"city": city, "weather": data}
    
    except Exception as e:
        print(f"❌ Error fetching weather: {e}")
        return {"error": "Failed to fetch weather data"}

