from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI

load_dotenv()  # Load environment variables from .env file

llm = ChatAnthropic(model="claude-4-5-sonnet-20250929")
