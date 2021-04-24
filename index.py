# Import
import random
import time
import sys
import os

# Loading Animation
def load_animation():
    load_str = "Loading Application..."
    ls_len = len(load_str)
    animation = "|/-\\"
    anicount = 0
    counttime = 0
    i = 0
    while counttime != 15:
        time.sleep(0.075)
        load_str_list = list(load_str)
        x = ord(load_str_list[i])
        y = 0
        if x != 32 and x != 46:
            if x > 90:
                y = x - 32
            else:
                y = x + 32
            load_str_list[i] = chr(y)
        res = ""
        for j in range(ls_len):
            res = res + load_str_list[j]
        sys.stdout.write("\r" + res + animation[anicount])
        sys.stdout.flush()
        load_str = res
        anicount = (anicount + 1) % 4
        i = (i + 1) % ls_len
        counttime = counttime + 1
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# Main Menu
def mainMenu():
    while True:
        # !conditions
        print("-------- MAIN MENU -------- \n")
        print("Hi, What do you want me to do? :")
        print("Enter 'A or a' Dice roll.")
        print("Enter 'B or b' Guessing the number game.")
        print("Enter 'C or c' Random password generator.")
        print("Enter 'E or e' Exit")
        print("--------------------------")

        # !choose
        print("\n")
        choose = input("Enter your choice: ")
        if choose == "A" or choose == "a":
            load_animation()
            diceRoller()
        elif choose == "b" or choose == "B":
            load_animation()
            guessingNumber()
        elif choose == "C" or choose == "c":
            load_animation()
            randPassword()
        elif choose == "E" or choose == "e":
            print("Quitting")
            sys.exit()
        else:
            print("Enter a Valid Input!")
            print("Running Again!")
            mainMenu()


# Dice Roller
def diceRoller():
     print("\n")
     print("<-- ROLLING DICE -->")
     number = random.randint(1, 6)
     print(f"Number is: {number}")
     print(f"---------------")
     Recall(1)


# Guessing The Number Game
def guessingNumber():
     print("\n")
     print("This is a Random Number Guessing game.")
     print("Range of numbers is from 1 to 10.")
     number = random.randint(1, 10)
     user = input("Guess Number: ")

     try:
          if int(user) == number:
               print("Hurray!!")
               print(f"you guessed the number right it's {number}")

          else:
               if int(user) > 10 or int(user) < 1:
                    print("Enter Within range")
               elif int(user) != number and int(user) <= 10 and int(
                    user) >= 1:
                    print(f"You guessed wrong number.The number was {number}")
     except:
          print("Invalid Input.\n")

     Recall(2)


# Random Password
def randPassword():
     try:
          print("Random Password Generator:")
          passlen = int(input("Enter the length of password: "))
          s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
          if passlen >= 1 and passlen < 30:
               p = "".join(random.sample(s, passlen))
               print(p)
          else:
               print("please enter length between (1 - 30)")
               print("Running again.....")

     except:
          print("Invalid Input!")
          print("Running Again..... \n")

     Recall(3)

# Recall
def Recall(flagTemp):
     print("\n")
     print("-----------------------------------")
     print("Enter 'A' or 'a' to run again")
     print("Enter 'M' or 'm' for Main menu")
     print("Enter 'E' or 'e' to Exit")
     print("-----------------------------------")
     dis = input("Enter :")
     if dis == "A" or dis == "a":
          reCallChoice(flagTemp)
     elif dis == "M" or dis == "m":
          print("going home!")
          mainMenu()
     elif dis == "E" or dis == "e":
          print("Bye!")
          sys.exit()    
     else:
        print("Invalid Input!")
        print("Running again!")
        Recall()

# Flag Calling Function
def reCallChoice(flag):
     if flag == 1:
          diceRoller()
     elif flag == 2:
          guessingNumber()
     elif flag == 3:
          randPassword()

# main function
def main():
    mainMenu()


# calling
if __name__ == "__main__":
    load_animation()
    main()
