#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 21:49:05 2022

@author: ary
"""

class Cat:
    # characteristics
    name = None
    age = None
    isHappy = None
    #some = [] {}
    
    # functions
    def set_data(self, name, age, isHappy):
    #def sat_data(self, q, w, e): # OK
        self.name = name # =q
        self.age = age
        self.isHappy = isHappy
        
    def get_data(self):
        print(self.name, " age:", self.age, ". Happy", self.isHappy)
    
# objects
cat1 =  Cat() # creates default object
cat1.name = "Barsik"
cat1.age = 3
cat1.isHappy = True   

cat2 =  Cat()
cat2.name = "Zusja"
cat2.age = 2
cat2.isHappy = False 

print(cat1.name)
print(cat2.name)

# The same using functions
cat1 =  Cat()
cat1.set_data("Barsik", 3, True)
cat1.get_data()


#%% Konstructor
class Cat:
    # characteristics
    name = None
    age = None
    isHappy = None
    #some = [] {}
    
    def __init__(self, name, age, isHappy):
        self.name = name # =q
        self.age = age
        self.isHappy = isHappy
        
        self.get_data()


    def get_data(self):
        print(self.name, " age:", self.age, ". Happy", self.isHappy)

cat1 =  Cat("Barsik", 3, True) # creates object with parameters

class Cat:
    # characteristics
    name = None
    age = None
    isHappy = None
    #some = [] {}
    
    def __init__(self, name, age, isHappy):
        # self.name = name # =q
        # self.age = age
        # self.isHappy = isHappy
        self.set_data(name, age, isHappy)
        
        self.get_data()

    # functions
    def set_data(self, name, age, isHappy):
    #def sat_data(self, q, w, e): # OK
        self.name = name # =q
        self.age = age
        self.isHappy = isHappy

    def get_data(self):
        print(self.name, " age:", self.age, ". Happy", self.isHappy)

cat1 =  Cat("Barsik", 3, True) # creates object with parameters

#%%


class Cat:
    name = None
    age = None
    isHappy = None
    
    def __init__(self, name = None, age = None, isHappy = None):
        self.set_data(name, age, isHappy)
        self.get_data()

    def set_data(self, name = None, age = None, isHappy = None):
        self.name = name # =q
        self.age = age
        self.isHappy = isHappy

    def get_data(self):
        print(self.name, " age:", self.age, ". Happy", self.isHappy)

cat1 =  Cat("John", 2, True)
cat1.set_data("John", 6)

cat1 =  Cat()