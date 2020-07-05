#!/usr/bin/env python3

from abc import ABC, abstractmethod
from random import randint
from math import sqrt

class Quiz(ABC):
    
   
    def __init__(self, min_int, max_int):
        self.operator = self.get_operator()
        self.operand_1, self.operand_2 = self.generate_operands(min_int, max_int)
        self.result = self.operate()
        

    @abstractmethod
    def get_operator(self):
        pass


    @abstractmethod
    def generate_operands(self, min_int, max_int):
        pass
    

    @abstractmethod
    def operate(self):
        pass
    
    def __str__(self):
        return str(self.operand_1) + " " + self.operator + " " + str(self.operand_2) + " = "
    
    def print(self, includeAnswer):
        if includeAnswer:
            return str(self.operand_1) + " " + self.operator + " " + str(self.operand_2) + " = " + str(self.result)
        else:
            return str(self.operand_1) + " " + self.operator + " " + str(self.operand_2) + " = ? " 

    

class Addition(Quiz):
    

    def get_operator(self):
        return "+"
    
    
    def generate_operands(self, min_int, max_int): 
        operand_1 = randint(min_int, max_int)
        operand_2 = randint(min_int, max_int)
        return operand_1, operand_2
    
        
    def operate(self):
        return self.operand_1 + self.operand_2


class Subtraction(Quiz):
    

    def get_operator(self):
        return "-"
    
    
    def generate_operands(self, min_int, max_int): 
        
        operand_1 = randint(min_int, max_int)
        operand_2 = randint(min_int, max_int)
        
        if operand_1 > operand_2:
            return operand_1, operand_2
        else:
            return operand_2, operand_1
        
        
    def operate(self):
        return self.operand_1 - self.operand_2
    

class Multiplication(Quiz):
    

    def get_operator(self):
        return "*"
    

    def generate_operands(self, min_int, max_int): 

        operand_1 = randint(min_int, max_int)
        operand_2 = randint(min_int, max_int)

        return operand_1, operand_2

        
    def operate(self):

        return self.operand_1 * self.operand_2


class Division(Quiz):
    

    def get_operator(self):
        return "/"
    
    
    def generate_operands(self, min_int, max_int): 

        while True:

            operand_1 = randint(min_int, max_int)
            operand_2 = randint(min_int, max_int)

            if operand_1 % operand_2 == 0:
                return operand_1, operand_2
            else:
                continue          
                
        
    def operate(self):

        return int(self.operand_1 / self.operand_2)

class SquaredRoot(Quiz):
    

    def get_operator(self):
        return "$"
    
    
    def generate_operands(self, min_int, max_int): 

        while True:
              
             operand_2 = randint(min_int, max_int)
        
             # if isinstance(sqrt(operand_2), int):             # does not work.
             if sqrt(operand_2).is_integer():
                 return None, operand_2
        
    def operate(self):
        return int(sqrt(self.operand_2))

    def print(self, includeAnswer):
        s = "sqrt(" + str(self.operand_2) + ") = " 
        if includeAnswer:
            return s + str(self.result)
        else:
            return s + "? " 

class modular(Quiz):
    

    def get_operator(self):
        return "%"
    
    
    def generate_operands(self, min_int, max_int): 
        
        operand_1 = randint(min_int, max_int)
        operand_2 = randint(min_int, max_int)
        
        if operand_1 > operand_2:
            return operand_1, operand_2
        else:
            return operand_2, operand_1
        
        
    def operate(self):
        return self.operand_1 % self.operand_2
    

def supported_operators():
    return {"+" : "Add",
            "-" : "Subtract",
            "*" : "Multiply",
            "/" : "Divide",
            "$" : "Squared Root",
            "%" : "Modular"}


def create_quiz(operator, min_int, max_int):

    def get_operator(self):
        return "*"
    
    
    if operator == "+":
        q = Addition(min_int, max_int)
    elif operator == "-":
        q = Subtraction(min_int, max_int)
    elif operator == "*":
        q = Multiplication(min_int, max_int)
    elif operator == "/":
        q = Division(min_int, max_int)
    elif operator == "$":
        q = SquaredRoot(min_int, max_int)
    elif operator == "%":
        q = modular(min_int, max_int)
    else:
        raise RuntimeError('The system encountered a mysterious operation: {}'.format(operator))

    return q


if __name__ == "__main__":
    
    add = Addition(1, 10)
    print(add.print(True))
    
    sub = Subtraction(1, 10)
    print(sub.print(True))
    
    mul = Multiplication(1, 10)
    print(mul.print(True))
    
    div = Division(1, 10)
    print(div.print(True))
    
    sqr = SquaredRoot(1, 10)
    print(sqr.print(True))
    
    mod = Modular(1, 10)
    print(mod.print(True))
