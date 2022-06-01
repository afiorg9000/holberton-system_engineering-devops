#!/usr/bin/python3
"""Gather data from an API and export it in CSV format"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    username = requests.get(user_url + user).json().get('username')
    tasks = requests.get(todos_url, params={'userId': user}).json()

    with open("{}.csv".format(user), "w", newline="") as csvfile:
        my_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for t in tasks:
            my_writer.writerow([user, username, t.get("completed"),
                                t.get("title")])
