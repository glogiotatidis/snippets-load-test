import random
from urlparse import urljoin

from locust import HttpLocust, TaskSet, task


with open('urls/desktop.urls') as f:
    LINES = f.read().splitlines()

    DESKTOP_URLS = []
    for line in LINES:
        weight, url = line.split()
        DESKTOP_URLS += [url for i in range(int(weight))]

with open('urls/mobile.urls') as f:
    LINES = f.read().splitlines()

    MOBILE_URLS = []
    for line in LINES:
        weight, url = line.split()
        MOBILE_URLS += [url for i in range(int(weight))]


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
