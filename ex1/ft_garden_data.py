#!/usr/bin/env python3
class Plant:
    def __init__(self, name, height, age) -> None:
        self.name: str = name
        self.ht: float = height
        self.age_in: int = age
        self.total_grw: float = 0

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.ht}cm, {self.age_in} days old")


def main():
    print("=== Garden Plant Registry ===")
    plants = [Plant("Rose", "25", "30"),
              Plant("sunflower", "85", "45"),
              Plant("Cactus", "15", "120")
              ]

    for p in plants:
        p.show()


if __name__ == "__main__":
    main()
