#!/usr/bin/python3
"""Export an employee's TODO list to a JSON file."""
import json
import requests
import sys

user_id = sys.argv[1]
base_url = "https://jsonplaceholder.typicode.com"

user = requests.get("{}/users/{}".format(base_url, user_id)).json()
todos = requests.get("{}/todos".format(base_url),
                     params={"userId": user_id}).json()
username = user.get("username")

data = {user_id: [{"task": t.get("title"),
                   "completed": t.get("completed"),
                   "username": username} for t in todos]}

with open("{}.json".format(user_id), "w") as f:
    json.dump(data, f)
