import importlib.resources

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMessageBox, QWidget
from resource_getters import Image

from ..i18n import _
from .utils import get_app_icon


class AboutBox(QMessageBox):
    def __init__(self, parent: QWidget | None, pixmap_filename: str, text: str) -> None:
        super().__init__(parent)

        self.setWindowIcon(get_app_icon())

        self.setWindowTitle(_("About"))

        with importlib.resources.as_file(Image(pixmap_filename)) as real_path:
            pixmap: QPixmap = QPixmap(str(real_path))
        self.setIconPixmap(pixmap)

        self.setText(text)
