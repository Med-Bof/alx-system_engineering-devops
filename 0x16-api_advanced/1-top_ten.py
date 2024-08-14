#!/usr/bin/python3
"""Task 1"""
import requests

def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "python:subreddit.top.ten:v1.0.0 (by /u/Med-Bof)"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            posts = response.json().get("data", {}).get("children", [])
            for post in posts:
                print(post.get("data", {}).get("title"))
        else:
            print(None)
    except requests.RequestException:
        print(None)
