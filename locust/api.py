from datetime import datetime
from random import randint
from uuid import uuid4

from locust import HttpUser, task, between


def random_suffix():
    return uuid4().hex[:6]


def random_sku(name: str = None):
    return f'sku-{name}{random_suffix()}'


def random_batchref(name: str = None):
    return f'batch-{name}{random_suffix()}'


def random_order_id(name: str = None):
    return f'order-{name}{random_suffix()}'


class ApiUser(HttpUser):
    wait_time = between(0.1, 2)

    @task
    def allocate_batch(self):
        sku = random_sku()
        ref = random_batchref()
        qty = randint(1, 10**6)
        eta = datetime.today().date().isoformat()

        self.client.post(
            '/add_batch', json={
                'eta': eta,
                'ref': ref,
                'sku': ref,
                'qty': qty
            }            
        )


    # def on_start(self):
        # self.client
