import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Scripts.model_predict import predict_failure
from agents.diagnostic_agent import diagnose_component
from agents.retrieve_docs import retrieve_similar_docs
from agents.maintenance_agent import recommend_maintenance


def run_pipeline(sensor_data: dict):
    print("\nRunning ML Prediction...")
    failure_prob = predict_failure(sensor_data)
    print(f"Predicted failure probability: {failure_prob:.2f}%")

    if failure_prob > 70:
        print("\nRunning Diagnostic Agent...")
        diagnosis = diagnose_component(sensor_data)
        component = diagnosis['component']
        reason = diagnosis['reason']
        print(f"Component at risk: {component}")
        print(f"Reason: {reason}")

        print("\n Invoking RAG Agent for knowledge retrieval...")
        query = f"How to maintain and prevent failure in {component} system?"
        docs = retrieve_similar_docs(query)
        top_doc = docs[0][1] if isinstance(docs[0], tuple) else docs[0].page_content
        print(f"\nTop Retrieved Doc Snippet:\n{top_doc[:1000]}")
        
        print("\nRecommending Maintenance Actions...")
        maintenance = recommend_maintenance(component, failure_prob, sensor_data.get("Age_in_Days", 0))
        print(f"Urgency: {maintenance['urgency']}")
        print("Recommended Actions:")
        for action in maintenance["actions"]:
            print(f"- {action}")
        print(f"Next Service Due in: {maintenance['next_service_days']} days")



# Example input
if __name__ == "__main__":
    test_data = {
        "Machine_ID": "M001",
        "Temperature": 60,
        "Vibration": 0.55,
        "Pressure": 2.5,
        "RPM": 3100,
        "Oil_Viscosity": 6,
        "Age_in_Days": 300,
        "torque": 81.2,
        "tool_wear": 50,
        "coolant_temperature": 110,
        "hydraulic_pressure": 25
    }

    run_pipeline(test_data)
