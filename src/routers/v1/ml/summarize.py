from fastapi import APIRouter, HTTPException
import logging
from model import GenerateModel
from schemas.ml import SummarizeInput, SummarizeResponse

router = APIRouter()
logger = logging.getLogger(__name__)

generator = GenerateModel()

@router.post("/summarize", response_model=SummarizeResponse)
async def summarize(tests: SummarizeInput):
    try:
        test_1 = tests.test_1
        test_2 = tests.test_2
        test_3 = tests.test_3
        result = generator.summarize(test_1, test_2, test_3)
        return SummarizeResponse(**result)
    except Exception as e:
        logger.error(f"Ошибка суммаризации: {e}")
        raise HTTPException(status_code=500, detail=str(e))
