from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Import routes and database connection
# Adjusted for correct imports relative to Vercel’s /api directory
from app.routes import weather
from app.db.database import connect_to_mongo, close_mongo_connection

# Initialize FastAPI app
app = FastAPI(title="Weather Insight Dashboard API")

# Configure CORS (for both local and production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://weather-live-dashboard.vercel.app",
        "http://localhost:5173",  # local frontend
        "*"  # fallback for safety
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database event handlers
@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_event():
    await close_mongo_connection()

# Include routes
app.include_router(weather.router, prefix="/api", tags=["weather"])

# Health check root route
@app.get("/")
def read_root():
    return {"message": "✅ Weather Insight Dashboard API is running successfully!"}
