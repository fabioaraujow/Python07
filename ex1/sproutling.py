from ex0.creature import Creature
from .heal_cap import HealCapability


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")
        self._power = "Vine Whip!"

    def attack(self) -> str:
        return f"{self._name} uses {self._power}"

    def heal(self) -> str:
        return f"{self._name} heals itself for a small amount"
