class MainObject1C():
    objectList = [] # все объекты класса записываются в список
    def __init__(self, name, parent, startLine):
        self.name = name
        self.hashName = str(hash(self.name))
        self.parent = parent
        self.hashParent = str(hash(parent))
        self.startLine = startLine
        self.__class__.objectList.append(self)


class Object1C(MainObject1C):
    def __init__(self, name, parent, startLine):
        super().__init__(name, parent, startLine)
