from datetime import date

import pytest
from sqlalchemy.orm import clear_mappers
from unittest import mock

from allocation import bootstrap
from allocation.service_layer import unit_of_work


@pytest.fixture
def sqlite_bus(sqlite_session_factory):
    bus = bootstrap.bootstrap(
        start_orm=True,
        uow=unit_of_work.SqlAlchemyUnitOfWork(sqlite_session_factory),
        notifications=mock.Mock(),
        publish=lambda *args: None,
    )
    yield bus
    clear_mappers()


def test_stuff():
    assert 1
