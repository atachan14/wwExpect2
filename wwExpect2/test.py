from roles import *

class RegulationInput:
    role_regulation={"市民":4,"狼":1}
    strategy_option={
        "cant_vills_deceive":True,
        "admit_no_opposition_is_true":True
    }

class CastSetting:
    name_to_class_dict = {
        "潜伏": Latent,
        "市民": Villager,
        "占": Seer,
        "霊": Medium,
        "狩": Hunter,
        "狼": NormalWolf,
        "狂": Madman
    }

    def __init__(self, parameter):
        self.role_regulation = {}
        for role_name, count in parameter.role_regulation.items():
            role = self.name_to_class_dict.get(role_name)
            if role is None:
                raise ValueError(f"'{role_name}'取得失敗。name_to_class_dictの参照が間違ってるかも。")
            if not issubclass(role, Role):
                raise ValueError(f"'{role_name}'を取得したけどRoleじゃない。")
            self.role_regulation[role]=count

        self.can_co_list = [role for role in self.role_regulation.keys()]
        self.player_size = sum(self.role_regulation.values())

ri = RegulationInput
cs = CastSetting(ri)
print([role.name for role in cs.can_co_list])
print(cs.player_size)