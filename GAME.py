from typing import Tuple
from random import random

me = {
    'health': 100,
    'shield': 10,
    'strength': 5,
    'arm': 'magnum'
}

arms = {
    'pistol': 3,
    'magnum': 5,
    'rocket': 10,
    'laser': 25,
}

# enemies = [enemy1: dict, ...]
enemy = {
    'name': '적(외계인)',
    'health': 150,
    'arm': 'pistol'
}


def show_enemy_info(enemy: dict) -> None:
    print('--------')
    print('{} 등장했다'.format(enemy['name']))
    print('{}\'의 체력: {}'.format(enemy['name'], enemy['health']))
    print('-------------------------------')


def attack(me: dict, enemy: dict) -> None:
    damage = me['strength'] + (arms[me['arm']] * round(random()))
    print('공격!! {} 데미지'.format(damage))
    enemy['health'] -= damage
    print('{}\'의 체력: {}'.format(
        enemy['name'],
        enemy['health'] >= 0 and enemy['health'] or 0
    ))
    enemy_hit_me(me, enemy)


def enemy_hit_me(me: dict, enemy: dict) -> None:
    damage = arms[enemy['arm']] * round(random())
    print('{}\'의 공격!! {} 데미지'.format(enemy['name'], damage))
    me['health'] -= damage
    print('나의 체력: {}'.format(
        me['health'] >= 0 and me['health'] or 0
    ))


def end() -> None:
    print('--------')
    print('~게임끝~')


def lose() -> None:
    print('--------')
    print('졌습니다.')


if __name__ == '__main__':
    print('갤러그게임 시작')
    show_enemy_info(enemy)
    while enemy['health'] > 0:
        print('1. 공격\n2. 오른쪽 이동\n3. 왼쪽 이동')
        your_choice = int(input('>>> '))
        if your_choice == 1:
            attack(me, enemy)
        elif your_choice == 2:
            print('오르쪽 이동')
        elif your_choice == 3:
            print('왼쪽 이동')

        if me['health'] <= 0:
            lose()
            break
    end()