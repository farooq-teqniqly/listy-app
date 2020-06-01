import json

import requests


class TaskService:
    def __init__(self, task_api_root_uri: str):
        self._task_api_root_uri = task_api_root_uri

    def get_tasks(self) -> list:
        response: requests.Response = requests.get(self._task_api_root_uri)

        if response.status_code in range(400, 600):
            raise Exception("Could not GET tasks.")

        return json.loads(response.content.decode("utf-8"))
