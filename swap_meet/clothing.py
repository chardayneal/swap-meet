from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id=None, fabric="Unknown",condition=0,age=0):
        super().__init__(id,condition)
        self.fabric = fabric
        self.age = age

    def __str__(self):
        return f"{super().__str__()} It is made from {self.fabric} fabric."
