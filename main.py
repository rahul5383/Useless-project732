from langchain_Ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
template = """
**Prompt:** Act as a motivational insult generator, something that would inspire someone to improve while also being a bit insulting. Keep it short and punchy. 

**Context:** {context}

**Question:** {question}
"""


model = OllamaLLM(model="llama3.2")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_convo():
    context=""
    print("Welcome to the AI Chatbot !, Type 'exit' to quit")
    while True:
        user_input = input("You : ")
        if user_input.lower() == "exit":
            break
        result = chain.invoke({"context":context,"question":user_input})
        print("Bot: ",result)
        context += f"\nUser:{user_input}\nAI:{result}"

if __name__ == "__main__":
    handle_convo()


