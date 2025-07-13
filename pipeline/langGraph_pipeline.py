
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from langgraph.graph import StateGraph, END
from Scripts.model_predict import predict_failure
from agents.diagnostic_agent import diagnose_component
from agents.retrieve_docs import retrieve_similar_docs
from agents.advisor_agent import advisor_agent


def predict_node(state):
    prob=predict_failure(state["sensor_data"])
    state["failure_probability"] = prob
    return state

def diagnose_node(state):
    diagnose =diagnose_component(state["sensor_data"])
    state["diagnosis"] = diagnose
    return state

def retrieve_docs_node(state):
    query = f"How to maintain and prevent failure in {state['diagnosis']['component']} system?"
    docs = retrieve_similar_docs(query)
    state["retrieved_docs"] = docs
    return state

def advisor_node(state):
    diagnose = state["diagnosis"]
    docs = state["retrieved_docs"]
    advise = advisor_agent(diagnose['component'], diagnose['reason'], docs)
    state["recommendation"] = advise
    return state

graph = StateGraph("Maintenance Pipeline")

graph.add_node("predict", predict_node)
graph.add_node("diagnose", diagnose_node)
graph.add_node("retrieve", retrieve_docs_node)
graph.add_node("advisor", advisor_node)

graph.set_entry_point("predict")

graph.add_edge("predict", "diagnose")
graph.add_edge("diagnose", "retrieve")
graph.add_edge("retrieve", "advisor")
graph.add_edge("advisor", END)

flow = graph.compile()

if __name__ == "__main__":
    sensor_input = {
        "Machine_ID": "M001",
        "Temperature": 82,
        "Vibration": 0.70,
        "Pressure": 3.8,
        "RPM": 3100,
        "Oil_Viscosity": 9.1,
        "Age_in_Days": 300,
        "torque": 81.2,
        "tool_wear": 50,
        "coolant_temperature": 72,
        "hydraulic_pressure": 16
    }

    result = flow.invoke({"sensor_data": sensor_input})
    print("\n--- Pipeline Result ---")
    print(f"Failure Probability: {result['failure_probability']:.2f}%")
    print(f"Diagnosis: {result['diagnosis']}")
    print(f"Retrieved Docs: {len(result['retrieved_docs'])} documents")
    print(f"Recommendation: {result['recommendation']}")
    print("-------------------------")


