import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ast

plt.rcParams['lines.markersize'] = 2

# Load the CSV file into a pandas DataFrame
df = pd.read_csv("df_emp_extralabels_clean_comments.csv")

# Display the first few rows of the DataFrame
print(df.head())

# 1. Visualization: Bar chart of highest scores by category
plt.figure(figsize=(10, 6))
sns.countplot(x="Top Empath Category", data=df, order=df["Top Empath Category"].value_counts().index)
plt.xticks(rotation=45, ha='right')
plt.title("Number of Comments by Highest Score Category")
plt.xlabel("Top Empath Category")
plt.ylabel("Number of Comments")
plt.tight_layout()
plt.savefig("empath_category_by_commentnum.png")  # Save the plot as PNG
plt.close()

# 1.5 Visualization: Bar chart of highest scores by category
plt.figure(figsize=(10, 6))
sns.countplot(x="Second Empath Category", data=df, order=df["Second Empath Category"].value_counts().index)
plt.xticks(rotation=45, ha='right')
plt.title("Number of Comments by Highest Score Category")
plt.xlabel("Second Empath Category")
plt.ylabel("Number of Comments")
plt.tight_layout()
plt.savefig("empath_category_by_commentnum_second.png")  # Save the plot as PNG
plt.close()

# 2. Visualization: Histogram of upvotes
plt.figure(figsize=(8, 5))
sns.histplot(df["upvotes"], bins=20, kde=True)
plt.title("Distribution of Upvotes")
plt.xlabel("Upvotes")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("upvotes_distribution.png")  # Save the plot as PNG
plt.close()

# 3. Visualization: Pairplot of numerical columns
sns.pairplot(df[["upvotes", "time_of_day"]])
plt.title("Pairplot of Upvotes and Created Timestamp")
plt.tight_layout()
plt.savefig("pairplot_upvotes_created.png")  # Save the plot as PNG
plt.close()

# 4. Visualization: Scatter plot of upvotes vs time of day
time_of_day_categories = ["Early Morning", "Morning", "Afternoon", "Evening", "Night"]

# Group by "time_of_day" and calculate the mean of "Upvotes" for each category
time_of_day_upvotes_mean = df.groupby("time_of_day")["upvotes"].mean().reindex(time_of_day_categories)

# Create a bar graph
plt.figure(figsize=(10, 6))
sns.barplot(x=time_of_day_upvotes_mean.index, y=time_of_day_upvotes_mean.values, palette="viridis")
plt.title("Mean Upvotes by Time of Day")
plt.xlabel("Time of Day")
plt.ylabel("Mean Upvotes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("mean_upvotes_by_time_of_day.png")  # Save the plot as PNG
plt.close()


# 5. Group by "Top Empath Category" and calculate the mean of "Upvotes" for each category
category_upvotes_mean = df.groupby("Top Empath Category")["upvotes"].mean().reset_index()

# Sort the data by the mean of "Upvotes" in descending order for better visualization
category_upvotes_mean = category_upvotes_mean.sort_values(by="upvotes", ascending=False)

# Create a bar graph
plt.figure(figsize=(10, 6))
plt.bar(category_upvotes_mean["Top Empath Category"], category_upvotes_mean["upvotes"], color='skyblue')
plt.xlabel("Top Empath Category")
plt.ylabel("Mean Upvotes")
plt.title("Mean Upvotes by Top Empath Category")
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent overlapping labels
plt.savefig("upvotes_for_top_empath_category.png")
plt.show()
