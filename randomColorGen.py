import random
import os
from random import seed
from random import random
from random import randint
import datetime
from datetime import datetime

class randomColorGen:
    def __init__(self):
        #unused vars after refactor
        self.color = ''
        self.seed = seed(datetime.utcnow().microsecond())
    def genRandRGB(self):
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)
        rgb = {'r': r, 'g': g, 'b':b}

        return rgb
    def genRandHex(self):
        hex = "%06x" % randint(0, 0xFFFFFF)
        return hex


class biasedRandomColorGen:
    def __init__(self, r_bias, g_bias, b_bias, grayscale):
        self.r_bias = r_bias
        self.g_bias = g_bias
        self.b_bias = b_bias
        self.grayscale = grayscale
    def genBiasedHex(self):

    def genBiasedRGB(self):
        rand_red = random()
        rand_green = random()
        rand_blue = random()
