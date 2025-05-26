from fastapi import APIRouter
from app.model import RequestState
from agents.ai_agents import get_response_from_ai_agent

router = APIRouter()

ALLOWED_MODEL_NAMES = ["llama3-70b-8192", "gpt-4o-mini"]

@router.post("/chat")
def chat_endpoint(request: RequestState):
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Invalid model name. Kindly select a valid AI model"}
    
    response = get_response_from_ai_agent(
        llm_id=request.model_name,
        query=request.messages,
        allow_search=request.allow_search,
        system_prompt=request.system_prompt,
        provider=request.model_provider,
    )
    return response
