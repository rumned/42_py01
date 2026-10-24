class Plant:
    def __init__(self, name, height, age) -> None:
        self.name: str = name
        self.set_height(height)
        self.set_age(age)
        self.total_grw: float = 0

    def show(self) -> None:
        print(f"{self.name}: {self.get_height()}cm, {self.get_age()} days old")

    def grow(self) -> None:
        curr_ht = self.get_height()
        if curr_ht >= 200:
            curr_ht = round(curr_ht + 0.05, 4)
        else:
            curr_ht = round(curr_ht + 0.8, 4)
        self.total_grw = round(self.total_grw + curr_ht - self.get_height(), 4)
        self.set_height(curr_ht)

    def get_height(self) -> float:
        return self._height

    def set_height(self, value: float) -> None:
        if value < 0:
            raise ValueError("Height cannot be negative.")
        self._height = float(value)

    def get_age(self) -> int:
        return self._age

    def set_age(self, value: int) -> None:
        if value < 0:
            raise ValueError("Age cannot be negative.")
        self._age = value

    def age(self) -> None:
        curr_age = self.get_age()
        self.set_age(curr_age + 1)


def main():
    print("=== Garden Security System ===")
    flower = Plant("Rose", 15.0, 10)
    print("Current state:", end=" ")
    flower.show()

    # flower._height = -15
    # flower.age = -15
    flower.set_height(25)
    print(f"Height updated:{flower.get_height()}cm")
    flower.set_age(30)
    print(f"Age updated:{flower.get_age()} days")
    flower.age()
    print(f"Age updated:{flower.get_age()} days")
    flower.grow()
    print(f"Plant grew:{flower.get_height()}cm")
    try:
        flower.set_age(-1)
    except ValueError as e:
        print(f"{e}")
    try:
        flower.set_height(-1)
    except ValueError as e:
        print(f"{e}")
    print()
    print("Current state:", end=" ")
    flower.show()


if __name__ == "__main__":
    main()
