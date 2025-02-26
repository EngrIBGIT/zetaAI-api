from langchain.memory import ConversationBufferMemory
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from langchain.chains.conversation.base import ConversationChain
from app.constants import SUCCESS_MESSAGE
from app.enums.custom_status_code import CustomStatusCode
from app.helpers import add_record_to_database, create_response
from app.models.conversation import Conversation


def start_chat(user_id, message, character):
    memory = ConversationBufferMemory(return_messages=True)
    memory.chat_memory.add_message(SystemMessage(content=f"You are a {character}, engage this user in a conversation"))

    langchain_conversation = ConversationChain(llm=fetch_llm(), memory=memory)
    ai_response = langchain_conversation.run(message)

    user_conversation = Conversation(
        user_id=user_id,
        title="New Chat",
        memory=[msg.model_dump() for msg in memory.chat_memory.messages]
    )

    add_record_to_database(user_conversation)

    response = {"conversation_id": user_conversation.id, "ai_response": ai_response}

    return create_response(CustomStatusCode.SUCCESS.value, SUCCESS_MESSAGE, response), 200

def fetch_llm():
    llm = ChatGroq(
        model="llama3-8b-8192",
        temperature=0.5,
        max_tokens=250,
        timeout=3,
        max_retries=2
    )

    return llm