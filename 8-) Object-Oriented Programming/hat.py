import random


class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Revenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")
