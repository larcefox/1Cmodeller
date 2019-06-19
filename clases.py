class MainObject1C():
    def __init__(self, name, parent, startLine):
        self.name = name
        self.hashName = str(hash(self.name))
        self.parent = parent
        self.hashParent = str(hash(parent))
        self.startLine = startLine


class Object1C(MainObject1C):
    def __init__(self, name, parent, startLine):
        super().__init__(name, parent, startLine)
