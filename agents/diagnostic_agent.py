
def diagnose_component(sensor_data: dict) -> dict:
    """
    Diagnoses the component likely at fault based on sensor thresholds.
    
    Args:
        sensor_data (dict): Dictionary containing sensor readings.
        
    Returns:
        dict: Component name and reason for failure detection.
    """
    
    # Example thresholds — tweak as per your domain knowledge
    if sensor_data.get("hydraulic_pressure", 100) < 20:
        return {
            "component": "hydraulic",
            "reason": "Hydraulic pressure is below operational threshold."
        }
    
    elif sensor_data.get("coolant_temperature", 0) > 90:
        return {
            "component": "cooling",
            "reason": "Coolant temperature exceeds safe limit."
        }
    
    elif sensor_data.get("torque", 0) > 80:
        return {
            "component": "mechanical",
            "reason": "Excessive torque detected."
        }
    
    elif sensor_data.get("vibration", 0) > 1.0:
        return {
            "component": "mechanical",
            "reason": "Abnormal vibration levels detected."
        }
    
    else:
        return {
            "component": "unknown",
            "reason": "No abnormal conditions detected in monitored parameters."
        }
