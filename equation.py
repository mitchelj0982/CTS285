
class Equation():
    
    def __init__(self, n1, op, n2, answer):
        self.num1 = n1
        self.operator = op
        self.num2 = n2
        self. answer = answer
        
    def __str__(self):
        return f'{self.num1} {self.operator} {self.num2} = {self.answer}'