# app/db/database.py

import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = None
db = None

def connect_to_mongo():
    """Connect to MongoDB (safe for Vercel serverless)."""
    global client, db
    try:
        if not MONGO_URI:
            print("⚠️  MONGO_URI not set — skipping MongoDB connection.")
            return
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        db = client["weather"]
        client.admin.command("ping")  # verify connection
        print("✅ Connected to MongoDB successfully.")
    except Exception as e:
        print(f"❌ Failed to connect to MongoDB: {e}")

def close_mongo_connection():
    """Close MongoDB connection."""
    global client
    if client:
        client.close()
        print("🔒 MongoDB connection closed.")

def get_db():
    """Get active database instance."""
    global db
    if db is None:
        raise Exception("MongoDB not connected")
    return db
