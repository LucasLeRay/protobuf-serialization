from types import SimpleNamespace
from pathlib import Path

directories = SimpleNamespace()

directories.root_dir = Path(__file__).parents[1]
directories.artefacts_dir = directories.root_dir / "artefacts"

for directory in vars(directories).values():
    directory.mkdir(exist_ok=True)
