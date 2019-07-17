from panda3d.core import *
from direct.showbase.ShowBase import ShowBase
import codecs, random
import dataPars


if __debug__: loadPrcFile('zConfig.prc')

class MainObjects(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.x = 0
        self.y = 150

        self.mainObjects = self.render.attachNewNode('Main 1C objects')

        self.acceptOnce('q',exit)

        self.mainVisualObj = dict()
        self.mainRegistryText = dict()
        self.text = dict()

        self.x = -60
        self.y = 150
        self.z = 0

        self.font = self.loader.loadFont('17430.otf')
        # self.text.setText('This is the text')
        # self.textNodePath = self.aspect2d.attachNewNode(self.text)
        # self.textNodePath.setScale(1)
        # self.textNodePath.setPos(-62 , 149, 0)
        # self.textNodePath.reparentTo(self.mainObjects)

        with codecs.open("data.txt", 'rU', 'utf-16') as f_obj:
            mainObjs1C, objs1C = dataPars.csv_dict_reader(f_obj)

        for key in list(mainObjs1C.keys()):
            randx, randy, randz = random.randint(-5, 5), 90, random.randint(-5, 5)
            self.mainVisualObj[key] = self.loader.loadModel("1Cregistr.egg")
            self.mainVisualObj[key].setHpr(randx, randy, randz)
            self.mainVisualObj[key].setPos(self.x, self.y, self.z)
            self.mainVisualObj[key].reparentTo(self.mainObjects)
            self.mainVisualObj[key].setTwoSided(True)

            self.text[key] = TextNode('registry text node')
            self.text[key].setTextColor(1, 0, 0, 1)
            self.text[key].setFont(self.font)

            self.text[key].setText(key)
            self.mainRegistryText[key] = self.aspect2d.attachNewNode(self.text[key])
            self.mainRegistryText[key].setScale(1)
            self.mainRegistryText[key].setPos(-4, 0, 0.5)
            self.mainRegistryText[key].setHpr(0, randy+180, 0)
            self.mainRegistryText[key].reparentTo(self.mainVisualObj[key])
            print(key)
            self.x += 15

            if self.x > 60:
                self.x = 0
                self.z -= 8

app = MainObjects()
app.run()