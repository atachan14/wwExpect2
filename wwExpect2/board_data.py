import session_data
import roles

class Board:
    def __init__(self, fase,cs,player_list):
        self.fase = fase
        self.cs=cs
        self.player_list = player_list
        self.co_group_dict = {}
     
class Player:
    def __init__(self, index,co):
        self.index=index
        self.name="player."+ str(index)
        self.co = co

        self.alive = True
        self.ability_result = {} #role:result

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
    #     self.setup_ability_result()

    # def setup_ability_result():
    #     pass    #後で実装
