# Full-Stack Web Application

A full-stack web application built with **React, TypeScript, FastAPI, and PostgreSQL**.

The project uses a separated frontend and backend architecture. The frontend provides the user interface and communicates with the backend through a REST API, while the backend handles application logic, validation, and database operations.

## Tech Stack

### Frontend

- React 19
- TypeScript
- Redux Toolkit
- React Redux
- React Router
- React Hook Form
- Vite
- ESLint

### Backend

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- Alembic
- Uvicorn
- PostgreSQL
- asyncpg

## Project Structure

The project is organized as a monorepository containing separate frontend and backend applications.

```text
project/
│
├── backend/
│   ├── ...
│   └── pyproject.toml
│
├── frontend/
│   ├── src/
│   ├── package.json
│   └── ...
│
└── README.md
```

## Features

The application demonstrates a modern full-stack architecture with:

- REST API integration
- Asynchronous database operations
- Data validation with Pydantic
- Database interaction using SQLAlchemy
- Database migrations with Alembic
- Client-side routing
- Global state management with Redux Toolkit
- Form handling and validation with React Hook Form
- Type-safe frontend development with TypeScript
- Separation of frontend and backend responsibilities

## Backend

The backend is implemented with **FastAPI** and uses **SQLAlchemy** for database interaction.

Database operations can be performed asynchronously using `asyncpg`.

### Main backend dependencies

```text
FastAPI
SQLAlchemy
Alembic
Pydantic
Pydantic Settings
asyncpg
psycopg
Uvicorn
```

### Environment Variables

Create a `.env` file in the backend directory.

Example:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_DB=postgres
POSTGRES_SERVER=localhost
POSTGRES_PORT=5432

ORIGINS=["http://localhost:5173"]
```

### Install Backend Dependencies

The backend uses `pyproject.toml` for dependency management.

Using `uv`:

```bash
cd backend
uv sync
```

### Database Migrations

Apply existing migrations:

```bash
uv run alembic upgrade head
```

Create a new migration:

```bash
uv run alembic revision --autogenerate -m "migration description"
```

### Run Backend

```bash
uv run uvicorn app.main:app --reload
```

By default, the API will be available at:

```text
http://localhost:8000
```

FastAPI automatically provides interactive API documentation:

```text
http://localhost:8000/docs
```

## Frontend

The frontend is built with **React 19 and TypeScript** and uses Vite as the development and build tool.

Application state is managed with **Redux Toolkit**, while forms are handled using **React Hook Form**.

### Install Frontend Dependencies

```bash
cd frontend
npm install
```

### Environment Variables

Create a `.env` file in the frontend directory if the API URL is configurable.

Example:

```env
VITE_API_URL=http://localhost:8000
```

### Run Frontend

```bash
npm run dev
```

The development server will normally be available at:

```text
http://localhost:5173
```

## Running the Project

The frontend and backend should be started separately.

### 1. Start PostgreSQL

Make sure PostgreSQL is running and the database specified in `DATABASE_URL` exists.

### 2. Start the Backend

```bash
cd backend
uv sync
uv run alembic upgrade head
uv run uvicorn app.main:app --reload
```

### 3. Start the Frontend

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

Then open:

```text
http://localhost:5173
```

## Development

### Frontend production build

```bash
cd frontend
npm run build
```

### Frontend linting

```bash
npm run lint
```

### Backend dependency lock

After changing backend dependencies:

```bash
uv lock
```

## API

The frontend communicates with the FastAPI backend through REST endpoints.

During development, the available API endpoints can be explored through Swagger UI:

```text
http://localhost:8000/docs
```

## Requirements

To run the project locally, you need:

- Python
- Node.js
- npm
- PostgreSQL
- uv

## License

This project is intended for educational and portfolio purposes.