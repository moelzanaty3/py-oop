class Human:
  def sprint_right(self):
    self.__sprint(self.move_right)

  def sprint_left(self):
    self.__sprint(self.move_left)

  def sprint_up(self):
    self.__sprint(self.move_up)

  def sprint_down(self):
    self.__sprint(self.move_down)

  def __sprint(self, move_method):
    self.__raise_if_cannot_sprint()
    move_method()
    move_method()
    self.__use_sprint_stamina()

  def __raise_if_cannot_sprint(self):
    if self.__stamina == 0:
      raise Exception("not enough stamina to sprint")

  def __use_sprint_stamina(self):
    self.__stamina -= 1

  # don't touch below this line

  def move_right(self):
    self.__pos_x += self.__speed

  def move_left(self):
    self.__pos_x -= self.__speed

  def move_up(self):
    self.__pos_y += self.__speed

  def move_down(self):
    self.__pos_y -= self.__speed

  def get_position(self):
    return self.__pos_x, self.__pos_y

  def __init__(self, pos_x, pos_y, speed, stamina):
    self.__pos_x = pos_x
    self.__pos_y = pos_y
    self.__speed = speed
    self.__stamina = stamina


run_cases = [
    ((0, 0, 5, 3), ["sprint_right"], (10, 0, None)),
    (
        (0, 0, 20, 3),
        [
            "sprint_left",
            "sprint_left",
            "sprint_left",
        ],
        (-120, 0, None),
    ),
    (
        (1, 1, 3, 1),
        ["sprint_down", "sprint_right"],
        (1, -5, "not enough stamina to sprint"),
    ),
]


submit_cases = run_cases + [
    ((3, 5, 5, 1), ["sprint_up"], (3, 15, None)),
    ((2, 15, 6, 2), ["sprint_down"], (2, 3, None)),
    (
        (1, 1, 5, 2),
        ["sprint_left", "sprint_up", "sprint_down"],
        (-9, 11, "not enough stamina to sprint"),
    ),
]


def test(human_args, methods, expected_output):
  print("---------------------------------")
  print(f"Inputs:")
  human = Human(*human_args)
  print(f" * human({human_args})")
  print(f" * methods: {methods}")
  expected_x, expected_y, expected_error = expected_output
  print(f"Expected: x: {expected_x}, y: {expected_y}, error: {expected_error}")
  try:
    for method in methods:
      getattr(human, method)()
    actual_x, actual_y = human.get_position()
    actual_err = None
  except Exception as e:
    actual_x, actual_y = human.get_position()
    actual_err = str(e)
  print(f"Actual: x: {actual_x}, y: {actual_y}, error: {actual_err}")
  if (
      actual_x == expected_x
      and actual_y == expected_y
      and actual_err == expected_error
  ):
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
