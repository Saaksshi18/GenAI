from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

prompt1 = PromptTemplate(
    template = "Give a detailed report on the {topic}",
    input_variables = ["topic"])

prompt2 = PromptTemplate(
    template = "Give a 5 point summary of the report on {text}",
    input_variables = ["text"])

model = ChatGroq(model="openai/gpt-oss-20b")

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({"topic": "space exploration"})
print(result)