from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

prompt = PromptTemplate(
    template = "Give me 5 interesting facts about {topic}.",
    input_variables = ["topic"])

model = ChatGroq(model="openai/gpt-oss-20b")
parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"topic": "space exploration"})
print(result)