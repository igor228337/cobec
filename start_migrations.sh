#!/bin/bash
docker exec cobec-backend-1 /app/.venv/bin/alembic revision --autogenerate -m "$1"