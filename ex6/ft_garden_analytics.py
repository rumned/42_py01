class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.set_height(height)
        self.set_age(age)
        self.total_grw = 0

    def show(self):
        print(f"{self.name}: {self.get_height()}cm, {self.get_age()} days old")

    def grow(self):
        curr_ht = self.get_height()
        if curr_ht >= 200:
            curr_ht = round(curr_ht + 0.05, 4)
        else:
            curr_ht = round(curr_ht + 0.8, 4)
        self.total_grw = round(self.total_grw + curr_ht - self.get_height(), 4)
        self.set_height(curr_ht)

    def get_height(self):
        return self._height

    def set_height(self, value):
        if value < 0:
            raise ValueError("Height cannot be negative.")
        self._height = value

    def get_age(self):
        return self._age

    def set_age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative.")
        self._age = value

    @staticmethod
    def check_age(age_to_check):
        if age_to_check > 365 :
            return True
        return False


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self):
        print(f"[asking the {self.name.lower()} to bloom]")
        self.is_blooming = True

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if self.is_blooming is False:
            print(f"{self.name} has not bloomed yet")
        else:
            print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade = False

    def produce_shade(self):
        print(f"[asking the {self.name.lower()} to produce shade]")
        self.shade = True

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")
        if self.shade is True:
            print(
                f"{self.__class__.__name__} {self.name} "
                f"now produces a shade of {self.get_height()}cm long "
                f"and {self.trunk_diameter}cm wide."
            )


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = self.total_grw

    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def grow(self):
        super().grow()
        self.set_age(self.get_age() + 1)
        self.total_grw += 1
        self.nutritional_value += 20

flower = Plant("Rose", 15.0, 10)
tree = Plant("Oak", 300, 1000)
print(flower.check_age(flower.get_age()))
print(Plant.check_age(tree.get_age()))
