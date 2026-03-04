
def f2(num1, num2, index): 
    if index == num2:
        return 0
    
    return num1 + f2(num1, num2, index + 1)

print(f2(4, 6, 0))
