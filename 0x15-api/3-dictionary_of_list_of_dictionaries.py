#!/usr/bin/python3
"""Script that accesses a REST API for a given employee ID,
returns information about his/her TODO list progress"""
from urllib import request
import json


def fetch_data(url):
    """Return all the information in json from an URL given"""
    find = request.Request(url)
    with request.urlopen(find) as r:
        return json.loads(r.read().decode('utf-8'))


if __name__ == "__main__":

    url_all_usr = 'https://jsonplaceholder.typicode.com/users/'
    all_employes = fetch_data(url_all_usr)
    url_todo = 'https://jsonplaceholder.typicode.com/todos'
    all_tasks = fetch_data(url_todo)

    all_records = {}

    for employee in all_employes:
        list_task = []
        for task in all_tasks:
            if employee['id'] == task['userId']:
                dict = {"username": employee['username'],
                        "task": task['title'],
                        "completed": task['completed']}
                list_task.append(dict)
        all_records[employee['id']] = list_task

    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(all_records, jsonfile)
