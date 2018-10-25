#Logan Nelson and Cameron Murphy
#10/25/18
#Final game for term one
import sys


def game_over():
    print("You lost the game,You have been DISQUALIFIED. Don't worry, you can try again now")
    main_menu()
    
print("Running Simulator")


def main_menu():
    answer= input("Would you like to Play? yes or no: ").lower()
    if answer == ("yes"):
        print("Good choice! You are now at a race course. ")
        run_race()
    elif answer == ("no"):
        game_over()
    else:
        print("please only enter yes or no")
        



def run_race():
        answer= input("Would you like to run in the race? yes or no: ").lower()
        if answer == ("yes"):
            print("Good choice! ")
            sprint()
        elif answer == ("no"):
            game_over()
        else:
            print("please only enter yes or no")



def sprint():
    print("Proceed to the starting line of the race")
    answer= input("Would you like to Sprint? yes or no: ").lower()
    if answer == ("yes"):
        print("You sprint when you hear the gun. You get into a good position ahead of a lot of people.")
        sandpit()
    elif answer == ("no"):
        game_over()
    else:
        print("please only enter yes or no")

def sandpit():
    print("You've reached a sandpit.")
    answer= input("Do you run on your toes or heels? toes or heels: ").lower()
    if answer == ("toes"):
        print("You sprint when you hear the gun. You get into a good position ahead of a lot of people.")
        tree_root_1()
    elif answer == ("heels"):
        print("You trip because you are too slow and get trampled")
        game_over()
    else:
        print("please only enter toes or heels")
        
def tree_root_1():
    print("You've reached a tree in your way.")
    answer= input("Do you run on the inside of the tree or the outside? inside or outside: ").lower()
    if answer == ("outside"):
        print("You run in the dirt and pass some people.")
        turn_1()
    elif answer == ("inside"):
        print("You run on the roots and twist your ankle and can't finish the race.")
        game_over()
    else:
        print("please only enter inside or outside")
        
def turn_1():
    print("You've reached the first turn.")
    answer= input("Do you turn left or right? left or right: ").lower()
    if answer == ("left"):
        print("You turn left and you continue along the course.")
        baseball()
    elif answer == ("right"):
        print("You turn the wrong way and run off the course.")
        game_over()
    else:
        print("please only enter left or right")
        

def baseball():
    print("You look ahead and see the baseball diamond.")
    answer= input("Do you want to keep running or go play baseball? run or play: ").lower()
    if answer == ("run"):
        print("You keep running and aren't distracted")
        tree_root_2()
    elif answer == ("play"):
        print("You run off the course to play baseball and have more fun.")
        game_over()
    else:
        print("please only enter run or play")
        

def tree_root_2():
    print("You've reached a tree in your way.")
    answer= input("Do you run on the inside of the tree or the outside? inside or outside: ").lower()
    if answer == ("inside"):
        print("You run in the dirt and pass some people.")
        turn_2()
    elif answer == ("outside"):
        print("You ran on the roots and twist your ankle and can't finish the race.")
        game_over()
    else:
        print("please only enter inside or outside")
        
def turn_2():
    print("You've reached a turn.")
    answer= input("Do you turn left or right? left or right: ").lower()
    if answer == ("left"):
        print("You turn left and you continue along the course.")
        turn_3()
    elif answer == ("right"):
        print("You turn the wrong way and run off the course.")
        game_over()
    else:
        print("please only enter left or right")
        
def turn_3():
    print("You've reached a turn.")
    answer= input("Do you turn left or right? left or right: ").lower()
    if answer == ("right"):
        print("You turn right and you continue along the course.")
        tree_root_3()
    elif answer == ("right"):
        print("You turn the wrong way and run off the course.")
        game_over()
    else:
        print("please only enter left or right")
        
def tree_root_3():
    print("You've reached a tree in your way.")
    answer= input("Do you run on the inside of the tree or the outside? inside or outside: ").lower()
    if answer == ("outside"):
        print("You run in the dirt and pass some people.")
        turn_4()
    elif answer == ("inside"):
        print("You run on the roots and twist your ankle and can't finish the race.")
        game_over()
    else:
        print("please only enter inside or outside")

def turn_4():
    print("You've reached a turn.")
    answer= input("Do you turn left or right? left or right: ").lower()
    if answer == ("right"):
        print("You turn right and you continue along the course.")
        tree_root_4()
    elif answer == ("right"):
        print("You turn the wrong way and run off the course.")
        game_over()
    else:
        print("please only enter left or right")


def tree_root_4():
    print("You've reached a tree in your way.")
    answer= input("Do you run on the inside of the tree or the outside? inside or outside: ").lower()
    if answer == ("inside"):
        print("You run in the dirt and pass some people.")
        turn_5()
    elif answer == ("outside"):
        print("You ran on the roots and twist your ankle and can't finish the race.")
        game_over()
    else:
        print("please only enter inside or outside")


def turn_5():
    print("You've reached a turn.")
    answer= input("Do you turn left or right? left or right: ").lower()
    if answer == ("right"):
        print("You turn right and you continue along the course.")
        home_base()
    elif answer == ("right"):
        print("You turn the wrong way and run off the course.")
        game_over()
    else:
        print("please only enter left or right")


def home_base():
    print("You are comming back towards camp and hear your teamates cheering.")
    answer= input("Do you stop at camp or keep going? camp or run : ").lower()
    if answer == ("run"):
        print("You are almost done so you keep going.")
        turn_6()
    elif answer == ("camp"):
        print("You take a break and Johnson yells at you.")
        game_over()
    else:
        print("please only enter camp or run ")
 

def turn_6():
    print("You've reached a turn.")
    answer= input("Do you turn left or right? left or right: ").lower()
    if answer == ("left"):
        print("You turn left and you continue along the course.")
        turn_7()
    elif answer == ("right"):
        print("You turn the wrong way and run off the course.")
        game_over()
    else:
        print("please only enter left or right")
      
def turn_7():
    print("You've reached a turn.")
    answer= input("Do you turn left or right? left or right: ").lower()
    if answer == ("left"):
        print("You turn left and you continue along the course.")
        sprint_2()
    elif answer == ("right"):
        print("You turn the wrong way and run off the course.")
        game_over()
    else:
        print("please only enter left or right")
      

def sprint_2():
    print("You can see the finish line!")
    answer= input("Would you like to Sprint? yes or no: ").lower()
    if answer == ("yes"):
        print("You sprint and pass 10 people, but wait what's that??.")
        blue_shell()
    elif answer == ("no"):
        print("You get passed by 5 people.\nYou placed in the top 20. Congratulations!")
        print("Game Over")
    else:
        print("please only enter yes or no")

def blue_shell():
    print("Oh NO! It's a flying blue shell! It's coming straight at you.")
    answer= input("What do you do? slow down  or keep going : ").lower()
    if answer == ("slow down"):
        print("The shell hits the person that just passed you.")
        celebrate()
    elif answer == ("keep going"):
        print("You are shellshocked!\nYou finished the race in second Place.\nCongrats first loser")
    else:
        print("please only enter slow down or keep going")
 
def celebrate():
    print("You pass him back because he is now temporarily dazed, you're about to win!")
    answer= input("Do you want to celebrate early? yes or no : ").lower()
    if answer == ("yes"):
        print("You decided to celebrate.")
        celebration()
    elif answer == ("no"):
        print("You kept going strong and finished in First Place!\nCongrats!!!")
    else:
        print("please only enter yes or no")
 
def celebration():
    print("You are now going to celebrate")
    answer= input("How do you want to celebrate? dab or dance: ").lower()
    if answer == ("dab"):
        print("You dab and the person in second place(who just got hit by a blue shell) has passed you! You are a failure!")
        game_over()
    elif answer == ("dance"):
        print("You did a cringy dance.\nThe crowd now boo's you and since you took the extra time, you get passed at the very last second and finish in second place.")
        
    else:
        print("please only enter dab or dance")
 

















main_menu()
##def ():
##    print("")
##    answer= input("?  or : ").lower()
##    if answer == (""):
##        print("")
##        ()
##    elif answer == (""):
##        print("")
##        game_over()
##    else:
##        print("please only enter  or ")
 




        
