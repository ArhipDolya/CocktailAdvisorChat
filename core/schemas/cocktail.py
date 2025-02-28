from pydantic import BaseModel


class CocktailData(BaseModel):
    id: int
    name: str
    alcoholic: str
    category: str
    glassType: str
    instructions: str
    drinkThumbnail: str
    ingredients: list[str]
    ingredientMeasures: list[str | None]
    text: str

class ChatRequest(BaseModel):
    question: str

class ChatResponse(BaseModel):
    answer: str
