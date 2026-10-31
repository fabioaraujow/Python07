from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, c_name: str, c_type: str) -> None:
        self._type = c_type
        self._name = c_name

    @abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        return (f"{self._name} is a "
                f"{self._type} type Creature")
