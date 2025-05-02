import requests
import pandas as pd
import os

def fetch_youtube_data():
    API_KEY = "abcd"

    brands = ['iPhone 15', 'Galaxy S24', 'Pixel 8']
    all_titles = []

    for brand in brands:
        query = f"{brand} review"
        url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&maxResults=20&type=video&key={API_KEY}"
        response = requests.get(url).json()
        for item in response['items']:
            title = item['snippet']['title']
            all_titles.append([title, brand])

    df = pd.DataFrame(all_titles, columns=['Title', 'Brand'])
    output_path = "/tmp/data/youtube_data.csv"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    df.to_csv(output_path, index=False)
    print(" YouTube data saved to /tmp/data/youtube_data.csv")
