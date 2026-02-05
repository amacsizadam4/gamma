"""Write a program in Python that calculates how many numbers bigger 
than 0 and smaller than 1000 are there both prime and Fibonacci numbers."""



def is_prime_and_fibonacci():
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_fibonacci(n):
        a, b = 0, 1
        while a < n:
            a, b = b, a + b
        return a == n

    count = 0
    for num in range(1, 1000):
        if is_prime(num) and is_fibonacci(num):
            count += 1

    return count

result = is_prime_and_fibonacci()
print(f"Count of numbers that are both prime and Fibonacci between 0 and 1000: {result}")
