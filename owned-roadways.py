import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("accident2020.csv", encoding_errors='replace')
df = pd.DataFrame(data)