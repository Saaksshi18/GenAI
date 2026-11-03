from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model = ChatGroq(
      model="openai/gpt-oss-20b")

message = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Hello! How are you?"),
]

result = model.invoke(message)

message.append(AIMessage(content= result.content))

print(message)

