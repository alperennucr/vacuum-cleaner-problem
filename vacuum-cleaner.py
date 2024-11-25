# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 17:18:40 2024

@author: Alperen
"""

import random as r

randNum = r.randint(0,1)
randNum2 = r.randint(0, 1)
isSucceed = False
print("NOTE: Carpet array has two spaces. That spaces means there are two carpets. And the numbers specify if there any dirt on the carpet.")
carpets = [randNum, randNum2] # 0-> dirty, 1-> clean
print("Carpets: ["+str(carpets[0]) +", "+str(carpets[1])+"]")
visits = [0,0]

robot = r.randint(0,1)
print("Robot is on carpet "+str(robot)+"\n\n")

def Move():
    global robot
    
    if robot == 0:
        robot = 1
    else:
        robot = 0
    print("Robot is on carpet "+str(robot)+" from now on")

def CheckGoalState():
    global isSucceed
    #print("visits içindeki 0 sayısı: "+str(visits.count(0)))
    #visits içindeki hepsi 0 ise true dön, 1 tane dahi 1 var ise false dön
    if visits.count(1) == len(visits):
        print("---> ALL carpets are CLEAN ")
        isSucceed = True
    else:
        Move()
        isSucceed = False

while isSucceed == False:
    if carpets[robot] == 1:#If the carpet that robot stands on is dirty
        carpets[robot] = 0
        visits[robot] = 1
        print("Carpet "+str(robot)+" is cleaned")
        print("Carpets: ["+str(carpets[0]) +", "+str(carpets[1])+"]")
        CheckGoalState()
        
    else:#If the carpet that robot stands on is clean
        visits[robot] = 1
        print("No dirt on carpet "+ str(robot))
        CheckGoalState()