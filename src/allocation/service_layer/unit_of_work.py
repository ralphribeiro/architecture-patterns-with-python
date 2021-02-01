from abc import ABC, abstractclassmethod

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.allocation.adapters import repository
from src.allocation.config import get_postgres_uri


DEFAULT_SESSION_FATORY = sessionmaker(create_engine(get_postgres_uri()))


class AbstractUnitOfWork(ABC):
    batches = repository.AbstractRepository

    def __exit__(self, *args):
        self.rollback()

    @abstractclassmethod
    def commit(self):
        raise NotImplementedError

    @abstractclassmethod
    def rollback(self):
        raise NotImplementedError


class SqlAlchemyUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session_factory=DEFAULT_SESSION_FATORY):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        self.batches = repository.SqlAlchemyRepository(self.session)

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()