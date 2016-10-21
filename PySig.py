# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 16:59:45 2016

@author: PRABIR GHOSH
"""

import Image

class Signature():
    __signature__ = None
    def __init__(self, data):
        #
        #cropping signature area from raw
        #
        Img = Image.open(data)
        ub = (0,0)
        lb = (0,0)
        for x in range(Img.width):
            for y in range(Img.height):
                pixel = Img.getpixel((x,y))
                if(pixel == (239,228,176)):
                    ub = (x,y)
                    break
            if(ub != (0,0)):
                break
        for x in range(Img.width):
            for y in range(Img.height):
                pixel = Img.getpixel((Img.width - x - 1,Img.height - y - 1))
                if(pixel == (239,228,176)):
                    lb = (Img.width - x - 1,Img.height - y - 1)
                    break
            if(lb != (0,0)):
                break
        SignatureArea = Img.crop((ub[0],ub[1], lb[0],lb[1]))
            
        #
        #extracting signature from signature area
        #
        for y in range(SignatureArea.height):
            for x in range(SignatureArea.width):
                pixel = SignatureArea.getpixel((x,y))
                if(pixel == (239,228,176)):
                    SignatureArea.putpixel((x,y),(255,255,255))
        
        top = 0
        for y in range(SignatureArea.height):
            for x in range(SignatureArea.width):
                pixel = SignatureArea.getpixel((x,y))
                if(pixel[0] < 30 and pixel[1] < 30 and pixel[2] < 30):
                    top = y
                    break
            if(top != 0):
                break
        left = 0
        for x in range(SignatureArea.width):
            for y in range(SignatureArea.height):
                pixel = SignatureArea.getpixel((x,y))
                if(pixel[0] < 30 and pixel[1] < 30 and pixel[2] < 30):
                    left = x
                    break
            if(left != 0):
                break
        right = 0
        for x in range(SignatureArea.width):
            for y in range(SignatureArea.height):
                pixel = SignatureArea.getpixel((SignatureArea.width - x - 1, SignatureArea.height -y - 1))
                if(pixel[0] < 30 and pixel[1] < 30 and pixel[2] < 30):
                    right = SignatureArea.width - x
                    break
            if(right != 0):
                break
        bottom = 0
        for y in range(SignatureArea.height):
            for x in range(SignatureArea.width):
                pixel = SignatureArea.getpixel((SignatureArea.width - x - 1,SignatureArea.height -  y - 1))
                if(pixel[0] < 30 and pixel[1] < 30 and pixel[2] < 30):
                    bottom = SignatureArea.height - y
                    break
            if(bottom != 0):
                break
        self.__signature__ =  SignatureArea.crop((left,top,right,bottom))
        
    def saveSig(self, id):
        if(self.__signature__ != None):
        	self.__signature__.save(id + '.jpg')
        
    def getSignature(self):
        img = self.__signature__
        if(img != None):
        	return img
    def filteration(self):
        print('None')

    def fitTest(self, sample):
        print('None')

    def verify(self, signature2):
        match = 0
        total = 0
        sample = signature2.getSignature()
        if(sample != None or self.__signature__ != None):
        	for x in range(self.__signature__.width):
        		for y in range(self.__signature__.height):
        			if(self.__signature__.getpixel((x,y)) == sample.getpixel((x,y))):
        				match = match + 1
        				total = total + 1
        	return match/total
        return 0
