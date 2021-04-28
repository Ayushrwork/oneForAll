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
        print("-------------- MAIN MENU ---------------- \n")
        print("Hi (◠‿◠) , What do you want me to do? ")
        print("Enter 'A' or 'a' Dice roll.")
        print("Enter 'B' or 'b' Guessing the number game.")
        print("Enter 'C' or 'c' Random password generator.")
        print("Enter 'D' or 'd' calculator.")
        print("Enter 'E' or 'e' Exit")
        print("-----------------------------------------")

        # !choose
        print("\n")
        choose = input("Enter your choice (͠≖ ͜ʖ͠≖): ")
        if choose == "A" or choose == "a":
            load_animation()
            diceRoller()
        elif choose == "b" or choose == "B":
            load_animation()
            guessingNumber()
        elif choose == "C" or choose == "c":
            load_animation()
            randPassword()
        elif choose == "D" or choose == "d":
            load_animation()
            calculator()
        elif choose == "E" or choose == "e":
            print("Quitting ( ❛ ︵ ❛ )")
            load_animation()
            sys.exit()
        else:
            print("Enter a Valid Input! ( ͡❛ ⏥ ͡❛ )")
            print("Running Again!")
            mainMenu()


# Dice Roller
def diceRoller():
     print("\n")
     print("<------ ROLLING DICE (• ‿ •)--->\n")
     number = random.randint(1, 6)
     print(f"       Number is: {number}")
     print(f"-----------------------------")
     Recall(1)


# Guessing The Number Game
def guessingNumber():
     print("\n")
     print("<-----------Guess The Number--------->\n")
     print("This is a Random Number Guessing game.")
     print("Range of numbers is from 1 to 10.")
     print("--------------------------------------\n")
     number = random.randint(1, 10)
     user = input("Make a Guess: ")

     try:
          if int(user) == number:
               print("( ͡• ‿ ͡•)")
               print("Hurray!!")
               print(f"you guessed the number right it's {number}")

          else:
               if int(user) > 10 or int(user) < 1:
                    print("Enter Within range!!!")
               elif int(user) != number and int(user) <= 10 and int(
                    user) >= 1:
                    print("( ͡• ᴗ ͡•)👎")
                    print(f"You guessed wrong number.The number was {number}")
     except:
          print("Invalid Input.( ͡❛ ⏥ ͡❛)👎\n")
     Recall(2)


# Random Password
def randPassword():
     try:
          print("<- ( * ‿ * )Random Password Generator ->\n")
          print("R. To Generate Password.")
          print("H. To View Saved Password.")
          userInp = input("Your Choice: ")
          f = open("./password.txt", "a+")
          if userInp == "R" or userInp == "r":     
               print("<- ( * ‿ * )Random Password Generator ->\n")
               passlen = int(input("Enter the length of password: "))
               print("-------------------------------------------")
               s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
               if passlen >= 1 and passlen < 30:
                    p = "".join(random.sample(s, passlen))
                    print(f"Your password is {p}")
                    print("<-- Passwords Generator --> \n")
                    f.write(f"Password is : {p}\n")
                    print("Your password is saved in Password.txt file.")               
               else:
                    print("Please Enter Length Between (1 - 30)")
                    print("Running Again.....")
          elif userInp == "H" or userInp == "h":
                    print("Your Password History ->\n")
                    f.seek(0) 
                    data = f.read()
                    print(data)
                    f.close()
          else:
               print("Invalid Input.")
               print("Running Again.")
               randPassword()

     except:
          print("Invalid Input!( ͡❛ ⏥ ͡❛)👎")
          print("Running Again..... \n")
     
     finally:
          f.close()

     Recall(3)

def calculator():
     def sum(x, y):
          return x + y 

     def sub(x,y):
          return x - y 

     def multi(x, y):
          return x * y 

     def division(x,y):
          return x / y 
     print("<--------- Basic Calculator --------->\n")
     print("Select Your Operation: ")
     print("Enter 'A' or 'a' for addition.")
     print("Enter 'S' or 's' for Subtraction.")
     print("Enter 'M' or 'm' for Multiplication.")
     print("Enter 'D' or 'd' for Division.")
     print("-------------------------------------")

     try:
          dis = input("Enter the operation: ")

          if dis in ("a","A","s","S","m","M","d","D"):
               num1 = int(input("Enter First number: ")) 
               num2 = int(input("Enter Second number: ")) 

               if dis == "A" or dis == "a":
                    print(f"{num1} + {num2} = {sum(num1,num2)}")
               elif dis == "S" or dis == "s":
                    print(f"{num1} - {num2} = {sub(num1,num2)}")
               elif dis == "M" or dis == "m":
                    print(f"{num1} * {num2} = {multi(num1,num2)}")
               elif dis == "D" or dis == "d":
                    if num2 == 0:
                         print("Can't divide by 0. ")
                    else:
                         print(f"{num1} / {num2} = {division(num1,num2)}")
          else:
               print("Invalid input!!")

     except:
          print("Invalid Input!!")
     Recall(4)

# Recall
def Recall(flagTemp):
     print("\n")
     print("-----------------------------------")
     print("Enter 'A' or 'a' to run again")
     print("Enter 'M' or 'm' for Main menu")
     print("Press Any Other Key to Exit")
     print("-----------------------------------\n")
     dis = input("Enter (͠≖ ͜ʖ͠≖): ")
     if dis == "A" or dis == "a":
          reCallChoice(flagTemp)
     elif dis == "M" or dis == "m":
          print("going home!( ▀̿ ̿ _⦣ ▀̿ ̿  )\n")
          load_animation()
          mainMenu()
     else:
          print("Bye! ( ❛ ︵ ❛ )")
          load_animation()
          sys.exit()    

# Flag Calling Function
def reCallChoice(flag):
     if flag == 1:
          print("Running Again!\n")
          diceRoller()
     elif flag == 2:
          print("Running Again!\n")
          guessingNumber()
     elif flag == 3:
          print("Running Again!\n")
          randPassword()
     elif flag == 4:
          print("Running Again!\n")
          calculator()

# main function
def main():
    mainMenu()


# calling
if __name__ == "__main__":
    load_animation()
    main()
