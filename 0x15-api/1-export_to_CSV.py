#!/usr/bin/python3
"""
export data in the CSV format
"""
import requests
import sys
import csv

if __name__ == '__main__':
    employee_id = sys.argv[1]
    url_todo = 'https://jsonplaceholder.typicode.com/todos/'
    url_user = 'https://jsonplaceholder.typicode.com/users/'
    todo = requests.get(url_todo, params={'user_id': employee_id})
    user = requests.get(url_user, params={'id': employee_id})

    todo_dict_list = todo.json()
    user_dict_list = user.json()

    employee = user_dict_list[0].get('username')

    with open("{}.csv".format(employee_id), "w") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todo_dict_list:
            status = task['completed']
            title = task['title']
            writer.writerow(["{}".format(employee_id),
                             "{}".format(employee),
                             "{}".format(status),
                             "{}".format(title)])
