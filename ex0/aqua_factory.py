from .factory import CreatureFactory
from .aquabub import Aquabub
from .torragon import Torragon


class AquaFactory(CreatureFactory):
    def create_base(self) -> Aquabub:
        return Aquabub()

    def create_evolved(self) -> Torragon:
        return Torragon()
