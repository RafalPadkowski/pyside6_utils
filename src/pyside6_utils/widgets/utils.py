import importlib.resources

from PySide6.QtGui import QIcon
from resource_getters import Icon


def get_app_icon() -> QIcon:
    with importlib.resources.as_file(Icon("app.ico")) as real_path:
        icon: QIcon = QIcon(str(real_path))

    return icon
