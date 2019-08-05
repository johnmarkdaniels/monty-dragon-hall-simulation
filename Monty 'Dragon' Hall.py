# This is a modification of the Dragon Realm guessing game found in "Invent Your Own Computer
# Games with Python" by Al Sweigart. I've modified it to be a simulator for the Monty Hall
# Problem from probability theory. I first learned about the problem in Leonard Mlodinow's book
# "The Drunkard's Walk" which served as my textbook when I taught a capstone psychology course
# at Fairmont State University. The original program is commented out at the end of this file.

import random
import time

def displayIntro():
    print('''You are in a land full of dragons. In front of you,
you see three caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragons
are greedy and hungry, and they will eat you on sight.''')

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2' and cave != '3':
        print('Which cave will you go into? (1, 2, or 3)')
        cave = input()
    return cave

def freebie(caveNumber):
    deathCaves = caveList
    deathCaves.remove(friendlyCave)
    if caveNumber in deathCaves:
        deathCaves.remove(caveNumber)
        giveaway = deathCaves[0]
        return giveaway
    else:
        giveaway = random.choice(deathCaves)
        return giveaway

def approach():
    print('You approach the cave...')
    print()
    time.sleep(1)
    print('It is dark and spooky...')
    print()
    time.sleep(1)
    print('''A large dragon jumps out in front of you! He opens his jaws and...
offers you a choice.

This is your lucky day, human. I'm going to help you out!''')
    
def switchChoice(giveaway):
    print(f'Cave number {giveaway} will result in your immediate death.')
    switch = ''
    while switch != 'yes' or switch != 'y' or switch != 'no' or switch != 'n':
        print()
        print('Would you like to choose the other door? (yes or no)')
        switch = input()
        return switch

def Switch():
    switchlist = [1,2,3]
    if giveaway in switchlist:
        switchlist.remove(giveaway)
    if caveNumber in switchlist:
        switchlist.remove(caveNumber)
    SwitchedcaveNumber = random.choice(switchlist)
    return SwitchedcaveNumber

def pathinlife(switch, caveNumber):
    if switch == 'yes' or switch == 'y':
        pathinlife = 'learned'
        caveNumber = Switch()
        print(f'Ahh, you are wise in the ways of probability, and you\'ve \ndecided to switch to door number {caveNumber}!')
        print()
        time.sleep(1)
        if caveNumber == friendlyCave:
            print('Congratulations, you are both learned and a little lucky.\nYou survive, AND YOU\'RE RICH!!! I\'m sure you will \nuse your wealth wisely. Enjoy!')
        else:
            print('Despite your mathematical achievements, today just wasn\'t \nyour day. Life isn\'t always fair you know. Brace yourself, \nthis may hurt a little.')
    else:
        print('You really should review how probability works...')
        print()
        time.sleep(1)
        print("You: Math blows! I'm feeling LUCKY! Let's DO this!")
        print()
        time.sleep(1)
        pathinlife = 'lucky'
        if caveNumber == friendlyCave:
            print('Congratulations, you are mathematically inept, but very \nlucky. You win (ie get to live), and you\'re rich!')
        else:
            print('Oh, I\'m so, so sorry. This may sting a bit...')
        

       
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveList = [1, 2, 3]
    friendlyCave = random.randint(1, 3)
    caveNumber = int(chooseCave())
    giveaway = freebie(caveNumber)
    approach()
    switch = switchChoice(giveaway)
    pathinlife(switch, caveNumber)
    
    
    print()
    print()
    print('****************************************')
    print()
    print('Do you want to play again? (yes or no)')
    playAgain = input()


##import random
##import time
##
##def displayIntro():
##    print('''You are in a land full of dragons. In front of you,
##you see two caves. In one cave, the dragon is friendly
##and will share his treasure with you. The other dragon
##is greedy and hungry, and will eat you on sight.''')
##print()
##def chooseCave():
##    cave = ''
##    while cave != '1' and cave != '2':
##        print('Which cave will you go into? (1 or 2)')
##        cave = input()
##    return cave
##def checkCave(chosenCave):
##    print('You approach the cave...')
##    time.sleep(2)
##    print('It is dark and spooky...')
##    time.sleep(2)
##    print('A large dragon jumps out in front of you! He opens his jaws and...')
##    print()
##    time.sleep(2)
##
##    friendlyCave = random.randint(1, 2)
##
##    if chosenCave == str(friendlyCave):
##        print('Gives you his treasure!')
##    else:
##        print('Gobbles you down in one bite!')
##
##playAgain = 'yes'
##while playAgain == 'yes' or playAgain == 'y':
##    displayIntro()
##    caveNumber = chooseCave()
##    checkCave(caveNumber)
##
##    print('Do you want to play again? (yes or no)')
##    playAgain = input()
