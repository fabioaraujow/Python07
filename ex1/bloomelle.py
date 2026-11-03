from ex0.creature import Creature
from .heal_cap import HealCapability


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")
        self._power = "Petal Dance!"

    def attack(self) -> str:
        return f"{self._name} uses {self._power}"

    def heal(self) -> str:
        return (f"{self._name} heals itself and others "
                "for a large amount")
