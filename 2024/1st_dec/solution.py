import pandas as pd

INPUT_FILE = r"input.txt"

df = pd.read_csv(INPUT_FILE, delimiter="\s+", header=None, index_col=False)
df.columns = ['left', 'right']

## PART ONE
left = df['left'].to_list()
left.sort()
right = df['right'].to_list()
right.sort()

sum_distance = 0
for l, r in zip(left, right):
    sum_distance+=abs(l-r)

# print(sum_distance)

######################################################
## PART TWO

similarity_value = 0
left = df['left'].to_list()
right_count_unique = df['right'].value_counts().to_dict() #counts how many times value appeared in column

# print(right_count_unique) #counts how many times value appeared in column

for value in left:
    add_score = value*right_count_unique[value] if value in right_count_unique.keys() else 0
    similarity_value += add_score

print(similarity_value)
