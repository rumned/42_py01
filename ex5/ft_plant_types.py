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


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(self, name, height, age)
        self.color = color
        self.bloom = False

    def bloom(self):
        print("[asking the {self.name} to bloom]")
        self.bloom = True

    def show(self):
        print(f"{self.name}: {self.get_height()}cm, {self.get_age()} days old")
        print(f"Color: {self.color}")
        if self.bloom is False:
            print("{self.name} has not bloomed yet")
        else:
            print("{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(self, name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade = False

    def produce_shade(self):
        print("[asking the {self.name} to produce shade]")
        self.shade = True

    def show(self):
        print(f"{self.name}: {self.get_height()}cm, {self.get_age()} days old")
        print(f"Trunk diameter: {self.trunk_diameter}")
        if self.shade is True:
            print(f"{self.__class__.__name__} {self.name}")
            print("now produces a shade of")
            print(f"{self.get_height()}cm long")
            print(f"and {self.trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(self, name, height, age, total_grw, harvest_season):
        super().__init__(self, name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = total_grw

    def show(self):
        print(f"{self.name}: {self.get_height()}cm, {self.get_age()} days old")
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")
