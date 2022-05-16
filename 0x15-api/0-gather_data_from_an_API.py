#!/usr/bin/python3
"""Gather data from an API"""
import requests
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    username = requests.get('https://jsonplaceholder.typicode.com/users/'
                            + user).json().get('name')
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos',
                         params={'userId': user}).json()
    completed = requests.get('https://jsonplaceholder.typicode.com/todos',
                             params={'userId': user,
                                     'completed': 'true'}).json()

    print("Employee", username, "is done with tasks("
          + str(len(completed)) + "/" + str(len(tasks)) + "):")

    for i in completed:
        print("\t " + i['title'])
