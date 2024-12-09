import re


INPUT_PATH = 'input.txt'
TEST_PATH = 'test.txt'

with open(INPUT_PATH, "r") as f:
    input_data = f.read()

pattern = r"mul\(\s*\d+\s*,\s*\d+\s*\)" 

def mul(n1:int, n2:int)->int:
    return n1*n2

def find_matches(text: str)-> list:
    matches = re.findall(pattern, input_data)
    return matches

def return_product(matches:list)-> int:
    product = 0
    for match in matches:
        product += eval(match)
    return product


def sol(input_data:str)-> int:
    matches = find_matches(input_data)
    final_product = return_product(matches)

    return final_product

print(sol(input_data))


