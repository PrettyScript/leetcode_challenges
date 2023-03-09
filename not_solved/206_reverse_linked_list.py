def reverseList(head: list) -> list:
    # reversed_list = [i for i in reversed(head)]
    # return reversed_list
    reversed_list = [i for i in head[::-1]]
    # for i in head[::-1]:
    #     reversed_list.append(i)
    return reversed_list
    

print(reverseList([1,2,3,4,5]))
