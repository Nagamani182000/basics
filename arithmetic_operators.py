def arithmetic_ope(a, b):
    sum = a + b
    sub = a - b
    mul = a * b
    div = a // b
    mod = a % b
    print(f"The sum of two number:{sum}")
    print(f"The subtraction of two number:{sub}")
    print(f"The multiplication of two number:{mul}")
    print(f"The division of two number:{div}\nThe modulo of two number:{mod}") 
n = int(input("Enter the a value:"))
m = int(input("Enter the b value:"))
arithmetic_ope(n, m)