############################################
# Coy Kwan 
# cs101
# Program 6
############################################
import random 
class bacteria(object):
    def __init__(self, health = 10, lifeSpan = 15, resistance = 3, birthCounter = 3):
        self.health = health

        self.lifeSpan = lifeSpan

        self.resistance = resistance + random.randint(-1,1) # <== Im am not for sure if this properly mutates the bacteria instance 
        if self.resistance <= 0:
            self.resistance = 1
        if self.resistance >= 10:
            self.resistance = 10

        self.birthCounter = birthCounter

    def __str__(self):
        return ('H = {} R = {} LS = {} BC = {}'.format(self.health, self.resistance, self.lifeSpan, self.birthCounter))

    def isAlive(self):
        if self.health <= 0:
            return False 
        elif self.lifeSpan <= 0:
            return False 
        else:
            return True 

    def tick(self):
        self.lifeSpan += -1
        self.birthCounter += -1

    def dose(self, dosage):
        damage = 1/self.resistance * dosage
        return damage
        

    def reproduce(self):
        if self.isAlive() is True:
            if self.birthCounter == 0:
                self.birthCounter = 3
                return bacteria(resistance = self.resistance)

class host(object):
    def __init__(self, bacteriaNum):
        self.bacteriaNum = bacteriaNum

    def __str__(self): # string im host also returns the averages of all the data associated with the hosts infection 
        HealthTotal = 0
        HealthAverage = 0
        for bact in self.bacteriaNum:
            HealthTotal += bact.health
            HealthAverage = HealthTotal/len(self.bacteriaNum)
        resistanceTotal = 0
        resistacneAverage = 0

        for bact in self.bacteriaNum:
            resistanceTotal += bact.resistance
            resistacneAverage = resistanceTotal/len(self.bacteriaNum)
        if len(self.bacteriaNum) == 0 :
            return ('Count = 0 Average Health = 0 Average Resistance = 0')
        return ('Count = {} Average Health = {} Average Resistance = {}'.format(len(self.bacteriaNum), HealthAverage, resistacneAverage ))  





# This Function is used to set up the infection that takes place in the host, it keeps track of all the bacteria and returns the bacteria in list form 
def Infection(doseAmount, halfDose):
    bacterialst = []
    alphaBacteria = bacteria()
    bacterialst.append(alphaBacteria)
    numTicks = 0
    for x in range(45):
        for bact in bacterialst:
            bact.tick()
            numTicks += 1
        if halfDose is True:
            if numTicks >= 37:
                for bact in bacterialst:
                    if numTicks % 2 == 0: 
                        bact.health = bact.health - bact.dose(doseAmount)
        elif numTicks >= 30:
            for bact in bacterialst:                
                bact.health = bact.health - bact.dose(doseAmount)
        for bact in bacterialst:
            if bact.isAlive() is False:
                bacterialst.remove(bact)
            else:
                spawn = bact.reproduce()
                if spawn is not None:
                    bacterialst.append(spawn)
    return(bacterialst)


# Passing all of the functions their parameters 
noDoesInfection = Infection(0, False)
noDose = host(noDoesInfection)
halfDoseInfection = Infection(19, True) # The half dose group always is eliminated upon using 25 dosage strength I was unsure why 19 was the dosage that would survive some of the time
halfDose = host(halfDoseInfection)
fullDoseInfection = Infection(25, False)
fullDose = host(fullDoseInfection)

print('No Dose')
print(noDose)

print('Half dose')
print(halfDose)

print('Full Dose')
print(fullDose)







