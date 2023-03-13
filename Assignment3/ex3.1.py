# Assignment 3, Exercise 3.1

# Contributors: Axel Sanchez, Mariia Podgaietska


import sys


class Node:
    def __init__(self, data, next_=None):
        self.data = data
        self.next = next_


class Stack:
    def __init__(self):
        self.head = None

    def push(self, item):
        self.head = Node(item, self.head)

    def pop(self):
        if self.head is None:
            return None
        item = self.head.data
        self.head = self.head.next
        return item

    def peek(self):
        if self.head is None:
            return None
        return self.head.data


precedence = {'+': 1, '-': 1, '*': 2, '/': 2}


def infix_to_postfix(tokens):
    output = []
    operator_stack = Stack()
    paren_count = 0

    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token in precedence:
            while (operator_stack.peek() is not None and
                    operator_stack.peek() != '(' and
                    precedence[operator_stack.peek()] >= precedence[token]):
                output.append(operator_stack.pop())
            operator_stack.push(token)
        elif token == '(':
            operator_stack.push(token)
            paren_count += 1
        elif token == ')':
            while operator_stack.peek() != '(':
                output.append(operator_stack.pop())
            if operator_stack.peek() == '(':
                operator_stack.pop()
                paren_count -= 1
            else:
                raise ValueError('Unbalanced parentheses')

    if paren_count != 0:
        raise ValueError('Unbalanced parentheses')

    while operator_stack.peek() is not None:
        output.append(operator_stack.pop())

    return output


def evaluate_postfix(tokens):
    operand_stack = Stack()

    for token in tokens:
        if token.isdigit():
            operand_stack.push(int(token))
        elif token in precedence:
            b = operand_stack.pop()
            a = operand_stack.pop()
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                result = a // b  # Integer division
            operand_stack.push(result)

    return operand_stack.pop()


def parse_expression(tokens):
    postfix_tokens = infix_to_postfix(tokens)
    result = evaluate_postfix(postfix_tokens)
    return result


# Main program
if __name__ == '__main__':
    expression = sys.argv[1]
    tokens = [x for x in expression if x != ' ']
    result = parse_expression(tokens)
    print(result)
