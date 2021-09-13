#!/usr/bin/python3
"""Script that accesses a REST API for a given employee ID,
returns information about his/her TODO list progress"""
from urllib import request
import sys
import json


def fetch_data(url):
    """Return all the information in json from an URL given"""
    find = request.Request(url)
    with request.urlopen(find) as r:
        return json.loads(r.read().decode('utf-8'))


if __name__ == "__main__":
    user_id = sys.argv[1]
    url_usr = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    name = fetch_data(url_usr).get('name')
    url_todo = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
    lst_todo = fetch_data(url_todo)

    tasks_done = [task for task in lst_todo if task['completed'] is True]
    length_done = len(tasks_done)
    length_all = len(lst_todo)

    print(f'Employee {name} is done with tasks({length_done}/{length_all}):')

    for task in tasks_done:
        print('\t ' + task['title'])
