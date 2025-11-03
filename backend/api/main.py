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

# Configure CORS properly
origins = [
    "https://weather-live-dashboard.vercel.app",
    "http://localhost:5173",
    "http://localhost:3000",  # Add common dev ports
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

# Alternative: If you need to allow all origins during development
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Use this temporarily for testing
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

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

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}
