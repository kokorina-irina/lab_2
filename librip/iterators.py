# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        self.items = list(items)
        self.index = 0
        self.unique_items = []
        if 'ignore_case' not in kwargs:
            self.ignore_case = False
        else:
            self.ignore_case = kwargs['ignore_case']

        pass

    def __next__(self):
        if self.index == len(self.items):
            raise StopIteration

        result = self.items[self.index]
        self.index += 1

        if self.ignore_case and type(result) == str:
            if str.casefold(result) not in self.unique_items:
                self.unique_items.append(str.casefold(result))
                return result
            else:
                return next(self)
        elif result not in self.unique_items:
            self.unique_items.append(result)
            return result
        else:
            return next(self)

    def __iter__(self):
        return self
