class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):
        return min(self.__x1, self.__x2)

    def get_right_x(self):
        return max(self.__x2, self.__x1)

    def get_top_y(self):
        return max(self.__y1, self.__y2)

    def get_bottom_y(self):
        return min(self.__y2, self.__y1)

    # don't touch below this line

    def __repr__(self):
        return f"Rectangle({self.__x1}, {self.__y1}, {self.__x2}, {self.__y2})"


run_cases = [
    (Rectangle(0, 0, 4, 4), (0, 4, 4, 0)),
    (Rectangle(4, 4, 0, 0), (0, 4, 4, 0)),
]

submit_cases = run_cases + [
    (Rectangle(1, 2, 3, 4), (1, 3, 4, 2)),
    (Rectangle(3, 4, 1, 2), (1, 3, 4, 2)),
    (Rectangle(2, 1, 5, 4), (2, 5, 4, 1)),
    (Rectangle(5, 4, 2, 1), (2, 5, 4, 1)),
    (Rectangle(3, 3, 3, 3), (3, 3, 3, 3)),
]


def test(rectangle, expected_output):
    print("---------------------------------")
    print(f"Inputs: {rectangle}")
    print(f"Expecting: {expected_output}")
    result = (
        rectangle.get_left_x(),
        rectangle.get_right_x(),
        rectangle.get_top_y(),
        rectangle.get_bottom_y(),
    )
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
