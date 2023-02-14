from fastapi import UploadFile

from application.use_cases.get_video import GetVideoUseCase
from application.use_cases.upload_video import UploadVideoUseCase
from domain.entities.video import Video
from infrastructure.persistence.repository_registry import RepositoryRegistry


class VideoService:
    def __init__(self, entity_type: str = "video"):
        self.video_repository = RepositoryRegistry.get_repository(entity_type)

    def upload_video(self, file: UploadFile) -> str:
        video = Video(filename=file.filename)
        upload_video_use_case = UploadVideoUseCase(self.video_repository)
        video.id = upload_video_use_case.execute(file)
        return video.id

    def get_video(self, video_id: str) -> Video:
        get_video_use_case = GetVideoUseCase(self.video_repository)
        return get_video_use_case.execute(video_id)
