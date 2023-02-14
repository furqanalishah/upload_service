from abc import ABC, abstractmethod

from domain.entities.video import Video


class MongoRepository(ABC):

    @abstractmethod
    def upload(self, video: Video) -> str:
        pass

    @abstractmethod
    def get(self, vid: str) -> Video:
        pass

    @abstractmethod
    def delete(self, vid: str):
        pass
