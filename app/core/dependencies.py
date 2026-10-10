from fastapi import Depends, HTTPException, status, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.core.security import decode_access_token

_bearer = HTTPBearer(auto_error=True)


def get_current_user_id(
    request: Request,
    credentials: HTTPAuthorizationCredentials = Depends(_bearer),
) -> str:
    """
    FastAPI dependency — extracts and validates the JWT Bearer token.

    Returns the user UUID string (the ``sub`` claim).
    Raises HTTP 401 on any token error.
    """
    try:
        payload = decode_access_token(credentials.credentials)
        user_id: str | None = payload.get("sub")
        if not user_id:
            raise ValueError("Missing sub claim")
        
        # Inject into request state for other dependencies (like limiter)
        request.state.user_id = user_id
        
        return user_id
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        ) from exc


def get_auth_rate_limiter(request: Request) -> RateLimiter:
    return request.app.state.auth_rate_limiter


def get_global_rate_limiter(request: Request) -> RateLimiter:
    return request.app.state.global_rate_limiter
