from roles import *


class CastSetting:
    role_map = {
        "市民": Villager,
        "占": Seer,
        "霊": Medium,
        "狩": Hunter,
        "狼": Wolf,
        "狂": Madman
    }

    def __init__(self, parameter):
        for role_name, count in parameter.role_regulation.items():
            role_class = self.role_map.get(role_name)
            self.role_regulation = {role_class: count}


class OptionSetting:
    def __init__(self):
        strategy_option = {"cant_vills_deceive": True,
                           "no_opponent_is_true": True}
        vills_team_option = {"select_max_execution": True}
        wolfs_team_option = {"select_max_bite": True,
                             "can_self_bite": True}


class Board:
    def __init__(self, rs):
        player_list = [Player(rs) * range(rs.role_regulation)]
        # player

class Player:
    def __init__(self, rs):
        alive = True
        can_co_list = [role for role in CastSetting.keys]
