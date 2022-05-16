#!/usr/bin/python3
"""Gather data from an API"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    username = requests.get(user_url + user).json().get('name')
    tasks = requests.get(todos_url, params={'user': user}).json()

    with open("{}.json".format(user), "w") as file:
        json.dump({user: [{"task": t.get("title"),
                  "completed": t.get("completed"),
                   "username": username} for t in tasks]}, file)
