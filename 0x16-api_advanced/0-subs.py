#!/usr/bin/python3
"""task 0"""


def number_of_subscribers(subreddit):
    """Returns the number of subscribers
    to the subreddit"""
    import requests

    subscrib_info = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "Med"},
                            allow_redirects=False)
    if subscrib_info.status_code >= 300:
        return 0

    return subscrib_info.json().get("data").get("subscribers")
