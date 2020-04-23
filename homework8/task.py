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
    def __init__(self, title):
        self.unique_numbers = []
        line_1 = sorted([(self.make_unique(), False) for no_matter in range(0, 5)])
        line_2 = sorted([(self.make_unique(), False) for no_matter in range(0, 5)])
        line_3 = sorted([(self.make_unique(), False) for no_matter in range(0, 5)])

        for i in range(0, 4):
            line_1.insert(random.choice(range(0, len(line_1))), None)
            line_2.insert(random.choice(range(0, len(line_2))), None)
            line_3.insert(random.choice(range(0, len(line_3))), None)

        self.lines = [line_1, line_2, line_3]
        self.title = title

    def __str__(self):
        output  = f"{self.title}\n"
        output += " ".join([self.print_number(number) for number in self.lines[0]]) + "\n"
        output += " ".join([self.print_number(number) for number in self.lines[1]]) + "\n"
        output += " ".join([self.print_number(number) for number in self.lines[2]]) + "\n"
        output += "--------------------------\n"

        return output
    
    def make_unique(self):
        not_unique = True
        while not_unique:
            new_number = random.randint(0, 90)
            if new_number not in self.unique_numbers:
                self.unique_numbers.append(new_number)
                not_unique = False
                return new_number
            else: continue

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
        if number_to_check in self.unique_numbers:
            for line_idx, line in enumerate(self.lines):
                for num_idx, number in enumerate(line):
                    if number == number_to_check:
                        self.lines[line_idx][num_idx][1] = True
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

    def run(self):
        game_over = False
        while not game_over:
            self.total_moves -= 1
            print(f"Новый бочонок: {self.numbers[self.current_index]} (осталось {self.total_moves})")
            for player in self.players:
                print(player.card)
            
            users_choice = input("Зачеркнуть цифру? (y/n): ")
            if users_choice.lower() == "y":
                result = self.players[0].card.check_number(self.numbers[self.current_index])
                
                if not result:
                    print("Вы проиграли")
            else:
                result = self.players[0].card.origin_numbers
            
            self.current_index += 1
            game_over = True


players_card = Card("------ Ваша карточка -----")
computers_card = Card("--- Карточка компьютера ---")

player = Player(players_card)
computer = Player(computers_card)

game = Game([player, computer])

game.run()