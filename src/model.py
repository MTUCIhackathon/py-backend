import logging
import json
from yandex_neural_api.client import YandexNeuralAPIClient
from settings import Settings
from dotenv import load_dotenv
import os

load_dotenv() 
folder_id = os.getenv("FOLDER_ID")
iam_token = os.getenv("IAM_TOKEN")

settings = Settings()

class GenerateModel:
    def __init__(self, 
                 folder_id=settings.FOLDER_ID,
                 iam_token=settings.IAM_TOKEN,
                 model_type=settings.MODEL_TYPE, 
                 llm_temperature=settings.LLM_TEMPERATYRE, 
                 llm_max_tokens=settings.LLM_MAX_TOKENS, 
                 log_level=logging.INFO):
      
        self.folder_id = folder_id
        self.iam_token = iam_token
        self.client = YandexNeuralAPIClient(
            iam_token=self.iam_token,
            folder_id=self.folder_id,
            model_type=model_type,
            llm_temperature=llm_temperature,
            llm_max_tokens=llm_max_tokens,
            log_level=log_level
        )
        self.logger = logging.getLogger(__name__)
        
    def read_prompt(self, file_path:str):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                template = f.read()
        except FileNotFoundError:
            self.logger.error("Файл шаблона промпта не найден.")
            raise
        return template 
        
    def _parse_json_response(self, response: str) -> dict:
        try:
            cleaned = response.replace("```json", "").replace("```", "").strip()
            return json.loads(cleaned)
        except json.JSONDecodeError as e:
            self.logger.error("Ошибка парсинга JSON: %s; исходный ответ: %s", e, response)
            return {"error": "Ошибка парсинга JSON", "raw_response": response}
    
    def get_response(self, prompt):
        response = self.client.generate_text(prompt)
        parsed_response = self._parse_json_response(response)
        return parsed_response
    
        
    """ Test 1 """
    def scientific_test_prompt(self, test_result: dict) -> str:
        template = self.read_prompt('src/prompts/scientific_test_prompt.txt')
        prompt = template.format(test_result=json.dumps(test_result, ensure_ascii=False, indent=2))
        return prompt

    def get_professions_scientific_test(self, test_results:dict):
        prompt = self.scientific_test_prompt(test_results)
        responce = self.get_response(prompt)
        return responce
    
    
    """ Test 2 """
    def personality_test_prompt(self, test_result: str) -> str:
        template = self.read_prompt('src/prompts/personality_test_prompt.txt')
            
        prompt = template.format(test_result=json.dumps(test_result, ensure_ascii=False, indent=2))
        return prompt
    
    def get_professions_personality_test(self, test_result:str):
        prompt = self.personality_test_prompt(test_result)
        response = self.get_response(prompt)
        return response
        
        
    """ Test 3 """
    def ai_test_prompt(self, answers_history: dict) -> str:
        template = self.read_prompt('src/prompts/AI_test_prompt.txt')         
        prompt = template.format(answers_history=json.dumps(answers_history, ensure_ascii=False, indent=2))
        return prompt
    
    def generate_ai_test(self, answers_history: dict):
        prompt = self.ai_test_prompt(answers_history)
        response = self.get_response(prompt)
        return response
    
    def professions_ai_test_prompt(self, answers_history: dict):
        template = self.read_prompt('src/prompts/AI_result_prompt.txt')         
        prompt = template.format(answers_history=json.dumps(answers_history, ensure_ascii=False, indent=2))
        return prompt
        
    def get_professions_ai_test(self, answers_history: dict):
        prompt = self.professions_ai_test_prompt(answers_history)
        responce = self.get_response(prompt)
        return responce
    
    
    """ Summarize """
    def summarize_prompt(self, test_1:dict, test_2:dict, test_3:dict):
        template = self.read_prompt('src/prompts/summarize_prompt.txt')

        prompt = template.format(
            test_1_professions=json.dumps(test_1, ensure_ascii=False),
            test_2_professions=json.dumps(test_2, ensure_ascii=False),
            test_3_professions=json.dumps(test_3, ensure_ascii=False)
        )
        
        return prompt
      
    def summarize(self, test_1:list, test_2:list, test_3:list):
        print(test_1, test_2, test_3)
        prompt = self.summarize_prompt(test_1, test_2, test_3)
        response = self.get_response(prompt)
        return response
    