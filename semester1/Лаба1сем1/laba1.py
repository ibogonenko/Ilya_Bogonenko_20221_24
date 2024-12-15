def find_expression(numbers, target, index=0, current_rez=0, expression="", is_first=True):
    # Рекурсивная функция для поиска выражения с использованием + и - для достижения целевого значения. Возвращает: Строку с выражением, если решение найдено; иначе None.
    # Параметры:
    # numbers - список чисел для формирования выражения
    # target - целевое значение, которое должно быть равно текущей сумме/разности в выражении
    # index - текущее обрабатываемое число из списка, по умолчанию = 0
    # current_rez - результат выражения на текущий момент, по умолчанию = 0
    # expression - строка, представляющая текущее выражение, по умолчанию = ""
    # is_first - указывает, первое ли число из списка обрабатывается, по умолчанию = True
    if index == len(numbers): # Проверка на достижение конца списка, возвращает выражение, если оно приводит к необходимому числу
        if current_rez == target:
            return expression 
        return None




    # Обработка первого числа без постановки перед ним знака
    if is_first:
        next_expr_plus = f"{numbers[index]}" if expression == "" else f"{expression}+{numbers[index]}"
        result_plus = find_expression(numbers, target, index + 1, current_rez + numbers[index], next_expr_plus, False)
        
        if result_plus is not None: # Если найдено решение с +, возвращаем его
            return result_plus



    # Если это не первое число, обрабатываем варианты с постановкой "+" и "-"
    else:
        # Вариант с "+"
        next_expr_plus = f"{expression}+{numbers[index]}"
        result_plus = find_expression(numbers, target, index + 1, current_rez + numbers[index], next_expr_plus, False)

        if result_plus is not None: # Если найдено решение с "+", возвращаем его
            return result_plus

        # Вариант с "-"
        next_expr_minus = f"{expression}-{numbers[index]}"
        result_minus = find_expression(numbers, target, index + 1, current_rez - numbers[index], next_expr_minus, False)

        if result_minus is not None: # Если найдено решение с "-", возвращаем его
            return result_minus

    return None # Возврат None при отсутствии решений




def main():
    # Основная функция программы, считывает данные из файла, проверяет их и вызывает find_expression для поиска выражения, если выражение найдено - выводит его, если не найдено - выводит об этом сообщение
    try:
        with open("input.txt", "r") as file:
            data = list(map(int, file.read().strip().split())) # Преобразование данных из файла в целые числа
        

        N = data[0]           # Количество чисел
        numbers = data[1:N+1] # Список чисел
        S = data[N+1]         # Предполагаемый результат

        # Проверка ограничений на входные данные
        if not(2 < N < 30):
            raise ValueError("N должно быть в диапазоне [2, 30]")
        if not all(0 <= x < 5 * 10**7 for x in numbers):
            raise ValueError("Числа должны быть в диапазоне [0, 5*10^7]")
        if not (-10**9 < S < 10**9):
            raise ValueError("S должно быть в диапазоне [-10^9, 10^9]")
        
        # Вызов функции
        result = find_expression(numbers, S)

        if result is not None: # Проверка наличия решения и последующая запись в файл
            result += f'={data[N+1]}'
            with open("output.txt", "w") as file:
                file.write(result) 
        else:
            result = "No solution"
            with open("output.txt", "w") as file:
                file.write(result)
    except Exception as e: # Обработка ошибок
        print(f'ошибка: {e}')


if __name__ =="__main__":
    main()