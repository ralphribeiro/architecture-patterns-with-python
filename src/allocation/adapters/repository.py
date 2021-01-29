from abc import ABC, abstractmethod

from src.allocation.domain import model


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, batch: model.Batch):
        raise NotImplementedError

    @abstractmethod
    def get(self, reference) -> model.Batch:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session) -> None:
        self.session = session

    def add(self, batch):
        self.session.add(batch)

    def get(self, ref):
        return self.session.query(model.Batch).filter_by(reference=ref).one()

    def list(self):
        return self.session.query(model.Batch).all()


class FakeRepository(AbstractRepository):
    def __init__(self, batches):
        self._batches = set(batches)

    def add(self, batch):
        self._batches.add(batch)

    def get(self, ref):
        return next(b for b in self._batches if b.reference == ref)

    def list(self):
        return list(self._batches)
