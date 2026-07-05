import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY not found in environment variables. Please set it in your .env file.")

keyword = input("Enter a keyword to search for news articles:")

url = f"https://newsapi.org/v2/everything?q={keyword}&sortBy=publishedAt&apiKey={API_KEY}"