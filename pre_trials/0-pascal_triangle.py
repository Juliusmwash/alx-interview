main_list = []
array_first = []
array_sec = []
n = 10

for i in range(0, n):
    tmp_length = len(array_first)

    for j in range(0, tmp_length):
        if j == 0:
            array_sec.append(1)
        else:
            tmp_num = array_first[j] + array_first[j - 1]
            array_sec.append(tmp_num)
    array_sec.append(1)
    array_first = array_sec.copy()
    main_list.append(array_sec)
    array_sec = []

for list in main_list:
    print(str(list))


