fireball_damage = 500
potion_mana = 100
fireball_cost = 50


class Wizard:
  def __init__(self, name, stamina, intelligence):
    self.name = name
    self.__stamina = stamina
    self.__intelligence = intelligence
    self.mana = self.__intelligence * 10
    self.health = self.__stamina * 100

  def cast_fireball(self, target):
    if self.mana < fireball_cost:
      raise Exception(f"{self.name} cannot cast fireball")
    else:
      self.mana -= fireball_cost
      self.get_fireballed(target)

  def is_alive(self):
    if self.health > 0:
      return True
    return False

  def get_fireballed(self, target):
    target.health -= fireball_damage

  def drink_mana_potion(self):
    self.mana += potion_mana


run_cases = [
    (
        [
            [
                ("Gandalf", 20, 15),
                ("Saruman", 18, 14),
            ],
            [
                ("cast_fireball", 0, 1),
            ],
        ],
        [
            [
                {"mana": 100},
                {"health": 1300},
            ],
            None,
        ],
    ),
    (
        [
            [
                ("Rincewind", 20, 3),
                ("no one in particular", 10, 10),
            ],
            [
                ("cast_fireball", 0, 1),
            ],
        ],
        [
            None,
            "Rincewind cannot cast fireball",
        ],
    ),
]

submit_cases = run_cases + [
    (
        [
            [
                ("Merlin", 18, 100),
                ("Morgana", 15, 100),
            ],
            [
                ("battle", 0, 1),
            ],
        ],
        [
            None,
            "Merlin",
        ],
    ),
    (
        [
            [
                ("Khadgar", 20, 5),
                ("Medivh", 18, 140),
            ],
            [
                ("cast_fireball", 0, 1),
            ],
        ],
        [
            [
                {"mana": 0},
                {"health": 1300},
            ],
            None,
        ],
    ),
]


def test(test_input, expected_output):
  print("---------------------------------")
  wizards_list, actions = test_input
  expected_wizards_attrs, expected_result = expected_output

  wizards = []
  for wizzer in wizards_list:
    wizard = Wizard(*wizzer)
    wizards.append(wizard)

  actual_exception = None
  try:
    for action in actions:
      action_name = action[0]

      if action_name == "cast_fireball":
        caster = wizards[action[1]]
        target = wizards[action[2]]

        print(f"{caster.name} cast fireball at {target.name}")
        caster.cast_fireball(target)

      elif action_name == "battle":
        caster = wizards[action[1]]
        target = wizards[action[2]]

        print(f"{caster.name} vs {target.name}")
        print(f"{target.name} health: {target.health}")
        print(f"{caster.name} health: {caster.health}")

        while caster.is_alive() and target.is_alive():
          caster.drink_mana_potion()
          print(f"{caster.name} cast fireball at {target.name}")
          caster.cast_fireball(target)
          print(f"{target.name} health: {target.health}")
          if target.is_alive():
            target.drink_mana_potion()
            print(f"{target.name} cast fireball at {caster.name}")
            target.cast_fireball(caster)
            print(f"{caster.name} health: {caster.health}")

        winner = caster if caster.is_alive() else target

    if actual_exception is None:
      pass
  except Exception as e:
    actual_exception = str(e)

  if expected_result is not None:
    if isinstance(expected_result, str):
      if "cannot cast fireball" in expected_result:
        print(f"Expected exception: {expected_result}")
        print(f"Actual exception: {actual_exception}")
        if actual_exception == expected_result:
          print("Pass")
          return True
        else:
          print("Fail")
          return False
      else:
        winners = []
        for wizard in wizards:
          if wizard.is_alive():
            winners.append(wizard.name)

        if len(winners) == 0:
          print(f"Expected winner: {expected_result}")
          print(f"Actual winner: None")
          print("Fail")
          return False

        if len(winners) > 1:
          print(f"Expected winner: {expected_result}")
          print(f"Actual winners: None")
          print("Fail")
          return False

        winner = winners[0]
        print(f"Expected winner: {expected_result}")
        print(f"Actual winner: {winner}")
        if winner != expected_result:
          print("Fail")
          return False

        print("Pass")
        return True
    else:
      print(f"Unexpected expected: {type(expected_result)}")
      return False
  else:
    if actual_exception is not None:
      print(f"Unexpected exception: '{actual_exception}'")
      print("Fail")
      return False

  passed = True
  for i, expected_wizard_data in enumerate(expected_wizards_attrs):
    wizard = wizards[i]
    for attr, expected_value in expected_wizard_data.items():
      actual_value = getattr(wizard, attr)
      print(f"Expected {wizard.name}'s {attr}: {expected_value}")
      print(f"Actual {wizard.name}'s {attr}: {actual_value}")
      if actual_value != expected_value:
        passed = False

  if passed:
    print("Pass")
  else:
    print("Fail")
  return passed


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
