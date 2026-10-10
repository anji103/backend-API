from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException
from pyrate_limiter import Duration, Rate

from app.core.config import settings
from app.modules.auth.router import router as auth_router
from app.modules.users.router import router as users_router
from app.core.limiter import init_limiter
from app.core.dependencies import get_global_rate_limiter
from app.shared.middleware.error_handler import (
    http_exception_handler,
    validation_exception_handler,
)


# ── Lifespan ──────────────────────────────────────────────────────────────────
@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    # Startup: initialise connections, warm caches, etc.
    app.state.global_rate_limiter = await init_limiter(
        rates=[
            Rate(settings.RATE_LIMIT_GLOBAL_TIMES, Duration.SECOND * settings.RATE_LIMIT_GLOBAL_SECONDS),
        ],
        bucket_key="api-rate-limit",
    )

    app.state.auth_rate_limiter = await init_limiter(
        rates=[
            Rate(settings.RATE_LIMIT_AUTH_TIMES, Duration.SECOND * settings.RATE_LIMIT_AUTH_SECONDS),
        ],
        bucket_key="auth-rate-limit",
    )
    yield
    # Shutdown: close connections, flush buffers, etc.
    # Shutdown: close connections, flush buffers, etc.

# ── Application ───────────────────────────────────────────────────────────────
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
    lifespan=lifespan,
    # Only expose interactive docs in debug/development
    docs_url="/api/docs" if settings.DEBUG else None,
    redoc_url="/api/redoc" if settings.DEBUG else None,
    openapi_url="/api/openapi.json" if settings.DEBUG else None,
    dependencies=[Depends(get_global_rate_limiter)],
)

# ── Middleware ────────────────────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Tighten in production via env
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Exception Handlers ────────────────────────────────────────────────────────
app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)

# ── Routers ───────────────────────────────────────────────────────────────────
API_PREFIX = "/api/v1"

app.include_router(auth_router, prefix=API_PREFIX)
app.include_router(users_router, prefix=API_PREFIX)


# ── Health Check ──────────────────────────────────────────────────────────────
@app.get("/health", tags=["Health"], summary="Service health check")
async def health() -> dict:
    return {"status": "ok", "version": settings.APP_VERSION, "env": settings.ENV}
