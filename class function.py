# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 16:12:58 2018

@author: Administrator
"""
class person:
    def __init__(self,name):
        self.__aname=name
    def __sayhi(self):
        print('hi i\'m %s'%self.aname)

p=person('mars')
p.__init__('ss')
print(p.__aname)
p.__sayhi()
