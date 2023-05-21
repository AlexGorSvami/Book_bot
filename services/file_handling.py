import re

BOOK_PATH = 'book/besy.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}

#Функция, возвращающая строку с текстом страницы и её размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    edit_text = re.sub(r'[.,!?:;]\.+$', '', text[start:start + size])
    edit_text = re.findall(r'(?s).+[.,!?:;]', edit_text)
    return *edit_text, len(*edit_text)

#Функция, форматирующая словарь книги
def prepare_book(path: str) -> None:
    pass

#Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(BOOK_PATH)

