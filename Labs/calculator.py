"""
# Problem 1: Welcome Message
if __name__ == "__main__":
    print("Welcome to the calculator program.")
    current_value = 0
    print("Current value:", current_value)


# Problem 2: Displaying the Current Value
def display_current_value():
  print("Current value:", current_value)

if __name__ == "__main__":
  print("Welcome to the calculator program.")
  current_value = 0
  display_current_value()
  """

# Problem 3-5
def display_current_value():
    global current_value
    print("Current value:", current_value)

# Problem 3: Addition
def add(to_add):
    global current_value
    global last_value
    last_value = current_value
    current_value += to_add

# Problem 3: Subtraction
def subtract(to_sub):
    global current_value
    global last_value
    last_value = current_value
    current_value -= to_sub

# Problem 4: global
# You get an error that the variable current_value is 'undefined'. When you don't defne the variable as a global variable, the function creates a local variable without a value. You cannot add or subtract a value from a variable without an inital value like 0, which is why we are given an error.

# Problem 5: Division
def divide (to_div):
    global current_value
    global last_value
    last_value = current_value
    current_value /= to_div
# Division may cause an error if the user attempts to divide by 0.

# Problem 5: Multiplication
def mult (to_mult):
    global current_value
    global last_value
    last_value = current_value
    current_value *= to_mult

# Problem 6: Memory and Recall
def memory():
    global current_value
    global mem
    mem = current_value

def recall():
    global current_value
    global mem
    current_value = mem

# Problem 7: Undo
def undo():
    global current_value
    global last_value
    temp = last_value
    last_value=current_value
    current_value = temp

if __name__ == "__main__":
    print("Welcome to the calculator program.")
    current_value = 0
    last_value = 0
    mem = 0
    display_current_value() # 0
    add(5)
    subtract(2)
    display_current_value() # 3
    undo()
    display_current_value() # 5
    memory()
    undo()
    display_current_value() # 3
    mult(10)
    display_current_value() # 30
    undo()
    undo()
    display_current_value() # 30
    undo()
    undo()
    undo()
    display_current_value() # 3
    recall()
    display_current_value() # 5
