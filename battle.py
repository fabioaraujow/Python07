#!/usr/bin/env python3
from ex0 import CreatureFactory, AquaFactory, FlameFactory


def check_factory(factory: CreatureFactory) -> None:
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def battle(family_type1: CreatureFactory,
           family_type2: CreatureFactory) -> None:
    creature1 = family_type1.create_base()
    creature2 = family_type2.create_base()
    print(creature1.describe())
    print(" vs.")
    print(creature2.describe())
    print(" fight!")
    print(creature1.attack())
    print(creature2.attack())


if __name__ == "__main__":
    flame = FlameFactory()
    aqua = AquaFactory()
    print("Testing factory")
    check_factory(flame)
    print()
    print("Testing factory")
    check_factory(aqua)
    print()
    print("Testing battle")
    battle(flame, aqua)
