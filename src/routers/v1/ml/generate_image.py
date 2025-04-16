from fastapi import APIRouter, HTTPException
import logging
from model import GenerateModel
from schemas.ml import GenerateImageInput, GenerateImageResponce

router = APIRouter()
logger = logging.getLogger(__name__)

generator = GenerateModel()

@router.post("/generate_image", response_model=GenerateImageResponce)
async def generate_image(profession: GenerateImageInput):
    try:
        image_data = await generator.generate_image(profession.profession)
        return GenerateImageResponce(image_data=image_data)
    except Exception as e:
        logger.error(f"Ошибка генерации изображения: {e}")
        raise HTTPException(status_code=500, detail=str(e))
