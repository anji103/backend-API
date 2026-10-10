# OHMIND

## Overview

OHMIND is an AI-powered mental wellness platform designed to provide users with a safe, structured, and supportive conversational experience.

The platform combines modern AI capabilities with safety-first design principles to help users engage in reflective conversations, emotional check-ins, and guided wellness journeys.

---

## Technology Stack

- **Framework:** FastAPI
- **Language:** Python 3.13
- **ORM:** SQLAlchemy 2.0 (Async)
- **Database:** PostgreSQL
- **Cache/Queue:** Redis
- **Package Manager:** uv

---

## Getting Started

### Prerequisites

- **Python 3.13+**
- **[uv](https://github.com/astral-sh/uv)** - Python package manager.

### 1. Environment Setup

Copy the example environment file and fill in the necessary values:

```bash
cp .env.example .env
```

### 2. Generate RSA Keys (for JWT RS256)

The project uses RS256 for JWT tokens. You need to generate a private/public key pair:

```bash
# Generate private key
openssl genrsa -out private.pem 2048

# Extract public key
openssl rsa -in private.pem -pubout -out public.pem
```

Then, update the `.env` file:

1.  Read the keys and replace newlines with `\n` to fit into a single line in `.env` (or use the multi-line format if your loader supports it).
2.  `JWT_PRIVATE_KEY`: Content of `private.pem`
3.  `JWT_PUBLIC_KEY`: Content of `public.pem`

### 3. Installation

Install dependencies using `uv`:

```bash
uv sync
```

### 4. Migrations

This project uses **Alembic** with an async driver for migrations.

```bash
# Create a new migration
uv run alembic revision --autogenerate -m "description_of_changes"

# Apply migrations
uv run alembic upgrade head
```

### 5. Run the Project

```bash
uv run uvicorn app.main:app --reload --port 8000
```

---

## Code Quality

We use **Ruff** for linting and formatting.

```bash
# Check for linting issues
uv run ruff check .

# Fix linting issues
uv run ruff check . --fix

# Format code
uv run ruff format .
```

---

## Project Structure

```text
app/
├── core/         # Core configuration, database setup, and security
├── shared/       # Shared utilities, exceptions, and middleware
├── modules/      # Domain-driven modules (auth, users, etc.)
│   ├── auth/     # Authentication & Identity
│   ├── users/    # User lifecycle & device management
│   └── ...
├── migrations/   # Alembic database migrations
└── main.py       # Application entry point
```

Detailed rules for module structure are in `docs/AGENTS.md`.

---
