from typing import TypedDict

class AgentState(TypedDict):
    question: str
    question_type: str
    answer: str