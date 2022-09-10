class Inventory:
    max_capacity = 5
    items = []

    def __init__(self):
        self.max_capacity = 5
        self.items = ["pocket lint"]

    def list_inventory(self):
        res = []
        for item in self.items:
            res.append(item)
        return res

    def print_inventory(self):
        print("You are carrying")
        print(", ".join(self.items))

    def add_item(self, item):
        self.items.append(item)
