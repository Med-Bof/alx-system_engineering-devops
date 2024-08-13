#!/usr/bin/python3
import requests

def get_subscriber_count(subreddit_name):
    api_url = "https://www.reddit.com/r/{}/about.json".format(subreddit_name)
    request_headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(api_url, headers=request_headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    response_data = response.json().get("data")
    return response_data.get("subscribers")
