#Emergence Project V1.0
#Date Created 29th December 2013
#No Idea what We are Doing

#Create general program loop
#While you choose to live, you live.
import time
import random
Gameover = False;
print("You face the Dragon. How long can you live?")
time.sleep(5)
Dragon_HP=10
Dragon_Attack=0
Your_life=0
Player_Attack=0
while not Gameover:
    Player_Input = input("Press 'd' to dodge or 'r' to run or 's' to strike: "); #Gather user Input
    Dragon_Attack = random.randint(1,10)
    Player_Attack = random.randint(1,10)+Your_life
    
    #Begin processing user input
    if Dragon_Hp<0:
        break
    else:
        if Player_Input == 'r':
            Gameover = True;
            print("You lived for %s seconds. You did not slay the Dragon.")%Your_life
            time.sleep(5)
        elif Player_Input =='s':
            print("You lunge at the Dragon!")
            time.sleep(5)
            if Dragon_Attack>Player_Attack:
                print("The Dragon snaps and swallows you whole!")
                print("You lived for %s seconds. You did not slay the Dragon.")%Your_life
            else:
                print("You cut the Dragon!")
                Your_life+=1
                Dragon_Hp-=1
        else Player_Input=='d':
            print("You try to dodge the Dragon's attack!")
            Player_Attack=Player_Attack+2
            if Dragon_Attack>Player_Attack:
                print("The Dragon snaps and swallows you whole!")
                print("You lived for %s seconds. You did not slay the Dragon.")%Your_life
                time.sleep(5)
        else:
            print("You dodged the Dragon!")
print("You defeated the Dragon!")
time.sleep(5)
