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

# print("=== Garden Security System ===")

# flower = Plant("Rose", 15.0, 10)
# print(f"Plant created: {flower}\n")

# # flower._height = -15
# # flower.age = -15
# flower.set_height(25)
# flower.set_age(30)
# print()
# flower.set_height(-25)
# flower.set_age(-30)
# print()

# print(f"Current state: {flower}")
