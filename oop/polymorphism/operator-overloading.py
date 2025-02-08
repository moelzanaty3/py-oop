class Sword:
    CRAFTING_RECIPES = {
        ('bronze', 'bronze'): 'iron',
        ('iron', 'iron'): 'steel'
    }

    def __init__(self, sword_type):
        self.sword_type = sword_type

    def __add__(self, other):
        recipe = (self.sword_type, other.sword_type)
        if recipe in self.CRAFTING_RECIPES:
            return Sword(self.CRAFTING_RECIPES[recipe])
        raise Exception('cannot craft')


run_cases = [
    (Sword("bronze"), Sword("bronze"), "iron", None),
    (Sword("bronze"), Sword("iron"), None, "cannot craft"),

]

submit_cases = run_cases + [
    (Sword("steel"), Sword("steel"), None, "cannot craft"),
    (Sword("iron"), Sword("iron"), "steel", None),
    (Sword("bronze"), Sword("steel"), None, "cannot craft"),
]


def test(sword1, sword2, expected_result, expected_err):
    try:
        print("---------------------------------")
        print(
            f"Crafting a {sword1.sword_type} sword with a {sword2.sword_type} sword..."
        )
        result = sword1 + sword2

        if expected_err:
            print(f"Expected Exception: {expected_err}")
            print("Actual: no exception raised")
            print("Fail")
            return False

        print(f"Expected: {expected_result}")
        print(f"Actual: {result.sword_type}")
        print(f"A new {result.sword_type} sword was crafted!")
        if result.sword_type != expected_result:
            print("Fail")
            return False

    except Exception as e:
        print(f"Expected Exception: {expected_err}")
        print(f"Actual Exception: {e}")
        if expected_err != str(e):
            print("Fail")
            return False

    print("Pass")
    return True


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
