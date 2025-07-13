import pandas as pd
import numpy as np


n=1000

df= pd.DataFrame({
    "Machine_ID": np.random.choice(["M001", "M002", "M003"], n),
    "Temperature": np.random.normal(70, 5, n),
    "Vibration": np.random.normal(0.5, 0.1, n),
    "Pressure": np.random.normal(3.5, .5, n),
    "RPM": np.random.normal(2500, 3200, n),
    "Oil_Viscosity": np.random.normal(8.5, 1, n),
    "Age_in_Days": np.random.randint(30, 500, n),
})

df["Failure"] = np.where(
    (df["Temperature"] > 78) | 
    (df["Vibration"] > 0.65) | 
    (df["Pressure"] < 3) | 
    (df["RPM"] > 3000) | 
    (df["Oil_Viscosity"] < 7) | 
    (df["Age_in_Days"] > 350), 
    1, 0
)

df.to_csv("dataset/machine_data.csv", index=False)
print("Simulated data saved to dataset/machine_data.csv")