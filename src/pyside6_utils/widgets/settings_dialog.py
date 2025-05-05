from typing import Any

from app_settings import AppSettings, SettingType
from PySide6.QtWidgets import (
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QVBoxLayout,
    QWidget,
)

from ..i18n import _
from .utils import get_app_icon


class SettingsDialog(QDialog):
    def __init__(self, settings: AppSettings, parent: QWidget | None) -> None:
        super().__init__(parent)

        self.setWindowIcon(get_app_icon())

        self.setWindowTitle(_("Settings"))

        self.fields: dict[str, QWidget] = dict()

        form_layout: QFormLayout = QFormLayout()

        for field_name, field_info in AppSettings.model_fields.items():
            assert field_info.title is not None
            label_text: str = _(field_info.title) + ": "

            assert isinstance(field_info.json_schema_extra, dict)
            extra: dict[str, Any] = field_info.json_schema_extra

            current_value: Any = getattr(settings, field_name)

            if extra["type"] == SettingType.OPTIONS.value:
                combo_box: QComboBox = QComboBox()
                current_value_index: int

                for i, choice in enumerate(extra["choices"]):
                    combo_box.addItem(_(choice["text"]), userData=choice["data"])

                    if choice["data"] == current_value:
                        current_value_index = i

                combo_box.setCurrentIndex(current_value_index)

                form_layout.addRow(label_text, combo_box)

                self.fields[field_name] = combo_box

        button_box: QDialogButtonBox = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        main_layout: QVBoxLayout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addStretch()
        main_layout.addWidget(button_box)

        self.setLayout(main_layout)

    def get_new_settings(self) -> dict[str, Any]:
        new_settings: dict[str, Any] = dict()

        for field_name, field in self.fields.items():
            if isinstance(field, QComboBox):
                new_settings[field_name] = field.currentData()

        return new_settings
