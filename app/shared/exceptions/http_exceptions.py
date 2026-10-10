from fastapi import HTTPException, status


class NotFoundException(HTTPException):
    def __init__(self, message: str = "Resource not found") -> None:
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=message)


class UnauthorizedException(HTTPException):
    def __init__(self, message: str = "Unauthorized") -> None:
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=message,
            headers={"WWW-Authenticate": "Bearer"},
        )


class ForbiddenException(HTTPException):
    def __init__(self, message: str = "Forbidden") -> None:
        super().__init__(status_code=status.HTTP_403_FORBIDDEN, detail=message)


class ConflictException(HTTPException):
    def __init__(self, message: str = "Conflict") -> None:
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail=message)


class BadRequestException(HTTPException):
    def __init__(self, message: str = "Bad request") -> None:
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=message)


class UnprocessableEntityException(HTTPException):
    def __init__(self, message: str = "Unprocessable entity") -> None:
        super().__init__(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=message)


class RateLimitException(HTTPException):
    def __init__(self, message: str = "Too many requests. Please slow down.") -> None:
        super().__init__(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail=message)
