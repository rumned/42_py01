class Plant:
    def __init__(self, name, height, age) -> None:
        self.name: str = name
        self.set_height(height)
        self.set_age(age)
        self.total_grw: float = 0
        self._stats = self.Status()

    def show(self) -> None:
        self._stats.plus_show_stat()
        print(f"{self.name}: {self.get_height()}cm, {self.get_age()} days old")

    def grow(self) -> None:
        self._stats.plus_grow_stat()
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
        self._stats.plus_age_stat()
        curr_age = self.get_age()
        self.set_age(curr_age + 1)

    def display(self) -> None:
        self._stats.display_stat()

    @staticmethod
    def check_age(age_to_check: int) -> bool:
        if age_to_check > 365:
            return True
        return False

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    class Status:
        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0

        def plus_grow_stat(self) -> None:
            self._grow_calls += 1

        def plus_age_stat(self) -> None:
            self._age_calls += 1

        def plus_show_stat(self) -> None:
            self._show_calls += 1

        def display_stat(self) -> None:
            print("Stats:", end=" ")
            print(f"{self._grow_calls} grow", end=" ")
            print(f"{self._age_calls} age", end=" ")
            print(f"{self._show_calls} show")


class Flower(Plant):
    def __init__(self, name, height, age, color) -> None:
        super().__init__(name, height, age)
        self.color: str = color
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
        self._stats: Tree.Status = self.Status()

    def produce_shade(self) -> None:
        self._stats.plus_shade_stat()
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

    class Status(Plant.Status):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls: int = 0

        def plus_shade_stat(self) -> None:
            self._shade_calls += 1

        def display_stat(self) -> None:
            super().display_stat()
            print(f"{self._shade_calls} shade")


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


class Seed(Flower):
    def __init__(self, name, height, age, color) -> None:
        super().__init__(name, height, age, color)
        self.color = color
        self.is_blooming = False
        self.seed_number = 67

    def bloom(self) -> None:
        print(f"[asking the {self.name.lower()} to bloom]")
        self.is_blooming = True

    def show(self) -> None:
        super().show()
        if self.is_blooming is False:
            print("Seeds: 0")
        else:
            print(f"Seeds: {self.seed_number}")


def display_from_outside(plant: Plant) -> None:
    plant.display()


def main():
    flower = Plant("Rose", 15.0, 10)
    tree = Plant("Oak", 300, 1000)
    print(f"Flower age: {flower.get_age()}")
    print(f"Is more than 1yr? {flower.check_age(flower.get_age())}")
    print(f"Tree age: {tree.get_age()}")
    print(f"Is more than 1yr? {tree.check_age(tree.get_age())}")
    print(f"Is 365 days more than 1yr? {Plant.check_age(365)}")
    print(f"Is 366 days more than 1yr? {Plant.check_age(366)}")
    print("="*20)
    seed = Seed("sunflower", 80.0, 45, "yellow")
    seed.show()
    seed.grow()
    seed.age()
    seed.bloom()
    seed.show()
    seed.display()
    print("="*20)
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    rose.bloom()
    rose.grow()
    rose.show()
    rose.display()
    print("="*20)
    oak = Tree("Oak", 300.0, 1000, 50)
    oak.show()
    oak.produce_shade()
    oak.show()
    for _ in range(3):
        oak.grow()
    oak.age()
    oak.produce_shade()
    oak.display()
    print("="*20)
    carrot = Vegetable("Carrot", 5.0, 20, "Carrot Season")
    carrot.grow()
    carrot.grow()
    carrot.age()
    carrot.show()
    carrot.display()
    print("="*20)
    unknown = Plant.anonymous()
    unknown.show()
    unknown.display()
    print("="*20)
    display_from_outside(carrot)
    display_from_outside(oak)
    display_from_outside(rose)
    display_from_outside(seed)
    display_from_outside(unknown)


if __name__ == "__main__":
    main()
