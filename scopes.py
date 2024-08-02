
x: int = 10

def print_x(x: int):
    # bad practice to use global variables
    # everything should be declared or passed by parameters
    print(f"x is {x}")  # x is read-only
    #x = 1  # creates a new x because i did x = 1

def change_x():
    global x
    x = x + 1
    # bad practice to use global variables
    # everything should be declared or passed by parameters
    print(f"x is {x}")  # x is read-only
    #x = 1  # creates a new x because i did x = 1
    y = 1

print_x(2)

change_x()
# print(y)  # Error
print('last print', x)  # ?