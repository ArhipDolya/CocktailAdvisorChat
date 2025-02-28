from fastapi import APIRouter, Depends

from core.clients.weaviate_client import WeaviateClient, get_weaviate_client
from core.schemas.cocktail import ChatRequest, ChatResponse
from core.services.langchain import LangchainService, get_langchain_service


router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat_with_advisor(
    request: ChatRequest,
    langchain_service: LangchainService = Depends(get_langchain_service),
):
    response = await langchain_service.get_response(request.question)
    return ChatResponse(answer=response)
