from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.lifespan import app_lifespan
from app.routers import router as routers
from settings import get_settings

app = FastAPI(
    lifespan=app_lifespan
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=get_settings().ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

routes = APIRouter()

app.include_router(routers)
