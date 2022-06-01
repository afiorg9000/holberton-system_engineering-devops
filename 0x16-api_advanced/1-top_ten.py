#!/usr/bin/python3
"""top_tenfunction"""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts"""
    if subreddit is None or type(subreddit) is not str:
        print(None)
    request = requests.get('http://www.reddit.com/r/{}/hot.json'
                           .format(subreddit),
                           headers={'User-Agent': 'Python/requests:APIproject:\
                     v1.0.0 (by /u/aaorrico23)'},
                           params={'limit': 10}).json()
    posts = request.get('data', {}).get('children', None)
    if posts is None:
        print(None)
    else:
        for p in posts:
            print(p.get('data', {}).get('title', None))
