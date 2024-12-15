import time

# Функция для чтения входных данных из файла
def read_input():
    with open('input_loc.txt', 'r') as file:
        # Читаем n, l и k из первой строки
        n, l, k = map(int, file.readline().strip().split())
        # Читаем занятые позиции в виде множества кортежей
        occupied = {tuple(map(int, file.readline().strip().split())) for _ in range(k)}
    return n, l, occupied

# Функция для проверки, находится ли позиция под атакой
def is_under_attack(x, y, occupied):
    # Проверка по горизонтали и вертикали (как ладья)
    for ox, oy in occupied:
        if ox == x or oy == y:
            return True
    
    # Ходы для коня (8 возможных направлений движения)
    knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                    (1, 2), (1, -2), (-1, 2), (-1, -2)]
    
    # Проверка каждой позиции, куда может пойти конь
    for dx, dy in knight_moves:
        if (x + dx, y + dy) in occupied:
            return True
    return False

# Рекурсивная функция для размещения фигур на доске
def place_figures(n, l, occupied, solutions, current_solution):
    if len(current_solution) == l:
        solutions.append(current_solution[:])
        return
    
    # Перебор всех возможных позиций на доске
    for x in range(n):
        for y in range(n):
            # Проверка, не под атакой ли позиция (x, y)
            if not is_under_attack(x, y, occupied.union(current_solution)):
                current_solution.append((x, y))  # Добавляем текущую позицию
                place_figures(n, l, occupied, solutions, current_solution)  # Рекурсивный вызов
                current_solution.pop()  # Удаление последней позиции

            # Оптимизация: если оставшееся количество позиций слишком мало, прерываем
            if len(current_solution) + (n - x) * n - y < l:
                return
            

# Вывод решений в файл
def output_solutions(solutions):
    with open('output.txt', 'w') as file:
        if not solutions:
            file.write('no solutions')  # Если решений нет
        else:
            # Запись каждого решения в файл
            for solution in solutions:
                file.write(' '.join(f'({x},{y})' for x, y in solution) + '\n')

# Функция для отрисовки доски
def draw_board(n, occupied):
    board = [['0' for _ in range(n)] for _ in range(n)]
    for x, y in occupied:
        board[x][y] = '#'
    for row in board:
        print(' '.join(row))

# Главная функция программы
def main():
    start_time = time.time()  # Засекаем время выполнения
    n, l, occupied = read_input()  # Читаем входные данные
    solutions = []
    place_figures(n, l, occupied, solutions, [])  # Размещаем фигуры
    output_solutions(solutions)  # Записываем найденные решения
    end_time = time.time()  # Засекаем время завершения
    draw_board(n, occupied)  # Отрисовка доски
    print(end_time-start_time)  # Вывод времени работы программы

if __name__ == "__main__":
    main()