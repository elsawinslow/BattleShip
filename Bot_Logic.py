class Bot_Logic:
    __first_bot_hit: []
    __last_bot_hit: []
    __bot_dir: str
    __bot_turn_counter: bool
    __turn_around_counter: int

    def __init__(self):
        self.__bot_dir = ""
        self.__bot_turn_counter = False
        self.__turn_around_count = 0

    def set_first_bot_hit(self,coord):
        self.__first_bot_hit = coord
    
    def get_first_bot_hit(self):
        return self.__first_bot_hit

        
    def set_last_bot_hit(self,coord):
        self.__last_bot_hit = coord
    
    def get_last_bot_hit(self):
        return self.__last_bot_hit


    def set_bot_dir(self,dir):
        self.__bot_dir = dir
    
    def get_bot_dir(self):
        return self.__bot_dir


    def set_bot_turn_counter(self,bot_turn_counter):
        self.__bot_turn_counter = bot_turn_counter
    
    def get_bot_turn_counter(self):
        return self.__bot_turn_counter    


    def set_turn_around_count(self,num):
        self.__turn_around_count = num

    def get_turn_around_count(self):
        return self.__turn_around_count   


    def reset(self):
        self.__first_bot_hit = []
        self.__last_bot_hit = []
        self.__bot_dir = ""
        self.__bot_turn_counter = 0
        self.__turn_around_count = 0