def biggest(a: int, b: int) -> str:
    if a > b:
        return f"{a} is bigger than {b}"
    if b > a:
        return f"{b} is bigger than {a}"
    return f"{a} and {b} are equal"


def main():
    try:
        a = int(input("Enter first integer: "))
        b = int(input("Enter second integer: "))
    except ValueError:
        print("Error: inputs must be integers.")
        return

    print(biggest(a, b))


main()
