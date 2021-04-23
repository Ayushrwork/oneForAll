# import
import random 
import sys

# main function
def main():
    conditionMain = True;
    while conditionMain:
        # !conditions
        print("Main Menu")
        print("Please enter one of the number:")
        print("1. Dice roll.")
        print("2. Guessing the number game.")
        print("3. Random password generator.")
        print("4. Exit")

        # !choose
        print("\n")
        try:
            choose = input("Enter your choice: ")
            if int(choose) == 1:
                diceRoller()
            elif int(choose) == 2:
                guessingNumber()
            elif int(choose) == 3:
                randPassword()
            elif int(choose) == 4:
                print("Bye")
                break
            else:
                print("Invalid Input.\n")
                print("Running Again.\n")
                continue
        except:
            print("Invalid Input.\n")
            print("Running Again\n")
            continue

        
# dice roller
def diceRoller():
    print("\n")
    condition = True
    while condition:     
        try:
            print("<-- ROLLING DICE -->")    
            number = random.randint(1,6)         
            print(f"Number is: {number}")
            print(f"---------------")
            print("1. Roll again")     
            print("2. Exit to Main Menu")       
            print("\n") 
            user = input("Enter: ")    
            if int(user)==1:
                print("Rolling Again!")         
                continue
            elif int(user)==2: 
                print("\n")
                condition = False
                break
            else:
                print("Invalid input.\n")
                print("Running Again.\n")
                continue
        except:
            print("Invalid Input.\n")
            print("Running Again.\n")
            continue
# guessing the number game
def guessingNumber():
    print("\n")
    while True:
        print("This is a Random Number Guessing game.")
        print("Range of numbers is from 1 to 10.")
        number = random.randint(1,10)
        user = input("Guess Number: ")

        try:
            if int(user) == number:
                print("Hurray!!")
                print(f"you guessed the number right it's {number}")

            else:
                if int(user) > 10 or int(user) < 1:
                    print("Enter Within range")
                elif int(user) != number and int(user) <= 10 and int(user) >= 1:
                    print(f"You guessed wrong number.The number was {number}")
        except:
            print("Invalid Input.\n")
    
        print("\n")    
        print("Press 'A' to play again")
        print("Press 'M' to Exit to Main Menu")
        cond = input("Enter your choice: ")
        if cond == "A" or cond == "a":
            continue     
        elif cond == "M" or cond == "m":
            break
        else:
            print("Invalid input guessing")
            print("Going to Main Menu")
            break


# random password
def randPassword():
     while True:
          try:
               print("Random Password Generator:")
               passlen = int(input("Enter the length of password: "))
               s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
               if passlen >= 1 and passlen < 30:
                    p =  "".join(random.sample(s,passlen))
                    print (p)
               else:
                    print("please enter length between (1 - 30)")
                    print("Running again.....")
                    continue
     
          except:
               print("Invalid Input!")
               print("Running Again..... \n")
               continue


          print("\n")
          print("1. Run Again.")
          print("2. Exit to Main Menu.")
          choice = input("Choice: ")
          try:
               if int(choice) == 1:
                    continue
               elif int(choice) == 2:
                    break
               else:
                    print("Invalid Input.")
                    print("Running Again!")
                    continue
          except:
               print("Invalid input.")
               print("Running again")
               continue
        
        

if __name__ == "__main__":
    main()