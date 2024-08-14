#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    for a given subreddit. If the subreddit is invalid, return 0."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "python:subreddit.subscriber.count:v1.0.0 (by /u/your_username)"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get("data", {})
            return data.get("subscribers", 0)
        else:
            return 0
    except requests.RequestException:
        return 0
