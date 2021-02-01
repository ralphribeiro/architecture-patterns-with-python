from datetime import date, timedelta

from pytest import raises

from src.allocation.adapters.repository import FakeRepository
from src.allocation.domain import model
from src.allocation.service_layer import services, unit_of_work


tomorrow = date.today() - timedelta(days=-1)


class FakeUnitOfWork(unit_of_work.AbstractUnitOfWork):    
    def __init__(self):
        self.batches = FakeRepository([])
        self.commited = False

    def commit(self):
        self.commited = True
    
    def rollback(self):
        pass


def test_returns_allocation():
    uow = FakeUnitOfWork()
    services.add_batch("batch1", "COMPLICATED-LAMP", 100, None, uow)
    result = services.allocate("o1", "COMPLICATED-LAMP", 10, uow)
    assert result == "batch1"


def test_add_batch():
    uow = FakeUnitOfWork()
    services.add_batch("b1", "CRUNCHY-ARMCHAIR", 100, None, uow)
    assert uow.batches.get("b1") is not None
    assert uow.commited

def test_allocate_erros_for_invalid_sku():
    uow = FakeUnitOfWork()
    services.add_batch("b1", "AREALSKU", 100, None, uow)
    
    with raises(services.InvalidSku, match='Invalid sku NONEXISTENTSKU'):
        services.allocate("o1", "NONEXISTENTSKU", 10, uow)