import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the JSON file
df = pd.read_json("sales.json")

# Plot a lineplot showing sales per product over months
plt.figure(figsize=(8, 5))
sns.lineplot(data=df, x='Month', y='Sales', hue='Product', marker='o')

plt.title("Product Sales Over Months")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.show()
