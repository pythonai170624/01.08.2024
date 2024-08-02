
# create a list with the positive numebrs
list1: list[int] = [-4, 10, 0, -1, -1, 20]

result: list[int] = []
for number in list1:
    if number > 0:
        result.append(number)

print(result)

result2 = [number for number in list1 if number > 0]
print(result2)

def are_you_in(x: int) -> bool:
    if x > 0:
        return True
    else:
        return False

# filter
def my_filter(numbers: list[int]) -> list[int]:
    func_result: list[int] = []
    for x in numbers:  # [-4, 10, 0, -1, -1, 20]
        if are_you_in(x):
            func_result.append(x)
        else:
            pass

def only_negative(x: int) -> bool:
    if x < 0:
        return True
    else:
        return False

only_negative = lambda x: x < 0
print(only_negative(-12))

list_result = my_filter([-4, 10, 0, -1, -1, 20])

print("filter", list(filter(are_you_in, [-4, 10, 0, -1, -1, 20])))
print("filter", list(filter(only_negative, [-4, 10, 0, -1, -1, 20])))
# lambda:
# one time - disappear after
# one line
# the operation is return

lambda x, y: True if x > 0 else False

def ____(x, y):
    return x > 0

print("filter", list(filter(lambda x: x > 0, [-4, 10, 0, -1, -1, 20])))

print("filter", list(filter(lambda x: True if x > 0 else False, [-4, 10, 0, -1, -1, 20])))

print("filter", list(filter(lambda x: x > 0, [-4, 10, 0, -1, -1, 20])))

def is_zugi(x: int) -> bool:
    # return x % 2 == 0
    if x % 2 == 0:
        return True
    else:
        return False
print("filter zugi", list(filter(is_zugi, [-2, 0, 4, 1, -30, 400, 11])))
print("filter zugi", list(filter(lambda x: True if x % 2 == 0 else False, [-2, 0, 4, 1, -30, 400, 11])))
print("filter zugi", list(filter(lambda x: x % 2 == 0, [-2, 0, 4, 1, -30, 400, 11])))
print("filter positive", list(filter(lambda x: x > 0, [-2, 0, 4, 1, -30, 400, 11])))

# lambda return all items not equal to 0
print("filter non-zero", list(filter(lambda x: x != 0, [-2, 0, 4, 1, -30, 400, 11])))
# *Bonus: create a list of string , filter to get only strings start with a
print("filter starts with a", list(filter(lambda word: word.upper().startswith("A"), \
                                          ["apple", "anaconda", "banana"])))
# *Bonus: create a list of string , filter to get only strings longer than 3 characters
print("filter more than 3 letters", list(filter(lambda word: len(word) > 3, \
                                          ["oz", "danny", "moshe", "roy", "sharona"])))

# map
# take a list of numbers and return all numbers ** 2
result = [x ** 2 for x in [-2, 0, 4, 1, -30, 400, 11]]
# [-2, 0,  4, 1, -30, 400, 11]
#   |  |,  |
# [ 4, 0, 16 ... ]
print('map x ** 2', list(map(lambda x: x ** 2, [-2, 0, 4, 1, -30, 400, 11])))
print('map int', list(map(int, ["-2", "0", "4", "1", "-30", "400", "11"])))

# 1 use map on a list of numbers return each number // 10
print('map x // 10', list(map(lambda x: x // 10, [-2, 0, 4, 1, -30, 400, 11])))
# 2 use map on a list of numbers each zugi number will be 1 else 0
#     [1, 2, 3, 4, 8] => [0, 1, 0, 1, 1]
print('map x % 2', list(map(lambda x: 1 if x % 2 == 0 else 0, [-2, 0, 4, 1, -30, 400, 11])))
# 3 use map on a list of numbers each even number will be "zugi" else "e-zugi"
#     [1, 2, 3, 4, 8] => ["ezugi", "zugi", "ezugi", "zugi", "zugi"]
print('map zugi ezugi', list(map(lambda x: "zugi" if x % 2 == 0 else "e-zugi", [-2, 0, 4, 1, -30, 400, 11])))

# how to write filter my self
# def my_filter(func: callable, items: list[int | float]) -> list:
#     func_result: list[int] = []
#     for x in items:  # [-4, 10, 0, -1, -1, 20]
#         if func(x):
#             func_result.append(x)
#     return func_result
#my_filter(are_you_in, [-4, 10, 0, -1, -1, 20]))

# def run_me(f) -> None:
#     f()
# run_me(are_you_in)


print(["zzzzz", "b", "abc", "cccc", "bb", "t"])
res1 = list(map(lambda word: len(word), ["zzzzz", "b", "abc", "cccc", "bb", "t"]))
print(res1)
print(sorted(res1))
def key_func(word):
    return len(word)
print(sorted(["zzzzz", "b", "abc", "cccc", "bb", "t"], key=lambda word: len(word)))
print(sorted(["zzzzz", "b", "abc", "cccc", "bb", "t"], key=lambda word: (len(word), word))) # 2 criteria
print(sorted(["zzzzz", "b", "abc", "cccc", "bb", "t"], key=key_func))
# map
#               5       1     3      4      2    1

# sort this list [["danny", 12], ["bob", 30], ["aaron", 42]]
# sort 1. by age (second item) 2. by name (first item)
print("sort by age", sorted([["danny", 12], ["bob", 30], ["aaron", 42]], key=lambda list_item: list_item[1]))
print("sort by name", sorted([["danny", 12], ["bob", 30], ["aaron", 42]], key=lambda list_item: list_item[0]))
# "110" "88"
#  aac   gg

# lazy
list_1: list[int] = [-1, -2, 0, -10]
filter_me = filter(lambda x: x > 0, list_1)
print(filter_me)
list_1.append(100)
print(list(filter_me))

print(sorted([1, 5, 10, -100, 20, 0], key=lambda x: -1 * x))
print("one key", sorted([1, 5, 10, -100, 20, 3, 1, 0], key=lambda x: 1 if x % 2 == 0 else 0))
#             0  0  1     1    1  0  0  1
print("two key", sorted([1, 5, 10, -100, 20, 3, 1, 0], key=lambda x: (1 if x % 2 == 0 else 0, x)))
#             0  0  1     1    1  0  0  1
print(sorted([1, 5, 10, -100, 20, 3, 1, 0], key=lambda x: (1 if x % 2 == 0 else 0, x)))
print(sorted([1, 5, 10, -100, 20, 3, 1, 0], key=lambda x: (0 if x % 2 == 0 else 1, x)))