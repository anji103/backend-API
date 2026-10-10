"""
Auth Repository
===============
All database access for the auth module lives here.
Services MUST NOT use the session directly.
"""

from sqlalchemy.ext.asyncio import AsyncSession


class AuthRepository:
    """
    Handles all database operations for the auth module.

    Responsibilities:
    ─────────────────
    - User lookup and creation
    - UserIdentity management (per provider)
    - RefreshToken storage and revocation
    - OTPVerification management
    """

    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    # TODO: implement
    # async def get_user_by_email(self, email: str) -> User | None
    # async def get_user_by_id(self, user_id: UUID) -> User | None
    # async def create_user(self, email: str) -> User
    # async def set_email_verified(self, user_id: UUID) -> None

    # async def get_identity_by_email(self, email: str) -> UserIdentity | None
    # async def get_identity_by_provider(self, provider: str, provider_user_id: str) -> UserIdentity | None
    # async def create_email_identity(self, user_id: UUID, password_hash: str) -> UserIdentity
    # async def create_social_identity(self, user_id: UUID, provider: str, provider_user_id: str) -> UserIdentity

    # async def store_refresh_token(self, user_id: UUID, token_hash: str, expires_at: datetime, device_id: str | None) -> RefreshToken
    # async def get_refresh_token_by_hash(self, token_hash: str) -> RefreshToken | None
    # async def revoke_refresh_token(self, token_id: UUID) -> None
    # async def revoke_all_user_tokens(self, user_id: UUID) -> None

    # async def create_otp(self, user_id: UUID, otp_hash: str, purpose: str, expires_at: datetime) -> OTPVerification
    # async def get_valid_otp(self, user_id: UUID, purpose: str) -> OTPVerification | None
    # async def mark_otp_used(self, otp_id: UUID) -> None
