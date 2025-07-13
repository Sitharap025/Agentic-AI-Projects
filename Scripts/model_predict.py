import pandas as pd
import joblib

# Load model once
model = joblib.load('model/xgb_model.pkl')

def map_sensor_to_model_input(sensor_data: dict) -> pd.DataFrame:
    """
    Maps raw sensor input to the expected model input format.
    Fills missing values with defaults or dummy values.
    """
    # Use defaults or estimate from domain knowledge
    model_input = {
        "Machine_ID": "M001",
        "Temperature": sensor_data.get("coolant_temperature", 75),
        "Vibration": sensor_data.get("vibration", 0.7),
        "Pressure": sensor_data.get("hydraulic_pressure", 3.5),
        "RPM": sensor_data.get("torque", 3000),  # Assuming torque maps loosely to RPM
        "Oil_Viscosity": 9.0,  # Could be estimated or fixed
        "Age_in_Days": 250     # Assume average machine age if unknown
    }
    return pd.DataFrame([model_input])

def predict_failure(sensor_data: dict) -> float:
    df_input = map_sensor_to_model_input(sensor_data)
    prob = model.predict_proba(df_input)[0][1]
    return round(prob * 100, 2)