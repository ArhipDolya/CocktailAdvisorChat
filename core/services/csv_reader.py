import pandas as pd

from core.schemas.cocktail import CocktailData


class CSVReader:
    def __init__(self, file_path: str = "final_cocktails.csv"):
        self.file_path = file_path

    async def read_cocktails(self) -> list[CocktailData]:
        df = pd.read_csv(self.file_path)
        cocktails = []

        for _, row in df.iterrows():
            # Convert string representations of lists to actual lists
            ingredients = eval(row['ingredients']) if isinstance(row['ingredients'], str) else row['ingredients']
            measures = eval(row['ingredientMeasures']) if isinstance(row['ingredientMeasures'], str) else row['ingredientMeasures']
            
            cocktail = CocktailData(
                id=row['id'],
                name=row['name'],
                alcoholic=row['alcoholic'],
                category=row['category'],
                glassType=row['glassType'],
                instructions=row['instructions'],
                drinkThumbnail=row['drinkThumbnail'],
                ingredients=ingredients,
                ingredientMeasures=measures,
                text=row['text']
            )
            cocktails.append(cocktail)
            
        return cocktails
