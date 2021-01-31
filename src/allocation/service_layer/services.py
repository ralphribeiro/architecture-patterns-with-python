from typing import Optional
from datetime import date

from src.allocation.adapters.repository import AbstractRepository
from src.allocation.domain import model
from src.allocation.domain.model import OrderLine, Batch


class InvalidSku(Exception):
    pass


def is_valid_sku(sku, batches):
    return sku in {b.sku for b in batches}


def add_batch(
    ref: str, sku: str, qty: int, eta: Optional[date],
    repo: AbstractRepository, session,
):
    repo.add(Batch(ref, sku, qty, eta))
    session.commit()


def allocate(
    orderid: str, sku: str, qty: int, repo: AbstractRepository, session
) -> str:
    batches = repo.list()
    if not is_valid_sku(sku, batches):
        raise InvalidSku(f'Invalid sku {sku}')
    line = OrderLine(orderid, sku, qty)
    batchref = model.allocate(line, batches)
    session.commit()
    return batchref
