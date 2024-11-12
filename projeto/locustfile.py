from locust import HttpUser, task, between

class APIUser(HttpUser):
    # Atraso entre as requisições (de 1 a 5 segundos)
    wait_time = between(1, 5)

    # Definindo uma tarefa que vai realizar uma requisição GET
    @task
    def get_todo(self):
        self.client.get("/todos/1")
