from datetime import UTC, datetime, timedelta

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
import jwt

from app.core.config import settings

# ── Password Hashing (Argon2id) ───────────────────────────────────────────────
_ph = PasswordHasher()


def hash_password(plain: str) -> str:
    """Return an Argon2id hash of *plain*."""
    return _ph.hash(plain)


def verify_password(plain: str, hashed: str) -> bool:
    """Return True if *plain* matches *hashed*. Never raises."""
    try:
        return _ph.verify(hashed, plain)
    except VerifyMismatchError:
        return False


# ── JWT (RS256) ───────────────────────────────────────────────────────────────
def create_access_token(subject: str, extra: dict | None = None) -> str:
    """Create a short-lived RS256 access token for *subject* (user UUID)."""
    now = datetime.now(UTC)
    payload: dict = {
        "sub": subject,
        "iat": now,
        "exp": now + timedelta(minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES),
        "type": "access",
        **(extra or {}),
    }
    return jwt.encode(
        payload,
        settings.JWT_PRIVATE_KEY.replace("\\n", "\n"),
        algorithm=settings.JWT_ALGORITHM,
    )


def decode_access_token(token: str) -> dict:
    """Decode and verify an RS256 access token. Raises jwt.InvalidTokenError on failure."""
    return jwt.decode(
        token,
        settings.JWT_PUBLIC_KEY.replace("\\n", "\n"),
        algorithms=[settings.JWT_ALGORITHM],
    )
