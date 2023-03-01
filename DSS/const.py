from enum import Enum


class CustomEnum(bytes, Enum):
    def __new__(cls, value, friendly_name):
        obj = bytes.__new__(cls)
        obj._value_ = value
        obj.friendly_name = friendly_name
        return obj

    def dict(self):
        return dict(id=self.value,
                    name=self.friendly_name)


def friendly_choices(em):
    """
    Вспомогательная функция для ввода enum константы как choices
    :param em: класс CustomEnum
    :return: кортеж (значение, имя)
    """
    return [(e.value, e.friendly_name) for e in em]


class ClosesTypeEnum(CustomEnum):
    pants = (1, 'Штаны')
    shorts = (2, 'Шорты')
    jeans = (3, 'Джинсы')

    t_shorts = (4, 'Майки')
    sweater = (5, 'Свитер')
    vest = (6, 'Жилетка')
    Long_sleeve_shirt = (7, 'Рубашка с длинными рукавами')
    windbreaker = (8, 'Ветровка')
    jacket = (9, 'Куртка')
    fur_coat = (10, 'Шуба')
    coat = (11, 'Пальто')

    sandals = (12, 'Сандали')
    boots = (13, 'Ботинки')
    felt_boots = (14, 'Валенки')

    cap = (15, 'Кепка')
    hat = (16, 'Шапка')
