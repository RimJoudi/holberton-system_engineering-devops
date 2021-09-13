#!/usr/bin/python3
"""
Pings a To-Do API for data for a specified user and writes it to a JSON file
"""

import requests
import sys
import csv
import json

if __name__ == '__main__':
    employee_id = sys.argv[1]
    url_todo = 'https://jsonplaceholder.typicode.com/todos/'
    url_user = 'https://jsonplaceholder.typicode.com/users/'
    todo = requests.get(url_todo, params={'user_id': employee_id})
    user = requests.get(url_user, params={'id': employee_id})

    todo_dict_list = todo.json()
    user_dict_list = user.json()
    task_list = []
    user_tasks = {}
    employee = user_dict_list[0].get('username')

    with open("{}.json".format(employee_id), "w") as file:
        for task in todo_dict_list:
            status = task.get('completed')
            title = task.get('title')
            task_dict = {}
            task_dict['task'] = title
            task_dict['completed'] = status
            task_dict['username'] = employee
            task_list.append(task_dict)
        user_tasks[employee_id] = task_list

        data = json.dumps(user_tasks)
        file.write(data)
