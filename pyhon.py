class Superhero:
    def __init__(self, name, secret_identity, power_level):
        self.name = name
        self._secret_identity = secret_identity  # Protected (encapsulation)
        self.__power_level = power_level         # Private (encapsulation)

    def introduce(self):
        print(f"I am {self.name}! My power level is {self.__get_power()}.")

    def __get_power(self):  # Private method (encapsulation)
        return "MAX" if self.__power_level > 9000 else self.__power_level

    def use_power(self):
        raise NotImplementedError("Subclasses must implement this!")  # Polymorphism

# Inheritance (Polymorphism)
class IronMan(Superhero):
    def __init__(self, secret_identity, power_level, suit_model):
        super().__init__("Iron Man", secret_identity, power_level)
        self.suit_model = suit_model

    def use_power(self):  # Polymorphism (overrides parent)
        print(f"*Flies with {self.suit_model} suit and repulsor blasts*")

class SpiderMan(Superhero):
    def __init__(self, secret_identity, power_level):
        super().__init__("Spider-Man", secret_identity, power_level)

    def use_power(self):  # Polymorphism (overrides parent)
        print("*Thwip!* Swing between buildings with webs!")

# Encapsulation in action
tony = IronMan("Tony Stark", 8500, "Mark XLII")
peter = SpiderMan("Peter Parker", 7000)

tony.introduce()  # Output: "I am Iron Man! My power level is 8500."
tony.use_power()  # Output: "*Flies with Mark XLII suit and repulsor blasts*"

peter.introduce() # Output: "I am Spider-Man! My power level is 7000."
peter.use_power() # Output: "*Thwip!* Swing between buildings with webs!"
