#!/usr/bin/python3
"""Gather data from an API and export it in CSV format"""
import requests
from sys import argv
import csv
if __name__ == "__main__":
    user = argv[1]
    username = requests.get(
        'https://jsonplaceholder.typicode.com/users/'
        + user).json().get('name')
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos',
                         params={'userId': user}).json()

    with open("{}.csv".format(user), "w", newline="") as csvfile:
        my_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [my_writer.writerow([user, username, t.get("completed"),
                            t.get("title")]) for t in tasks]
