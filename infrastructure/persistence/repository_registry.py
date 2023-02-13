from pymongo import MongoClient

from domain.repository.video_repository import VideoRepository
from .exceptions import EntityTypeNotFound


class RepositoryRegistry:
    repositories = {'video': VideoRepository}
    client = MongoClient("mongodb://localhost:27017/")  # use envs instead

    @staticmethod
    def get_repository(entity_type: str):
        try:
            return RepositoryRegistry.repositories[entity_type](RepositoryRegistry.client)
        except KeyError:
            raise EntityTypeNotFound("only ['video', 'mp3'] entity_types allowed.")
