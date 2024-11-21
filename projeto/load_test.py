from locust import HttpUser, task, between

import random

class APIUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def get_todo(self):
        
        with self.client.get(f"/todos/1", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Status code: {response.status_code}")
