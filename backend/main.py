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



import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "app"))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import weather
from db.database import connect_to_mongo, close_mongo_connection

app = FastAPI(title="Weather Insight Dashboard API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://weather-live-dashboard.vercel.app",
        "http://localhost:5173",
        "*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB handlers
app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_mongo_connection)

# Include routes
app.include_router(weather.router, prefix="/api", tags=["weather"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Weather Insight Dashboard API"}


# # if __name__ == "__main__":
# #     import uvicorn
# #     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
