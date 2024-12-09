import re


INPUT_PATH = 'input.txt'
TEST_PATH = 'test.txt'
TEST_2_PATH = 'test2.txt'

with open(INPUT_PATH, "r") as f:
    input_data = f.read()

FUNC_PATTERN = r"mul\(\s*\d+\s*,\s*\d+\s*\)" 
COMBINED_PATTERN = rf"{FUNC_PATTERN}|do\(\s*\)|don't\(\s*\)"

def extract_numbers(match:str)-> tuple[int, int]:
    nums = re.findall(r"\d+", match)
    return int(nums[0]), int(nums[1])

def mul(n1:int, n2:int)->int:
    return n1*n2

def find_matches(text: str, pattern)-> list: 
    matches = re.findall(pattern, input_data)
    return matches

def find_enabled_matches(matches: list[str])-> list[str]:
    enabled_matches = list()
    enabled = True
    for match in matches:
        if match.startswith("do()"):
            enabled= True
        elif match.startswith("don't("):
            enabled = False
        elif enabled == True and match.startswith("mul("):
            enabled_matches.append(match)

    return enabled_matches
    

def return_product(matches:list)-> int:
    product = 0
    for match in matches:
        n1, n2 = extract_numbers(match)
        product += mul(n1, n2)
    return product


def solve_aoc_problem(input_data:str, part_one:bool = False)-> int:
    matches = re.findall(FUNC_PATTERN if part_one else COMBINED_PATTERN, input_data)
    if not part_one:
        matches = find_enabled_matches(matches)
    return return_product(matches)

print(solve_aoc_problem(input_data))
