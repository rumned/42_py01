#!/usr/bin/env python3
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.ht = height
        self.age_init = age
        self.total_growth = 0

    def show(self):
        print(f"{self.name}: {self.ht}cm, {self.age_init} days old")

    def grow(self):
        curr_ht = self.ht
        if curr_ht >= 200:
            curr_ht = round(curr_ht + 0.05, 4)
        else:
            curr_ht = round(curr_ht + 0.8, 4)
        self.total_growth = round(self.total_growth + curr_ht - self.ht, 4)
        self.ht = curr_ht

    def age(self):
        self.age_init = self.age_init + 1


def main():
    print("=== Garden Plant Growth===")
    plants = [Plant("Oak", 250, 30),
              ]

    for p in plants:
        for day in range(1, 8):
            p.show()
            print(f"=== Day {day} ===")
            p.grow()
            p.age()
    plants[0].show()
    print(f"Growth this week: {plants[0].total_growth}cm")


if __name__ == "__main__":
    main()
