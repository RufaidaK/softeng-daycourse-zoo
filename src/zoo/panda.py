from .animal import Animal

class Panda(Animal):
    def __init__(self, name= "Sally"):
      super().__init__(name, species="Panda")

    def sound(self):
        return "Hellooo"

    def action(self):
        return "sleeps all day"

    def test_panda():
        assert self.name() == "Sally"
        assert self.species() == "Panda"
        assert self.sound() == "Hellooo"
        assert self.action() == "sleeps all day"