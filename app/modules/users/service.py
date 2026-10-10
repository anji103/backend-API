"""
Auth Service
============
All business logic for authentication lives here.
This layer must NOT access the database directly — use the repository.
"""

from app.modules.auth.repository import AuthRepository


class AuthService:
    """
    Business logic for authentication.

    Responsibilities:
    ─────────────────
    - Email signup / login
    - OTP generation and verification
    - JWT access + refresh token lifecycle
    - Social login (Google OAuth, Apple OAuth)
    - Token rotation on refresh
    - Logout (token revocation)
    """

    def __init__(self, repository: AuthRepository) -> None:
        self.repository = repository

    # TODO: implement
    # async def signup_with_email(self, email: str, password: str) -> TokenResponse
    #     1. Check email not already registered → raise ConflictException
    #     2. Create User record
    #     3. Create UserIdentity with hashed password (Argon2id)
    #     4. Generate and store OTP for email verification
    #     5. Send OTP via email (notification service — future)
    #     6. Return access + refresh tokens

    # async def login_with_email(self, email: str, password: str) -> TokenResponse
    #     1. Look up UserIdentity by email
    #     2. Verify password with Argon2id
    #     3. Check user is active and not deleted
    #     4. Issue access + refresh tokens

    # async def verify_otp(self, email: str, otp: str, purpose: str) -> None
    #     1. Fetch valid OTP record for user + purpose
    #     2. Compare hash
    #     3. Mark OTP used
    #     4. Set is_email_verified = True (if purpose == email_verification)

    # async def refresh_tokens(self, raw_refresh_token: str) -> TokenResponse
    #     1. Hash the incoming token
    #     2. Look up RefreshToken record — must exist and not be revoked/expired
    #     3. Revoke old token
    #     4. Issue new access + refresh token pair (token rotation)

    # async def logout(self, raw_refresh_token: str) -> None
    #     1. Hash the token
    #     2. Revoke the matching RefreshToken record

    # async def login_with_google(self, id_token: str) -> TokenResponse
    #     1. Verify id_token with Google
    #     2. Extract email + google_user_id
    #     3. Upsert User + social UserIdentity
    #     4. Issue tokens

    # async def login_with_apple(self, id_token: str, authorization_code: str) -> TokenResponse
    #     1. Verify id_token with Apple
    #     2. Extract email + apple_user_id
    #     3. Upsert User + social UserIdentity
    #     4. Issue tokens
