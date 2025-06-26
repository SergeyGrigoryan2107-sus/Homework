#Задание1

'''def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)'''


#задание 2
'''import random

# Функция проверки количества быков и коров
def check_guess(secret_number, guess):
    cows_and_bulls = {'cows': 0, 'bulls': 0}

    # Проверка каждой цифры
    for i in range(len(guess)):
        if secret_number[i] == guess[i]:
            cows_and_bulls['cows'] += 1
        elif guess[i] in secret_number:
            cows_and_bulls['bulls'] += 1

    return cows_and_bulls


# Рекурсивная функция игры
def play_game(attempts=0):
    print("Игра Быки и Коровы")
    secret_number = ''.join(random.sample('0123456789', 4))  # Генерация случайного числа
    attempts += 1

    while True:
        user_input = input("Угадай число (четыре цифры): ")

        # Проверка формата ввода
        if len(user_input) != 4 or not user_input.isdigit():
            print("Неверный формат! Повторите попытку.")
            continue

        result = check_guess(secret_number, user_input)

        print(f"Быкив: {result['bulls']} | Коров: {result['cows']}")

        if result['cows'] == 4:
            print(f"Победа! Вы отгадали число за {attempts} попыток!")
            break
        else:
            attempts += 1
            play_game(attempts)


play_game()'''
#Задание 3
'''N = 8  # Размер доски (можете изменить на 6x6 для тестирования)

# Все допустимые ходы коня
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]


# Проверяет, находится ли клетка внутри доски
def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N


# Фунция для вывода результата
def print_board(board):
    for row in board:
        print(row)


# Рекурсивная функция поиска маршрута
def solve_knight_tour(board, x, y, move_count):
    if move_count >= N * N:
        return True  # Нашли полный маршрут

    for k in range(8):
        next_x = x + dx[k]
        next_y = y + dy[k]

        if is_valid(next_x, next_y) and board[next_x][next_y] == 0:
            board[next_x][next_y] = move_count + 1
            if solve_knight_tour(board, next_x, next_y, move_count + 1):
                return True
            board[next_x][next_y] = 0  # Откатываем изменения (backtrack)

    return False


# Запуск программы
if __name__ == "__main__":
    start_x = int(input("Введите начальную строку (от 0 до {}): ".format(N - 1)))
    start_y = int(input("Введите начальный столбец (от 0 до {}): ".format(N - 1)))

    # Создание пустой доски
    board = [[0] * N for _ in range(N)]
    board[start_x][start_y] = 1  # Ставим коня на стартовую позицию

    if solve_knight_tour(board, start_x, start_y, 1):
        print("\\nРешение найдено:")
        print_board(board)
    else:
        print("Нет возможного маршрута.")'''

#Задание4

'''class FifteenPuzzle:
    def __init__(self):
        self.board = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, None]
        ]
        self.empty_pos = (3, 3)  # Начальная позиция пустого места

    def display(self):
        for row in self.board:
            print(' '.join(str(cell) if cell is not None else '-' for cell in row))
        print()

    def swap(self, pos1, pos2):
        """Меняет местами две ячейки"""
        r1, c1 = pos1
        r2, c2 = pos2
        self.board[r1][c1], self.board[r2][c2] = self.board[r2][c2], self.board[r1][c1]

    def can_move(self, direction):
        """Проверяет возможность движения плитки в заданном направлении"""
        er, ec = self.empty_pos
        if direction == 'up' and er > 0:
            return True
        elif direction == 'down' and er < 3:
            return True
        elif direction == 'left' and ec > 0:
            return True
        elif direction == 'right' and ec < 3:
            return True
        return False

    def move(self, direction):
        """Перемещает плитку в указанном направлении"""
        er, ec = self.empty_pos
        if direction == 'up':
            new_pos = (er - 1, ec)
        elif direction == 'down':
            new_pos = (er + 1, ec)
        elif direction == 'left':
            new_pos = (er, ec - 1)
        elif direction == 'right':
            new_pos = (er, ec + 1)
        self.swap((er, ec), new_pos)
        self.empty_pos = new_pos

    def shuffle(self):
        """Перемешивает плитки случайным образом"""
        import random
        moves = ['up', 'down', 'left', 'right']
        for _ in range(100):
            possible_moves = [m for m in moves if self.can_move(m)]
            if possible_moves:
                self.move(random.choice(possible_moves))

    def is_solved(self):
        """Проверяет условие победы"""
        target_board = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, None]
        ]
        return all([all([self.board[i][j] == target_board[i][j] for j in range(4)]) for i in range(4)])

    def play(self):
        print("Игра Пятнашки\nВы можете двигаться вверх ('w'), вниз ('s'), влево ('a') и вправо ('d').\n")
        self.shuffle()  # Перемешиваем игровое поле
        while True:
            self.display()
            move = input("Ход (w/a/s/d/q для выхода): ").strip().lower()
            if move == 'q':
                print("Вы вышли из игры.")
                break
            if move == 'w' and self.can_move('up'):
                self.move('up')
            elif move == 's' and self.can_move('down'):
                self.move('down')
            elif move == 'a' and self.can_move('left'):
                self.move('left')
            elif move == 'd' and self.can_move('right'):
                self.move('right')
            else:
                print("Невозможно переместить плитку сюда.\n")
            if self.is_solved():
                print("Поздравляю! Вы выиграли!\n")
                break'''