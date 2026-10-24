#!/usr/bin/env python3
class Plant:
    def __init__(self, name, height, age) -> None:
        self.name: str = name
        self.ht: float = height
        self.age_in: int = age
        self.total_grw: float = 0


def main():
    plant = Plant("Kekwa", "25", "30")
    print("=== Welcome to My Garden ===")
    print(f"Plant: {plant.name}")
    print(f"Height: {plant.ht}cm")
    print(f"Age: {plant.age_in} days")
    print()
    print("=== End of Program ===")


if __name__ == "__main__":
    main()
