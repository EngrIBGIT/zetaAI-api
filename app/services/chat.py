from langchain.memory import ConversationBufferMemory
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from langchain.chains.conversation.base import ConversationChain
from app.constants import SUCCESS_MESSAGE
from app.enums.custom_status_code import CustomStatusCode
from app.helpers import add_record_to_database, create_response
from app.models.conversation import Conversation
from langchain.prompts import PromptTemplate



def start_chat(user_id, message, character):
    memory = ConversationBufferMemory(return_messages=True)

    memory.chat_memory.add_message(SystemMessage(content=f"You are a {character}, engage this user in a conversation"))

    langchain_conversation = ConversationChain(llm=fetch_llm(), memory=memory)
    ai_response = langchain_conversation.run(message)

    user_conversation = Conversation(
        user_id=user_id,
        title="New Chat",
        memory={0: memory}
    )

    add_record_to_database(user_conversation)

    response = {"conversation_id": user_conversation.id, "ai_response": ai_response}

    return response

def fetch_llm():
    llm = ChatGroq(
        model="llama3-8b-8192",
        temperature=0.5,
        max_tokens=250,
        timeout=3,
        max_retries=2
    )

    return llm

def fetch_prompt_template(character):
    return PromptTemplate(
        input_variables=["history", "input"],
        template=(
            f"System: You are a {character}, engage this user in a conversation\n\n"
            "The following is a conversation between User and AI:\n\n"
            "{history}\n\n"
            "User: {input}\nAI:"
        )
    )