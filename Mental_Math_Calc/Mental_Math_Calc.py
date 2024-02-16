###
### Program: Mental Math Calc
###
### Beginning of project: 14 / 02 / 2024
###
### Motive of creation: Making a mental math trainer for the user, that can be as
### customizable as possible.
###

# ver. Thu/15/Nov/2024
#
# Made by: CyberCoral
# ------------------------------------------------
# Github:
# https://www.github.com/CyberCoral
#

###
### Modules:
###

import math, random, os, sys
import Automated_Error_Checks as AEC

with open("requirements.txt","r") as f:
    a =[f.readlines()][0]
    a = [(lambda b,c: c[b][::-1][1:][::-1] if b != len(c) - 1 else c[b])(i, a) for i in range(len(a))]

    import importlib
    for i in range(len(a)):
        loader = importlib.util.find_spec(a[i])
        if loader == None:
            os.system(f"python -m pip install {a[i]}")

# Other modules:
import time, threading

raise OSError("Check for your output in math problems.")

###
### Global variables:
###

name = ""
time_remaining = 10
tries = 3
difficulty = 1
skip = False

defaut = {name: "",
    time_remaining: 10,
    tries: 3,
    difficulty: 1,
    skip: False}

operations = {"Addition": (lambda x,y: x + y,"+",2),
                      "Substraction":(lambda x,y: x - y,"-",2),
                      "Multiplication":(lambda x,y: x * y, "*",2)}


###
### The actual program for math operations.
###

def mental_math(difficulty: float = difficulty, problems: int = 3,*,operation: str = "Addition", time_remaining: int = time_remaining, tries: int = tries, base_diff: int = 10, operations: dict = operations, variables: int = 2, skip: bool = False):
    '''
    The core of the project,
    it lets the user make,
    play and customize their
    math training experience.
    '''

    if skip != True:
        print("Your current operation is:\n",operation,"\n")
        time.sleep(2)
    print("Let's begin,",name,".\n")
    time.sleep(0.5)
    
    # This function creates a problem that the user has to solve.
    def problem_creator(difficulty, operation, base,*, variables = 2, operations = operations):

        v = variables
        oper = operations[operation][0]
        sign = operations[operation][1]
        ### Variable / error check
        
        sample = [str(1) for i in range(variables)]
        preview = sample[0]
        for i in sample[1:len(sample)]:
            preview += ","+i
            
        try:
            exec(compile("result = oper("+preview+")","<string>","exec"),None,{"oper":oper, "preview":preview})
        except ValueError:
            raise SyntaxError("Operation is not supported because the number of variables does not match.\n")

        ###
        
        max_num = base ** (int(math.log(difficulty, base)) + 1) + 1
        min_num = base ** (int(math.log(difficulty, base))) + 1

        var = [str(round(random.randint(min_num, max_num) * random.random(),0)) for i in range(variables)]

        preview = var[0]

        for i in var[1:len(var)]:
            preview += ","+i

        result = eval("oper("+preview+")")
            
        #result = <correct answer>

        return (sign.join(var), result)

    for i in range(problems):
        
        problem = problem_creator(difficulty,operation,base_diff,variables = variables)
        print(f"\n{problem[0]} = ?\n")

        t = threading.Timer(time_remaining, lambda: print(""))

        t.start()

        while True:

            if tries <= 0:
                print("You do not have more tries to answer.")
                print("\nThe correct answer is:\n",problem[1],"\n")
                break

            result = input("Answer: ")

            if float(result) == float(problem[1]):
                    print("\nYou are correct!\n")
                    break
            elif float(result) != float(problem[1]):
                print("You are incorrect.\n")
                tries -= 1

            t.cancel()

        print("The time is over.")
        print("\nThe correct answer is:\n",problem[1],"\n")

        print("Let's do another one!")
        time.sleep(0.5)

###
### Start menu for the program
###
        
def start(*,operations = operations, time_remaining: int = time_remaining, tries: int = tries, base_diff: int = 10, name: str = name, skip: bool = skip, difficulty: int = difficulty) -> None:
    '''
    Starts the program
    and shows the main
    options.
    '''

    booleans =  ["Yes","yes","Y","1",1,"No","no","N","0",0]
    options_1 = ["1","2","3"]
    
    print("Hello, this program is used to train your brain to do\nmental math calculus.\n")
    if skip != True:
        time.sleep(1)
        print("What's your name?\n")
        name = input("Your name is: ")
    
        print(f"Hello {name}")
        time.sleep(1)

    while True:
        print("You can do the following:\n1. Mental Calculus\n2. Enter configuration menu\n3. Exit.\n")
        time.sleep(1)
        print("What do you choose?\n")
        option = input("Your option: ")
        if option not in options_1:
            print("Your option is not in the possible options, try again.")
            time.sleep(1)
        else:
            break

    if option == "1":

        print("The current options for operations are: \n")
        time.sleep(1)
        for i in list(operations.keys()):
            print(i)

        while True:
            print("What operation will you choose?\n")
            operation = input("Operation: ")
            if operation not in list(operations.keys()):
                print("Your operation is not in the available operations, try again.")
            else:
                variables = operations[operation][2]
                break

        print("Great! Your operation is: ",operation,"\n")

        while True:
            print("How many operations do you want to solve?\n")
            problems = input("Number of problems (non-negative or zero): ")
            try:
                problems = int(problems)
                
                if problems <= 0:
                    print("Problems cannot be negative or zero.")
                else:
                    print("Your current number of problems is: ",problems,"\n")
                    break

            except ValueError:
                print("Your option is not possible, try again.")             
                        
        print("Now, you will enter the challenge of ",str(problems)+" "+operation," problems. Enjoy!")
            
        mental_math(difficulty, problems, operation = operation,time_remaining = time_remaining, tries = tries, base_diff = base_diff, operations = operations, variables = variables, skip = skip)

    elif option == "2":

        options_2 = ["0","1","2","3","4","5"]

        while True:
            print("You are now in the configuration menu, what do you want to check?\n")
            print("1. Time remaining\n2. Tries\n3. Base for the upper and lower limits.\n4. Skip.\n5. Exit.\n")
            time.sleep(1.2)

            option = input("Your option: ")

            if option not in options_2:
                print("Your option is not in the possible options, try again.")
                time.sleep(1)
            else:
                break

        if option == "1":
            while True:
                print("Your current time between tries is: ",time_remaining,"\nDo you want to change it?")
                bo = input("Yes (1) or no(0)?")
                if bo not in booleans:
                    print("Your option is not in the available options, try again.")
                    time.sleep(1)
                elif bo in booleans[:5]:
                    print("Which value do you want to use for time_remaining?\n")
                    time_remaining = input("Time remaining (non-negative): ")
                    try:
                        time_remaining = int(time_remaining)
                        if tries == "inf":
                            time_remaining = 10 ** 100
                            break
                        
                        if time_remaining <= 0:
                            print("Time cannot be negative or 0.\n")
                            time_remaining = 10
                        else:
                            print("Your new time is: ", time_remaining)
                            break

                    except ValueError:
                         print("Your option is not possible, try again.")
                            
                else:
                    print("If that is the case, we will exit the option.")
                    break

        if option == "2":
            while True:
                print("Your current try number is: ",tries,"\nDo you want to change it?")
                bo = input("Yes (1) or no(0)?")
                if bo not in booleans:
                    print("Your option is not in the available options, try again.")
                    time.sleep(1)
                elif bo in booleans[:5]:
                    print("Which value do you want to use for tries?\n")
                    time_remaining = input("Time remaining (non-negative or inf): ")
                    try:
                        if tries == "inf":
                            tries = 10 ** 100
                            break
                        
                        tries = int(tries)
                        if tries <= 0:
                            print("Tries cannot be negative or 0.\n")
                            tries = 3
                        else:
                            print("Your new tries is: ", tries)
                            break

                    except ValueError:
                        print("Your option is not possible, try again.")
                        
                else:
                    print("If that is the case, we will exit the option.")
                    break

        if option == "3":
            while True:
                print("Your current difficulty number is: ",difficulty,"\nDo you want to change it?")
                bo = input("Yes (1) or no(0)?")
                if bo not in booleans:
                    print("Your option is not in the available options, try again.")
                    time.sleep(1)
                elif bo in booleans[:5]:
                    print("Which value do you want to use for tries?\n")
                    difficulty = input("Difficulty (non-negative or inf): ")
                    try:
                        if tries == "inf":
                            tries = 10 ** 100
                            break
                        
                        difficulty = int(difficulty)
                        if tries <= 0:
                            print("Difficulty cannot be negative or 0.\n")
                            tries = 3
                        else:
                            print("Your new difficulty is: ", difficulty)
                            break

                    except ValueError:
                        print("Your option is not possible, try again.")
                        
                else:
                    print("If that is the case, we will exit the option.")
                    break

        if option == "4":
            while True:
                print("Your current base for upper and lower limits is: ",base_diff,"\nDo you want to change it?")
                bo = input("Yes (1) or no(0)?")
                if bo not in booleans:
                    print("Your option is not in the available options, try again.")
                    time.sleep(1)
                elif bo in booleans[:5]:
                    print("Which value do you want to use for base_diff?\n")
                    base_diff = input("Base (non-negative nor 1): ")
                    try:
                        
                        base_diff = int(base_diff)
                        if base_diff <= 2:
                            print("Base cannot be negative or 0.\n")
                        else:
                            print("Your new base is: ", base_diff)
                            break
                        
                    except ValueError:
                        print("Your option is not possible, try again.")      
                else:
                    print("If that is the case, we will exit the option.")
                    break

        elif option == "5":
            while True:
                print("Do you want to skip dialogues?")
                time.sleep(2)

                bo = input("Yes (1) or no(0)?")
                if bo not in booleans:
                    print("Your option is not in the available options, try again.")
                    time.sleep(1)
                elif bo in booleans[:5]:
                    print("You want to skip dialogues from now on.")
                    skip = True
                    break
                else:
                    print("You do not want to skip dialogues.")
                    skip = False
                    break

        elif option == "0":
            print("Do you want to exit the program (1) or only the configuration (0)?")
            bo = input("Yes (1) or no(0)?")
            if bo not in booleans:
                print("Your option is not in the available options, try again.")
                time.sleep(1)
            elif bo in booleans[:5]:
                print("I understand, see you later :D\n")
                sys.exit()
            else:
                print("Okay, let's continue with the program, but first we will go back to the beginning.")
                return start(name = name, skip = True)

    elif option == "3":
        print("I understand, see you later :D\n")
        sys.exit()


    while True:
        print("Do you want to repeat the experience again?")
        bo = input("Your option: ")

        if bo not in booleans:
            print("Your option is not in the available options, try again.")
            time.sleep(1)
        elif bo in booleans[:5]:
            print("Let's go back to the beginning:")
            return start(name = name)
        else:
            print("I understand, see you later :D\n")
            sys.exit()
        
if __name__ == "__main__":
    start()
