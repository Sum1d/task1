def fib(high):
    fib1, fib2 = 0, 1
    summa = 0
    while fib2 <= high:
        fib1, fib2 = fib2, fib1+fib2
        if fib1 % 2 == 0:
            summa += fib1
    print(summa)


if __name__ == "__main__":
    fib(4000000)
