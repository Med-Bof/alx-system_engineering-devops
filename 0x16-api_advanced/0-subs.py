#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    api_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    request_headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(api_url, headers=request_headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    response_data = response.json().get("data")
    return response_data.get("subscribers", 0)
