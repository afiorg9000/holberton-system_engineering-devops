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
    completed = requests.get(todos_url,
                             params={'user': user,
                                     'completed': 'true'}).json()

    print("Employee", username, "is done with tasks(" +
          str(len(completed)) + "/" + str(len(tasks)) + "):")

    for i in completed:
        rint("\t " + i['title'])
