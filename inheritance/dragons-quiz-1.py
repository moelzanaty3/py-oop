class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        # Check if pos_x is between x1 and x2 (inclusive)
        x_condition = x_1 <= self.pos_x <= x_2
        # Check if pos_y is between y1 and y2 (inclusive)
        y_condition = y_1 <= self.pos_y <= y_2
        # Return True only if both conditions are True
        return x_condition and y_condition


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        # Initialize empty list to store units that get hit by fire
        hit_units = []

        # Calculate the boundaries of the fire area
        # Fire spreads in a square pattern from the target point (x,y)
        # The size of the square is determined by fire_range
        min_x = x - self.__fire_range
        max_x = x + self.__fire_range
        min_y = y - self.__fire_range
        max_y = y + self.__fire_range

        # Check each unit to see if it falls within the fire area
        for unit in units:
            if unit.in_area(min_x, min_y, max_x, max_y):
                hit_units.append(unit)

        # Return list of all units that were hit by the fire
        return hit_units


run_cases = [
    (
        [Unit("Cian", 3, 3), Unit("Andrew", -1, 4), Unit("Baran", -6, 5)],
        Dragon("Draco", 2, 2, 3),
        2,
        3,
        ["Cian", "Andrew"],
    ),
]

submit_cases = run_cases + [
    (
        [
            Unit("Carbry", 2, 1),
            Unit("Yvor", 1, 0),
            Unit("Eoin", 2, 0),
            Unit("Edwin", 10, 10),
        ],
        Dragon("Fafnir", 1, 1, 1),
        1,
        1,
        ["Carbry", "Yvor", "Eoin"],
    ),
    (
        [Unit("Nicholas", 0, 1), Unit("Andrew", -1, 4), Unit("Baran", -6, 5)],
        Dragon("Hydra", 0, 0, 2),
        0,
        1,
        ["Nicholas"],
    ),
    (
        [
            Unit("Yvor", 1, 0),
            Unit("Nicholas", 0, 1),
            Unit("Eoin", 2, 0),
            Unit("Cian", 3, 3),
            Unit("Andrew", -1, 4),
            Unit("Baran", -6, 5),
            Unit("Carbry", 2, 1),
        ],
        Dragon("Smaug", 6, 6, 2),
        1,
        1,
        ["Yvor", "Nicholas", "Eoin", "Cian", "Carbry"],
    ),
]


def test(units, dragon, x_target, y_target, expected_hit_units):
    print("---------------------------------")
    print(f"Testing Dragon {dragon.name} at ({dragon.pos_x}, {dragon.pos_y})")
    for unit in units:
        print(f"Unit {unit.name} at ({unit.pos_x}, {unit.pos_y})")
    print(f"Breathing fire at ({x_target}, {y_target})")
    print(f"Expecting hit units: {expected_hit_units}")
    hit_units = dragon.breathe_fire(x_target, y_target, units)
    hit_unit_names = [unit.name for unit in hit_units]
    print(f"Actual hit units: {hit_unit_names}")
    if set(hit_unit_names) == set(expected_hit_units):
        print("Pass")
        return True
    else:
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
