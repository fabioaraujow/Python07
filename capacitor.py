#!/usr/bin/env python3
from ex1 import HealingCreatureFactory, TransformCreatureFactory


def run_heal_factory(factory: HealingCreatureFactory) -> None:
    print(" base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(base.heal())
    print(" evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def run_transform_factory(factory: TransformCreatureFactory) -> None:
    print(" base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())
    print(" evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


if __name__ == "__main__":
    print("Testing Creature with healing capability")
    run_heal_factory(HealingCreatureFactory())
    print()
    print("Testing Creature with transform capability")
    run_transform_factory(TransformCreatureFactory())
