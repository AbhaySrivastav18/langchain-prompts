from langchain_core.prompts import ChatPromptTemplate

chatTemplate = ChatPromptTemplate([
    ('system','You are a helpful {domain} expert')
    ('human','Explain in simple terms,What is {topic}')

])
prompt = chatTemplate.invoke({'domain':'Cricket','topic':'Mid Off'})
print(prompt)
