from pipeline.langGraph_pipeline import flow

def get_recommendation(sensor_input:str):
    
    # Execute the flow with the provided sensor data
    result=flow.invoke({"sensor_data": sensor_input})
    
    return {
        "diagnosis": f"{result['diagnosis']}",
        "recommendation":f"{result['recommendation']}"
    }