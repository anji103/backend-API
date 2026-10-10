from pydantic import BaseModel, EmailStr, Field

# ── Request Schemas ───────────────────────────────────────────────────────────


class EmailSignupRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)


class EmailLoginRequest(BaseModel):
    email: EmailStr
    password: str


class OTPVerifyRequest(BaseModel):
    email: EmailStr
    otp: str = Field(min_length=4, max_length=10)


class RefreshTokenRequest(BaseModel):
    refresh_token: str


class GoogleLoginRequest(BaseModel):
    id_token: str


class AppleLoginRequest(BaseModel):
    id_token: str
    authorization_code: str


# ── Response Schemas ──────────────────────────────────────────────────────────


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
