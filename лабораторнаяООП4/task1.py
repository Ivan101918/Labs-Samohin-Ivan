import doctest


class Building:
    """
        Базовый класс для строений

        Атрибуты:

        adress: адрес здания
        construction_year : год постройки
        number_of_floors: кол-во этажей в здании
        floor_height: фиксированная высота этажа

    """
    def __init__(self, adress: str, construction_year: int, number_of_floors: int) -> None:
        """
            Конструктор класса Building

            :param adress: адрес здания
            :param construction_year : год постройки
            :param number_of_floors: кол-во этажей в здании

            Пример:
            >>> bld1 = Building('проспект Ленина 12', 2008, 10)
            >>> bld1.adress
            'проспект Ленина 12'
            >>> bld1.construction_year
            2008
            >>> bld1.number_of_floors
            10
        """
        self._adress = adress
        self._construction_year = construction_year
        self._number_of_floors = number_of_floors

    def __str__(self) -> str:
        """ Возвращает строковое представление объекта Building """
        return f'Адрес: "{self._adress}", год постройки: {self._construction_year}, кол-во этажей: {self._number_of_floors}'

    def __repr__(self) -> str:
        """ Возвращает строковое представление объекта Building для отладки """
        return f'{self.__class__.__name__}(adress={self._adress!r}, construction_year={self._construction_year!r}, number_of_floors={self._number_of_floors!r})'

    _FLOOR_HEIGHT = 2.7

    @property
    def floor_height(self) -> float:
        """
        Неизменяемая константа, одинаковая для всех зданий (предполагается, что все они будут непроизводственные).

        :return: 2.7
        """
        return self._FLOOR_HEIGHT

    @property
    def adress(self) -> str:
        """
        Геттер для адреса здания

        :return: адрес здания
        """
        return self._adress

    @property
    def construction_year(self) -> int:
        """
        Геттер для года постройки

        :return: год постройки
        """
        return self._construction_year

    @property
    def number_of_floors(self) -> int:
        """
        Геттер для кол-ва этажей здания

        :return: кол-во этажей в здании
        """
        return self._number_of_floors

    @adress.setter
    def adress(self, new_adress: str) -> None:
        """
            Сеттер для адреса, проверка параметра new_adress на принадлежность строке

            :raise TypeError: если новый адрес НЕ строка
            :raise ValueError: если введена пустая строка
        """
        if not isinstance(new_adress, str):
            raise TypeError('Адрес здания должен быть строкой!')
        elif new_adress == '':
            raise ValueError('Адрес не может быть пустой строкой!')
        self._adress = new_adress

    @construction_year.setter
    def construction_year(self, new_construction_year: int) -> None:
        """
        Сеттер для года постройки, проверка на принадлежность int

        :param new_construction_year:новый год для установи, можеть быть отрицательным, если год постройки до нашей эры

        :raise TypeError: если введено не целое число
        """
        if not isinstance(new_construction_year, int):
            raise TypeError('Год постройки можеть быть только целым числом!')
        self._construction_year = new_construction_year

    @number_of_floors.setter
    def number_of_floors(self, new_number_of_floors: int) -> None:
        """
        Сеттер для кол-ва этажей в здании

        :param new_number_of_floors: новое кол-во этажей

        :raise TypeError: если введено не целое число
        :raise ValueError: если введено число меньше единицы
        """
        if not isinstance(new_number_of_floors, int):
            raise TypeError('Кол-во этажей можеть быть только целым числом!')
        elif new_number_of_floors <= 0:
            raise ValueError('Кол-во этажей должно быть больше нуля!')
        self._number_of_floors = new_number_of_floors

    def get_height(self) -> float:
        """
            Возвращает высоту здания в метрах: кол-во этажей * высоту этажа

            Например:

            >>> bld1 = Building('проспект Ленина 12', 2008, 10)
            >>> bld1.get_height()
            27.0
        """
        return self.floor_height * self.number_of_floors

    def get_age(self, current_year: int) -> int:
        """
        Вычисляет возраст здания на текущий год.

        :param current_year: Текущий год.

        :raise ValueError: Если текущий год меньше года постройки (возраст не может быть отрицательным)

        :return: возраст здания.
        """
        if not isinstance(current_year, int):
            raise TypeError('Год может быть записан только целым числом')
        elif current_year < self.construction_year:
            raise ValueError('Текущий год не может быть меньше года посройки')
        return current_year - self.construction_year

    def get_required_area(self, length: (int, float), width: (int, float)) -> (int, float):
        """
        Высчитывает площадь в м2, необходимую под застройку, учитывая только длину и ширину здания

        :param length: длина здания в метрах
        :param width: ширина здания в метрах

        :raise TypeError: если введен нечисловой тип данных
        :raise ValueError: если введенные числа меньше либо равны нулю

        :returns: площадь здания: длина * ширина в м2
        """
        if (not isinstance(length, (int, float))) or (not isinstance(width, (int, float))):
            raise TypeError('Длина и ширина могут быть только числом!')
        elif length <= 0 or width <= 0:
            raise ValueError('Длина и ширина должны быть больше нуля!')
        return length * width


class LivingBuilding(Building):
    """
    Класс для жилых зданий, наследуемый от класса Building

    Атрибуты:

    number_of_apartments: кол-во квартир в здании
    includes_lift: наличие лифта в здании
    """

    def __init__(self, adress: str, construction_year: int, number_of_floors: int, number_of_apartments: int, includes_lift: bool) -> None:
        """
        Конструктоор класса LivingBuilding, расширение конструктора Building

        :param adress: адрес здания
        :param construction_year : год постройки
        :param number_of_floors: кол-во этажей в здании
        :param number_of_apartments: кол-во квартир в здании
        :param includes_lift: наличие лифта в здании

        Пример:
        >>> bld2 = LivingBuilding('улица Горького 34', 1975, 9, 36, True)
        >>> bld2.includes_lift
        True
        >>> bld2.number_of_apartments
        36
        """
        super().__init__(adress, construction_year, number_of_floors)
        self._number_of_apartments = number_of_apartments
        self._includes_lift = includes_lift

    def __str__(self) -> str:
        """ Перегруженный метод __str__, добавляет информацию о количестве квартир и наличии лифта """
        return super().__str__() + f', количество квартир: {self._number_of_apartments}, наличие лифтa: {self._includes_lift}'

    def __repr__(self) -> str:
        """ Перегруженный метод __repr__, добавляет информацию для отладки """
        base_repr = super().__repr__()
        return base_repr.rstrip(')') + f', number_of_apartments={self._number_of_apartments!r}, includes_lift={self._includes_lift!r})'

    @property
    def number_of_apartments(self) -> int:
        """
        Геттер для количества квартир в жилом доме

        :return: кол-во квартир в жилом доме
        """
        return self._number_of_apartments

    @property
    def includes_lift(self) -> bool:
        """
        Геттер для наличия лифта в жилом здании

        :return: наличие лифта False/True
        """
        return self._includes_lift

    @number_of_apartments.setter
    def number_of_apartments(self, new_number_of_apartments: int) -> None:
        """
        Сеттер для кол-ва квартир в жилом доме

        :raise TypeError: если кол-во квартир не целое число')
        :raise ValueError: если кол-во квартир меньше либо равно нулю'
        """
        if not isinstance(new_number_of_apartments, int):
            raise TypeError('Кол-во квартир может быть только целым числом')
        elif new_number_of_apartments <= 0:
            raise ValueError('Кол-во квартир должно быть больше нуля')
        self._number_of_apartments = new_number_of_apartments

    @includes_lift.setter
    def includes_lift(self, new_includes_lift) -> None:
        """
        Сеттер для наличия лифта в жилом доме

        :raise TypeError: если введено небулевое значение
        """
        if not isinstance(new_includes_lift, bool):
            raise TypeError('Наличие лифта может быть только булевым значеинем')
        self._includes_lift = new_includes_lift


    def get_required_area(self, length: (int, float), width: (int, float), local_area: (int, float)) -> (int, float):
        """
        Перегруженный метод get_required_area для класса LivingBuilding, теперь с учётом придомовой территории в м2

        :param local_area: площадь придомовой территории м2

        :raise TypeError: если введен нечисловой тип данных
        :raise ValueError: если введенно число меньшее либо равное нулю

        :return: площаль здания + придомовая территория в м2
        """
        if not (local_area, (int, float)):
            raise TypeError('Площадь должна быть числом!')
        elif local_area <= 0:
            raise ValueError('Площадь должна быть больше нуля')
        return super().get_required_area(length, width) + local_area


if __name__ == "__main__":
    bld1 = Building('улица Пушкина 4', 2000, 12)
    print(bld1.get_height())
    print(bld1.get_required_area(12, 30))

    bld2 = LivingBuilding('проспект Нахимова 57', 2022, 5, 20, False)
    print(bld2.get_age(2025))
    print(bld2.get_required_area(30, 50, 100))


