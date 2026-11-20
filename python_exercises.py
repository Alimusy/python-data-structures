# Python built-in data structures: exercise solutions

# ---------------------------------------------------------------
# Question 1: Multiply all the items in a list
# ---------------------------------------------------------------
def multiply_list(items):
    result = 1
    for x in items:
        result *= x
    return result

sample_list = [2, 3, 6]
print("Q1:", multiply_list(sample_list))  # 36


# ---------------------------------------------------------------
# Question 2: Sort a list of tuples by the last element of each tuple
# ---------------------------------------------------------------
tuples = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
tuples.sort(key=lambda t: t[-1])
print("Q2:", tuples)  # [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]


# ---------------------------------------------------------------
# Question 3: Combine two dictionaries, adding values for common keys
# ---------------------------------------------------------------
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

combined = dict(d1)               # start with a copy of d1
for key, value in d2.items():
    combined[key] = combined.get(key, 0) + value
print("Q3:", combined)  # {'a': 400, 'b': 400, 'c': 300, 'd': 400}


# ---------------------------------------------------------------
# Question 4: Build {i: i*i} for i from 1 to n (inclusive)
# ---------------------------------------------------------------
def squares_dict(n):
    return {i: i * i for i in range(1, n + 1)}

# To read n from the keyboard instead, use:  n = int(input("Enter n: "))
n = 8
print("Q4:", squares_dict(n))  # {1: 1, 2: 4, ..., 8: 64}


# ---------------------------------------------------------------
# Question 5: Sort tuples by their float element (highest first)
# ---------------------------------------------------------------
items = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
sorted_items = sorted(items, key=lambda t: float(t[1]), reverse=True)
print("Q5:", sorted_items)  # [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]


# ---------------------------------------------------------------
# Question 6: Sets - create, iterate, add and remove
# ---------------------------------------------------------------
# 6a. Create a set
num_set = {0, 1, 2, 3, 4}
print("Q6a: created set:", num_set)
empty_set = set()  # note: {} creates an empty dict, not a set

# 6b. Iterate over a set
print("Q6b: iterating:", end=" ")
for item in num_set:
    print(item, end=" ")
print()

# 6c. Add members to a set
num_set.add(5)               # add a single item
num_set.update([6, 7, 8])    # add several items
print("Q6c: after adding:", num_set)

# 6c. Remove items from a set
num_set.remove(8)            # raises KeyError if the item is missing
num_set.discard(10)          # no error if the item is missing
popped = num_set.pop()       # removes and returns an arbitrary item
print("Q6c: popped", popped)
print("Q6c: after removing:", num_set)
