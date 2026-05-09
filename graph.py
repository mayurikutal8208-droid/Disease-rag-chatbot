from langgraph.graph import StateGraph, END

from app.state import AgentState

from app.nodes import (classifier_node, theory_node, code_node)

## Workflow is being stitched together using "workflow"
workflow = StateGraph(AgentState)

## Adding nodes 1 by 1
workflow.add_node("classifier", classifier_node)
workflow.add_node("theory", theory_node)
workflow.add_node("code", code_node)

## Setting the entry point for the workflow
workflow.set_entry_point("classifier")

def router(state):
    if state["question_type"] == "THEORY":
        return "theory"
    elif state["question_type"] == "CODE":
        return "code"
    else:
        raise ValueError("Invalid question type")
    
workflow.add_conditional_edges("classifier", router)

## Now we will add edges
workflow.add_edge("theory", END)
workflow.add_edge("code", END)

## Now our graph is complete

##  Final step after building graph is to initiate it using compile

graph = workflow.compile()