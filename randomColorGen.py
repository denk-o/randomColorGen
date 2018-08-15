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
        g = g_bias+r+_bias
        self.b_bias = b_bias
        b=g+b_bias
        self.grayscale = grayscale
        tot = b+grayscale
        self.color_list = ['red', 'green', 'blue', 'grayscale']
        self.bias_list = [self.r_bias, g, b, tot]
    def genBiasedHex(self):
        rgb = random()
        res = 0
        for bias in bias_list:
            if rgb < bias:
                return self.makeColorPart(self.color_list[self.bias_list.index(bias)])
    def genBiasedRGB(self):
        rgb = random()
        res = 0
        for bias in bias_list:
            if rgb < bias:
                return self.makeColor(self.color_list[self.bias_list.index(bias)])
    def makeColor(self, color):
        col = randint(40,255)
        if color == 'red':
            return "rgb(%, 0, 0)" % col
        elif color == 'green':
            return "rgb(0, %, 0)" % col
        elif color == 'blue':
            return "rgb(0, 0, %)" % col
        else:
            col = randint(0,255)
            return "rgb(%(color), %(color), %(color))" % {'color': col}
    def makeColorPart(self, color):
        col = randint(40,255)
        hex = hex(col)
        if color == 'red':
            return "0x%0000" % hex
        elif color == 'green':
            return "0x00%00" % hex
        elif color == 'blue':
            return "0x0000%" % hex
        else:
            col = randint(0,255)
            return "0x%(color)%(color)%(color)" % {'color': hex}
