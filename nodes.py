from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

from app.prompts import (CLASSIFIER_PROMPT, THEORY_PROMPT, CODE_PROMPT)

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model=os.getenv("MODEL"),
    temperature=0
)



def classifier_node(state):

    prompt = CLASSIFIER_PROMPT.format(question=state["question"])

    result = llm.invoke(prompt)

    return {
        "question_type": result.content.strip()
    }

def theory_node(state):

    prompt = THEORY_PROMPT.format(question=state["question"])

    result = llm.invoke(prompt)

    return {
        "answer": result.content.strip()
    }

def code_node(state):

    prompt = CODE_PROMPT.format(question=state["question"])

    result = llm.invoke(prompt)

    return {
        "answer": result.content.strip()
    }