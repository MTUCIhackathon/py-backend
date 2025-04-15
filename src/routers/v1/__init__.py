from fastapi import APIRouter

from .wml.ml import router as ml

router = APIRouter(prefix="/v1")
router.include_router(ml, prefix="/ml", tags=["ml"])