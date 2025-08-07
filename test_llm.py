from review_engine.parser import CodeParser

code = '''
import os

def greet(name):
    print("Hello", name)

def farewell():
    print("Goodbye")
'''

parser = CodeParser("python")
structure = parser.parse_code(code)

for item in structure:
    print(item)
