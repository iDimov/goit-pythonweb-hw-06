#!/bin/bash

# Швидкий старт проекту

echo "=== Homework 6 Setup Script ==="

# 1. Запуск Docker контейнера
echo "Step 1: Starting PostgreSQL container..."
docker run --name postgres-hw6 -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres

# Чекаємо поки контейнер запуститься
echo "Waiting for PostgreSQL to start..."
sleep 5

# 2. Створення віртуального середовища (якщо не існує)
if [ ! -d ".venv" ]; then
    echo "Step 2: Creating virtual environment..."
    python3 -m venv .venv
fi

# 3. Активація віртуального середовища та встановлення залежностей
echo "Step 3: Installing dependencies..."
source .venv/bin/activate
pip install -r requirements.txt

# 4. Створення міграцій
echo "Step 4: Creating migrations..."
alembic revision --autogenerate -m "Initial migration"

# 5. Застосування міграцій
echo "Step 5: Applying migrations..."
alembic upgrade head

# 6. Наповнення БД
echo "Step 6: Seeding database..."
python seed.py

echo ""
echo "=== Setup Complete! ==="
echo ""
echo "You can now:"
echo "  - Activate venv: source .venv/bin/activate"
echo "  - Run queries: python my_select.py"
echo "  - Use CLI: python main.py -a list -m Teacher"
echo ""
