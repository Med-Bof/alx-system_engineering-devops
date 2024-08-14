#!/usr/bin/python3
""" Task 100"""


def count_words(subreddit, word_list, after="", counts=None):
    """Function to count words in all hot posts of a given Reddit subreddit."""
    if counts is None:
        counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "python:subreddit.keyword.counter:v1.0.0 (by /u/Med-Bof)"}
    params = {"after": after, "limit": 100}
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return
        
        data = response.json().get("data")
        posts = data.get("children", [])
        after = data.get("after")

        for post in posts:
            title = post.get("data", {}).get("title", "").lower().split()
            for word in word_list:
                word_lower = word.lower()
                counts[word_lower] = counts.get(word_lower, 0) + title.count(word_lower)

        if after:
            count_words(subreddit, word_list, after, counts)
        else:
            if counts:
                sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_counts:
                    if count > 0:
                        print(f"{word}: {count}")
    
    except requests.RequestException:
        return
