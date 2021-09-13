#!/usr/bin/python3
"""
 using this REST API, for a given employee ID,
 returns information about his/her TODO list progress.
"""
import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]
    url_todo = 'https://jsonplaceholder.typicode.com/todos/'
    url_user = 'https://jsonplaceholder.typicode.com/users/'
    todo = requests.get(url_todo, params={'user_id': employee_id})
    user = requests.get(url_user, params={'id': employee_id})

    todo_dict_list = todo.json()
    user_dict_list = user.json()

    done_tasks = []
    total_tasks = len(todo_dict_list)
    employee = user_dict_list[0].get('name')

    for task in todo_dict_list:
        if task.get('completed') is True:
            done_tasks.append(task)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee, len(done_tasks), total_tasks))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
