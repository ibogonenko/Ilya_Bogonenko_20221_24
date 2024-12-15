from math import factorial

def comb_number(Candies, Packages):
    
    summ = 0
    for i in range(Packages + 1):
        summ += (-1) ** (Packages - i) * factorial(Packages) // (factorial(i) * factorial(Packages - i)) * (i ** Candies)
    combinations = summ // factorial(Packages)

    if Packages > Candies:
        combinations = 'No solutions'
    if Packages == Candies:
        combinations = 1

    return combinations


def main():
    print(comb_number(4, 3))
    print(comb_number(3, 2))
    print(comb_number(4, 7))
    print(comb_number(6, 6))
    print(comb_number(15, 9))

if __name__ =="__main__":
    main()