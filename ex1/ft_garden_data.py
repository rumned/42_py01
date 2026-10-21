#!/usr/bin/env python3
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.ht = height
        self.age_in = age

    def show(self):
        print(f"{self.name.capitalize()}: {self.ht}cm, {self.age_in} days old")


def main():
    print("=== Garden Plant Registry ===")
    plants = [Plant("Rose", "25", "30"),
              Plant("Sunflower", "85", "45"),
              Plant("Cactus", "15", "120")
              ]

    for p in plants:
        p.show()


if __name__ == "__main__":
    main()
