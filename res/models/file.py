from typing import Union, List
from pathlib import Path

from ..base_class.mode_type import ModeType
from ..models.mode import Mode


class File:
    @staticmethod
    def read_modes(modeType: ModeType) -> List[Mode]:
        subfolders = [Mode(f) for f in Path(modeType.value).iterdir() if f.is_dir()]
        return subfolders

    @staticmethod
    def write(path: Union[Path, str], data):
        if isinstance(path, Path):
            path = path.as_posix()

        with open(path, "w", encoding='utf8') as f:
            f.write(data)

    @staticmethod
    def read(path: Union[Path, str]):
        if isinstance(path, Path):
            path = path.as_posix()

        with open(path, "r", encoding='utf8') as f:
            data = f.read()
        return data