import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file into a pandas DataFrame
df = pd.read_csv("df_emp_clean_comments.csv")

# Display the first few rows of the DataFrame
print(df.head())

# Visualization 1: Bar chart of highest scores by category
plt.figure(figsize=(10, 6))
sns.countplot(x="Highest score", data=df, order=df["Highest score"].value_counts().index)
plt.xticks(rotation=45, ha='right')
plt.title("Number of Comments by Highest Score Category")
plt.xlabel("Highest Score Category")
plt.ylabel("Number of Comments")
plt.tight_layout()
plt.savefig("highest_score_category.png")  # Save the plot as PNG
plt.close()

# Visualization 2: Histogram of upvotes
plt.figure(figsize=(8, 5))
sns.histplot(df["upvotes"], bins=20, kde=True)
plt.title("Distribution of Upvotes")
plt.xlabel("Upvotes")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("upvotes_distribution.png")  # Save the plot as PNG
plt.close()

# Visualization 3: Pairplot of numerical columns
sns.pairplot(df[["upvotes", "created"]])
plt.title("Pairplot of Upvotes and Created Timestamp")
plt.tight_layout()
plt.savefig("pairplot_upvotes_created.png")  # Save the plot as PNG
plt.close()
