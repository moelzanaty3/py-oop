class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x1, y1, x2, y2):
        pass


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, height, width, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.fire_range = fire_range
        self.height = height
        self.width = width
        self.__hit_box = Rectangle(
            pos_x - width/2, pos_y - height/2, pos_x + width/2, pos_y + height/2)

    def in_area(self, x1, y1, x2, y2):
        rect = Rectangle(x1, y1, x2, y2)
        return self.__hit_box.overlaps(rect)


# Don't touch below this line


class Rectangle:
    def overlaps(self, rect):
        return (
            self.get_left_x() <= rect.get_right_x()
            and self.get_right_x() >= rect.get_left_x()
            and self.get_top_y() >= rect.get_bottom_y()
            and self.get_bottom_y() <= rect.get_top_y()
        )

    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):
        if self.__x1 < self.__x2:
            return self.__x1
        return self.__x2

    def get_right_x(self):
        if self.__x1 > self.__x2:
            return self.__x1
        return self.__x2

    def get_top_y(self):
        if self.__y1 > self.__y2:
            return self.__y1
        return self.__y2

    def get_bottom_y(self):
        if self.__y1 < self.__y2:
            return self.__y1
        return self.__y2


run_cases = [
    (Dragon("Green Dragon", -1, -2, 1, 2, 1), -2, -3, 0, 0, True),
    (Dragon("Red Dragon", 2, 2, 2, 2, 2), 0, 1, 1, 0, True),
    (Dragon("Blue Dragon", 4, -3, 2, 1, 1), -5, -5, 5, 5, True),
    (Dragon("Silver Dragon", 0, 0, 5, 5, 10), 4, 0, 5, 1, False),
    (Dragon("Gold Dragon", 0, 0, 5, 5, 10), 4, 0, 5, 1, False),
    (Dragon("Gold Dragon", 0, 0, 20, 20, 20), 10, 10, 20, 20, True),
]

submit_cases = run_cases + [
    (Dragon("Green Dragon", -1, -2, 1, 2, 1), -3, -3, -1, -1, True),
    (Dragon("Red Dragon", 2, 2, 2, 2, 2), 5, 5, 10, 10, False),
    (Dragon("Blue Dragon", 4, -3, 2, 1, 1), 0, 0, 10, 10, False),
    (Dragon("Black Dragon", 5, -1, 3, 2, 2), -10, -10, 10, 10, True),
    (Dragon("White Dragon", 0, 0, 1, 1, 1), -1, -1, 1, 1, True),
]


def test(dragon, input1, input2, input3, input4, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(
        f" * Dragon position and size: {dragon.pos_x}, {dragon.pos_y}, {dragon.height}, {dragon.width}"
    )
    print(f" * Area corners: ({input1}, {input2}), ({input3}, {input4})")
    print(f"Expected in area: {expected_output}")
    result = dragon.in_area(input1, input2, input3, input4)
    print(f"  Actual in area: {result}")
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
