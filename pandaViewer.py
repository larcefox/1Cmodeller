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
        self.x = -60
        self.y = 150
        self.z = 0

        font = self.loader.loadFont('arial.ttf')


        with codecs.open("data.txt", 'rU', 'utf-16') as f_obj:
            mainObjs1C, objs1C = dataPars.csv_dict_reader(f_obj)

        for key in list(mainObjs1C.keys()):
            self.mainVisualObj[key] = self.loader.loadModel("1Cregistr.egg")
            self.mainVisualObj[key].setHpr(random.randint(-5, 5), random.randint(85, 95), random.randint(-5, 5))
            self.mainVisualObj[key].setPos(self.x, self.y, self.z)
            self.mainVisualObj[key].reparentTo(self.mainObjects)
            self.x += 15

            if self.x > 60:
                self.x = 0
                self.z -= 8

app = MainObjects()
app.run()