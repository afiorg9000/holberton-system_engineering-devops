#!/usr/bin/python3
"""Gather data from an API and export it into JSON format"""

import json
import requests

if __name__ == "__main__":
    user_url = 'https://jsonplaceholder.typicode.com/users/'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    username = requests.get(user_url).json()
    tasks = requests.get(todos_url).json()
    urdict = {}
    for u in username:
        user = u['username']
        userlist = []

        for t in tasks:
            userdata = {}
            userdata['username'] = user
            userdata['task'] = t['title']
            userdata['completed'] = t['completed']
            userlist.append(userdata)
        urdict[u['id']] = userlist

    with open("todo_all_employees.json", "w") as f:
        json.dump(urdict, f)
