import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("easy.csv")
sns.set(style="whitegrid")

numeric_df = df.select_dtypes(include=['int64', 'float64'])

if not numeric_df.empty:
    sns.pairplot(numeric_df)
    plt.suptitle("Pairplot of Numeric Columns", y=1.02)
    plt.show()

if not numeric_df.empty:
    corr = numeric_df.corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()

for col in numeric_df.columns:
    sns.histplot(df[col], kde=True)
    plt.title(f"Distribution of {col}")
    plt.show()

for col in numeric_df.columns:
    sns.boxplot(x=df[col])
    plt.title(f"Boxplot of {col}")
    plt.show()
