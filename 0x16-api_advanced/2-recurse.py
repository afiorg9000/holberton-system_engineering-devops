#!/usr/bin/python3
"""recursive function that queries the Reddit API"""
from requests import request


def recurse(subreddit, hot_list=[], after=""):
    """recursive function"""
    url = "https://api.reddit.com/r/{}/hot?after={}".format(subreddit, after)
    headers = {"User-Agent": "Python3"}
    response = request("GET", url, headers=headers).json()
    try:
        hot = response['data']['children']
        aftertmp = response['data']['after']
        for i in hot:
            hot_list.append(i['data']['title'])
        if aftertmp is not None:
            recurse(subreddit, hot_list, aftertmp)
        return hot_list
    except Exception:
        return None
