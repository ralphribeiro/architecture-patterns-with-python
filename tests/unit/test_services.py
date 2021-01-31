from datetime import date, timedelta

from pytest import raises

from src.allocation.adapters.repository import FakeRepository
from src.allocation.domain import model
from src.allocation.domain.model import OrderLine, Batch, allocate
from src.allocation.service_layer import services


tomorrow = date.today() - timedelta(days=-1)


class FakeSession():    
    commited = False

    @staticmethod
    def for_batch(ref, sku, qty, eta=None):
        return FakeRepository([
            model.Batch(ref, sku, qty, eta),
        ])

    def commit(self):
        self.commited = True


def test_returns_allocation():
    repo, session = FakeRepository([]), FakeSession()
    services.add_batch("batch1", "COMPLICATED-LAMP", 100, None, repo, session)
    result = services.allocate("o1", "COMPLICATED-LAMP", 10, repo, session)
    assert result == "batch1"


def test_add_batch():
    repo, session = FakeRepository([]), FakeSession()
    services.add_batch("b1", "CRUNCHY-ARMCHAIR", 100, None, repo, session)
    assert repo.get("b1") is not None
    assert session.commited

def test_allocate_erros_for_invalid_sku():
    repo, session = FakeRepository([]), FakeSession()
    services.add_batch("b1", "AREALSKU", 100, None, repo, session)
    
    with raises(services.InvalidSku, match='Invalid sku NONEXISTENTSKU'):
        services.allocate("o1", "NONEXISTENTSKU", 10, repo, session)