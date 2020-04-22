# -*- coding:utf-8 -*-

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""

import random

class Card:
    def __init__(self, title, numbers=None):
        if numbers == None:
            numbers = [random.randint(0, 50) for i in range(0, 27)]

        self.origin_numbers = [(number, False) for number in numbers] + [None for i in range(0, len(numbers) - 1)]
        random.shuffle(self.origin_numbers)

        self.lines = [self.origin_numbers[0:9],
                      self.origin_numbers[9:17],
                      self.origin_numbers[18:27]]

        self.title = title
    
    @property
    def actual_numbers(self):
        return [number[0] if number else None for number in self.origin_numbers]

    def __str__(self):
        output  = f"{self.title}\n"
        output += " ".join([self.print_number(number) for number in self.origin_numbers[0:9]]) + "\n"
        output += " ".join([self.print_number(number) for number in self.origin_numbers[9:18]]) + "\n"
        output += " ".join([self.print_number(number) for number in self.origin_numbers[18:27]]) + "\n"
        output += "--------------------------\n"

        return output

    def print_number(self, number):
        if number == None:
            return "  "
        elif number[1] == True:
            return "  -"
        elif len(str(number[0])) == 1:
            return f" {number[0]}"
        else:
            return str(number[0])

    def check_number(self, number_to_check):
        index = self.actual_numbers.index(number_to_check)

        if index is not None:
            self.origin_numbers[index][1] = True

            return True

        return False


class Player:
    def __init__(self, card):
        self.card = card

class Game:
    def __init__(self, players):
        self.players = players
        self.current_index = 0
        self.total_moves = 90
        self.numbers = [number for number in range(0, 90)] 
        random.shuffle(self.numbers)
        return

    def make_move(self):
        is_game_in_progress = True
        while is_game_in_progress:
            self.total_moves -= 1
            print(f"Новый бочонок: {self.numbers[self.current_index]} (осталось {self.total_moves})")
            for player in self.players:
                print(player.card)
            
            users_choice = input("Зачеркнуть цифру? (y/n): ")
            if users_choice.lower() == "y":
                self.players[0].card.check_number(self.numbers[self.current_index])
            
            self.current_index += 1
            is_game_in_progress = False


players_card = Card("------ Ваша карточка -----")
computers_card = Card("--- Карточка компьютера ---")

player = Player(players_card)
computer = Player(computers_card)

game = Game([player, computer])

print(players_card)
print(computers_card)