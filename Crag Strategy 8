import random

def diceRoll():
    return random.randint(1,6)

def Roll3():
    return [diceRoll(),diceRoll(),diceRoll()]

## Finds the highest score out of 3 dice, then removes category
def Highest(p1_r1, cat):
    if ((p1_r1[0] == p1_r1[1]) and (p1_r1[0] == p1_r1[2]) and p1_r1[0] in cat):
        triple = sum(p1_r1)
        try:
            cat.remove(p1_r1[0])
        except: ValueError
        return triple
    elif ((p1_r1[0] == p1_r1[1]) and (p1_r1[0] in cat) and (p1_r1[2] in cat)):
        double = p1_r1[0] + p1_r1[1]
        single = p1_r1[2]
    elif ((p1_r1[0] == p1_r1[1]) and (p1_r1[0] in cat) and (p1_r1[2] not in cat)):
        double = p1_r1[0] + p1_r1[1]
        single = 0
        
    elif ((p1_r1[0] == p1_r1[2]) and (p1_r1[0] in cat) and (p1_r1[1] in cat)):
        double = p1_r1[0] + p1_r1[2]
        single = p1_r1[1]
    elif ((p1_r1[0] == p1_r1[2]) and (p1_r1[0] in cat) and (p1_r1[1] not in cat)):
        double = p1_r1[0] + p1_r1[2]
        single = 0
        
    elif ((p1_r1[1] == p1_r1[2]) and (p1_r1[1] in cat) and (p1_r1[0] in cat)):
        double = p1_r1[1] + p1_r1[2]
        single = p1_r1[0]
    elif ((p1_r1[1] == p1_r1[2]) and (p1_r1[1] in cat) and (p1_r1[0] not in cat)):
        double = p1_r1[1] + p1_r1[2]
        single = 0
        
    else:
        HRD1= []
        for i in range(3):
            if (p1_r1[i] in cat):
                HRD1.append(p1_r1[i])
            else:
                HRD1.append(0)
        try:
            cat.remove(max(HRD1))
        except: ValueError
        return max(HRD1)
    
    if double >= single:
        try:
            cat.remove(double/2)
        except: ValueError
        return double
    else:
        try:
            cat.remove(single)
        except: ValueError
        return single


games = 0
p1_avg = 0
g = 10000
p1_SC = []
p1_total = []

while games < g:
    
    cat = [6, 5, 4, 3, 2, 1]
    turn = 0
    p1_tot = 0

    while turn < 6:
        
        p1_r1 = Roll3()
        HRD = []
        p1_max = max(p1_r1)
        
## Checks if the rolled dice was a triple not necessary but oh well lmao
        if((p1_r1[0] == p1_r1[1]) and (p1_r1[0] == p1_r1[2]) and p1_r1[0] in cat):
            pass

## Checks if the rolled dice was a double & available in cat, then rolls the other dice
        elif((p1_r1[0] == p1_r1[1]) and (p1_r1[0] in cat)):
            p1_r1[2] = diceRoll()
        elif((p1_r1[0] == p1_r1[2]) and (p1_r1[0] in cat)):
            p1_r1[1] = diceRoll()
        elif((p1_r1[1] == p1_r1[2]) and (p1_r1[1] in cat)):
            p1_r1[0] = diceRoll()
    

## All 3 dice are different, find the highest dice available in catergories
        else: 
            for i in range(3):
                if (p1_r1[i] in cat):
                    HRD.append(p1_r1[i])
                else:
                    HRD.append(0)
            p1_max = max(HRD)

## Rerolls dice that aren't equal to the highest rolled dice, then finds the highest score 
        for i in range(3):
            if (p1_r1[i] in cat and p1_r1[i] == p1_max):
                pass
            elif (p1_r1[i] in cat and p1_r1[i] != p1_max):
                p1_r1[i] = diceRoll()
            elif (p1_r1[i] not in cat):
                p1_r1[i] = diceRoll()
            else:
                pass
        
        p1_tot += Highest(p1_r1, cat)
        p1_SC.append(p1_r1)
        turn += 1    
            
    games += 1
    p1_total.append(p1_tot)

p1_avg = (sum(p1_total)/g)  
