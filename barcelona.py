# Get the input
num_bags, benni_bag = map(int, input().split())
bags = list(map(int, input().split()))

# Find the index of Benni's bag
benni_bag_index = bags.index(benni_bag) + 1

# Determine the output based on the index
if benni_bag_index == 1:
  print("fyrst")
elif benni_bag_index == 2:
  print("naestfyrst")
else:
  print(benni_bag_index, "fyrst")