import pandas as pd
import codecs
import csv
from clases import *
import re


def pandasDataParce():
    analiticDF = pd.DataFrame()
    configuration1C, mainObject1C, object1C, = dict(), dict(), dict()
    # iterestIn = ('Отчеты')

    with codecs.open("ConfReport_190717.txt", 'rU', 'utf-16') as f_obj:
        reader = csv.reader(f_obj, delimiter='	')
        df = pd.DataFrame(reader)

    for data in df[1]:
        if data:
            configuration1C[(str(data)[2:str(data).find('.')])+'_configuration'] = Configuration1C(str(data)[str(data).find('.') + 1:], None, [])  # создает словарь конфигураций [отступает 2 знака и берет имя до точки + номер строки] = объект [от точки до конца строки, номер строки]


    for index, data in enumerate(df[2]):

        if re.match(r'Версия:', str(data)):
            configuration1C[list(configuration1C.keys())[-1]].version = \
                (str(data)[str(data).find(': ')+2:]) # определяется версия 1С

        if re.match(r'- ', str(data)):  #  and (str(data)[2:str(data).find('.')]) in iterestIn
            mainObject1C[(str(data)[2:str(data).find('.')])] = \
                    MainObject1C(
                    (str(data)[2:str(data).find('.')]),
                    list(configuration1C.values())[-1].name,
                    list(configuration1C.values())[-1].hashName,
                    (index, None)) # создает словарь объектов [отступает 2 знака и берет имя до точки + номер строки] = объект [отступает 2 знака и берет имя до точки, номер строки, родитель как -1 элемент словаря конфигураций]

        if re.match(r'- ', str(data)):  #  and (str(data)[2:str(data).find('.')]) in iterestIn
            object1C[(str(data)[str(data).find('.')+1:])] = \
                    Object1C(
                    (str(data)[str(data).find('.')+1:]),
                    list(mainObject1C.values())[-1].name,
                    list(mainObject1C.values())[-1].hashName,
                    (index, None),
                    None)  # создает словарь объектов [отступает 2 знака и берет имя до точки + номер строки] = объект [отступает 2 знака и берет имя до точки, номер строки, родитель как -1 элемент словаря конфигураций]

    for lineNum, mainObj in enumerate(list(mainObject1C.keys())):  #Генерация позиции в файле
        try:
            mainObject1C[mainObj].pos = mainObject1C[mainObj].pos[0], list(mainObject1C.values())[lineNum + 1].pos[0] - 1
        except IndexError:
            mainObject1C[mainObj].pos = mainObject1C[mainObj].pos[0], len(df[1])

    for lineNum, obj in enumerate(list(object1C.keys())):  #Генерация позиции в файле
        try:
            object1C[obj].pos = object1C[obj].pos[0], list(object1C.values())[lineNum + 1].pos[0] - 1
        except IndexError:
            object1C[obj].pos = object1C[obj].pos[0], len(df[1])

    propAgregator(df, object1C)

    return configuration1C, mainObject1C, object1C

def propAgregator(df, object1C):

    docMove = list()

    for key in list(object1C.keys()):
        if object1C[key].parent == 'Документы':
            for lineNumber, lineData in enumerate(df.iloc[object1C[key].pos[0]:object1C[key].pos[1], 3]):
                if re.match(r'Движения:', str(lineData)):
                    count = 1
                    while df.iloc[object1C[key].pos[0] + lineNumber + count, 4]:
                        docMove.append(*([(str(df.iloc[object1C[key].pos[0] + lineNumber + count, 4])[str(df.iloc[object1C[key].pos[0] + lineNumber + count, 4]).find('.')+1:])]))
                        count += 1
                    object1C[key].prop = docMove

if __name__ == "__main__":
    pandasDataParce()
