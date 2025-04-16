from fastapi import APIRouter

from .ml.ml import router as ml
from .ml.generate_ai_test import router as generate_ai_test
from .ml.scientific_test import router as scientific_test
from .ml.personality_test import router as personality_test
from .ml.summarize import router as summarize
from .ml.generate_image import router as generate_image

router = APIRouter(prefix="/v1")

router.include_router(ml, prefix="/ml", tags=["ml"])

router.include_router(generate_ai_test, prefix="/ai_test", tags=["AI Test"])

router.include_router(scientific_test, prefix="/test", tags=["Test"])
router.include_router(personality_test, prefix="/test", tags=["Test"])

router.include_router(summarize, prefix="/summary", tags=["Summary"])

router.include_router(generate_image, prefix="/image", tags=['Image'])