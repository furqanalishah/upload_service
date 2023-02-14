from domain.entities.video import Video
from domain.repository.mongo_repository import MongoRepository


class MongoRepository(MongoRepository):
    def save(self, video: Video) -> str:
        # logic to save this `video` object in the mongodb GridFS
        pass

    def get(self, vid: str) -> Video:
        # logic to get this `video` object in the mongodb GridFS
        pass

    def delete(self, vid: str):
        # logic to delete  `video` object in the mongodb GridFS
        pass
