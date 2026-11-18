#!/usr/bin/python3
"""Export the TODO lists of all employees to a JSON file using a REST API."""
import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    users = requests.get("{}/users".format(base_url)).json()
    todos = requests.get("{}/todos".format(base_url)).json()

    data = {}
    for user in users:
        user_id = user.get("id")
        data[str(user_id)] = [{"username": user.get("username"),
                               "task": todo.get("title"),
                               "completed": todo.get("completed")}
                              for todo in todos
                              if todo.get("userId") == user_id]

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(data, json_file)
