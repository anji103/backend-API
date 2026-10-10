from redis.asyncio import Redis
import redis.asyncio as redis
from fastapi import Request
from pyrate_limiter import Duration, Limiter, Rate, RedisBucket
from fastapi_limiter.depends import RateLimiter


from app.core.config import settings


async def key_func(request: Request) -> str:
    """
    Custom key function for rate limiting.
    Uses user_id if authenticated, otherwise fallback to client IP.
    """
    # Check if user_id is injected in request.state (if you set it in a middleware)
    # Or check if it's available via previous dependencies.
    # For now, we check if there's a user object in request.state
    user_id = getattr(request.state, "user_id", None)
    if user_id:
        return f"rate_limit:{user_id}"

    # Fallback to IP
    forwarded = request.headers.get("X-Forwarded-For")
    if forwarded:
        return f"rate_limit:{forwarded.split(',')[0]}"
    return f"rate_limit:{request.client.host if request.client else 'unknown'}"

async def init_limiter(rates: list[Rate], bucket_key: str) -> RateLimiter:
    """Initialise FastAPILimiter with Redis."""
    redis = Redis.from_url(
        settings.REDIS_URL,
        decode_responses=True,
    )

    bucket = await RedisBucket.init(
        rates=rates,
        redis=redis,
        bucket_key=bucket_key,
    )

    limiter = Limiter(bucket)

    return RateLimiter(limiter=limiter, identifier=key_func)
