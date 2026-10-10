FROM python:3.13-slim AS base

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# ---------------------------------------------------------------------------
# Dependencies layer — cached unless pyproject.toml / uv.lock changes
# ---------------------------------------------------------------------------
FROM base AS deps

COPY pyproject.toml uv.lock* ./
RUN uv sync --frozen --no-dev

# ---------------------------------------------------------------------------
# Production image
# ---------------------------------------------------------------------------
FROM base AS production

COPY --from=deps /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"

COPY . .

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
