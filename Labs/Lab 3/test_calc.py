# Problem 1

import lab02

if __name__ == '__main__':
    lab02.initialize()
    lab02.add(42)

    if lab02.get_current_value() == 42:
      print("Test 1 passed")
    else:
      print("Test 1 failed")

    lab02.subtract(20)
    if lab02.get_current_value() == 22:
      print("Test 1 passed")
    else:
      print("Test 1 failed")