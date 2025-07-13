
from fastapi import FastAPI
from pydantic import BaseModel
from pipeline.langGraph_pipeline import flow
from fastapi.middleware.cors import CORSMiddleware
import json
from typing import Dict 


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],
    allow_headers=["*"],
)

class SensorInput(BaseModel):
    sensor_data: Dict


@app.post("/analyze")
def analyze(sensor: SensorInput):
    result = flow.invoke({"sensor_data": sensor.sensor_data})

    return {
        "failure_probability": float(result.get("failure_probability", 0)),  
        "diagnosis": str(result.get("diagnosis", "")),                       
        "recommendation": str(result.get("recommendation", ""))              
    }
