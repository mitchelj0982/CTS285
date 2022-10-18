
from equation import Equation
#The memory bank array,"Empty" means the slot it empty and will be skipped.
memoryBank = ["Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty",]

#####################################################################

"""
- Prompts user to enter an equation to be stored

- the user can enter clear to make the slot empty or exit to return to 
  the main menu
  
- The user enters the operands and the operator , then it validates the 
  equations if operator is subtracting or dividing
  
- Finally it fills the slot with the full equation with the correct answer
  calculated for the user
"""

# getProblem FUNCTION
def getProblem(slot):
    print("\n")
    print("Please input an equation into the memory bank using the format \"2 + 2\", \n")
    print("Type 'exit' to return to the main menu, or type 'clear' to make the memory slot blank\n")
    userProblem = input()
    
    if userProblem.lower() == "exit":
        import MainMenu as mm
        mm.mainMenu()
      
        
    
    if userProblem.lower() == "clear":
        memoryBank[slot] = "Empty"
    else:
        brokenEq = userProblem.split(" ")
        N1 = int(brokenEq[0])
        OP = brokenEq[1]
        N2 = int(brokenEq[2])
        ANS = 1
        userEquation = Equation(N1, OP, N2, ANS)
        
        
        import AnswerChecker as a
        
        if a.validateEQ(userEquation) != False :
            
            if userEquation.operator == "-":
                
                validateBankSub(userEquation, slot)
                
            elif userEquation.operator == "/":
                validateBankDiv(userEquation, slot)
                
            else:
                memoryBank[slot] = userEquation.getCorrectEquation()
        
    



########################################################################
"""

- Displays all the options in the memory bank

- prompts user to make as selection, If a valid integer is selected it 
  prompts for a problem to be input in that slot

- If an valid answer is entered it displays an error then prompts again

- If exit is entered then it returns to the main menu.

"""

# selectBank FUNCTION
def selectBank():
    #Display Menu for bank
    print(("-" * 10) + 'MEMORY BANK' + ("-" * 10))
    for i in range(0,10):
        print(f'{i + 1}). {memoryBank[i]}')
        
    print(('-' * 32) + "\n")
    
    
    
    
    
    print("Please select a slot to input an equation or type 'exit' to \nreturn to return to the main menu\n" )
    user = input()
    
    if user.lower() != "exit":
        valid = ["1",'2','3','4','5','6','7','8','9','10']
        if user not in valid:
            print("\nPlease enter a valid answer")
        else:
            getProblem(int(user) - 1)
    else:
        import MainMenu as MM
        MM.mainMenu()
            
    if user != "exit":
        selectBank()
    
###############################################################    
"""
- Checks to make sure the problem answered isn't going to give a negative answer
  and displays error if so. If not then it passes the equation given to have
  the correct equation stored in the slot selected
"""
# validateBankSub FUNCTION
def validateBankSub(prob,slot):
    if prob.num2 <= prob.num1:
        memoryBank[slot] = prob.getCorrectEquation()
    else:
        print("\nPlease make sure your second number is less than or equal to your first number for subtraction.\n")
        getProblem(slot)
        
######################################################## 
"""
- Checks to make sure the problem answered isn't being divided by zero.
  and displays error if so. If not then it passes the equation given to have
  the correct equation stored in the slot selected
"""

# validateBankDiv FUNCTION    
def validateBankDiv(prob,slot):
        if prob.num2 == 0:
            print("\nERROR: We cannot divide by zero")
            getProblem(slot)
            
        else:
            memoryBank[slot] = prob.getCorrectEquation()
            
            
            
###########################################################



#----------------PRACTICE BANK---------------------------#




#####################################################
"""
- the function iterates over each problem in the memoryBank array

- If the problem has 'Empty' as the value it skips it and moves to the next
  item in the array
  
- It prompts the user to input the correct answer for the displayed question
  and will repeat the question if answered incorrectly

- If the user inputs the correct answer before its been asked twice a congrats
  message is diplayed before moving to the next question
  
- If the question was wrong after being asked twice it displays the correct answer

- Once done asking all questions in bank, it displays a bank complete message
  and returns to the main menu.
  
Note: Displays the remainder for division answers too.

"""
# practiceBank FUNCTION
def practiceBank():  
    for problem in memoryBank:
        if problem == "Empty":
            pass
        else:
            brokenEq = problem.split(" ")
            N1 = int(brokenEq[0])
            OP = brokenEq[1]
            N2 = int(brokenEq[2])
            ANS = int(brokenEq[4])
            
            prob = Equation(N1, OP, N2, ANS)
    
    
            rightAnswer = prob.correctAnswer
            Qcounter = 0
            answer = -1
            
            while answer != rightAnswer and Qcounter != 2:
                if Qcounter > 0:
                    print("Incorrect try again.\n")
                
                print(f'\n{prob.num1} {prob.operator} {prob.num2} = ?')
                
                print("\nPlease input the correct answer only.")
                answer = int(input())
                
                
                
                if answer == rightAnswer:
                    if prob.operator == "/":
                        print("with a remainder of "+ str(prob.num1 % prob.num2))
                    print("Great work\n")
                    break
                   
                else:
                    Qcounter += 1
                    
                    
            if Qcounter  == 2:
                if prob.operator == "/":
                    print(f"The correct answer was: {rightAnswer}" + " remainder: " + str(prob.num1 % prob.num2))
                else:
                    print(f"The correct answer was: {rightAnswer}")
    print("\nMemory bank complete, returning to main menu.\n")
    import MainMenu as mm
    mm.mainMenu()                

            











