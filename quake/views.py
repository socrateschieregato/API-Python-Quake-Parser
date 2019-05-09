import re
from collections import OrderedDict
from django.http import JsonResponse


# regex para iniciar o game
start_regex = re.compile(r".*InitGame:.*")

# regex sempre que houver Kill
kill_regex = re.compile(r".*Kill:.*:(.*).*killed(.*)by(.*)")

#diretório do arquivo de log
source = './quake/games.log'

def parse_game_kills(source):
    """Get logfile and parse results into OrderedDict"""
    game_match_count = 1
    key_map = "game_{}"
    parsed_game_matches = OrderedDict()
    with open(source, "r", encoding="utf-8") as fp:
        for line in fp.readlines():
            if start_regex.match(line):
                key = key_map.format(game_match_count)
                parsed_game_matches[key] = {
                    "total_kills": 0,
                    "players": [],
                    "kills": {},
                }
                game_match_count += 1

            if kill_regex.match(line):
                parse_kill_line(line, parsed_game_matches[key])
    
    return parsed_game_matches


def parse_kill_line(line, game_match):
    """Specific parse to kill line"""
    m = kill_regex.match(line)
    player_alive = m.group(1).strip()
    player_dead = m.group(2).strip()
    weapon = m.group(3).strip()[4:].title()

    game_match["total_kills"] += 1
    if (player_alive != "<world>" and player_alive
            not in game_match["players"]):
        game_match["players"].append(player_alive)
        game_match["kills"][player_alive] = 0

    if player_dead not in game_match["players"]:
        game_match["players"].append(player_dead)

    if player_alive != "<world>":
        if player_alive in game_match["kills"].keys():
            game_match["kills"][player_alive] += 1
            print('O ' + player_alive + ' matou o ' + player_dead + ' usando a arma ' + weapon)
        else:
            game_match["kills"][player_alive] = 1
    else:
        if player_dead in game_match["kills"].keys():
            game_match["kills"][player_dead] -= 1
        else:
            game_match["kills"][player_dead] = -1
        print('O ' + player_dead + ' morreu pois estava ferido e caiu de uma altura que o matou')

def games(request):
    response_data = {}
    response_data['result'] = parse_game_kills(source)

    return JsonResponse(response_data)

def game(request, id):
    response_data = {}
    response_data['result'] = parse_game_kills(source)['game_' + str(id)]

    return JsonResponse(response_data)

