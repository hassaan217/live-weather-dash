# Setup and Installation

## Prerequisites
- OS: Windows, macOS, or Linux
- RAM: 4GB+ (8GB recommended)
- Node.js: v14+ (LTS recommended)
- npm: v6+ (bundled with Node.js)
- Python: 3.8+
- Git
- Browser: Chrome, Firefox, Safari, or Edge
- Accounts: OpenWeatherMap API key, MongoDB Atlas (optional)

## Clone
```bash
git clone <repo-url>
cd live dash
```

## Backend
```bash
cd backend
python -m venv .venv
# Windows
.venv\Scripts\activate
pip install -r app/requirements.txt
# Run
uvicorn app.main:app --reload --port 8000
```
Configure backend/.env (API keys, DB URIs). See backend/README.md.

## Frontend
```bash
# New terminal
cd frontend
npm install
npm run dev
```

## Configuration
- Frontend base API URL: src/services/api.js
- Backend CORS: app/main.py (allow frontend origin)

## Build
- Frontend: npm run build → dist/
- Backend: run with production ASGI server behind a reverse proxy

## Troubleshooting
- Clear Vite cache: delete node_modules/.vite
- Verify environment variables and API keys
- Check browser console and backend logs for errors
