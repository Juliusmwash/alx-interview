def pascal_func(n):
    main_array = []
    first_array = []
    sec_array = []

    for i in range(0, n):
        array_len = len(first_array)
        for j in range(0, array_len):
            if j == 0:
                sec_array.append(1)
            else:
                tmp_num = first_array[j] + first_array[j - 1]
                sec_array.append(tmp_num)
        sec_array.append(1)
        first_array = sec_array.copy()
        main_array.append(sec_array)
        sec_array = []
    
    for list in main_array:
        print(str(list))


pascal_func(2)

