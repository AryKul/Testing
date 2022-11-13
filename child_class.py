#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 22:23:14 2022

Nasledovanie
https://www.youtube.com/watch?v=4N4GSzLF7JM&list=PLDyJYA6aTY1lPWXBPk0gw6gR8fEtPDGKa&index=19

@author: ary
"""

class Building: # superClass
    year = None
    city = None
    
    def __init__(self, year, city):
        self.city = city
        self.year = year
        
    def get_info(self):
        print("Year:", self.year, ". City:", self.city)
        
    
school = Building(2000, "Moscow")
house = Building(2000, "Moscow") # we need to add 10 specific funcs for "house", can be added to common class
shop = Building(2000, "Moscow")

#%%
class School(Building): # same
    pass

school = School(2000, "Moscow")
school.get_info() # funcs from Building

#%%
class House(Building): # same
    pass

class Shop(Building): # same
    pass

class School(Building): # same + specific props. Only 1 parent
    pupils = 0
    
    def __init__(self, pupils, year, city):
        super(School, self).__init__(year, city) # call parent and peredayutsya emu?
        self.pupils = pupils
       
    def get_info(self): # overwrite the same fun of parent
        super().get_info()
        print("Pupils:", self.pupils)
        
school = School(100, 2000, "Moscow")    
school.get_info()

# grandchildren
class PrimarySchool(School): # sameBuilding -> School -> Primary School
    pass
#%% Incapsulation -not rally realized in Python
school.year = 5 # dostup otkrit
school.get_info()


# limit access "__name"
class Building: # superClass
    __year = None
    __city = None
    
    def __init__(self, year, city):
        self.city = city
        self.year = year
        
    def get_info(self):
        print("Year:", self.year, ". City:", self.city)

school.__year = 10   # can overwrite     
#print(school.year)
print(school.__year) # cannot print?

