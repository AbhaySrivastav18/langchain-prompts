from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
load_dotenv()

llm = HuggingFacePipeline.from_model_id(
    model_id="microsoft/Phi-3-mini-4k-instruct",
    task="text-generation",
    pipeline_kwargs={
        "temperature": 0.5,
        "max_new_tokens": 300
    }
)

model = ChatHuggingFace(llm=llm)
chatHistory = [
    SystemMessage(content="You are an AI Assistant")
]
while True:
    user_input = input("You: ")
    chatHistory.append(HumanMessage(content=user_input))
    if user_input.lower() == "exit":
        break

    result = model.invoke(user_input)
    chatHistory.append(AIMessage(content=result))
print(chatHistory)