from itertools import combinations
def subsets_count(list1):
    working_list = []
    for i in range(len(list1)):
        working_list += combinations(list1, i+1)
    working_set = set(working_list)
    subsets = {frozenset(i) for i in working_set}
    subsets = sorted(subsets)
    return [subsets, len(subsets)]
def main():
    list1, list2 = [1,2,3,4], ['a','b','c','d','d']
    #print(*subsets_count(list1))
    print(*subsets_count(list2))

if __name__ == "__main__":
    main()