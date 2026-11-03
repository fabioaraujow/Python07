from abc import ABC, abstractmethod


class TransformCapability(ABC):
    _transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        ...

    @abstractmethod
    def revert(self) -> str:
        ...
