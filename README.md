# Predictive Maintenance Pipeline

This project implements a predictive maintenance pipeline using a modular, agent-based architecture. It leverages sensor data to predict failures, diagnose issues, retrieve relevant documentation, and provide actionable recommendations.

## Project Structure

```
requirements.txt
agents/
    __init__.py
    advisor_agent.py
    agent_retrieve.py
    diagnostic_agent.py
    maintenance_agent.py
    retrieve_docs.py
dataset/
    machine_data.csv
embeddings/
model/
myenv/
pipeline/
rag_docs/
Scripts/
vectorstore_index/
```

- **agents/**: Contains agent modules for diagnosis, document retrieval, and advisory logic.
- **dataset/**: Includes datasets and supporting documents for model training and evaluation.
- **pipeline/**: Contains the main pipeline script ([pipeline/langGraph_pipeline.py](pipeline/langGraph_pipeline.py)).
- **Scripts/**: Utility scripts, including model prediction logic.
- **embeddings/**, **model/**, **vectorstore_index/**: For storing models, embeddings, and vector indices.
- **myenv/**: Python virtual environment (not tracked in version control).

## Main Pipeline

The core pipeline is implemented in [`pipeline/langGraph_pipeline.py`](pipeline/langGraph_pipeline.py) using [LangGraph](https://github.com/langchain-ai/langgraph). It consists of the following steps:

1. **Prediction**: Predicts failure probability from sensor data using [`Scripts/model_predict.py`](Scripts/model_predict.py).
2. **Diagnosis**: Diagnoses the likely component and reason for failure using [`agents/diagnostic_agent.py`](agents/diagnostic_agent.py).
3. **Document Retrieval**: Retrieves relevant maintenance documents using [`agents/retrieve_docs.py`](agents/retrieve_docs.py).
4. **Advisory**: Provides actionable recommendations using [`agents/advisor_agent.py`](agents/advisor_agent.py).

## Usage

1. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

2. **Run the pipeline**:
    ```sh
    python pipeline/langGraph_pipeline.py
    ```

3. **Sample Output**:
    ```
    --- Pipeline Result ---
    Failure Probability: 12.34%
    Diagnosis: {'component': 'Hydraulic Pump', 'reason': 'High Vibration'}
    Retrieved Docs: 3 documents
    Recommendation: Replace hydraulic pump and check for leaks.
    -------------------------
    ```

## Customization

- Add or modify agents in the `agents/` directory to extend pipeline capabilities.
- Update datasets in `dataset/` for improved model accuracy.
- Adjust the pipeline flow in [`pipeline/langGraph_pipeline.py`](pipeline/langGraph_pipeline.py) as needed.

## Requirements

- Python 3.9+
- See [`requirements.txt`](requirements.txt) for full dependency list.

## License

This project is licensed under the MIT License.

---

*For questions or contributions, please open an issue or pull request*