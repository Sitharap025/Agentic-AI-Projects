import streamlit as st
import ast
import json
import requests

st.title("Maintenance AI Advisor")

# JSON input box
raw_json = st.text_area("Paste sensor data (JSON):", height=200)

if st.button("Get Diagnosis & Advice"):
    try:
        sensor_dict = json.loads(raw_json)

        # Send parsed dict directly (no need to wrap as a string)
        response = requests.post("http://localhost:8000/analyze", json={"sensor_data": sensor_dict})


        if response.status_code == 200:
            result = response.json()
            st.subheader("🔍 Failure Probability")
            st.write(f"{result['failure_probability']}%")

            st.subheader("🛠️ Diagnosis")
            st.write(result['diagnosis'])

            st.subheader("📄 Recommendation")
            st.markdown(result['recommendation'])
        else:
            st.error(f"Backend error: {response.text}")

    except json.JSONDecodeError:
        st.error("Invalid JSON. Please check your input.")




