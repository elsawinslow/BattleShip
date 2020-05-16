
class Ship:
    __length: int
    __num_hit: int
    __coord: []

    def __init__(self, coord):
        self.__coord = coord
        self.__num_hit = 0
        self.__length = len(coord)

    def hit(self):
        self.__num_hit += 1

    def check_sunk(self):
        if self.__length == self.__num_hit:
            return True
        else:
            return False    

    def get_coords(self):
        return self.__coord

   
