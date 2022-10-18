#Equation Class used to hold math problems and calculates correct answer for you
class Equation():
    
    def __init__ (self, n1, op, n2, ans):
        self.num1 = n1
        self.operator = op
        self.num2 = n2
        self.answer = ans
        self.correctAnswer = findOperation(self)
        
    def __str__(self):
        return f'{self.num1} {self.operator} {self.num2} = {self.answer}'
    
    #Method used to display the equation with the proper calculated answer
    def getCorrectEquation(self):
        return f'{self.num1} {self.operator} {self.num2} = {self.correctAnswer}'
        
 
        
 
#Gets the correct answer fto be used regardless of answer entered
def findOperation(prob):
    if prob.operator == "+":
        return prob.num1 + prob.num2
    elif prob.operator == "-":
        return prob.num1 - prob.num2
    elif prob.operator == "*":
        return prob.num1 * prob.num2
    elif prob.operator == "/":
            if prob.num2 != 0:
                return int(prob.num1 / prob.num2)
            else:
                return "Error"



