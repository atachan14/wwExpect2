from roles import *
from board_data import *
import input_data
import session_data


#初回のみの処理____
ri = input_data.RegulationInput
cs = session_data.CastSetting(ri)
os = session_data.OptionSetting(ri)

first_player_list = []
for i in range(cs.player_size):
    first_player_list.append(Player(i + 1, Latent))

first_board = Board(1.0, cs, os,first_player_list)
# debug
# print(first_board.player_list)

#____ブラウザに送信して終わり

#2回目以降の処理
