from .animal import Animal

class Panda(Animal):
    def_init_(self, name= "Sally")
    super().__init__(name, species="Panda")

    def sound(self):
        return ""

    def action(self):
        return "sleeps all day"
    