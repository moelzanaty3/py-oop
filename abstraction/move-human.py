class Human:
  def __init__(self, pos_x, pos_y, speed):
    self.__pos_x = pos_x
    self.__pos_y = pos_y
    self.__speed = speed

  def move_right(self):
    self.__pos_x += self.__speed

  def move_left(self):
    self.__pos_x -= self.__speed

  def move_up(self):
    self.__pos_y += self.__speed

  def move_down(self):
    self.__pos_y -= self.__speed

  def get_position(self):
    return (self.__pos_x, self.__pos_y)


run_cases = [
    (0, 0, 5, "left", -5, 0),
    (0, 0, 5, "right", 5, 0),
    (0, 0, 5, "up", 0, 5),
]

submit_cases = run_cases + [
    (0, 0, 5, "down", 0, -5),
    (10, 10, 2, "left", 8, 10),
    (10, 10, 2, "right", 12, 10),
    (10, 10, 2, "up", 10, 12),
    (10, 10, 2, "down", 10, 8),
]


def test(input1, input2, input3, move_direction, expected_output_x, expected_output_y):
  print("---------------------------------")
  print(f"Inputs:")
  print(f" * pos_x: {input1}")
  print(f" * pos_y: {input2}")
  print(f" * speed: {input3}")
  print(f" * move_direction: {move_direction}")
  expected_output = (expected_output_x, expected_output_y)
  print(f"Expecting: {expected_output}")
  human = Human(input1, input2, input3)
  if move_direction == "left":
    human.move_left()
  elif move_direction == "right":
    human.move_right()
  elif move_direction == "up":
    human.move_up()
  elif move_direction == "down":
    human.move_down()
  result = human.get_position()
  print(f"Actual: {result}")
  if result == expected_output:
    print("Pass")
    return True
  print("Fail")
  return False


def main():
  passed = 0
  failed = 0
  for test_case in test_cases:
    correct = test(*test_case)
    if correct:
      passed += 1
    else:
      failed += 1
  if failed == 0:
    print("============= PASS ==============")
  else:
    print("============= FAIL ==============")
  print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
  test_cases = run_cases

main()
