from fastapi import APIRouter

from src.api.routers import embrapa

router = APIRouter()
router.include_router(embrapa.router, tags=["Embrapa"])
