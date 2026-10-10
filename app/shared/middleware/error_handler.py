from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException


async def http_exception_handler(
    _request: Request,
    exc: StarletteHTTPException,
) -> JSONResponse:
    """Converts FastAPI/Starlette HTTP exceptions into the standard error envelope."""
    error_code = f"HTTP_{exc.status_code}"
    if exc.status_code == 429:
        error_code = "RATE_LIMIT_EXCEEDED"

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": {
                "code": error_code,
                "message": exc.detail or "An error occurred",
            },
        },
    )


async def validation_exception_handler(
    _request: Request,
    exc: RequestValidationError,
) -> JSONResponse:
    """Converts Pydantic validation errors into the standard error envelope."""
    errors = exc.errors()
    # Surface the first human-readable message as the top-level message
    first_message = errors[0]["msg"] if errors else "Validation error"
    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "error": {
                "code": "VALIDATION_ERROR",
                "message": first_message,
                "details": errors,
            },
        },
    )
