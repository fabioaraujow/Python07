from ex0.creature import Creature
from .battle_strategy import BattleStrategy
from .error_class import CheckSuitableError
from ex1.transf_cap import TransformCapability
from ex1.heal_cap import HealCapability


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise CheckSuitableError("Invalid Creature "
                                     f"'{type(creature).__name__}'"
                                     " for this normal strategy")
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, TransformCapability):
            raise CheckSuitableError("Invalid Creature "
                                     f"'{type(creature).__name__}'"
                                     " for this aggressive strategy")
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, HealCapability):
            raise CheckSuitableError("Invalid Creature "
                                     f"'{type(creature).__name__}'"
                                     " for this defensive strategy")
        print(creature.attack())
        print(creature.heal())
