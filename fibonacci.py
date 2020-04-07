#!/usr/bin/python3

def fibonacci(count):
    first = 1
    second = 1
    result_list = []
    
    result_list.append(first)
    result_list.append(second)
    counter = 0
    while count > counter + 2:
        result = first + second
        result_list.append(result)
        first = second
        second = result
        counter = counter + 1
#        if count < counter + 3:
#            break
    print(result_list)
        
fibonacci(10)

