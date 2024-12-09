import re


INPUT_PATH = 'input.txt'
TEST_PATH = 'test.txt'
TEST_2_PATH = 'test2.txt'

with open(INPUT_PATH, "r") as f:
    input_data = f.read()

pattern = r"mul\(\s*\d+\s*,\s*\d+\s*\)" 
pattern_part_two = r"mul\(\s*\d+\s*,\s*\d+\s*\)|do\(\s*\)|don't\(\s*\)"

def mul(n1:int, n2:int)->int:
    return n1*n2

def find_matches(text: str, pattern)-> list: # not needed for part two
    matches = re.findall(pattern, input_data)
    return matches

def find_enabled_matches(matches: list):
    enabled_matches = list()
    enabled = True
    for match in matches:
        if "do" in match:
            enabled= True

        if "don't" in match:
            enabled = False
        
        if enabled == True and "mul" in match:
            enabled_matches.append(match)

    return enabled_matches
    

def return_product(matches:list)-> int:
    product = 0
    for match in matches:
        product += eval(match)
    return product


def sol(input_data:str, part_one:bool = False)-> int:
    if part_one:
        matches = find_matches(input_data, pattern)
    else:
        raw_matches = find_matches(input_data, pattern_part_two)
        matches = find_enabled_matches(raw_matches)
    
    final_product = return_product(matches)

    return final_product

print(sol(input_data))
