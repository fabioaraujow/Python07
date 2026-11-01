from .creature import Creature


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__("Torragon", "Water")
        self._power = "Hydro Pump!"

    def attack(self) -> str:
        return f"{self._name} uses {self._power}"
