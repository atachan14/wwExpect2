import session_data
from collections import defaultdict
from roles import *


class Board:
    def __init__(self, fase, cs, os, player_list):
        self.fase = fase
        self.cs = cs
        self.os = os
        self.player_list = player_list

        self.co_group_dict = {}
        self.latent_group

        # setup_co_group
        self.co_list_dict = defaultdict(list)
        for player in player_list:
            self.co_list_dict[player.co].append(player)

        for co in self.co_list_dict:
            if not isinstance(co, Latent):
                self.co_group_dict[co] = CoGroup(
                    self, co, self.co_list_dict[co])

        for co in self.co_list_dict:
            if isinstance(co, Latent):
                self.latent_group = LatentGroup(
                    self, co, self.co_list_dict[co])


class CoGroup:
    def __init__(self, b, co, player_list):
        self.co = co
        self.player_list = player_list

        self.size = b.cs.role_regulation[co]
        self.vacate = self.size - len(player_list)


class LatentGroup(CoGroup):
    def __init__(self, b, co, player_list):
        super().__init__(co, player_list)


class Player:
    def __init__(self, index, name=None, alive=True, co=Latent()):
        self.index = index
        self.name = name or "player." + str(index)
        self.alive = alive
        self.co = co
        self.ability_result = {}  # role:result あとで実装

        # ここまでがユーザーの入力や前回のボードから引き継ぐ情報
        # 以降のパーセンテージは別の関数で後から追加する

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    #     self.setup_ability_result()

    # def setup_ability_result():
    #     pass    #後で実装
