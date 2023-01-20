from dataclasses import dataclass


@dataclass
class Video:
    path: str
    size: float
    format: str
