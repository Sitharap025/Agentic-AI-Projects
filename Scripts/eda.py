import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df= pd.read_csv("dataset/machine_data.csv")

df.describe()
df.info()
# Visualizing the distribution of numerical features
numerical_features = df.select_dtypes(include=[np.number]).columns.tolist()
for feature in numerical_features:  
    plt.figure(figsize=(10, 6))
    plt.hist(df[feature], bins=30, alpha=0.7, color='blue')
    plt.title(f'Distribution of {feature}')
    plt.xlabel(feature)
    plt.ylabel('Frequency')
    plt.grid(axis='y', alpha=0.75)
    plt.show()

