#!/usr/bin/python3
"""
 export data in the JSON format
"""
import requests
import json

if __name__ == '__main__':
    employee_id = 1
    user_tasks = {}
    url_todo = 'https://jsonplaceholder.typicode.com/todos/'
    url_user = 'https://jsonplaceholder.typicode.com/users/'
    users = requests.get(url_user).json()

    for employee_id in range(1, len(users) + 1):
        todo = requests.get(url_todo, params={'userId': employee_id})
        user = requests.get(url_user, params={'id': employee_id})

        todo_dict_list = todo.json()
        user_dict_list = user.json()
        task_list = []
        employee = user_dict_list[0].get('username')

        for task in todo_dict_list:
            status = task.get('completed')
            title = task.get('title')
            task_dict = {}
            task_dict['task'] = title
            task_dict['completed'] = status
            task_dict['username'] = employee
            task_list.append(task_dict)
        user_tasks[employee_id] = task_list

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(user_tasks, jsonfile)
