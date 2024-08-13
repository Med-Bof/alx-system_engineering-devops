#!/usr/bin/python3
"""Task 1"""


def top_ten(sub):
    """Returns the top 10 hot posts
    of the subreddit"""
    import requests

    response = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                            .format(sub),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if response.status_code >= 300:
        print('None')
    else:
        [print(item.get("data").get("title"))
         for item in response.json().get("data").get("children")]
