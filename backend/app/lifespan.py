from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db import create_schema


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    await create_schema()
    
    yield