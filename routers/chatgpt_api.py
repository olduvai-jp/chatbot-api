from fastapi import APIRouter
from pydantic import BaseModel
from chatgpt import ChatGPT, ChatGPTRole, ChatGPTInput
import os

router = APIRouter()

# body = [{
#    "role": "user",
#    "message": "Hello, how are you?"
# }, {
#    "role": "assistant",
#    "message": "I am fine, thank you. How are you?"
# }]

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

class Message(BaseModel):
    role: str
    message: str

@router.post("/chatgpt/chatbot")
async def chatgpt_message(body: list[Message]):
    print(body)
    chatgpt = ChatGPT(token=OPENAI_API_KEY)

    messages = [
        chatgpt.create_message(role=ChatGPTRole.system, content="You are a very competent chatbot. You provide precise answers to any question."),
    ]

    for message in body:
        messages.append(chatgpt.create_message(role=message.role, content=message.message))

    inputs = ChatGPTInput(messages)
    reply = chatgpt.chat(inputs)

    return Message(role=ChatGPTRole.assistant, message=reply)

@router.post("/chatgpt/raw")
async def chatgpt_message(body: list[Message]):
    print(body)
    chatgpt = ChatGPT(token=OPENAI_API_KEY)

    messages = []

    for message in body:
        messages.append(chatgpt.create_message(role=message.role, content=message.message))

    inputs = ChatGPTInput(messages)
    reply = chatgpt.chat(inputs)

    return Message(role=ChatGPTRole.assistant, message=reply)

@router.post("/chatgpt/gpt4")
async def chatgpt_message(body: list[Message]):
    print(body)
    chatgpt = ChatGPT(token=OPENAI_API_KEY, model="gpt-4")

    messages = []

    for message in body:
        messages.append(chatgpt.create_message(role=message.role, content=message.message))

    inputs = ChatGPTInput(messages)
    reply = chatgpt.chat(inputs)

    return Message(role=ChatGPTRole.assistant, message=reply)
