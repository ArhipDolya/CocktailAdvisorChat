from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from core.clients.weaviate_client import get_weaviate_client
from core.services.langchain import get_langchain_service
from core.handlers.cocktails import router as cocktail_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    client = get_weaviate_client()
    await client.setup_schema()
    await client.populate_data()
    get_langchain_service()
    
    yield
    
    # Shutdown logic
    client = get_weaviate_client()
    await client.close()


def create_app() -> FastAPI:
    app = FastAPI(
        title="CocktailAdvisorChat",
        docs_url="/api/v1/docs",
        description="A cocktail advisor chatbot using RAG",
        lifespan=lifespan,
    )

    app.include_router(cocktail_router, prefix="/api/v1")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.mount("/static", StaticFiles(directory="core/static"), name="static")

    return app


app = create_app()
