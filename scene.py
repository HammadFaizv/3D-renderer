from model import *
import random

class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()

        # skybox
        self.skybox = SkyBox(app)

    def add_object(self, obj):
        self.objects.append(obj)
    
    def load(self):
        app = self.app
        add = self.add_object

        n, s = 6, 4
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cube(app, pos=(x, -s, z), tex_id=random.randint(0, 3), rot=(random.choice([0, 45]), random.choice([0, 45]), random.choice([0, 45]))))

    def render(self):
        for obj in self.objects:
            obj.render()
        self.skybox.render()