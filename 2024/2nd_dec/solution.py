import numpy as np # type: ignore
import re

INPUT_PATH = "input.txt"
with open(INPUT_PATH, "r") as f:
    input_data = f.read()

if re.search(r'\s{2,}', input_data):
    print("It has missing value")


input_array = input_data.split('\n') #list of reports, each report is a string (for now)

def recheck_order(array:list, array_copy:list) -> bool:
    pos_check = []
    for a, c in zip(array, array_copy):
        if a==c: pos_check.append(0)
        else: pos_check.append(1)
    occur = 0
    for idx in range(len(pos_check)):
        if idx+2 <= len(pos_check):
            if pos_check[idx:idx+2] == [1, 1]: occur += 1
    if occur == 1: return True
    else: return False


def check_if_in_order(array: list) -> bool:
    array_copy = array.copy()

    #asc
    array_copy.sort()
    if array_copy == array: return True    
    else:
        if recheck_order(array, array_copy):
                return True
        #desc
        array_copy.sort(reverse=True)
        if array_copy == array: return True
        else: 
            if recheck_order(array, array_copy):
                return True
            else: return False
    


def check_diffs(array: list)-> bool:
    accetable_diffs_set = set([1, 2, 3, -1, -2, -3])
    diffs = np.diff(array)
    if len(set(diffs)-accetable_diffs_set) == 0:
        return True
    else:
        if np.count_nonzero(diffs == 0) == 1: return True
        else: return False


CHECKS = {
    'check_diffs': check_diffs,
    'check_order': check_if_in_order
}



def check_reports(reports: list, checks:dict)->int:
    numOfSafeReports = 0
    not_safe = []

    for report in reports:
        report_as_list = list(map(int, report.split()))

        checked = {}
        for check_name, check in CHECKS.items():
            if check(report_as_list):
                checked[check_name] = 1
                        
            else: checked[check_name] = 0

        if sum(checked.values()) == len(CHECKS):
            numOfSafeReports+=1
        else: not_safe.append(report_as_list)



    return numOfSafeReports

print(check_reports(input_array,CHECKS))


######################################################
## PART TWO

# for recheck in not_safe:
#     for pos, val in enumerate(recheck):






    



