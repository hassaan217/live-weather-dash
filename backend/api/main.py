from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Import routes and database connection
from app.routes import weather
from app.db.database import connect_to_mongo, close_mongo_connection

# Initialize FastAPI app
app = FastAPI(title="Weather Insight Dashboard API")

# Configure CORS for both local and production
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://weather-live-dashboard.vercel.app",
        "http://localhost:5173",  # Local dev
        "*"  # fallback
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database connection events
@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_event():
    await close_mongo_connection()

# Register routes
app.include_router(weather.router, prefix="/api", tags=["weather"])

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "✅ Weather Insight Dashboard API is running successfully!"}
