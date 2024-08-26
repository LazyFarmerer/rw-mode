import xml.etree.ElementTree as et
from pathlib import Path

class Mode:
    def __init__(self, mode_path: Path) -> None:
        self.__mode_path = mode_path
        self.__about_xml = mode_path / "About/About.xml"
        self.__xml = et.parse(self.__about_xml)

        self.__name = self.__xml.find("name")
        self.__description = self.__xml.find("description")

    @property
    def name(self) -> str:
        "모드 이름"
        return self.__name.text # type: ignore
    @property
    def path(self) -> str:
        "모드 주소"
        return self.__name.text # type: ignore
    @property
    def description(self) -> str:
        "어떤 모드인가를 설명"
        return self.__description.text # type: ignore
    @description.setter
    def description(self, n: str):
        self.__description.text = n # type: ignore
        self.__xml.write(self.__about_xml)


    def __repr__(self) -> str:
        return f"< {self.__name.text} || {self.__description.text} >" # type: ignore