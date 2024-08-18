n = int(input())
best_gift = 0
best_giver = ""

for _ in range(n):
  giver, fun_level = input().split()
  fun_level = int(fun_level)
  if fun_level > best_gift:
    best_gift = fun_level
    best_giver = giver

print(best_giver)