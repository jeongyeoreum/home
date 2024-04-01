import random
from abc import abstractmethod, ABC, ABCMeta
from typing import Type, Set


class Die:
    def __init__(self):
        self.__face = random.randint(1, 6)

    @property
    def face(self):
        return self.__face

    # 페이스가 프라이빗이니까 숨겨진 걸 엑세스가 가능하도록> getter역할

    def roll(self) -> None:
        self.__face = random.randint(1, 6)

    def __str__(self):
        return f'{self.face}'
    # 다이 객체를 프린트 할 때 속성값을 찍기 위해서


class YahtzeeDice:
    def __init__(self):
        self.__dice = [Die() for _ in range(5)]  # n을 안써먹어서 언더바 // 왜 안써먹지?

    @property
    def dice(self):
        return self.__dice

    @property
    def faces(self):
        return [die.face for die in self.__dice]

    def roll_dice(self, target_dice: [int]):
        for n in target_dice:
            self.__dice[n - 1].roll()
            # n이 1이면 [0}번쨰 객체

    def show_faces(self):
        for n, f in enumerate(self.faces):
            print(f'주사위 {n + 1}의 눈 :{f}')

    def get_faces(self):
        face_list = []
        for d in self.dice:
            face_list.append(d.face)
        return face_list

    def count_faces(self, face):
        return self.faces.count(face)

    def sum_faces(self):
        return sum(self.faces)

    @property
    def get_point(self, names):
        print(names.points())

    def __str__(self):
        result = ''
        for n in range(5):
            result += f'주사위 {n + 1}\t'
        result += '\n'

        for f in self.faces:
            result += f'{f:5d}\t'
        result += '\n'

        return result


class Rule(ABC):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def points(self, dice: YahtzeeDice) -> int:
        ...


class Samevalue(Rule):
    def __init__(self, value: int, name: str):
        super().__init__(name)
        self.__value = value

    def points(self, dice: YahtzeeDice) -> int:
        return dice.count_faces(self.__value) * self.__value


class ThreeOfAKind(Rule):
    def points(self, dice: YahtzeeDice) -> int:
        for face in range(1, 7):
            if dice.count_faces(face) >= 3:
                return dice.sum_faces()
        return 0


class FourOfKind(Rule):
    def points(self, dice: YahtzeeDice) -> int:
        for face in range(1, 7):
            if dice.count_faces(face) >= 4:
                return dice.sum_faces()
        return 0


class FullHouse(Rule):
    def points(self, dice: YahtzeeDice) -> int:
        for face in range(1, 7):
            if dice.count_faces(face) == 3:
                if dice.count_faces(face) == 2:
                    return 25
        return 0


class Yahtzee(Rule):
    def points(self, dice: YahtzeeDice) -> int:
        for face in range(1, 7):
            if dice.count_faces(face) == 4:
                return 50
        return 0


class Chance(Rule):
    def points(self, dice: YahtzeeDice) -> int:
        for face in range(1, 7):
            return dice.sum_faces()


class Straight(Rule):
    def is_straight(self, list) -> bool:
        my_list = YahtzeeDice()
        new_list = []
        for f in my_list:
            if f not in new_list:
                new_list.append(f)
                return new_list
            if len(new_list) <= 3:
                return True


class SmallStraight(Straight):
    def points(self, dice: YahtzeeDice) -> int:
        for face in range(1, 7):
            ...


class LargeStraight(Straight):
    def points(self, dice: YahtzeeDice) -> int:
        ...


if __name__ == '__main__':
    rules = [Samevalue(1, 'Aces'),
             Samevalue(2, 'Twos'),
             Samevalue(3, 'Threes'),
             Samevalue(4, 'Fours'),
             Samevalue(5, 'Fives'),
             Samevalue(6, 'Sixs'),
             ThreeOfAKind('Three of a kind'),
             FourOfKind('Four Of Kind'),
             FullHouse('FullHouse'),
             SmallStraight('SmallStraight'),
             LargeStraight('LargeStraight'),
             Chance('Chance'),
             Yahtzee('Yahtzee')
             ]
    b = YahtzeeDice()

    target_dice = list(range(1, 6))  # 1에서 5까지 5개의 다이스리스트 생성.타겟 다이스다

    b.roll_dice(target_dice)
    print(b)
    print(b.sum_faces())

    for n in range(1, 7):
        print(f'눈{n}의 수: {b.count_faces(n)}')
    b.show_faces()

    for die in b.dice:
        print(die)
    b_dice = b.get_faces()
    print(b_dice)

    for rule in rules:
        print(rule.points(b), f'{rule.name}')

    Straight.is_straight(b)
