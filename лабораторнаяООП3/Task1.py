class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self) -> str:
        return f"Книга: {self.name}. Автор: {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    def __str__(self):
        return f"Книга: {self.name}. Автор: {self.author}. Количество страниц: {self.pages}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError('Число страниц должно быть целым числом')
        elif new_pages <= 0:
            raise ValueError('Число страниц должно быть больше нуля')
        self._pages = new_pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    def __str__(self) -> str:
        return f"Книга: {self.name}. Автор: {self.author}. Продолжительность: {self.duration}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

    @property
    def duration(self) -> (int, float):
        return self._duration

    @duration.setter
    def duration(self, new_duration):
        if not isinstance(new_duration, (int, float)):
            raise TypeError('Продолжительность должна быть числом')
        elif new_duration <= 0:
            raise ValueError('Продолжительность не может быть меньше нуля')
        self._duration = new_duration


au = AudioBook('pisya', 'popa', 9)
p = PaperBook('la', 'yy', 99)
au.duration = 7
p.pages = 94
print(p)
print(repr(p))

print(au)
print(repr(au))


