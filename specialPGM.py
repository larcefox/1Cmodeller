from graphviz import Digraph, Graph
from pandasParser import *

if __name__ == "__main__":

    listIterestedInMainObj = ['Документы', 'РегистрыНакопления', 'Справочники']
    listIterestedInObj = ['ндк_КарточкаШтрафа', 'бит_АктуализацияБюджета', 'ндк_ВзаимозачетПоДоговорам_НДК']
    configuration1C, mainObject1C, object1C = pandasDataParce()
    print (len(configuration1C), len(mainObject1C), len(object1C))

    dot = Digraph(format='pdf', comment='1C object model', engine='sfdp') # node_attr={'shape': 'circle'}, engine='osage'

    for graph in list(configuration1C.keys()):

        dot.node(str(configuration1C[graph].hashName), configuration1C[graph].name,
                 fontsize=configuration1C[graph].fontSize,
                 shape=configuration1C[graph].shape, width=configuration1C[graph].width,
                 height=configuration1C[graph].height)

        # Цикл считает количество элементов в словаре, высчитывает хеш названия узла и создает вершины по хешу названия и названию, потом связывает вершины по хешу родителя и хешу узла
        for nodeNumber, node in enumerate(list(mainObject1C.keys())):
            if node in listIterestedInMainObj:
                dot.node(mainObject1C[node].hashName, mainObject1C[node].name, fontsize=mainObject1C[node].fontSize,
                         shape=mainObject1C[node].shape, width=mainObject1C[node].width, height=mainObject1C[node].height,
                         cluster=mainObject1C[node].parent)  # объявление ноды - хэш ноды, имя ноды

        for node in list(mainObject1C.keys()):
            if node in listIterestedInMainObj:
                dot.edge(mainObject1C[node].hashParent, mainObject1C[node].hashName,
                         arrowhead='vee')  # объявление связи с родителем - хэш родителя, хэш ноды style = 'dotted'

        for nodeNumber, subnode in enumerate(list(object1C.keys())):
            if subnode in listIterestedInObj:
                if object1C[subnode].name not in mainObject1C:
                    dot.node(object1C[subnode].hashName, object1C[subnode].name, fontsize=object1C[subnode].fontSize,
                             shape=object1C[subnode].shape, width=object1C[subnode].width, height=object1C[subnode].height,
                             cluster=object1C[subnode].parent)
                    dot.edge(object1C[subnode].hashParent, object1C[subnode].hashName, arrowhead='normal')

dot.render('output', '.', view=True)