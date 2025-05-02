import praw
import pandas as pd
import os

def fetch_reddit_data():
    reddit = praw.Reddit(
        client_id="abcd",
        client_secret="abcd",
        user_agent="pmg_sentiment_project"
    )

    posts = []
    for brand in ['iPhone 15', 'Galaxy S24', 'Pixel 8']:
        for post in reddit.subreddit("technology").search(brand, sort='new', limit=30):
            posts.append([post.title, post.selftext, post.score, brand])

    df = pd.DataFrame(posts, columns=['Title', 'Text', 'Score', 'Brand'])
    output_path = "/tmp/data/reddit_data.csv"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    df.to_csv(output_path, index=False)
    print(" Reddit data saved to /tmp/data/reddit_data.csv")
    print(" Number of posts fetched:", len(df))
    print(" File exists after save?", os.path.exists(output_path))
    
