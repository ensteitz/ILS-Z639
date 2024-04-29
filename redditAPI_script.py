#  Import praw and pandas (PRAW: The Python Reddit API Wrapper, PANDAS: for data visualization)
import praw
import pandas as pd
from datetime import datetime, timedelta

# Creating an app: https://old.reddit.com/prefs/apps
# Get personal use script (14ch) and secret (27ch)

# Create a reddit object
reddit = praw.Reddit(
	client_id="9eaZgAHFqJAkFbK6fFJAMg", \
	client_secret="o1hw9hNDdt_JfYQJg0_37A2lwaQ6gA", \
	password="password", \
	user_agent="Project to analyze public sentiment about the Israel/Palestine war by /u/fallenfloral", \
	username="fallenfloral")
# Connect to a subreddit
subreddit = reddit.subreddit('r/IsraelPalestine')

# Getting submissions

submissions = subreddit.search('Palestine')
submissions = subreddit.new(limit=2000)

# Select a specific submission
submission = reddit.submission(id='1bk96ug')
print(submission.author)

# Print some info about the submission
print("ID: ", submission.id)
print("Name: ", submission.name)
print("Title: ", submission.title)
print("Upvote Ratio: ", submission.upvote_ratio)
print("Num of Comments: ", submission.num_comments)

# Print out the title of each submission as well as some attributes
for submission in submissions:
	print(submission.title+", "+str(submission.num_comments))
	# Output: the title of the submission and it's comment number
	print(submission.score)
	# Output: the submission's score
	print(submission.id)
	# Output: the submission's ID
	print(submission.url)
	# Output: the URL the submission points to or the submission's URL if it's a self post

#(list of submission attributes: https://praw.readthedocs.io/en/latest/code_overview/models/submission.html)
"""
Put in some code here about submission attributes
"""

# Print the comments under a submission. replace_more gets rid of "more comments"

submission.comments.replace_more(limit=None)
for comment in submission.comments:
	print(comment.body)

# Now that "more comments" is gone, we can start printing comments

submission.comments.replace_more(limit=None)
for top_level_comment in submission.comments:
    print(top_level_comment.body)
