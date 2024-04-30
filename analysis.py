import sys
import pandas as pd
import re

# Load the CSV file into a pandas DataFrame
df = pd.read_csv("df_emp_clean_comments.csv")

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

# Print the most frequent categories and their counts
print(f"The most frequent category in 'Highest score' column is '{most_frequent_highest}' with {highest_counts[most_frequent_highest]} occurrences.")
print(f"The most frequent category in 'Second highest' column is '{most_frequent_second_highest}' with {second_highest_counts[most_frequent_second_highest]} occurrences.")
print('\n')

# Extract numerical scores from "Highest score" column and calculate average
highest_scores = []
for value in df["Highest score"]:
    scores = re.findall(r"\((\d+\.\d+)\)", value)
    scores = [float(score) for score in scores]
    highest_scores.extend(scores)

# Calculate average of numerical scores in "Highest score" column
if highest_scores:
    average_highest_score = sum(highest_scores) / len(highest_scores)
    print(f"The average numerical score in 'Highest score' column is {average_highest_score:.2f}")
else:
    print("No numerical scores found in 'Highest score' column.")

# Extract numerical scores from "Second highest" column and calculate average
second_highest_scores = []
for value in df["Second highest"]:
    scores = re.findall(r"\((\d+\.\d+)\)", value)
    scores = [float(score) for score in scores]
    second_highest_scores.extend(scores)

# Calculate average of numerical scores in "Second highest" column
if second_highest_scores:
    average_second_highest_score = sum(second_highest_scores) / len(second_highest_scores)
    print(f"The average numerical score in 'Second highest' column is {average_second_highest_score:.2f}")
else:
    print("No numerical scores found in 'Second highest' column.")
print('\n')

# Extract numerical scores from "Highest score" column and find highest and lowest scores
highest_scores = []
for value in df["Highest score"]:
    scores = re.findall(r"\((\d+\.\d+)\)", value)
    scores = [float(score) for score in scores]
    highest_scores.extend(scores)

if highest_scores:
    highest_score_highest = max(highest_scores)
    lowest_score_highest = min(highest_scores)
    print(f"The highest numerical score in 'Highest score' column is {highest_score_highest:.2f}")
    print(f"The lowest numerical score in 'Highest score' column is {lowest_score_highest:.2f}")
else:
    print("No numerical scores found in 'Highest score' column.")
print('\n')

# Extract numerical scores from "Second highest" column and find highest and lowest scores
second_highest_scores = []
for value in df["Second highest"]:
    scores = re.findall(r"\((\d+\.\d+)\)", value)
    scores = [float(score) for score in scores]
    second_highest_scores.extend(scores)

if second_highest_scores:
    highest_score_second_highest = max(second_highest_scores)
    lowest_score_second_highest = min(second_highest_scores)
    print(f"The highest numerical score in 'Second highest' column is {highest_score_second_highest:.2f}")
    print(f"The lowest numerical score in 'Second highest' column is {lowest_score_second_highest:.2f}")
else:
    print("No numerical scores found in 'Second highest' column.")
