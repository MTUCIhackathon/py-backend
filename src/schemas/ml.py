from pydantic import BaseModel, Field
from typing import Dict, List

class Response(BaseModel):
    result: str
    
class ScientificTestInput(BaseModel):
    test_result: Dict[str, int]
    
class ScientificTestResponse(BaseModel):
    professions: List[str] = Field(..., alias="professions")

class PersonalityTestInput(BaseModel):
    test_result: str

class PersonalityTestResponse(BaseModel):
    personality_type: str
    description: str
    professions: List[str]
        
class SummarizeInput(BaseModel):
    test_1: List[str]
    test_2: List[str]
    test_3: List[str]
    
class SummarizeResponse(BaseModel):
    top_professions: List[str] = Field(..., alias="top_professions")
    
class GenerateAITestInput(BaseModel):
    questions: Dict[str, str]

class GenerateAITestResponce(BaseModel):
    question: str
    answers: List[str]

class ResultAITestInput(BaseModel):
    user_answers: Dict[str, str]

class ResultAITestResponce(BaseModel):
    top_professions: List[str]
    
class GenerateImageInput(BaseModel):
    profession: str
    
class GenerateImageResponce(BaseModel):
    image_data: str      
