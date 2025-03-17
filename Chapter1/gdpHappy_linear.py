import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

# Data prepare
data_root = "https://github.com/ageron/data/raw/main"
lifesat = pd.read_csv(data_root + "lifesat/lifesat.csv")
X = lifesat[["GDP per capita (USD)"]].values
y = lifesat[["Life satisfaction"]].values

# 