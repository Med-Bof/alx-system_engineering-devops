#!/usr/bin/python3
"""Task 2"""

import requests

def recurse(subreddit, hot_list=[]):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "python:subreddit.recurse:v1.0.0 (by /u/Med-Bof)"}
    params = {"limit": 100, "after": None if not hot_list else hot_list[-1]}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return None

        data = response.json().get("data", {})
        after = data.get("after")
        posts = data.get("children", [])

        for post in posts:
            hot_list.append(post.get("data", {}).get("title"))

        if after:
            return recurse(subreddit, hot_list)
        else:
            return hot_list if hot_list else None

    except requests.RequestException:
        return None
