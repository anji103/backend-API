from fastapi import APIRouter, Depends

from app.core.dependencies import get_auth_rate_limiter
from app.modules.auth.dependencies import get_auth_service
from app.modules.auth.schemas import (
    AppleLoginRequest,
    EmailLoginRequest,
    EmailSignupRequest,
    GoogleLoginRequest,
    OTPVerifyRequest,
    RefreshTokenRequest,
)
from app.modules.auth.service import AuthService
from app.shared.utils.response import success_response

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
    dependencies=[Depends(get_auth_rate_limiter)],
)


@router.post("/signup", summary="Register with email and password")
async def signup(
    payload: EmailSignupRequest,
    service: AuthService = Depends(get_auth_service),
):
    # TODO: result = await service.signup_with_email(payload.email, payload.password)
    # TODO: return success_response(data=result.model_dump(), status_code=201)
    return success_response(data={"message": "signup — not yet implemented"}, status_code=501)


@router.post("/login", summary="Login with email and password")
async def login(
    payload: EmailLoginRequest,
    service: AuthService = Depends(get_auth_service),
):
    # TODO: result = await service.login_with_email(payload.email, payload.password)
    # TODO: return success_response(data=result.model_dump())
    return success_response(data={"message": "login — not yet implemented"}, status_code=501)


@router.post("/verify-otp", summary="Verify email OTP")
async def verify_otp(
    payload: OTPVerifyRequest,
    service: AuthService = Depends(get_auth_service),
):
    # TODO: await service.verify_otp(payload.email, payload.otp, purpose="email_verification")
    # TODO: return success_response(data={"message": messages.AUTH_OTP_SENT})
    return success_response(data={"message": "verify-otp — not yet implemented"}, status_code=501)


@router.post("/refresh", summary="Rotate refresh token")
async def refresh(
    payload: RefreshTokenRequest,
    service: AuthService = Depends(get_auth_service),
):
    # TODO: result = await service.refresh_tokens(payload.refresh_token)
    # TODO: return success_response(data=result.model_dump())
    return success_response(data={"message": "refresh — not yet implemented"}, status_code=501)


@router.post("/logout", summary="Revoke refresh token")
async def logout(
    payload: RefreshTokenRequest,
    service: AuthService = Depends(get_auth_service),
):
    # TODO: await service.logout(payload.refresh_token)
    # TODO: return success_response(data={"message": messages.AUTH_LOGOUT_SUCCESS})
    return success_response(data={"message": "logout — not yet implemented"}, status_code=501)


@router.post("/social/google", summary="Login or signup with Google")
async def google_login(
    payload: GoogleLoginRequest,
    service: AuthService = Depends(get_auth_service),
):
    # TODO: result = await service.login_with_google(payload.id_token)
    # TODO: return success_response(data=result.model_dump())
    return success_response(data={"message": "google login — not yet implemented"}, status_code=501)


@router.post("/social/apple", summary="Login or signup with Apple")
async def apple_login(
    payload: AppleLoginRequest,
    service: AuthService = Depends(get_auth_service),
):
    # TODO: result = await service.login_with_apple(payload.id_token, payload.authorization_code)
    # TODO: return success_response(data=result.model_dump())
    return success_response(data={"message": "apple login — not yet implemented"}, status_code=501)
