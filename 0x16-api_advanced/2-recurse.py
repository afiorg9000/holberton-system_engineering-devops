#!/usr/bin/python3
"""recursive function that queries the Reddit API"""
import requests

def recurse(subreddit, hot_list=[]):
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {'User-agent': 'Python3'}
    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        data_json = res.json()['data']
        
        for post in data_json['children']:
            hot_list += [post['data']['title']]
        
        if data_json['after'] is not None:
            return recurse(subreddit, hot_list)
        return hot_list[:-1]
    else:
        return None
