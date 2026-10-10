from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # ── Application ──────────────────────────────────────────────────────────
    APP_NAME: str = "OhMind API"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = False
    ENV: str = "development"  # development | staging | production

    # ── Database ─────────────────────────────────────────────────────────────
    DATABASE_URL: str
    DATABASE_POOL_SIZE: int = 10
    DATABASE_MAX_OVERFLOW: int = 20

    # ── Redis ─────────────────────────────────────────────────────────────────
    REDIS_URL: str

    # ── JWT (RS256) ───────────────────────────────────────────────────────────
    JWT_ALGORITHM: str = "RS256"
    JWT_PRIVATE_KEY: str  # Full PEM string, newlines as \n in .env
    JWT_PUBLIC_KEY: str  # Full PEM string, newlines as \n in .env
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    JWT_REFRESH_TOKEN_EXPIRE_DAYS: int = 30

    # ── Google OAuth ──────────────────────────────────────────────────────────
    GOOGLE_CLIENT_ID: str = ""
    GOOGLE_CLIENT_SECRET: str = ""

    # ── Apple OAuth ───────────────────────────────────────────────────────────
    APPLE_CLIENT_ID: str = ""
    APPLE_TEAM_ID: str = ""
    APPLE_KEY_ID: str = ""
    APPLE_PRIVATE_KEY: str = ""
    # ── Rate Limiting ────────────────────────────────────────────────────────
    RATE_LIMIT_GLOBAL_TIMES: int = 120
    RATE_LIMIT_GLOBAL_SECONDS: int = 60
    RATE_LIMIT_AUTH_TIMES: int = 10
    RATE_LIMIT_AUTH_SECONDS: int = 60


settings = Settings()
