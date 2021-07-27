import os
import glob
import pathlib

"""
Программа для определения количества файлов по их расширению. 
Принцип действия: задаётся путь, откуда начинается поиск, затем программа ищет файлы по расширениям. Результат 
выводится на экран в виде ключа и значения. Например, .py: 1.
"""


class CountExtensions:
    """
    При создании экземпляра класса требуется указать путь (path), откуда начинается поиск файлов.
    """
    def __init__(self, path):
        self.path = path

    def count_extensions(self):
        """
        Функция ищет файлы и исправляет их названия, расширения складываются в специальный список.
        Полученные значения складываются в словарь, затем производится сортировка по убыванию.
        Функция возвращает генератор (через yield).
        """
        files = [os.path.basename(x) for x in glob.glob(self.path + '/**/*', recursive=True) if os.path.isfile(x)]
        ext_list = []
        count_dict = dict()

        for f in files:
            f = f.lower()
            ext = pathlib.Path(f).suffix
            ext_list.append(ext)
            if '' in ext_list:
                ext_list.remove('')
            ext_list = list(set(ext_list))

            for e in ext_list:
                if f.endswith(e):
                    count = count_dict.get(e, 0)
                    count_dict[e] = count + 1

        count_sorted = sorted(dict.items(count_dict), key=lambda x: x[1], reverse=True)

        for c in count_sorted:
            yield f'{c[0]}: {c[1]}'


count_extensions = CountExtensions(os.getcwd())  # создаём объект класса, в качестве пути задаём текущую директорию
result = count_extensions.count_extensions()  # создаём генератор

"""
Выводим на экран результат работы программы, используя цикл for.
"""
for i in result:
    print(i)
