from typing import Union

from fastapi import UploadFile
from gridfs import GridFS
from pymongo import MongoClient

from domain.entities.video import Video
from domain.repository.mongo_repository import MongoRepository


class VideoRepository(MongoRepository):
    def __init__(self, mongo_client: MongoClient):
        self.fs = GridFS(mongo_client.video)

    def upload(self, file: UploadFile) -> str:
        video_id = self.fs.put(file.file)
        return video_id

    def get(self, id: str) -> Union[Video, None]:
        gridout = self.fs.get(id)
        if gridout:
            return Video(id=gridout._id, file=gridout.file, file_path=gridout.filename)
        else:
            return None

    def delete(self, id: str):
        self.fs.delete(id)
