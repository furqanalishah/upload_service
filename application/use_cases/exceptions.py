class VideoUploadError(Exception):
    """Error raised when video upload fails."""
    pass


class VideoNotFoundError(Exception):
    """Error raised when video is not found in the repository."""
    pass
