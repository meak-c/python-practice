def next_valid_number(n):
    answer_num = n + 1
    while True:
        test = False
        check_num = str(answer_num)
        for i in range(len(check_num)):
            for j in range(i + 1, len(check_num)):
                if check_num[i] == check_num[j]:
                    test = True
                    
        if answer_num % 3 != 0 and answer_num % 5 != 0 and not test: 
            return answer_num
        
        answer_num += 1
        
print(next_valid_number(189))