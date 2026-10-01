python 3.13 
# Todo API

Простий REST API для керування Todo задачами, побудований на FastAPI.

## Функціонал

- CRUD операції
- Валідація через Pydantic
- SQLAlchemy ORM
- Alembic міграції
- Swagger документація
- Асинхронний FastAPI застосунок

---

# Технології

- Python 3.13
- FastAPI
- SQLAlchemy
- Pydantic
- Alembic
- Uvicorn
- UV

---

# Запуск проєкту 

1. Клонування проєкту
git clone <repo>
cd <project>
2. Установка залежностей (UV сам створить середовище)
uv sync

👉 UV автоматично:

створює .venv
встановлює залежності
фіксує lock-файл 

3. Для запуску додатку в кореневу папку необхідно додати файл .env з даними для підключення до бази даних
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_DB=postgres
POSTGRES_SERVER=localhost
POSTGRES_PORT=5432

ORIGINS=http://127.0.0.1:3000



3. Запуск через UV (рекомендовано)
uvicorn app.main:app --reload