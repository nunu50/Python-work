character = input()
# Knuth-Morris-Pratt
'''
Approach:
name: Nuha-Samson-Mamo
if name[0] -> [N, ]
if name[i] == "-", name[i + 1] -> [N, S, M]

'''
length = len(character)
answer = []
# .append()
for i in range(length):
    if i == 0:
        answer.append(character[i])
    elif character[i] == "-":
        answer.append(character[i + 1])

# print(answer) N, S, M ==>>> NSM

print("".join(answer))  