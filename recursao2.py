def recursao2(num1, num2):
    if (num2 == 0):
        return num1
    return recursao2(num1 +1, num2-1)

print(recursao2(3,2))
