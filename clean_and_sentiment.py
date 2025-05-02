import pandas as pd
import re
import os
from textblob import TextBlob

def clean_text(text):
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^A-Za-z0-9\s]", "", text)
    return text.lower()

def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

def extract_polarity(text):
    return TextBlob(text).sentiment.polarity

def clean_and_analyze():
    df_r = pd.read_csv("/tmp/data/reddit_data.csv")
    df_y = pd.read_csv("/tmp/data/youtube_data.csv")

    df_r['Platform'] = 'Reddit'
    df_y['Platform'] = 'YouTube'

    df = pd.concat([df_r[['Title', 'Brand', 'Platform']], df_y], ignore_index=True)
    df['Cleaned'] = df['Title'].apply(clean_text)
    df['Sentiment'] = df['Cleaned'].apply(get_sentiment)
    df['Polarity'] = df['Cleaned'].apply(extract_polarity)

    output_path = "/tmp/data/combined_cleaned_data.csv"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    
    print(" Cleaned + sentiment analysis done")

