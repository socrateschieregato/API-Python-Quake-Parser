import os
import pytest

from quake.views import parse_game_kills, parse_kill_line


class TestTask1:
    """
    Run tests on quake parser
    """

    @pytest.fixture
    def task1_logfile(self):
        logfile = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'fixture',
            'games.log')
        return logfile

    def test_parse_game_kills(self, task1_logfile):
        parsed_dict = dict(parse_game_kills(task1_logfile))
        assert parsed_dict == {
            'game_1': {
                'total_kills': 0,
                'players': [],
                'kills': {}
            },
            'game_2': {
                'total_kills': 11,
                'players': ['Isgalamido', 'Mocinha'],
                'kills': {
                    'Isgalamido': -5
                }
            }
        }

    def test_parse_kill_line(self):
        game_match = {
            "total_kills": 0,
            "players": [],
            "kills": {}
        }
        line = ("20:54 Kill: 1022 2 22: <world> killed Isgalamido "
                "by MOD_TRIGGER_HURT")
        parse_kill_line(line, game_match)

        assert game_match == {
            'players': ['Isgalamido'],
            'total_kills': 1,
            'kills': {'Isgalamido': -1},
        }

        line = ("22:06 Kill: 2 3 7: Isgalamido killed Mocinha by "
                "MOD_ROCKET_SPLASH")
        parse_kill_line(line, game_match)

        assert game_match == {
            'players': ['Isgalamido', 'Mocinha'],
            'total_kills': 2,
            'kills': {'Isgalamido': 0},
        }
