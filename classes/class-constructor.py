class Wall:
    def __init__(self, depth, height, width):
        self.depth = depth
        self.height = height
        self.width = width
        self.volume = self.depth * self.height * self.width


run_cases = [
    (Wall(2, 3, 4), (2, 3, 4, 24)),
    (Wall(3, 4, 5), (3, 4, 5, 60)),
    (Wall(4, 5, 6), (4, 5, 6, 120)),
    (Wall(1, 2, 3), (1, 2, 3, 6)),
]

submit_cases = run_cases + [
    (Wall(7, 8, 9), (7, 8, 9, 504)),
    (Wall(10, 11, 12), (10, 11, 12, 1320)),
    (Wall(13, 14, 15), (13, 14, 15, 2730)),
    (Wall(16, 17, 18), (16, 17, 18, 4896)),
    (Wall(19, 20, 21), (19, 20, 21, 7980)),
    (Wall(22, 23, 24), (22, 23, 24, 12144)),
]


def test(wall, expected_output):
    print("---------------------------------")
    expected_depth, expected_height, expected_width, expected_volume = expected_output
    try:
        print(
            f"Expected Wall - volume: {expected_volume} depth: {expected_depth} height: {expected_height} width: {expected_width}"
        )
        print(
            f"Actual Wall   - volume: {wall.volume} depth: {wall.depth} height: {wall.height} width: {wall.width}"
        )
        if (
            expected_volume == wall.volume
            and expected_depth == wall.depth
            and expected_height == wall.height
            and expected_width == wall.width
        ):
            print("Pass")
            return True
        print("Fail")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def main():
    passed = 0
    failed = 0
    for wall, expected_outputs in test_cases:
        correct = test(wall, expected_outputs)
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
