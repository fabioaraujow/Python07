#!/usr/bin/env python3
from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (BattleStrategy, NormalStrategy,
                 AggressiveStrategy, DefensiveStrategy, CheckSuitableError)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    try:
        for i in range(len(opponents)):
            for j in range(i + 1, len(opponents)):
                print()
                print("* Battle *")
                factory_1, strategy_1 = opponents[i]
                factory_2, strategy_2 = opponents[j]
                creature_1 = factory_1.create_base()
                creature_2 = factory_2.create_base()
                print(creature_1.describe())
                print(" vs.")
                print(creature_2.describe())
                print(" now fight!")
                strategy_1.act(creature_1)
                strategy_2.act(creature_2)
    except CheckSuitableError as err:
        print(f"Battle error, aborting tournament: {err}")


if __name__ == "__main__":
    print("Tournament 0 (basic)")
    opponents = [(FlameFactory(), NormalStrategy()),
                 (HealingCreatureFactory(), DefensiveStrategy())]
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    battle(opponents)
    print()
    print("Tournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    opponents = [(FlameFactory(), AggressiveStrategy()),
                 (HealingCreatureFactory(), DefensiveStrategy())]
    battle(opponents)
    print()
    print("Tournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    opponents = [(AquaFactory(), NormalStrategy()),
                 (HealingCreatureFactory(), DefensiveStrategy()),
                 (TransformCreatureFactory(), AggressiveStrategy())]
    battle(opponents)
