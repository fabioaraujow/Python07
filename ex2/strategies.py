from ex0.creature import Creature
from .battle_strategy import BattleStrategy
from .error_class import CheckSuitableError
from ex1.transf_cap import TransformCapability


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise CheckSuitableError(f"{type(creature).__name__} "
                                     "isn't eligible for "
                                     f"{type(self).__name__}")
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, TransformCapability):
            raise CheckSuitableError(f"{type(creature).__name__} "
                                     "isn't eligible for "
                                     f"{type(self).__name__}")
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())
