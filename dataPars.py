import csv
import codecs
import re
from clases import *


def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    """
    lineCounter = 0  # Ссчетчик строк в документе
    mainObjects1C = dict()  # Список наименований объектов системы
    objects1C = dict()

    reader = csv.DictReader(file_obj, delimiter='	')
    for line in reader:
        lineCounter += 1  # Счетчик строк в файле конфигурации

        mainObjects1CName = re.match(r'- ',
                                     str(line["Уровень3"]))  # Ннаименование объектов системы начинается с символов "- "

        if (str(line["Уровень4"])):  # пропарсить свойства объектов
            print(str(line["Уровень4"]), lineCounter)

        if mainObjects1CName:
            # Собирает наименования состава объектов конфигурации как ключи и значения словаря как родителя
            mainObjects1C[(str(line["Уровень3"])[2:str(line["Уровень3"]).find('.')])] = MainObject1C(str(line["Уровень3"])[2:str(line["Уровень3"]).find('.')], "Конфигурация", lineCounter)

            objects1C[(str(line["Уровень3"])[str(line["Уровень3"]).find('.') + 1:])] = \
                Object1C(
                    str(line["Уровень3"])[str(line["Уровень3"]).find('.') + 1:],
                    str(line["Уровень3"])[2:str(line["Уровень3"]).find('.')],
                    lineCounter)

    return mainObjects1C, objects1C


if __name__ == "__main__":
    with codecs.open("data.txt", 'rU', 'utf-16') as f_obj:
        csv_dict_reader(f_obj)
