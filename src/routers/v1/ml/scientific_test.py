from fastapi import APIRouter, HTTPException
import logging
from model import GenerateModel
from schemas.ml import ScientificTestInput, ScientificTestResponse

router = APIRouter()
logger = logging.getLogger(__name__)

generator = GenerateModel()

@router.post("/scientific_test", response_model=ScientificTestResponse)
async def scientific_test(test_input: ScientificTestInput):
    try:
        result = generator.get_professions_scientific_test(test_input.test_result)
        return ScientificTestResponse(**result)
    except Exception as e:
        logger.error(f"Ошибка обработки научного теста: {e}")
        raise HTTPException(status_code=500, detail=str(e))
