class ShuntingYard:
    def __init__(self, expression):
        self.expression = expression  # Infix expression
        self.stack = []  # Stack for operators
        self.output = []  # Output for postfix expression
        self.steps = []  # List to store step-by-step outputs
    
    def is_operator(self, c):
        return c in "+-*/^"
    
    def precedence(self, op):
        precedence_dict = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        return precedence_dict.get(op, 0)
    
    def convert(self):
        for char in self.expression:
            if char.isalnum():  # Operand
                self.output.append(char)
                self.steps.append(''.join(self.output))  # Add current step
            elif char == '(':  # Opening parenthesis
                self.stack.append(char)
            elif char == ')':  # Closing parenthesis
                while self.stack and self.stack[-1] != '(':
                    self.output.append(self.stack.pop())
                    self.steps.append(''.join(self.output))  # Add current step
                self.stack.pop()  # Pop '('
            elif self.is_operator(char):  # Operator
                while (self.stack and self.stack[-1] != '(' and
                       self.precedence(self.stack[-1]) >= self.precedence(char)):
                    self.output.append(self.stack.pop())
                    self.steps.append(''.join(self.output))  # Add current step
                self.stack.append(char)
        
        while self.stack:
            self.output.append(self.stack.pop())
            self.steps.append(''.join(self.output))
        
        return ''.join(self.output)
    
    def get_steps(self):
        return self.steps