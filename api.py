import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY not found in environment variables. Please set it in your .env file.")

keyword = input("Enter a keyword to search for news articles:")

url = f"https://newsapi.org/v2/everything?q={keyword}&pageSize=5&apiKey={API_KEY}"
request = requests.get(url)

if request.status_code == 200:
    data = request.json()
    articles = data.get("articles")
    print(data)
    print(f"Top Headlines")
    for i, articel in enumerate(articles, start=1):
        print(f"{i}: Author: {articel["author"]}\n Title: {articel["title"]}")
        print(f"\nDescription: {articel["description"]}")
        print(f"\nPublishedAt: {articel["publishedAt"]}")
        print(f"\nContent: {articel["content"]}")
        print("-" * 60)
else:
    print("request is not going through the Url")