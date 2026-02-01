def fibonacci(n):
    first = 1
    second = 1
    list = []
    for x in range(n):
        if first%2==0:
            list.append(first)
            print(list)
        print(first)
        third = first
        first = first + second
        second = third
    return first
    
    
print(fibonacci(10))
