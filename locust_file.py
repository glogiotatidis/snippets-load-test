import random
from urlparse import urljoin

from locust import HttpLocust, TaskSet, task


with open('desktop.urls') as f:
    DESKTOP_URLS = f.read().splitlines()

with open('mobile.urls') as f:
    MOBILE_URLS = f.read().splitlines()


class DesktopTaskSet(TaskSet):
    @task
    def fetch_snippets(self):
        url = random.choice(DESKTOP_URLS)
        with self.client.get(url, catch_response=True, name="Desktop", allow_redirects=False) as response:
            if response.status_code == 301:
                response.success()


class MobileTaskSet(TaskSet):
    @task
    def fetch_snippets(self):
        url = random.choice(MOBILE_URLS)
        self.client.get(url, name="Fennec")


class DesktopLocust(HttpLocust):
    weight = 5
    task_set = DesktopTaskSet


class MobileLocust(HttpLocust):
    weight = 3
    task_set = MobileTaskSet
