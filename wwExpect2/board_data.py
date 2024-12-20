import session_data
from collections import defaultdict
from roles import *

class Board:
    def __init__(self, fase, cs, player_list):
        self.fase = fase
        self.cs = cs
        self.player_list = player_list
        self.co_group_dict = defaultdict(list)

        # player_list をループして分類
        for player in player_list:
            if isinstance(player.co, Latent):  # Latentの場合
                self.latent_group_
                self.co_group_dict[player.co].append(player)

        

class Player:
    def __init__(self, index, name=None, alive=True, co=Latent()):
        self.index = index
        self.name = name or "player." + str(index)
        self.alive = alive
        self.co = co
        self.ability_result = {}  # role:result あとで実装
        
        #ここまでがユーザーの入力や前回のボードから引き継ぐ情報
        #以降のパーセンテージは別の関数で後から追加する

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
    
    #     self.setup_ability_result()

    # def setup_ability_result():
    #     pass    #後で実装
