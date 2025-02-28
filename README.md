# Cocktail Advisor Chat

A Python-based chat application that uses Retrieval-Augmented Generation (RAG) with OpenAI's GPT model and Weaviate vector database to provide intelligent cocktail recommendations and information.

## Features

- Natural language chat interface for cocktail queries
- Memory retention of user preferences
- RAG-powered responses using cocktail dataset
- Vector-based similar cocktail recommendations
- Persistent conversation history
- Real-time chat interface

## Tech Stack

- **Backend**: FastAPI, Python 3.10
- **Vector Database**: Weaviate
- **LLM Integration**: LangChain with OpenAI GPT-3.5
- **Frontend**: HTML, CSS, JavaScript
- **Container**: Docker & Docker Compose
- **Package Management**: Poetry

## Prerequisites

- Docker and Docker Compose
- OpenAI API Key
- Python 3.10+ (for local development)
- Poetry (for local development)

## Quick Start

1. Clone the repository:
`git clone <repository-url>`
`cd cocktailadvisorchat`

2. Create a `.env` file in the root directory:
`OPENAI_API_KEY=your_openai_api_key_here`

3. Start the application:
`docker-compose up --build`

4. Access the chat interface at: `http://localhost:8000/static/index.html`

5. Access API interface at `http://localhost:8000/api/v1/docs`


## Knowledge base questions: 

What are the 5 cocktails containing lemon?

{
  "answer": "1. Lemon Drop Martini: Mix 2 oz vodka, 1 oz triple sec, 1 oz fresh lemon juice, and 1 tsp sugar in a shaker with ice. Shake well and strain into a chilled cocktail glass rimmed with sugar.\n\n2. Tom Collins: Combine 2 oz gin, 1 oz fresh lemon juice, 1/2 oz simple syrup, and ice in a shaker. Shake well and strain into a Collins glass filled with ice. Top with club soda and garnish with a lemon slice.\n\n3. Whiskey Sour: Mix 2 oz whiskey, 3/4 oz fresh lemon juice, 1/2 oz simple syrup, and ice in a shaker. Shake well and strain into a rocks glass filled with ice. Garnish with a cherry and a lemon slice.\n\n4. Lemon Ginger Mojito: Muddle mint leaves and fresh ginger in a glass. Add 2 oz rum, 1 oz fresh lemon juice, 1/2 oz simple syrup, and ice. Top with club soda and garnish with a mint sprig and lemon slice.\n\n5. French 75: Combine 1 oz gin, 1/2 oz fresh lemon juice, 1/2 oz simple syrup, and ice in a shaker. Shake well and strain into a Champagne flute. Top with Champagne and garnish with a lemon twist."
}

What are the 5 non-alcoholic cocktails containing sugar

{
  "answer": "1. Shirley Temple: Ginger ale or lemon-lime soda, grenadine, and a maraschino cherry for garnish. Simply mix the soda and grenadine in a glass over ice and garnish with a cherry.\n\n2. Virgin Pina Colada: Pineapple juice, coconut cream, and ice. Blend the ingredients together until smooth and serve in a glass garnished with a pineapple wedge and cherry.\n\n3. Roy Rogers: Cola, grenadine, and a maraschino cherry. Mix the cola and grenadine in a glass over ice and garnish with a cherry.\n\n4. Arnold Palmer: Iced tea and lemonade. Mix equal parts of iced tea and lemonade in a glass over ice and garnish with a lemon slice.\n\n5. Virgin Mojito: Mint leaves, lime juice, simple syrup, club soda, and ice. Muddle the mint leaves with lime juice and simple syrup, add ice, top off with club soda, and garnish with a mint sprig and lime wedge."
}

What are my favourite ingredients?

{
  "answer": "Based on your preferences for Sugar syrup 'rich', Lemon juice (freshly squeezed), Lime juice (freshly squeezed), Gin (dry), and Aromatic bitters, I would recommend a classic Gin Sour cocktail. To make it, combine 5cl of dry gin, 2cl of freshly squeezed lemon juice, 2cl of rich sugar syrup, and a few dashes of aromatic bitters. Shake well with ice, then strain into a glass filled with ice. Garnish with a lemon twist. Enjoy!"
}

Which cocktails use both rum and pineapple juice?

{
  "answer": "Based on your preferences for Gin, I would recommend a classic cocktail called the Pina Colada, which uses both rum and pineapple juice. To make it, blend 2 ounces of rum, 2 ounces of coconut cream, and 4 ounces of pineapple juice with ice until smooth. Pour into a glass and garnish with a pineapple wedge and a cherry. Enjoy!"
}

## Advisor questions:

Recommend 5 cocktails that contain my favourite ingredients

{
  "answer": "Based on your favorite ingredients, here are 5 cocktails that you might enjoy:\n\n1. **Classic Gin Sour**: Combine 5cl of dry gin, 2cl of freshly squeezed lemon juice, 2cl of rich sugar syrup, and a few dashes of aromatic bitters. Shake well with ice, then strain into a glass filled with ice. Garnish with a lemon twist.\n\n2. **Pina Colada**: Blend 2 ounces of rum, 2 ounces of coconut cream, and 4 ounces of pineapple juice with ice until smooth. Pour into a glass and garnish with a pineapple wedge and a cherry.\n\n3. **Midori Melon Margarita**: Mix 5cl of Midori melon liqueur, 3cl of tequila, 2cl of fresh lime juice, and 1cl of agave nectar. Shake with ice, then strain into a glass with a salted rim. Garnish with a lime wedge.\n\n4. **Rum Punch**: Combine 5cl of rum, 2cl of lime juice, 2cl of sugar syrup, and 4cl of pineapple juice. Shake with ice, then strain into a glass filled with ice. Garnish with a slice of pineapple and a cherry.\n\n5. **Aromatic Gin Fizz**: Mix 5cl of dry gin, 2cl of freshly squeezed lemon juice, 2cl of rich sugar syrup, a few dashes of aromatic bitters, and top with soda water. Shake well with ice, then strain into a glass. Garnish with a lemon twist. Enjoy!"
}

Recommend a cocktail similar to “Hot Creamy Bush”

{
  "answer": "Based on your preferences for gin, sugar syrup 'rich', lemon juice, lime juice, and aromatic bitters, I would recommend a cocktail similar to the \"Hot Creamy Bush.\" You can try a classic cocktail called the \"Gin Fizz.\" To make it, combine 5cl of dry gin, 2cl of freshly squeezed lemon juice, 2cl of rich sugar syrup, a few dashes of aromatic bitters, and top with soda water. Shake well with ice, then strain into a glass. Garnish with a lemon twist. Enjoy!"
}
