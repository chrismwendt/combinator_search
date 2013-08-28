from collections import deque
import copy

def last(generator):
    return deque(generator, maxlen=1).pop()

def reduce(expression):
    return last(rewrite(expression))['expression']

def rewrite(expression):
    for step in rewrite_left(expression):
        yield step
    expression = step['expression']
    for step in rewrite_right(expression):
        yield step

def rewrite_left(expression):
    if type(expression) == dict:
        yield {'expression': expression, 'combinator': expression, 'arguments': []}
        return
    step = None
    for step in rewrite_left(expression[0]):
        yield step
    expression[0], combinator, arguments = step['expression'], step['combinator'], step['arguments']
    arguments.append(expression[1])
    if len(arguments) < combinator['arguments']:
        yield {'expression': expression, 'combinator': combinator, 'arguments': arguments}
        return
    expression = substitute(copy.deepcopy(combinator['rewrite']), arguments)
    yield {'expression': expression, 'combinator': None, 'arguments': None}
    for step in rewrite_left(expression):
        yield step

def rewrite_right(expression):
    if type(expression) == dict:
        yield {'expression': expression, 'combinator': None, 'arguments': None}
        return
    for step in rewrite(expression[1]):
        yield step
    expression[1] = step['expression']
    yield {'expression': expression, 'combinator': None, 'arguments': None}
 

def substitute(expression, arguments):
    if type(expression) == int:
        return arguments[expression]
    for i, subexpression in enumerate(expression):
        expression[i] = substitute(subexpression, arguments)
    return expression
