from domain.entities.video import Video
from domain.repository.video_repository import VideoRepository
from .exceptions import VideoNotFoundError


class GetVideoUseCase:
    def __init__(self, repository: VideoRepository):
        self.repository = repository

    def execute(self, video_id: str) -> Video:
        video = self.repository.get(video_id)
        if not video:
            raise VideoNotFoundError(f"Video with id {video_id} not found")
        return video
