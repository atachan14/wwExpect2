class Role:
    pass

class VillsTeam(Role):
    team = "村陣営"

class WolfsTeam(Role):
    team = "狼陣営"

class Human:
    seer_result = "white"

class Wolf:
    seer_result = "black"


class Villager(VillsTeam,Human):
    name = "市民"

class Seer(VillsTeam,Human):
    name = "占"
    
class Medium(VillsTeam,Human):
    name = "霊"
    
class Hunter(VillsTeam,Human):
    name = "狩"

class NormalWolf(WolfsTeam,Wolf):
    name = "狼"

class Madman(WolfsTeam,Human):
    name = "狂人"