#!/usr/bin/python3
def number_of_subscribers(sub):
    import requests

    response = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(sub),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if response.status_code >= 300:
        return 0

    return response.json().get("data").get("subscribers")
