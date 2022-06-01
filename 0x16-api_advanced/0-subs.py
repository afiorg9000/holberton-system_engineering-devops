!/usr/bin/python3
"""queries the Reddit AP """
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    request = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
               headers={'User-Agent': 'Python/requests:APIproject:
                        v1.0.0 (by /u/aaorrico23)'}).json()
            subscribers = request.get("data", {}).get("subscribers", 0)
    return subscribers
