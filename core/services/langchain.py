from functools import lru_cache
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate
from langchain_weaviate import WeaviateVectorStore

from core.settings.config import get_config
from core.clients.weaviate_client import get_weaviate_client


class LangchainService:
    def __init__(self):
        self.config = get_config()
        self.weaviate_client = get_weaviate_client()
        self.llm = ChatOpenAI(
            api_key=self.config.OPENAI_API_KEY,
            model_name="gpt-3.5-turbo",
            temperature=0.7
        )

        self.embeddings = OpenAIEmbeddings(
            api_key=self.config.OPENAI_API_KEY,
        )
        
        self.vectorstore = WeaviateVectorStore(
            client=self.weaviate_client.client,
            index_name="Cocktail",
            text_key="text",
            attributes=["name", "ingredients", "instructions", "alcoholic"],
            embedding=self.embeddings,
        )
        
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
        
        self.qa_prompt = PromptTemplate(
            template="""You are a knowledgeable cocktail advisor who remembers user preferences from previous conversation.
            
            Context: {context}
            
            Chat History: {chat_history}
            
            Question: {question}
            
            Important instructions:
            1. If the user has previously mentioned their preferences or favorites, refer to those specific preferences in your answer.
            2. Never state your own preferences - only reflect what the user has told you about their preferences.
            3. If the user asks about their preferences but hasn't shared any, politely indicate that they haven't told you their preferences yet.
            4. If you don't know the answer to a question, just say you don't know.
            
            Please provide a personalized response based on the user's stated preferences from the chat history.
            If the question is about cocktail recommendations, include the ingredients and instructions if available.
            
            Answer:""",
            input_variables=["context", "chat_history", "question"]
        )
                
        self.qa_chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=self.vectorstore.as_retriever(search_kwargs={"k": 5}),
            memory=self.memory,
            combine_docs_chain_kwargs={"prompt": self.qa_prompt}
        )
    
    async def get_response(self, question: str) -> str:
        response = await self.qa_chain.ainvoke({
            "question": question
        })
        return response["answer"]

@lru_cache(1)
def get_langchain_service():
    return LangchainService()
