from dataclasses import dataclass
from pathlib import Path

from src.directories import directories


@dataclass
class _Config:
    compiled_regressor_path: Path = directories.artefacts_dir / "regressor"


config = _Config()
