def multiply_all(*args: int) -> int:
    multiply = 1
    for arg in args:
        multiply *= arg

    return multiply

print(multiply_all(1,2,3,4,5))
print(multiply_all())
print(multiply_all(7))