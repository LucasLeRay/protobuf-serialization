from dataclasses import dataclass
from pathlib import Path

from src.directories import directories


@dataclass
class _Config:
    message_path: Path = directories.artefacts_dir / "person"


config = _Config()
