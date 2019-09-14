import random
list_ten_num = [random.randint(0, 100) for i in range(10)]
print(list_ten_num)
def fun(array_list):
    for i in len(array_list):
        if array_list[i] == max(array_list):
            array_list[0],array_list[i] = max(array_list),array_list[0]
            return

fun(list_ten_num)
print(list_ten_num)
        
for i in range(1, 9):
    for j in range(9):
        if i != j:
            for m in range(9):
                if m != j and m != i:
                    print(“%d%d%d” % (i+j+m))
                    
list_num = (i for i in range(1000, 10000))
