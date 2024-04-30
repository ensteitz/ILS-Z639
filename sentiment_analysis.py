from empath import Empath
import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv("df_clean_comments.csv")

# Call Empath with the desired categories
lexicon = Empath()

# Perform sentiment analysis on the "body" column for the specified categories
sentiment_scores = df["body"].apply(lambda x: lexicon.analyze(x, categories=["discontent", "happiness", "optimism", "social_media", "anticipation", "dispute", "irritability", "politics", "aggression", "sadness", "exasperation", "deception"], normalize=True))

# Function to get top two categories with highest scores
def get_top_categories(scores):
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top_categories = [category for category, score in sorted_scores[:2]]
    return top_categories

# Calculate highest and second-highest categories and scores for each row
df["Top Empath Reading"] = sentiment_scores.apply(lambda x: ' '.join([f"{category} ({score})" for category, score in sorted(x.items(), key=lambda item: item[1], reverse=True)[:1]]))
df["Second Empath Reading"] = sentiment_scores.apply(lambda x: ' '.join([f"{category} ({score})" for category, score in sorted(x.items(), key=lambda item: item[1], reverse=True)[:2][1:]]))

# Print the modified DataFrame with new columns
print(df)

# Save the data frame in a new file
df.to_csv("df_emp_clean_comments.csv", index=False)
