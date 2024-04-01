from typing import Type, Any, Set, Iterable
from abc import ABC, abstractmethod
import random




'''
class YahtzeeGame:
    def __init__(self):
        self.score_board = []
        self.y_dice = YahtzeeDice()

    def play_game(self):
        pass

    def announce_winner(self):
        pass



class Rule(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def points(self, YahtzeeDice) -> int:
        pass


class SameValue(Rule):
    def __init__(self, value: int):
        self.value = value

    def points(self) -> int:
        pass

    '''

class ThreeOFAKind(Rule):
class FourOFKind(Rule):
class FullOFKind(Rule):
class Yathzee(Rule):
class Chance(Rule):
'''
class ScoreBoard:
    def __init__(self, player: str):
        self.player = player
        self.rules = [Rule]
        self.score_borad = [int]

    def get_rules(self):
        return Rule()

    def assign_points(self, Rule, YathzeeDice):
        pass

    def total_points(self):
        return [int]

    def show_board(self, YahtzeeDice):
        pass

'''
if __name__ == '__main__':
    dies = YahtzeeDice([1,2,3,4,5])
    dies.roll_dices()
    dies.show_faces()
    dies.get_faces()
    dies.count_faces()
    dies.sum_faces()
