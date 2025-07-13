def recommend_maintenance(component: str, failure_prob: float, age_in_days: int) -> dict:
    
    recommendations = {
        "hydraulic": [
            "Check for oil contamination and replace if needed",
            "Inspect seals, valves, and cylinders",
            "Perform pressure testing and replace worn parts"
        ],
        "cooling": [
            "Flush coolant and refill",
            "Inspect radiator and pump for blockage",
            "Replace thermostat if necessary"
        ],
        "mechanical": [
            "Lubricate all rotating joints",
            "Replace worn bearings",
            "Check torque specs for all fasteners"
        ]
    }

    urgency = "High" if failure_prob > 85 or age_in_days > 250 else "Moderate"

    return {
        "component": component,
        "urgency": urgency,
        "actions": recommendations.get(component.lower(), ["Perform full system check"]),
        "next_service_days": 7 if urgency == "High" else 30
    }
