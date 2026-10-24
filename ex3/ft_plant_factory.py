#!/usr/bin/env python3
class Plant:
    def __init__(self, name, height, age) -> None:
        self.name = name
        self.ht = height
        self.age_in = age
        self.total_grw: float = 0

    def show(self) -> None:
        print(f"{self.name}: {self.ht}cm, {self.age_in} days old")

    def grow(self) -> None:
        curr_ht = self.ht
        if curr_ht >= 200:
            curr_ht = round(curr_ht + 0.05, 4)
        else:
            curr_ht = round(curr_ht + 0.8, 4)
        self.total_grw = round(self.total_grw + curr_ht - self.ht, 4)
        self.ht = curr_ht

    def age(self) -> None:
        self.age_in = self.age_in + 1


def main():
    print("=== Garden Plant Growth===")
    plants = [Plant("Oak", 250, 30),
              Plant("Maple", 150, 20),
              Plant("Rose", 25, 30),
              Plant("Sunflower", 85, 45),
              Plant("Cactus", 5, 90)
              ]

    for p in plants:
        p.show()
        # p.grow()
        # p.age()
        # p.show()
        # print()


if __name__ == "__main__":
    main()
