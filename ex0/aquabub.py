from .creature import Creature


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__("Aquabub", "Water")
        self._power = "Water Gun!"

    def attack(self) -> str:
        return f"{self._name} uses {self._power}"
