from equation import Equation

#
def getEquation():
    print("Please input an equation to be checked using the format \"2 + 2 = 4\" \n")
    userProblem = input()
    brokenEq = userProblem.split(" ")
    N1 = int(brokenEq[0])
    OP = brokenEq[1]
    N2 = int(brokenEq[2])
    ANS = int(brokenEq[4])
    userEquation = Equation(N1, OP, N2, ANS)
    if validateNums(userEquation) == False :
        getEquation()
    else:
        findOperation(userEquation)

################################################################

    
#    
def findOperation(prob):
    if prob.operator == "+":
        checkAdd(prob)
    elif prob.operator == "-":
        validate4Sub(prob)
    elif prob.operator == "*":
        checkMult(prob)
    elif prob.operator == "/":
        validate4Div(prob)
    else:
        print("\nInvalid equation input. Please follow the valid format.")
        
    getEquation()

################################################################


#      
def checkAdd(prob):
    realAnswer = prob.num1 + prob.num2
    if (prob.num1 + prob.num2) == prob.answer:
        print("Correct.")

    else: 
        repeatQuestion(prob, realAnswer)
        
################################################################


 #           
def checkSub(prob):
    realAnswer = prob.num1 - prob.num2
    if (prob.num1 - prob.num2) == prob.answer:
        print("Correct.")

    else: 
        repeatQuestion(prob, realAnswer)

################################################################


#
def checkMult(prob):
    realAnswer = prob.num1 * prob.num2
    if (prob.num1 * prob.num2) == prob.answer:
        print("Correct.")

    else: 
        repeatQuestion(prob, realAnswer)  

################################################################


 #       
def checkDiv(prob):
    realAnswer = int(prob.num1 / prob.num2)
    if int(prob.num1 / prob.num2) == prob.answer:
        print("Correct.")
        if prob.num1 % prob.num2 != 0:
            print("remainder: " + str(prob.num1 % prob.num2))

    else: 
        repeatQuestion(prob, realAnswer)  

################################################################


#
def validate4Sub(prob):
    if prob.num2 <= prob.num1:
        checkSub(prob)
    else:
        print("Please make sure your second number is less than or equal to your first number for subtraction.\n")
################################################################  


#
def validate4Div(prob):
        if prob.num2 == 0:
            print("ERROR: We cannot divide by zero")
        else:
            checkDiv(prob)
            

############################################################


#
def validateNums(prob):
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

###########################################################


   
# repeatQuestion FUNCTION
def repeatQuestion(prob , rightAnswer):  
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
            getEquation()
        else:
            Qcounter += 1
    if Qcounter  == 2:
        if prob.operator == "/":
            print(f"The correct answer was: {rightAnswer}" + " remainder: " + str(prob.num1 % prob.num2))
        else:
            print(f"The correct answer was: {rightAnswer}")
        
    

        
################################################################


    
      
getEquation()