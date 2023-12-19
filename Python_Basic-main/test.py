'''
for i in range (1, 6):
    for j in range(i):
        print('*', end='')
    print()

for i in range(5, 0, -1):
    for j in range(i):
        print('*', end='')
    print()

for i in range(1, 6):
    for j in range(5-i):
        print(' ', end='')
    for j in range(2*i-1):
        print('*', end='')
    print()

for i in range(1, 6):
    for j in range(5-i):
        print(' ', end='')
    for j in range(2*i-1):
        print('*', end='')
    print()
for i in range(5, 0, -1):
    for j in range(5-i):
        print(' ', end='')
    for j in range(2*i-1):
        print('*', end='')
    print()

for i in range(1, 9):
    for j in range(i):
        print('*', end='')
    print()

def get_score(score):
    if score>=90:
        return 'A'
    elif score>=80:
        return 'B'
    elif score>=70:
        return 'C'
    elif score>=60:
        return 'D'
    else:
        return 'F'

num=int(input("성적: "))
grade=get_score(num)
print(grade)

def calculator(num1, op, num2):
    if op=='+':
        return num1+num2
    elif op=='-':
        return num1-num2
    elif op=='*':
        return num1*num2
    elif op=='/':
        return num1/num2
    else:
        return "error"

num1=float(input())
op=input("('+','-','*','/'중 하나를 입력하세요: ")
num2=float(input("두 번째 숫자를 입력하세요: "))
result=calculator(num1, op, num2)
print(result)

def find_min_max(numbers):
    if not numbers:
        return None, None
    min_val=max_val=numbers[0]

    for num in numbers:
        if num<min_val:
            min_val=num
        if num>max_val:
            max_val=num

    return min_val, max_val

num=input()
numbers=[]
for num in num.split():
    numbers.append(float(num))

min_val, max_val = find_min_max(numbers)
if min_val is not None and max_val is not None:
    print(f"최솟값={min_val}")
    print(f"최댓값={max_val}")
'''
