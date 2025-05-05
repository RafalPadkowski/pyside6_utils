from dataclasses import dataclass
from typing import Callable


@dataclass
class ActionData:
    text: str
    slot: Callable[..., None]
    tooltip: str = ""
    status_text: str = ""
    icon_filenames: tuple[str, ...] = ()
    visible: bool = True
    checkable: bool = False
    checked: bool = False


@dataclass
class MenuData:
    title: str
    action_names: tuple[str, ...]
