from fastapi import UploadFile
from gridfs.errors import GridFSError

from domain.repository.video_repository import VideoRepository
from infrastructure.communication.rabbitmq_connection import RabbitMQConnection
from .exceptions import VideoUploadError


class UploadVideoUseCase:
    def __init__(self, repository: VideoRepository):
        self.repository = repository

    def execute(self, file: UploadFile):
        try:
            video_id = self.repository.upload(file)
            payload = {
                "user_id": "some-user-id",
                "video_id": str(video_id),
                "mp3_id": ""
            }
            with RabbitMQConnection() as rabbit:
                rabbit.publish(payload)
            return video_id
        except GridFSError as e:
            raise VideoUploadError(f"Error uploading video: {e}")
