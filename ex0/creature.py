from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self) -> None:
        self.creature_name = ""
        self.creature_type = ""

    @abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        return (f"{self.creature_name} is a "
                f"{self.creature_type} type Creature")
