from equation import Equation
 

"""
- Prompts user to input equation and if exit is entered it returns to main menu

- Breaks string into parts, then submits part into 'userEquation'
  which is an Equation object

- If userEquation does not return false then it goes into a set of if statements

- If the operator in userEquation is (minus)'-' or (divide)'/' then it runs
  validate4sub function or validate4 Div
- Else it just submits userEquation into the checkProblem function

- Finally it just runs the get Equation Function again to get another equation
"""
# getEquation FUNCTION
def getEquation():
    print("\n")
    print("Please input an equation to be checked using the format \"2 + 2 = 4\" \n")
    print("or type 'exit' to return to the main menu")
    userProblem = input()
    
    if userProblem.lower() == "exit":
        import MainMenu as mm
        mm.mainMenu()
    
    brokenEq = userProblem.split(" ")
    N1 = int(brokenEq[0])
    OP = brokenEq[1]
    N2 = int(brokenEq[2])
    ANS = int(brokenEq[4])
    userEquation = Equation(N1, OP, N2, ANS)
    if validateEQ(userEquation) != False :
        if userEquation.operator == "-":
            validate4Sub(userEquation)
        elif userEquation.operator == "/":
            validate4Div(userEquation)
        else:
            checkProblem(userEquation)
    
    getEquation()
        
        
        

################################################################

"""
- This function is used to make sure the equation is valid

- It firsts checks for a valid operator

- Then it makes sure that the two numbers being operated on aren't 
  more than double digits
  
- Then it makes sure the answer isn't greater than three digits

- if any of those evaluates false it returns false but if it makes it
  to the end of the chain it returns true


"""
# validateEQ FUNCTION
def validateEQ(prob):
    validOps = ["+","-", "/", "*"]
    if prob.operator not in validOps:
        print("Please enter a valid operator [+,-,*,/]")
        return False
    else:
    
        if (prob.num1 <  0) or (prob.num2 < 0) or (prob.answer < 0):
            print("Numbers cannot be negative")
            return False
    
        else:
            if (prob.num1 >  99) or (prob.num2 > 99):
                print("Numbers being operated cannot be greater than two digits")
                return False
            else:
                if prob.answer > 999:
                    print("Answers cannot be greater than 3 digits")
                    return False
                else:
                    return True
    

#################################################################
"""
- This function makes sure that number 2 isn't 0 so divide by zero errors
  are prevented
- If num2 attribute is 0 it then displays an error
  and asks for a new equatiom
  
-  Else it takes the equation it was handed and gives it to the check
   Problem function
"""
# validate4Div FUNCTION
def validate4Div(prob):
        if prob.num2 == 0:
            print("ERROR: We cannot divide by zero")
        else:
            checkDiv(prob)
###################################################################
"""
- This function makes sure that number 2 isn't greater than number 1
  so that negative answers are prevented

- If num2 attribute is greater than num1 it then displays an error
  and asks for a new equatiom
  
-  Else it takes the equation it was handed and gives it to the check
   Problem function
"""
# validate4Sub FUNCTION
def validate4Sub(prob):
    if prob.num2 <= prob.num1:
        checkProblem(prob)
    else:
        print("Please make sure your second number is less than or equal to your first number for subtraction.\n")
        getEquation()
################################################################  

"""

- If the answer attribute submitted by the user is equal to the 
  correctAnswer attribute calculated then it prints correct
  
- Else it runs the repeatQuestion function with the 
  equation it was handed
"""

# checkProblem FUNCTION
def checkProblem(prob):
    
    if prob.answer == prob.correctAnswer:
        print("Correct")
    else:
        repeatQuestion(prob)
       
        
##############################################################


"""
- If the answer attribute is equal to the correctAnswer attribute
  calculated it then prints correct
- If num1 modulus num2 isn't equal to 0 then it displays the remainder
  calculated 
  
- Else it runs the repeatQuestion function with the equation it was
  handed
"""
# checkDiv FUNCTION      
def checkDiv(prob):
    if prob.answer == prob.correctAnswer:
        print("Correct.")
        if prob.num1 % prob.num2 != 0:
            print("remainder: " + str(prob.num1 % prob.num2))

    else: 
        repeatQuestion(prob)  
        
        
####################################################    


"""
- Runs while loop so that as long as the question count isnt 2
  and the correct answer isn't given it will repeat
  
-  if the correct answer isn't given by two repeats it will display the correct
   answer for you
   
- it also will display the remainder if it's a division problem
"""
# repeatQuestion FUNCTION    
def repeatQuestion(prob):  
    rightAnswer = prob.correctAnswer
    Qcounter = 0
    answer = -1
    while answer != rightAnswer and Qcounter != 2:
        print("Incorrect. try again")
        print(f'{prob.num1} {prob.operator} {prob.num2} = ?')
        
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

######################################################################