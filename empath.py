import sys
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import string
import datetime
import seaborn as sns
import matplotlib as plt

analyser = SentimentIntensityAnalyzer()


# Create a variable to use to open the file with the sentences for sentiment analysis
txt = open("clean_comments.txt", "r")

# Create a variable to store the text of the reddit post (comments and replies) for the individual sentences (not per users' post)
txt_write = open("sa_clean_comments.txt", "w")
