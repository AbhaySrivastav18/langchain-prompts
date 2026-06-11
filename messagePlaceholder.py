from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder


chatTemplate = ChatPromptTemplate([
    ('system','You are a helpful customer agent'),
    MessagesPlaceholder(variableName = 'chatHistory'),
    ('human','{query}')
])

chatHistory1 = []
with open('chatHistory.txt') as f:
    chatHistory1.extend(f.readlines())

prompt = chatTemplate.invoke({'chatHistory':chatHistory1,'query': 'Where is my refund'})