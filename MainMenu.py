import AnswerChecker as AC
import MemoryBank as MB

#############################################################
"""
- Displays main menu then runns getInput function
"""

# mainMenu FUNCTION
def mainMenu():
    print("\n")
    print(('-'*10) + "MENU"+('-'*10)  )
    print("1. Answer Checker")
    print("2. Fill Memory Bank")
    print("3. Practice Memory Bank")
    print("4. Exit")
    print('-'*24)
    
    getInput()

#################################################################
"""
- Prompts user to make a selection

- runs proper function accoording to the main menu

- also displays error message and reprompts for input if the input
  entered was invalid

"""

# getInput Function
def getInput():
    print("\nPlease make a selection: \n")
    user = input()
    
    if user == "1":
        AC.getEquation()
    elif user == "2":
        MB.selectBank()
    elif user == "3":
        MB.practiceBank()
    elif user == "4":
        print("Good Bye.")
    else:
        print("\nPlease input a valid answer")
        mainMenu()
        

#########################################################


#starts program
if __name__ == "__main__":
    mainMenu()
