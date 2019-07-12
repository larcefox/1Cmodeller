from graphviz import Digraph, Graph
import dataPars
import codecs

# dot = Graph(format='png', comment='The Round Table')
#
# dot.attr('node', shape = 'square', color = "red")
# dot.node('1', 'King Arthur')
# dot.node('2', 'Sir Bedevere the Wise')
# dot.node('3', 'Sir Lancelot the Brave')
# dot.edges(['12', '13'])
# dot.edge('2', '3', constraint='false')
#
# print(dot.source)
#
# dot.render('1.png','.',view=True)

if __name__ == "__main__":

    with codecs.open("data.txt", 'rU', 'utf-16') as f_obj:
        mainObjs1C, objs1C = dataPars.csv_dict_reader(f_obj)

    dot = Digraph(format='pdf', comment='1C object model', node_attr={'shape': 'oval'}, engine='fdp')
    # edge_attr = {'arrowhead': 'diamond', 'arrowsize': '2'}
    dot.node(str(hash('Конфигурация')), 'Конфигурация')

    # Цикл считает количество элементов в словаре, высчитывает хеш названия узла и создает вершины по хешу названия и названию, потом связывает вершины по хешу родителя и хешу узла

    for countOfDictItems in range(len(mainObjs1C.keys())):
        dot.node(list(mainObjs1C.values())[countOfDictItems].hashName, list(mainObjs1C.values())[countOfDictItems].name)
        dot.edge(list(mainObjs1C.values())[countOfDictItems].hashParent, list(mainObjs1C.values())[countOfDictItems].hashName, arrowhead='diamond')

    for countOfDictItems in range(10):
        dot.node(list(objs1C.values())[countOfDictItems].hashName, list(objs1C.values())[countOfDictItems].name)
        dot.edge(list(objs1C.values())[countOfDictItems].hashParent, list(objs1C.values())[countOfDictItems].hashName,
                 arrowhead='vee')

    # print(dot.source)
    dot.render('1', '.', view=True)


