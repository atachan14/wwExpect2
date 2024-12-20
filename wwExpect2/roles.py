class Role:
    pass

class VillsTeam:
    team = "村陣営"

class WolfsTeam:
    team = "狼陣営"

class FoxTeam:
    team="狐陣営"

class Human:
    seer_result = "white"

class Wolf:
    seer_result = "black"

class Fox:
    seer_result = "white"
    #呪殺の処理

class Latent(Role):
    name = "潜伏"
    calc_priority=0
    # def __init__(majority_team):
    #     team = majority_team

class Villager(Role,VillsTeam,Human):
    name = "市民"
    calc_priority=1


class Seer(Role,VillsTeam,Human):
    name = "占"
    calc_priority=3
    
class Medium(Role,VillsTeam,Human):
    name = "霊"
    calc_priority=2

    
class Hunter(Role,VillsTeam,Human):
    name = "狩"
    calc_priority=1

class NormalWolf(Role,WolfsTeam,Wolf):
    name = "狼"

class Madman(Role,WolfsTeam,Human):
    name = "狂人"