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
        self._height = value

    def get_age(self) -> int:
        return self._age

    def set_age(self, value: int) -> None:
        if value < 0:
            raise ValueError("Age cannot be negative.")
        self._age = value

    def age(self) -> None:
        curr_age = self.get_age()
        self.set_age(curr_age + 1)


class Flower(Plant):
    def __init__(self, name, height, age, color) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        print(f"[asking the {self.name.lower()} to bloom]")
        self.is_blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.is_blooming is False:
            print(f"{self.name} has not bloomed yet")
        else:
            print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade = False

    def produce_shade(self) -> None:
        print(f"[asking the {self.name.lower()} to produce shade]")
        self.shade = True

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")
        if self.shade is True:
            print(
                f"{self.__class__.__name__} {self.name} "
                f"now produces a shade of {self.get_height()}cm long "
                f"and {self.trunk_diameter}cm wide."
            )


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = self.total_grw

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 20


def main():
    print("==Flower")
    rose = Flower("Rose", 25, 30, "red")
    rose.show()
    rose.bloom()
    rose.show()
    print("-"*20)
    print("==Tree")
    pine = Tree("Pine", 500.0, 1825, 5.0)
    pine.show()
    pine.produce_shade()
    pine.show()
    print("-"*20)
    print("==Vegetable")
    tomato = Vegetable("Tomato", 80, 90, "April")
    while tomato.nutritional_value <= 100:
        tomato.show()
        print("-"*20)
        tomato.grow()


if __name__ == "__main__":
    main()
