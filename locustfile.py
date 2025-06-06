from locust import HttpUser, task

class MyUser(HttpUser):
    @task
    def hello(self):
        self.client.get("/api/hello")

    @task
    def post_data(self):
        self.client.post("/api/data", json={"name": "LoadTest", "role": "Stress"})
