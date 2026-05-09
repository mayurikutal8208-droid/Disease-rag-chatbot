CLASSIFIER_PROMPT = """
You are a classifier node. Classify the following text into one of the categories THEORY or CODE.
Return only 
- THEORY
OR
- CODE
Question: {question}
"""

THEORY_PROMPT = """
You are a theory node. Provide a detailed explanation of the following concept in simple and clear way
Question: {question}
"""

CODE_PROMPT = """
You are a code node. Provide a code implementation and explanation for the following task.
Question: {question}
"""