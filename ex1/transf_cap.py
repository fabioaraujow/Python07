from abc import ABC, abstractmethod


class TransformCapability(ABC):
    transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        ...

    @abstractmethod
    def revert(self) -> str:
        ...
