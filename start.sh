#!/bin/sh

# Применение миграций
until uv run alembic upgrade head; do
    sleep 5
    echo "Database is unavailable - sleeping"
done

uv run python src/main.py
 