from gettext import GNUTranslations
from importlib.abc import Traversable
from importlib.resources import as_file

from PySide6.QtCore import QTranslator
from resource_getters import Translations

gettext_translations: GNUTranslations | None = None
qt_translator: QTranslator = QTranslator()


def set_language(language: str) -> None:
    global gettext_translations

    if language == "en":
        gettext_translations = None
    else:
        with Translations(f"{language}.mo").open("rb") as file:
            gettext_translations = GNUTranslations(file)

    resource_path: Traversable = Translations(f"qtbase_{language}")
    with as_file(resource_path) as real_path:
        qt_translator.load(str(real_path))


def _(message: str) -> str:
    if gettext_translations is None:
        return message

    return gettext_translations.gettext(message)
