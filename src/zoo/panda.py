from .animal import Animal

class Panda(Animal):
    def __init__(self, name= "Sally"):
      super().__init__(name, species="Panda")

    def sound(self):
        return "Hellooo"

    def action(self):
        return "sleeps all day"

def test_Panda():
    s = Panda("Sally")
    assert s.name == "Sally"
    assert s.species == "Panda"
    assert s.sound() == "Hellooo"
    assert s.action() == "sleeps all day"