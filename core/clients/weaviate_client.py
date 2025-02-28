import weaviate
from weaviate.collections.classes.config import DataType
from loguru import logger

from core.services.csv_reader import CSVReader
from core.settings.config import get_config


class WeaviateClient:
    def __init__(self):
        self.settings = get_config()
        self.client = self._initialize_client()

    def _initialize_client(self):
        client = weaviate.connect_to_local(
            host="weaviate",
            port=8080,
            grpc_port=50051,
        )
        
        return client
    
    async def setup_schema(self):
        if not self.client.collections.exists("Cocktail"):
            self.client.collections.create(
                name="Cocktail",
                properties=[
                    {"name": "cocktailId", "data_type": DataType.INT},
                    {"name": "name", "data_type": DataType.TEXT},
                    {"name": "alcoholic", "data_type": DataType.TEXT},
                    {"name": "category", "data_type": DataType.TEXT},
                    {"name": "glassType", "data_type": DataType.TEXT},
                    {"name": "instructions", "data_type": DataType.TEXT},
                    {"name": "drinkThumbnail", "data_type": DataType.TEXT},
                    {"name": "ingredients", "data_type": DataType.TEXT_ARRAY},
                    {"name": "ingredientMeasures", "data_type": DataType.TEXT_ARRAY},
                    {"name": "text", "data_type": DataType.TEXT}
                ],
                vectorizer_config=None,
            )

    async def populate_data(self):
        csv_reader = CSVReader()
        cocktails = await csv_reader.read_cocktails()
        
        cocktail_collection = self.client.collections.get("Cocktail")

        with cocktail_collection.batch.dynamic() as batch:
            for cocktail in cocktails:
                cocktail_dict = cocktail.model_dump()
                
                try:
                    batch.add_object(
                        properties={
                            "cocktailId": cocktail_dict["id"],
                            "name": cocktail_dict["name"],
                            "alcoholic": cocktail_dict["alcoholic"],
                            "category": cocktail_dict["category"],
                            "glassType": cocktail_dict["glassType"],
                            "instructions": cocktail_dict["instructions"],
                            "drinkThumbnail": cocktail_dict["drinkThumbnail"],
                            "ingredients": cocktail_dict["ingredients"],
                            "ingredientMeasures": cocktail_dict["ingredientMeasures"],
                            "text": cocktail_dict["text"]
                        }
                    )
                except Exception as e:
                    logger.error(f"Error adding cocktail {cocktail_dict['name']}: {str(e)}")
                    continue
    
    async def close(self):
        if self.client:
            self.client.close()

def get_weaviate_client() -> WeaviateClient:
    return WeaviateClient()
