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
    t_shorts = (2, 'Майки')
