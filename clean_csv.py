import sys
import pandas as pd

# Creating a path
file_path = 'df_comments.csv'

# Read the CSV file into a pandas data frame
df = pd.read_csv(file_path)

#df['body'] = df['body'].str.lstrip('>')

# Define the phrases to search for
phrases_to_search = [
    "Please avoid using profanities to make a point or emphasis",
    "https://",
    "this action was performed automatically",
    "I'm a bot",
    "comments and analogies are inflammatory",
    "post is getting locked"
]

# Create a regular expression pattern to match any them
pattern = '|'.join(phrases_to_search)

# Filter the data frame to remove rows containing any of the specified phrases
df_clean = df[~df['body'].str.contains(pattern, case=False, na=False)]

df_clean = df_clean[df_clean['body'].notnull() & (df_clean['body'] != '')]

# Save the filtered data frame back to a CSV file
df_clean.to_csv('df_clean_comments.csv', index=False)

print(df_clean)
