class Room:
    def __init__(self, coord, exits):
        self.coord = coord
        self.exits = exits

    def __str__(self):
        str = f"You are in room at location {self.coord}.\nExits are "
        for i, e in enumerate(self.exits):
            if e[0] > self.coord[0]:
                str = str + "east"
            elif e[0] < self.coord[0]:
                str = str + "west"
            elif e[1] > self.coord[1]:
                str = str + "south"
            else:
                str = str + "north"
            if len(self.exits)-1 > i:
                str = str+", "
        return str


room = Room(coord=(0, 0), exits=((0, 1), (1, 0)))
print(room)
