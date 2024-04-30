import sys
import pandas as pd
import re

# Load the CSV file into a pandas DataFrame
df = pd.read_csv("df_emp_clean_comments.csv", parse_dates=["timestamp"])

# Get rid of this column
df.drop("created", axis=1, inplace=True)

# Extract numerical values from "Highest score" column
df["Top Empath Score"] = df["Top Empath Reading"].apply(lambda x: re.search(r"\((\d+\.\d+)\)", str(x)).group(1) if re.search(r"\((\d+\.\d+)\)", str(x)) else None)

# Extract numerical values from "Lowest score" column
df["Second Empath Score"] = df["Second Empath Reading"].apply(lambda x: re.search(r"\((\d+\.\d+)\)", str(x)).group(1) if re.search(r"\((\d+\.\d+)\)", str(x)) else None)

# Define the list of possible categories
possible_categories = ["discontent", "happiness", "optimism", "social_media", "anticipation",
                       "dispute", "irritability", "politics", "aggression", "sadness",
                       "exasperation", "deception"]

# Function to extract category name from the "score" string
def extract_category(score_str):
    for category in possible_categories:
        if category in score_str:
            return category
    return None

# Extract category names from "Highest score" column
df["Top Empath Category"] = df["Top Empath Reading"].apply(lambda x: extract_category(str(x)))

# Extract category names from "Second highest" column
df["Second Empath Category"] = df["Second Empath Reading"].apply(lambda x: extract_category(str(x)))

# Gives you the chart so you can see what it looks like now
print(df.head())




# Initialize dictionaries to store counts of each category in "Top Empath Category" and "Second Empath Category"
top_category_counts = {category: 0 for category in possible_categories}
second_category_counts = {category: 0 for category in possible_categories}

# Iterate over the "Top Empath Category" column and count occurrences of each category
for category in df["Top Empath Category"]:
    if category in possible_categories:
        top_category_counts[category] += 1

# Iterate over the "Second Empath Category" column and count occurrences of each category
for category in df["Second Empath Category"]:
    if category in possible_categories:
        second_category_counts[category] += 1

# Print the counts of each category in "Top Empath Category" and "Second Empath Category"
print("Counts of categories in 'Top Empath Category':")
print(top_category_counts)
print("\nCounts of categories in 'Second Empath Category':")
print(second_category_counts)



# When was the first and last comment posted
print("The first comment was posted on:")
print(df["timestamp"].min())
print('\n')

print("The last comment was posted on:")
print(df["timestamp"].max())
print('\n')

# How much time passed between the first and last comments
print("This is how much time passed between the first and last comments:")
print(df["timestamp"].max() - df["timestamp"].min())
print('\n')


# Initialize dictionaries to count occurrences of each category in "Highest score" and "Second highest" columns
highest_counts = {category: 0 for category in possible_categories}
second_highest_counts = {category: 0 for category in possible_categories}

# Iterate over the "Highest score" column and count occurrences of each category
for value in df["Top Empath Reading"]:
    for category in possible_categories:
        if category in value:
            highest_counts[category] += 1

# Iterate over the "Second highest" column and count occurrences of each category
for value in df["Top Empath Reading"]:
    for category in possible_categories:
        if category in value:
            second_highest_counts[category] += 1

# Find the most frequent category in "Top Empath Reading" column
most_frequent_highest = max(highest_counts, key=highest_counts.get)

# Find the most frequent category in "Second Empath Reading" column
most_frequent_second_highest = max(second_highest_counts, key=second_highest_counts.get)

# Print the most frequent categories and their counts
print(f"The most frequent category in 'Highest score' column is '{most_frequent_highest}' with {highest_counts[most_frequent_highest]} occurrences.")
print(f"The most frequent category in 'Second highest' column is '{most_frequent_second_highest}' with {second_highest_counts[most_frequent_second_highest]} occurrences.")



'''
HERE to.....
# Define the list of possible categories
possible_categories = ["discontent", "happiness", "optimism", "social_media", "anticipation",
                       "dispute", "irritability", "politics", "aggression", "sadness",
                       "exasperation", "deception"]

# Initialize dictionaries to count occurrences of each category in "Highest score" and "Second highest" columns
highest_counts = {category: 0 for category in possible_categories}
second_highest_counts = {category: 0 for category in possible_categories}

# Iterate over the "Highest score" column and count occurrences of each category
for value in df["Highest score"]:
    for category in possible_categories:
        if category in value:
            highest_counts[category] += 1

# Iterate over the "Second highest" column and count occurrences of each category
for value in df["Second highest"]:
    for category in possible_categories:
        if category in value:
            second_highest_counts[category] += 1

# Find the most frequent category in "Highest score" column
most_frequent_highest = max(highest_counts, key=highest_counts.get)

# Find the most frequent category in "Second highest" column
most_frequent_second_highest = max(second_highest_counts, key=second_highest_counts.get)




this has problem --
# Add new columns to the DataFrame for "Highest count" and "Second highest count"
df["Highest count"] = [highest_counts[category] for category in df["Highest score"]]
df["Second highest count"] = [second_highest_counts[category] for category in df["Second highest"]]
-- problm






# Save the updated DataFrame to a new CSV file
df.to_csv("df_emp_extralabels_clean_comments_updated.csv", index=False)
print("Updated DataFrame saved to df_emp_clean_comments_updated.csv")

'''




# Print the most frequent categories and their counts
print(f"The most frequent category in 'Top Empath Reading' column is '{most_frequent_highest}' with {highest_counts[most_frequent_highest]} occurrences.")
print(f"The most frequent category in 'Second Empath Reading' column is '{most_frequent_second_highest}' with {second_highest_counts[most_frequent_second_highest]} occurrences.")
print('\n')

# Extract numerical scores from "Top Empath Reading" column and calculate average
highest_scores = []
for value in df["Top Empath Reading"]:
    scores = re.findall(r"\((\d+\.\d+)\)", value)
    scores = [float(score) for score in scores]
    highest_scores.extend(scores)

# Calculate average of numerical scores in "Top Empath Score" column
if highest_scores:
    average_highest_score = sum(highest_scores) / len(highest_scores)
    print(f"The average numerical score in 'Top Empath Reading' column is {average_highest_score:.2f}")
else:
    print("No numerical scores found in 'Top Empath Reading' column.")

# Extract numerical scores from "Second Empath Reading" column and calculate average
second_highest_scores = []
for value in df["Second Empath Reading"]:
    scores = re.findall(r"\((\d+\.\d+)\)", value)
    scores = [float(score) for score in scores]
    second_highest_scores.extend(scores)

# Calculate average of numerical scores in "Second Top Empath Reading" column
if second_highest_scores:
    average_second_highest_score = sum(second_highest_scores) / len(second_highest_scores)
    print(f"The average numerical score in 'Second Empath Reading' column is {average_second_highest_score:.2f}")
else:
    print("No numerical scores found in 'Second Empath Reading' column.")
print('\n')

# Extract numerical scores from "Top Empath Reading" column and find highest and lowest scores
highest_scores = []
for value in df["Top Empath Reading"]:
    scores = re.findall(r"\((\d+\.\d+)\)", value)
    scores = [float(score) for score in scores]
    highest_scores.extend(scores)

if highest_scores:
    highest_score_highest = max(highest_scores)
    lowest_score_highest = min(highest_scores)
    print(f"The highest numerical score in 'Top Empath Reading' column is {highest_score_highest:.2f}")
    print(f"The lowest numerical score in 'Top Empath Reading' column is {lowest_score_highest:.2f}")
else:
    print("No numerical scores found in 'Top Empath Reading' column.")
print('\n')

# Extract numerical scores from "Second Empath Reading" column and find highest and lowest scores
second_highest_scores = []
for value in df["Second Empath Reading"]:
    scores = re.findall(r"\((\d+\.\d+)\)", value)
    scores = [float(score) for score in scores]
    second_highest_scores.extend(scores)

if second_highest_scores:
    highest_score_second_highest = max(second_highest_scores)
    lowest_score_second_highest = min(second_highest_scores)
    print(f"The highest numerical score in 'Second Empath Reading' column is {highest_score_second_highest:.2f}")
    print(f"The lowest numerical score in 'Second Empath Reading' column is {lowest_score_second_highest:.2f}")
else:
    print("No numerical scores found in 'Second Empath Reading' column.")

# Add the hour column to the data frame
df["hour"] = df["timestamp"].dt.hour

# Define a variable to turn the hours the comments were posted into a time of day
def categorize_time_of_day(hour):
    if hour < 6:
        return "Early Morning"
    elif 6 <= hour < 11:
        return "Morning"
    elif 11 <= hour < 15:
        return "Afternoon"
    elif 15 <= hour < 20:
        return "Evening"
    else:
        return "Night"

# Call the variable and add it to the CSV
df["time_of_day"] = df["hour"].apply(categorize_time_of_day)
print(df.head())
print('\n')

# Specify a new file path to store the results of these new columns
new_CSV = "df_emp_extralabels_clean_comments.csv"

# Save the data frame to a new CSV file
df.to_csv(new_CSV, index=False)

print(f"New data frame saved to '{new_CSV}'")
