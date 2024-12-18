def my_func(list1, list2):
    working_set1 = set(list1)
    working_set2 = set(list2)
    ans1 = len(working_set1.intersection(working_set2)) 
    ans2 = len(working_set1.symmetric_difference(working_set2))
    ans3 = len(working_set1.difference(working_set2))
    ans4 = len(working_set2.difference(working_set1))
    return [ans1, ans2, ans3, ans4]
if __name__ == "__main__":
    list1, list2 = [0, 33, 37, 6, 10, 44, 13, 47, 16, 18, 22, 25], [1, 38, 48, 8, 41, 7, 12, 47, 16, 40, 20, 23, 25]
    print(*my_func(list1, list2)) # вывод результата
    