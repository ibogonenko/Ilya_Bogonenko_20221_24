def get_pins(observed_pin):
    # Словарь возможных соседей для каждой цифры
    neighbor_num = {
        '0': ['0', '8'],
        '1': ['1', '2', '4'],
        '2': ['2', '1', '3', '5'],
        '3': ['3', '2', '6'],
        '4': ['4', '1', '5', '7'],
        '5': ['5', '2', '4', '6', '8'],
        '6': ['6', '3', '5', '9'],
        '7': ['7', '4', '8'],
        '8': ['8', '5', '7', '9', '0'],
        '9': ['9', '6', '8']
    }
    
    combinations = ['']
    
    # Перебор каждой цифры в наблюдаемом коде
    for digit in observed_pin:
        current_neighbors = neighbor_num[digit]
        # Создаем новые комбинации, добавляя соседние цифры
        combinations = [prefix + neighbor for prefix in combinations for neighbor in current_neighbors]
        


    return combinations
def main():
    print(get_pins("8"))  # Вывод: ['5','7','8','9','0']
    print(get_pins("11")) # Вывод: ["11", "22", "44", "12", "21", "14", "41", "24", "42"]
    print(get_pins("549"))
    print(get_pins("000"))

if __name__ =="__main__":
    main()