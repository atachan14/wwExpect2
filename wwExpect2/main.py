from roles import *
from board_data import *
import input_data
import session_data


ri = input_data.RegulationInput
cs = session_data.CastSetting(ri)

first_player_list=[]
for i in range(cs.player_size):
    first_player_list.append(Player(i+1,Latent))

#debug
# for player in first_player_list:
#     print(player.index,player.co.name)

first_board=Board(1.0,cs,first_player_list)
#debug
# print(first_board.player_list)


