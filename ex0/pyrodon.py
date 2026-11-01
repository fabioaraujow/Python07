from .creature import Creature


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")
        self._power = "Flamethrower!"

    def attack(self) -> str:
        return f"{self._name} uses {self._power}"
