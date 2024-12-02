import numpy as np # type: ignore
import re

INPUT_PATH = "input.txt"
with open(INPUT_PATH, "r") as f:
    input_data = f.read()

if re.search(r'\s{2,}', input_data):
    print("It has missing value")


input_array = input_data.split('\n') #list of reports, each report is a string (for now)

numOfSafeReports = 0
safe = []
not_safe = []

for report in input_array:

    report_as_list = list(map(int, report.split()))
    # print(report_as_list)
    report_as_list_copy = report_as_list.copy()

    if len(set(np.diff(report_as_list))-set([1, 2, 3, -1, -2, -3])) == 0:
        # print('is ok - good diffs')
        report_as_list_copy.sort() #ascending
        if report_as_list_copy == report_as_list:
            # print('is ok - asc')
            # safe.append(report_as_list)
            numOfSafeReports+=1
        else:
            report_as_list_copy.sort(reverse=True) #desc
            if report_as_list_copy == report_as_list:
                # print('is ok - desc')
                # safe.append(report_as_list)
                numOfSafeReports+=1
    else:
        not_safe.append(report_as_list)
print('\n')
print(numOfSafeReports)




    


