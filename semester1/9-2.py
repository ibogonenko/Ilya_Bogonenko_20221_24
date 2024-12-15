def roman_number(str_entered):
    #print(str_entered)

    str_entered += '  ' #изменение строки для избежания ошибок при вызове str_entered[i:i+2]
    result = 0
    i = 0
    rome_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IX': 9, 'IV': 4, 'XL': 40, 'XC': 90, 'CD': 400,'CM': 900} #словарь числа + особые сочетания
    while i < len(str_entered)-2: #итерация по строке
        if str_entered[i:i+2] in rome_num: #проверка на наличие одной из 6 комбинаций с вычитанием в даннам месте римского числа
            result += rome_num[str_entered[i:i+2]]
            i += 1
        elif str_entered[i] in rome_num:
            result += rome_num[str_entered[i]]
        i+=1
    return print(result)

def main():
    roman_number("MMMCMXCIX")

if __name__ =="__main__":
    main()