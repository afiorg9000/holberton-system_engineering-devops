#!/usr/bin/python3
"""Gather data from an API"""

from sys import argv
import requests

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
        print("\t " + i['title'])
