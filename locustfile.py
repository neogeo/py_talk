import os
import random
import json

from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(0.1, 0.2)

    @task
    def test_sync(self):
    	# use the host config to set the endpoint
        self.client.get('')
