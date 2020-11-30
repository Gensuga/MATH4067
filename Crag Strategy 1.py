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
        p1_max = max(p1_r1)
        check = False
        HRD = []
        tmp_array = []
        
## Checks if the rolled dice is equal to the max value and if dice is still available, rerolls if not
        while check == False:
            tmp_array = [i for i, j in enumerate(p1_r1) if (j != p1_max) or j not in cat]
            for i in range(len(tmp_array)):
                p1_r1[tmp_array[i]] = diceRoll()
            check = True   
       
## Finds the highest rolled dice still available in categories
        for i in range(3):
            if (p1_r1[i] in cat):
                HRD.append(p1_r1[i])
            else:
                HRD.append(0)
            p1_max1 = max(HRD)

## Sums the dice of highest value category available
        for i in range(3):
            if (p1_r1[i] in cat and p1_r1[i] == p1_max1):
                p1_tot += p1_r1[i]
            elif (p1_r1[i] not in cat):
                p1_tot += 0
        
## Adds this rounds dice onto the scorecard and removes used category
        p1_SC.append(p1_r1)
        try:
            cat.remove(p1_max1)
        except: ValueError
        
        turn += 1
    games += 1
    
    p1_total.append(p1_tot)

p1_avg = (sum(p1_total)/g)
