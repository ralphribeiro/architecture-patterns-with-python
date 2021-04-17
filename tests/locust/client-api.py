from datetime import datetime
from random import randint
from uuid import uuid4

from locust import HttpUser, task, between


def random_suffix():
    return uuid4().hex[:6]


def random_sku(name=''):
    return f'sku-{name}{random_suffix()}'


def random_batchref(name=''):
    return f'batch-{name}{random_suffix()}'


def random_order_id(name=''):
    return f'order-{name}{random_suffix()}'


class ClientApi(HttpUser):
    wait_time = between(0.2, 2.5)

    @task
    def allocate_batch(self):
        sku = random_sku()
        ref = random_batchref(1)
        qty = randint(1, 10**6)
        eta = datetime.today().date().isoformat()

        self.client.post(
            'add_batch', json={
                'ref': ref,
                'sku': sku,
                'qty': qty,
                'eta': eta
            }
        )

    # @task
    def get_root(self):
        self.client.get("/")
