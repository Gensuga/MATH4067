import random

def diceRoll():
    return random.randint(1,6)

def Roll3():
    return [diceRoll(),diceRoll(),diceRoll()]


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
        
## Checks if the rolled dice were a triple
        if((p1_r1[0] == p1_r1[1]) and (p1_r1[0] == p1_r1[2])):
            pass

## Checks if the rolled dice was a double & rolls the other dice
        elif((p1_r1[0] == p1_r1[1]) and (p1_r1[0] != p1_r1[2])):
            p1_r1[2] = diceRoll()
        elif((p1_r1[0] == p1_r1[2]) and (p1_r1[0] != p1_r1[1])):
            p1_r1[1] = diceRoll()
        elif((p1_r1[1] == p1_r1[2]) and (p1_r1[0] != p1_r1[2])):
            p1_r1[0] = diceRoll()
    
## No doubles/triples rolled
        else:
    
## Find highest dice rolled still available in categories
            for i in range(3):
                if (p1_r1[i] in cat):
                    HRD.append(p1_r1[i])
                else:
                    HRD.append(0)
            p1_max = max(HRD)

## Rerolls dice that aren't equal to the highest rolled dice
            for i in range(3):
                if (p1_r1[i] in cat and p1_r1[i] == p1_max):
                    pass
                elif (p1_r1[i] in cat and p1_r1[i] != p1_max):
                    p1_r1[i] = diceRoll()
                elif (p1_r1[i] not in cat):
                    p1_r1[i] = diceRoll()
                else:
                    pass
        
## Find the highest/lowest rolled dice still available in categories after rerolls
        HRD1 = []
        for i in range(3):
            if (p1_r1[i] in cat):
                HRD1.append(p1_r1[i])
            else:
                HRD1.append(0)
                
        LRD = []
        for i in range(3):
            if (p1_r1[i] in cat):
                LRD.append(p1_r1[i])
            else:
                HRD.append(7)
                
        p1_max1 = max(HRD1)
        p1_min = min(HRD1)

## If the highest rolled dice > 3 then select highest rolled dice
        if(max(p1_r1) > 3):
            for i in range(3):
                if (p1_r1[i] in cat and p1_r1[i] == p1_max1):
                    p1_tot += p1_r1[i]
                elif (p1_r1[i] not in cat):
                    p1_tot += 0
    
            try:
                cat.remove(p1_max1)
            except: ValueError
            p1_SC.append(p1_r1)
            turn += 1

## If the highest rolled dice <= 3 then select lowest rolled dice
        else:
            for i in range(3):
                if (p1_r1[i] in cat and p1_r1[i] == p1_min):
                    p1_tot += p1_r1[i]
                elif (p1_r1[i] not in cat):
                    p1_tot += 0
            
            try:
                cat.remove(p1_min)
            except: ValueError
            p1_SC.append(p1_r1)
            turn += 1
            
    games += 1
    p1_total.append(p1_tot)

p1_avg = (sum(p1_total)/g)
