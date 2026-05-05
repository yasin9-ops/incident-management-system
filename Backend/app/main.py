import asyncio
from app.utils.metrics import get_rate
from fastapi import FastAPI, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from starlette.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router

limiter = Limiter(key_func=get_remote_address)

app = FastAPI(title="Incident Management System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, lambda request, exc: JSONResponse(
    status_code=429,
    content={"error": "Too many requests"}
))
app.add_middleware(SlowAPIMiddleware)

app.include_router(router)

@app.get("/")
def health():
    return {"status": "IMS running 🚀"}

@app.on_event("startup")
async def start_metrics_logger():
    async def log_metrics():
        while True:
            print(f"Signals/sec: {get_rate():.2f}")
            await asyncio.sleep(5)

    asyncio.create_task(log_metrics())