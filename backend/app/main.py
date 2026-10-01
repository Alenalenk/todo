from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import engine


from app.lifespan import app_lifespan

from app.models import Todo
from app.schemas import TodoCreate
from settings import settings

app = FastAPI(
    lifespan=app_lifespan
)

session = Session(engine)

origins = settings.ORIGINS

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/todos")
async def get_todos():
    async with AsyncSession(engine) as session:
        result = await session.execute(select(Todo))
        todos = result.scalars().all()
        return todos

@app.post("/todos")
async def create_todo(todo: TodoCreate):
    async with AsyncSession(engine) as session:
        todo_db = Todo(title=todo.title, description=todo.description)
        session.add(todo_db)
        await session.commit()
        return todo_db
    
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo: TodoCreate):
    async with AsyncSession(engine) as session:
        todo_db = await session.get(Todo, todo_id)
        if not todo_db:
            raise HTTPException(status_code=404, detail="Todo not found")
        todo_db.title = todo.title
        todo_db.description = todo.description
        todo_db.status = todo.status
        await session.commit()
        return todo_db

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    async with AsyncSession(engine) as session:
        todo_db = await session.get(Todo, todo_id)
        if not todo_db:
            raise HTTPException(status_code=404, detail="Todo not found")
        await session.delete(todo_db)
        await session.commit()
        return todo_db