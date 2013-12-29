#Emergence Project V1.0
#Date Created 29th December 2013
#No Idea what We are Doing

#Create general program loop
import time
Gameover = False;

while not Gameover:
    Player_Input = input("Press 'e' to exit or 'l' to live: "); #Gather user Input
    
    #Begin processing user input
    if Player_Input == 'e':
        Gameover = True;
    elif Player_Input =='l':
        print("You have choosen to live indeed. A wise choice.")
        time.sleep(10)
