#Dice game

#The points rolled on each player’s dice are added to their score.
#If the total is an even number, an additional 10 points are added to their score.
#If the total is an odd number, 5 points are subtracted from their score.
#If they roll a double, they get to roll one extra die and get the number of points rolled added to their score.
#The score of a player cannot go below 0 at any point.
#The person with the highest score at the end of the 5 rounds wins.
#If  both  players  have  the  same  score  at  the  end  of  the  5  rounds,  they  each  roll  1  die  and  whoever gets the highest score wins (this repeats until someone wins).

import random
from random import randint
import time
from time import sleep
import re


def welcome():
#welcome messages using time.sleep to stagger them
    print("------------------Welcome To The Dice Game------------------")
    welcome = (""), ("Compete with a friend to get the most points"), ("Roll 2 dice each round"), ("If the total is even you gain 10 points"), ("If the total is odd you lose 5 points"), ("Roll a double and get an extra roll where what you roll is added to your score"), ("The player with the highest score after 5 rounds WINS!"), ("To begin the game please login with each player's accounts"), ("So good luck and enjoy"), ("")
    for i in welcome:
        time.sleep(3)
        print(i)

    
def register():
#registering an account, if rls was 'r'
    print("------------------------Registration------------------------")
    print("")
    PAlign = False

#entering username and and password twice for check
    username = input("Enter a username  ")
    
    
    while PAlign == False:
        print("")
        password = input("Please enter a password  ")
        passwordcheck = input("Please re-enter your password  ")

#if the passwords match, check password suitability
        if password == passwordcheck:
            
#if passwords entered match, check if it follows all rules put in place
#           > 8 characters minimum
#           > contains a symbol (@)
#           > contains a number (1)

#list of symbols
                regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

#checks if password length is less than 8     
                if len(password)<8:
                    x = (""), ("Your password is invalid"), ("It must:  ")
                    for i in x:
                        print(i)
                        time.sleep(1)
#prints requirements in password                       
                    print('''       > 8 characters minimum
       > contains a symbol ([@_!#$%^&*()<>?/\|}{~:])
       > contains a number (1)''')
                    print("")
                    print("Please try again")

#checks if there is a number in the password   
                elif not any(char.isdigit()for char in password):
                     x = (""), ("Your password is invalid"), ("It must:  ")
                     for i in x:
                        print(i)
                        time.sleep(1)
#prints requirements in password                        
                     print('''       > 8 characters minimum
       > contains a symbol ([@_!#$%^&*()<>?/\|}{~:])
       > contains a number (1)''')
                     print("")
                     print("Please try again")

#checks if there is an uppercase letter in the password                    
                elif not any (char.isupper() for char in password):
                    x = (""), ("Your password is invalid"), ("It must:  ")
                    for i in x:
                        print(i)
                        time.sleep(1)
#prints requirements in password                         
                    print('''       > 8 characters minimum
       > contains a symbol ([@_!#$%^&*()<>?/\|}{~:])
       > contains a number (1)''')
                    print("")
                    print("Please try again")

#checks for symbols in the password                    
                elif(regex.search(password) == None):
                    x = (""), ("Your password is invalid"), ("It must:  ")
                    for i in x:
                        print(i)
                        time.sleep(1)
#prints requirement messages                        
                    print('''       > 8 characters minimum
       > contains a symbol ([@_!#$%^&*()<>?/\|}{~:])
       > contains a number (1)''')
                    print("")
                    print("Please try again")

#if everything required is found, password is valid, loop is broken                   
                else:
                    print("")
                    time.sleep(1)
                    print("-------------------------------------------")
                    time.sleep(1)
                    print("Password valid")
                    time.sleep(1)
                    print("-------------------------------------------")
                    time.sleep(1)
                    print("Account created")
                    print("If you would like to play, please on login into each player's accounts")
                    print("")
                    PAlign == True
                    break
                    
#if they don't match displays message then continues loop
        elif password != passwordcheck:
            print("The passwords entered do not match. Please try again")

#writes username and password to accounts file
    Ufile = open("accounts.txt", "a")
    Ufile.write(username)
    Ufile.write(";")
    Ufile.write(password)
    Ufile.write("\n")
    Ufile.close()

#calls rlsF function for input options again
    rlsF()

            
def login_game():
#login to an account if rls was 'l'
    print("----------------------------Login---------------------------")
    print("")

#if login works is true
    login1 = True

#loop until login works    
    while login1:

#player 1 login, username and password

        print("Enter player 1 username and password")
        print("")
        usernameP1 = str(input("Username:  ")).strip()
        passwordP1 = str(input("Password:  ")).strip()
        print("")

#login value, checks if logs in
        login1 = False

#login authorisation, if user (point 1 in the line selected in accounts file,)
#= username entered, and if passwords (same point as username was in users) =
#password entered
        users = []
        passwords = []
        file = open("accounts.txt", 'r')
        for line in file:
            line = line.rstrip().split(";")
            users.append(line[0])
            passwords.append(line[1])
            for user in users:
                if user == usernameP1 and passwords[users.index(usernameP1)] == passwordP1:
                    login1 = True
                else:
                    continue
        file.close()
        
#if login was successful or not displays appropiate message

        #goes to next loop for P2 login
        if login1 == True:
            time.sleep(1)
            print("-------------------------------------------")
            print(usernameP1, "logged in")
            print("-------------------------------------------")
            time.sleep(1)
            print("")
            break

        #sends to start of loop for next attempt 
        else:
            time.sleep(1)
            print("-------------------------------------------")
            print("Login in failed. Please try again.")
            time.sleep(1)
            print("If login repeatedly fails please register a new account")
            print("")
            login1 = True

#player 2 login section
    login2 = True

#loop until login works    
    while login2:

#player 2 login, username and password

        print("Enter player 2 username and password")
        print("")
        usernameP2 = str(input("Username:  ")).strip()
        passwordP2 = str(input("Password:  ")).strip()
        print("")

#login value, checks if logs in
        login2 = False

#login authorisation, if user (point 1 in the line selected in accounts file,)
#= username entered, and if passwords (same point as username was in users) =
#password entered
        users = []
        passwords = []
        file = open("accounts.txt", 'r')
        for line in file:
            line = line.rstrip().split(";")
            users.append(line[0])
            passwords.append(line[1])
            for user in users:
                if user == usernameP2 and passwords[users.index(usernameP2)] == passwordP2:
                    login2 = True
                else:
                    continue
        file.close()
        
#if login was successful or not displays appropiate message

        #sends to game function 
        if login2 == True:
            time.sleep(1)
            print("-------------------------------------------")
            print(usernameP2, "logged in")
            print("-------------------------------------------")
            time.sleep(1)
            print("")
            print("")
            print("")
            time.sleep(3)
            break

        #sends to start of loop for next attempt 
        else:
            time.sleep(1)
            print("-------------------------------------------")
            print("Login in failed. Please try again.")
            time.sleep(1)
            print("If login repeatedly fails please register a new account")
            print("")
            login2 = True

#game module begins
    print("************************************************************")
    print("----------------------------GAME----------------------------")
    print("************************************************************")
    rules = (""),(""),("---------------Rules---------------"), (""), ("Roll 2 dice each round"), ("If the total is even you gain 10 points"), ("If the total is odd you lose 5 points"), ("Roll a double and get an extra roll where what you roll is added to your score"), ("The player with the highest score after 5 rounds WINS!"), ("Good luck and enjoy!")
    for i in rules:
        time.sleep(3)
        print(i)

#sets variables for game module
    rounds = 0
    total_scoreP1 = 0
    total_scoreP2 = 0
    P1Points = 0
    P2Points = 0
    roll_fail = True

#loops for 5 rounds
    while rounds < 5:

#score and rounds variable changes 
        total_scoreP1 = P1Points + total_scoreP1
        total_scoreP2 = P2Points + total_scoreP2
        rounds += 1
#dice 1 and dice 2 rolls, plus double-rolled dice 3
        dice1 = 2
        dice2 = 4
        dice3 = randint(1,6)

#messages plus input message for P1
        print("")
        print("Round", rounds)
        time.sleep(1)
        print("-------------------------------------------")
        print("")
        time.sleep(1)

#player 1 rolls
        P1Points = dice1 + dice2        

#roll 1 loop and input
        while roll_fail:
            P1roll = input(usernameP1+"'s first turn: Type 'roll' to roll the dice  ")
            P1roll = P1roll.lower()

#detects if roll 1 was placed            
            if P1roll == "roll":
                print("")
                time.sleep(1)
                print(usernameP1+"'s first roll is", dice1)
                print("-------------------------------------------")
                print("")
                break

#sends to start of loop for retry
            else:
                print("")
                print("That is not a valid response, please try again")
                print("-------------------------------------------")
                print("")
                (P1roll)

#roll 2 loop and input
        while roll_fail:
            P1roll = input(usernameP1+"'s second turn: Type 'roll' to roll the dice  ")
            P1roll = P1roll.lower()

#detects if roll 2 was placed            
            if P1roll == "roll":
                print("")
                time.sleep(1)
                print(usernameP1+"'s second roll is", dice2)
                break

#sends to start of loop for retry
            else:
                print("")
                print("That is not a valid response, please try again")
                print("")
                (P1roll)

#if rolled is equal to or less than zero (in case of error and to set requirement)
        if P1Points <= 0:
            P1Points = 0
            print("-------------------------------------------")
            print(usernameP1, "has", P1Points, "points")
            print("-------------------------------------------")

#if rolled is even, adds 10             
        elif P1Points % 2 == 0:
            P1Points += 10
            print(usernameP1+"'s total is even so + 10 POINTS!")
            time.sleep(1)
            print("")

#if a double is rolled, give extra roll
            if dice1 == dice2:
                print("Wow, a double was rolled!")
                time.sleep(1)
                print("As a reward you get an extra roll to add on to your score")
                print("")
                time.sleep(1)

#roll check
                while roll_fail:
                    P1roll = input(usernameP1+"'s reward turn: Type 'roll' to roll the dice  ")
                    P1roll = P1roll.lower()
                    
#detects if extra roll was placed            
                    if P1roll == "roll":
                        print("")
                        time.sleep(1)
                        print(usernameP1+"'s extra roll is", dice3)
                        print("")
                        P1Points = P1Points + dice3
                        break

#sends to start of loop for retry
                    else:
                        print("")
                        print("That is not a valid response, please try again")
                        print("-------------------------------------------")
                        print("")
                        (P1roll)

            print("-------------------------------------------")
            print(usernameP1, "has", P1Points, "points")
            print("-------------------------------------------")
            time.sleep(1)

#if rolled is odd, subtracts 5 but sets to 0 if goes below
        else:
            P1Points -= 5
            print(usernameP1+"'s total is odd so - 5 POINTS :(")
            time.sleep(1)
            print("")
            print("-------------------------------------------")
            if P1Points <= 0:
                P1Points = 0
            print(usernameP1, "has", P1Points, "points")
            print("-------------------------------------------")
            time.sleep(1)

#dice 1 and dice 2 rolls, plus double-rolled dice 3
        dice1 = 2
        dice2 = 4
        dice3 = randint(1,6)

#player 2 rolls
        P2Points = dice1 + dice2        

#roll 1 loop and input
        while roll_fail:
            print("")
            P2roll = input(usernameP2+"'s first turn: Type 'roll' to roll the dice  ")
            P2roll = P2roll.lower()

#detects if roll 1 was placed            
            if P2roll == "roll":
                print("")
                time.sleep(1)
                print(usernameP2+"'s first roll is", dice1)
                print("-------------------------------------------")
                print("")
                break

#sends to start of loop for retry
            else:
                print("")
                print("That is not a valid response, please try again")
                print("-------------------------------------------")
                print("")
                (P1roll)

#roll 2 loop and input
        while roll_fail:
            P2roll = input(usernameP2+"'s second turn: Type 'roll' to roll the dice  ")
            P2roll = P2roll.lower()

#detects if roll 2 was placed            
            if P2roll == "roll":
                print("")
                time.sleep(1)
                print(usernameP2+"'s second roll is", dice2)
                break

#sends to start of loop for retry
            else:
                print("")
                print("That is not a valid response, please try again")
                print("")
                (P2roll)

#if rolled is equal to or less than zero (in case of error and to set requirement)
        if P2Points <= 0:
            P2Points = 0
            print("-------------------------------------------")
            print(usernameP2, "has", P2Points, "points")
            print("-------------------------------------------")

#if rolled is even, adds 10             
        elif P2Points % 2 == 0:
            P2Points += 10
            print(usernameP2+"'s total is even so + 10 POINTS!")
            time.sleep(1)
            print("")

#if a double is rolled, give extra roll
            if dice1 == dice2:
                print("Wow, a double was rolled!")
                time.sleep(1)
                print("As a reward you get an extra roll to add on to your score")
                print("")
                time.sleep(1)

#roll check
                while roll_fail:
                    P2roll = input(usernameP2+"'s reward turn: Type 'roll' to roll the dice  ")
                    P2roll = P2roll.lower()
                    
#detects if extra roll was placed            
                    if P2roll == "roll":
                        print("")
                        time.sleep(1)
                        print(usernameP2+"'s extra roll is", dice3)
                        print("")
                        P2Points = P2Points + dice3
                        break

#sends to start of loop for retry
                    else:
                        print("")
                        print("That is not a valid response, please try again")
                        print("-------------------------------------------")
                        print("")
                        (P2roll)

            print("-------------------------------------------")
            print(usernameP2, "has", P2Points, "points")
            print("-------------------------------------------")
            time.sleep(1)

#if rolled is odd, subtracts 5 but sets to 0 if goes below
        else:
            P2Points -= 5
            print(usernameP2+"'s total is odd so - 5 POINTS :(")
            time.sleep(1)
            print("")
            print("-------------------------------------------")
            if P2Points <= 0:
                P2Points = 0
            print(usernameP2, "has", P2Points, "points")
            print("-------------------------------------------")
            time.sleep(1)

#total score for each player after 5 rounds are done
    time.sleep(1)
    print("")
    print("Total score for ", usernameP1, "is", total_scoreP1)
    print("-------------------------------------------")
    time.sleep(1)
    print("")
    print("Total score for", usernameP2, "is", total_scoreP2)
    print("-------------------------------------------")

#if player 1 has more points than player 2
    if total_scoreP1 > total_scoreP2:
        print("")
        print(usernameP1, "wins!")
        time.sleep(1)
        print("✌(◕‿-)✌")
#writes P1 score to file
        file = open("scores.txt", "a")
        file.write(usernameP1)
        file.write(";")
        file.write(str(total_scoreP1))
        file.write("\n")
        file.close
        quit()

#if player 2 has more points than player 1
    elif total_scoreP2 > total_scoreP1:
        print("")
        print(usernameP2, "wins!")
        time.sleep(1)
        print("✌(◕‿-)✌")
#writes P2 score to file
        file = open("scores.txt", "a")
        file.write(usernameP2)
        file.write(";")
        file.write(str(total_scoreP2))
        file.write("\n")
        file.close
        quit()

#if it was a draw, display messages then go to dice rollout
    elif total_scoreP1 == total_scoreP2:
        print("")
        print(usernameP1, "and", usernameP2, "drew!")
        time.sleep(1)
        print("TIE BREAKER")
        print("Each player gets one more roll: whoever gets the highest amount takes it home")
        time.sleep(2)
        print("-------------------------------------------")

#sets variable for if a winner if found
        winner = True

#loops until there is a winner
        while winner:

#sets dice as random
            dice1 = randint(1,1)
            dice2 = randint(1,1)
#loops until valid roll is placed
            while roll_fail:
                P1roll = input(usernameP1+"'s rollout turn: Type 'roll' to roll the dice  ")
                P1roll = P1roll.lower()

#detects if player 1 roll was placed            
                if P1roll == "roll":
                    print("")
                    time.sleep(1)
                    print(usernameP1, "rolled a", dice1)
                    print("-------------------------------------------")
                    break

#sends to start of loop for retry
                else:
                    print("")
                    print("That is not a valid response, please try again")
                    print("")
                    (P1roll)

#loops until valid roll is placed
            while roll_fail:
                P2roll = input(usernameP2+"'s rollout turn: Type 'roll' to roll the dice  ")
                P2roll = P2roll.lower()

#detects if player 2 roll was placed            
                if P2roll == "roll":
                    print("")
                    time.sleep(1)
                    print(usernameP2, "rolled a", dice2)
                    print("-------------------------------------------")
                    break

#sends to start of loop for retry
                else:
                    print("")
                    print("That is not a valid response, please try again")
                    print("")
                    (P2roll)

#if player 1 rolls higher than player 2
            if dice1 > dice2:
                print("")
                time.sleep(1)
                print(usernameP1, "WINS!")
                time.sleep(1)
                print("✌(◕‿-)✌")
                print("-------------------------------------------")
                
#write player 1 score to file, breaks loop
                file = open("scores.txt", "a")
                file.write(usernameP1)
                file.write(";")
                file.write(str(total_scoreP1))
                file.write("\n")
                file.close
                quit()

#if player 2 rolls higher than player 1
            elif dice2 > dice1:
                print("")
                time.sleep(1)
                print(usernameP2, "WINS!")
                time.sleep(1)
                print("✌(◕‿-)✌")
                print("-------------------------------------------")
                
#writes player 2 score to file, breaks loop
                file = open("scores.txt", "a")
                file.write(usernameP2)
                file.write(";")
                file.write(str(total_scoreP2))
                file.write("\n")
                file.close
                quit()

#if its a draw, continue loop
            elif dice1 == dice2:
                print("")
                time.sleep(1)
                print("It was a draw! Roll again.")


def scores():
#function for finding and displaying top 5 winning scores
    print("---------------------------Scores---------------------------")
    print("")
    

#creates users and scores lists, splits file into users and scores per line at
#';' then for each line adds user and score to lists, sets top5 scores as a variable
#after sorting scores, for the first 5 user is the same point in the list as correlating
#score is in scores list, then prints top 5 leaderboard then removes top from list for
#next in leaderboard
    users = []
    scores = []
    with open("scores.txt", 'r') as file:

        for line in file:
            line = line.rstrip("\n").split(";")
            users.append(line[0]) 
            scores.append(int(line[1]))
            top5 = sorted(scores, reverse = True)

        if len(scores) < 5:
            for x in range(len(scores)):
                user = users[scores.index(top5[x])]
                score = top5[x]
                print(f"{x+1} - {user}: {score}")
                del users[scores.index(top5[x])]
                scores.remove(top5[x])
                           
        else:
            for x in range(5):
                user = users[scores.index(top5[x])]
                score = top5[x]
                print(f"{x+1} - {user}: {score}")
                del users[scores.index(top5[x])]
                scores.remove(top5[x])
    quit()
                        
        
def rlsF():
#rls messages using time.sleep to stagger them
    print("------------------Login, Register or Scores------------------")
    print("")
    rlsM = ("If you are a new user type 'r' to register an account"), ("If you are an existing user type 'l' to login with an account"), ("If you want to view the highscores type 's'"), ("")
    for i in rlsM:
        time.sleep(2)
        print(i)
        
#input message
    rls = input("Please enter the corresponding letter for what you would like to do  ")
    rls = rls.lower()
    print("")

#if they want to register account, call register function
    if rls == "r":
        register()

#if they want to login and play the game
    elif rls == "l":
        login_game()

#if they want to view the top winning scores
    elif rls == "s":
        scores()

#if rls isn't a valid input restart function
    else:
        print("That is not a valid response please try again using the options about to be listed below")
        rlsF()
        

def FHub():
    welcome()
    rlsF()
FHub()
