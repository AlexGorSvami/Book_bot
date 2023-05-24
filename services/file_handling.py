import os

BOOK_PATH = 'book/New_book.txt'
PAGE_SIZE = 1200

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и её размер
def _get_part_text(text: str, start: int, page_size: int) -> tuple[str, int]:
    end_simbol = ['.', ',', '!', ':', ';', '?']
    end = start + page_size
    while text[end:][:1] in end_simbol:
        end -= 1
    text = text[start:end]
    text = text[: max(map(text.rfind, end_simbol)) + 1]
    return text, len(text)


#Функция, форматирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, 'r') as file:
        f = file.read()
        pages = (len(f) // PAGE_SIZE) + 1
        start = 0
        for p in range(1, pages + 1):
            book[p] = _get_part_text(f, start, PAGE_SIZE)[0].lstrip(' \n.')
            start += _get_part_text(f, start, PAGE_SIZE)[1]


#Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(os.getcwd(), BOOK_PATH))


