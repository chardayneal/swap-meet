from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id=None, fabric="Unknown",condition=0):
        super().__init__(id,condition)
        self.fabric = fabric
        # if not id:
        #     super().__init__()
        # else:
        #     self.id = id

    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."

# clothing1 = Clothing(condition=3.5)
# print(clothing1.condition_description())
# print(clothing1.condition_description())