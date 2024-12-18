from math import ceil
def main():
    #n = int(input('amount of banks: '))
    n = 5
    banks_info = []
    banks_info.append(input('names of banks: ').split()) # ввод названий банков
    banks_info.append(input('sum of money: ').split()) # ввод сумм денег банков
    for i in range(n): # преобразование к необходимому виду [[bank, sum], [bank, sum], ...]
        banks_info.append([banks_info[0][i]])
        banks_info[i+2].append(banks_info[1][i])
    del banks_info[0] #удаление первичных списков
    del banks_info[0]
    for i in range(n): # добавление индексов
        banks_info[i].insert(1,i)
        banks_info[i][2] = int(banks_info[i][2])
        banks_info[i] = tuple(banks_info[i])
    #print(*banks_info)
    robbery_sum = 0
    robbed_banks = [[],[]]
    robbed_banks_temp = [[], []]
    temp = 0
    #banks_info = [('sber', 0, 1), ('ZXC', 1, 6), ('spb', 2, 8), ('tink', 3, 3), ('poch', 4, 1)]
    for k in range(0, int(ceil(n/2))): # изменение выбора 1-го банка
        for j in range(2, n): # изменение шага
            for i in range(k, n, j): # суммирование комбинации банков и записывание выбранных
                temp += banks_info[i][2]
                robbed_banks_temp[0].append(banks_info[i][0])
                robbed_banks_temp[1].append(banks_info[i][1])
            if temp > robbery_sum:
                robbed_banks = robbed_banks_temp.copy()
                robbery_sum = temp
                temp = 0
                robbed_banks_temp = [[], []]
            else:
                temp = 0
                robbed_banks_temp = [[], []]
    robbed_banks[0] = tuple(robbed_banks[0])
    robbed_banks[1] = tuple(robbed_banks[1])
    print('max sum:', robbery_sum)
    print('robbed banks and their index: ', *robbed_banks)
if __name__ == "__main__":
    main()