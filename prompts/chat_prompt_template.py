from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

chat_temp = ChatPromptTemplate([
    ('system', "You are a helpful {domain} expert."),
    ('human', "explain the concept of {concept} in simple terms."),
])

prompt = chat_temp.format_prompt(domain="AI", concept="transformers")

model = ChatGroq(
      model="openai/gpt-oss-20b")

result = model.invoke(prompt)
print(result.content)          