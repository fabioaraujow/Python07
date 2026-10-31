from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, c_type: str, c_name: str) -> None:
        self.c_type = c_type
        self.c_name = c_name

    @abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        return (f"{self.c_type} is a "
                f"{self.c_name} type Creature")
