from pytest import fixture
from sqlalchemy.orm import Session


@fixture(scope='session')
def session():
    s = Session()
    try:
        yield s
    finally:
        s.close()
    