from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.weather import weather_router
from routes.geo import geo_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(weather_router, prefix="/api/weather")
app.include_router(geo_router, prefix="/api/geo")

@app.get("/api")
def root():
    return {"message": "API is working"}
