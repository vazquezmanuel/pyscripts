# Recursive
def fibonacci(num):
    if num <= 1:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)

# NOT recursive
def fibonacci_nrec(num):
    num1 = 1 
    num2 = 1 
    num3 = 0
    if num == 0 or num == 1:
        return 1
    else:
        for i in range(num - 1):
            num3 = num1 + num2
            num1 = num2
            num2 = num3
        return num3

def main():
    for f in range(8): print(fibonacci_nrec(f), fibonacci(f))

if __name__ == "__main__":
    main()
