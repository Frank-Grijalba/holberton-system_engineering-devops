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
    username = fetch_data(url_usr).get('username')
    url_todo = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
    lst_todo = fetch_data(url_todo)

    all_tasks = []

    for task in lst_todo:
        dict = {}
        dict['task'] = task['title']
        dict['completed'] = task['completed']
        dict["username"] = username
        all_tasks.append(dict)

    with open("{}.json".format(user_id), 'w') as jsonfile:
        json.dump({user_id: all_tasks}, jsonfile)
