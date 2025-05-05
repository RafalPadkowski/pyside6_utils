# pyside6-utils

A collection of reusable PySide6 utility widgets and helpers for building consistent Qt applications, including settings dialogs, about boxes, action definitions, internationalization (i18n) support, and resource handling.

## Features

- 🛠️ `SettingsDialog`: Auto-generated settings dialog using field metadata from `AppSettings`.
- 📦 `AboutBox`: Customizable "About" message box with embedded images.
- 🧭 `ActionData` & `MenuData`: Declarative structures for defining menus and actions.
- 🌐 i18n with gettext and Qt translation support.
- 🎨 Icon and resource loading via `importlib.resources`.

## Installation

```bash
pip install git+https://github.com/RafalPadkowski/pyside6_utils
```

> Ensure you also have `PySide6` and any required companion packages (like `app_settings`, `resource_getters`) available in your environment.

## Usage

### Settings Dialog

```python
from pyside6_utils import SettingsDialog
from app_settings import AppSettings

dialog = SettingsDialog(settings=AppSettings(), parent=main_window)
if dialog.exec():
    new_settings = dialog.get_new_settings()
    # Apply new_settings to your application
```

### About Box

```python
from pyside6_utils import AboutBox

about = AboutBox(parent=main_window, pixmap_filename="logo.png", text="My Application v1.0")
about.exec()
```

### Internationalization

```python
from pyside6_utils import set_language, _

set_language("pl")  # Load Polish translations
print(_("Settings"))  # Translated string if available
```

### Defining Actions

```python
from pyside6_utils import ActionData, MenuData

action_data = ActionData(
    text="Open",
    slot=open_file,
    tooltip="Open a file",
    icon_filenames=("open.png",),
)
```

## Project Structure

```
pyside6_utils/
├── widgets/
│   ├── about_box.py
│   ├── actions.py
│   ├── settings_dialog.py
│   └── utils.py
├── i18n.py
├── __init__.py
```

## Dependencies

- Python 3.10+
- [PySide6](https://pypi.org/project/PySide6/)
- `app_settings` – your structured settings definition module
- `resource_getters` – resource access layer for images, translations, icons

## License

MIT License
