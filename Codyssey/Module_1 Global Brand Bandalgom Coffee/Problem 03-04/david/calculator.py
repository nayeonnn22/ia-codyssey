# 📌 기능 요구사항
    # 1. 사용자 입력 받기
    # 1-1. 실수형 숫자 2개 입력
    # 1-2. 연산자 입력 (+, -, *, /)

# 📌 기본 연산 기능
    # add(a, b)
    # subtract(a, b)
    # multiply(a, b)
    # divide(a, b)

def add(a, b): # 덧셈
    return a + b

def subtract(a, b): # 뺼셈
    return a - b

def multiply(a, b): # 곱셈
    return a * b

def divide(a, b): # 나눗셈
    if (b == 0):
        print("Error: Division by zero.")
        return
    return a / b

# 예외 처리 => 조건문으로 예외를 처리하는 방법도 존재한다.
    # b == 0일 때 "Error: Division by zero." 출력
    # 잘못된 연산자는 "Invalid operator." 출력
    # [추가] 실수형 숫자를 입력받아야 하는데, 그렇지 않다면 예외 처리를 해주어야 할 것. -> 제대로 받을 때까지 while문으로 처리


def inputNumber(prompt): # 실수형 숫자를 입력받고 여기에 제대로 실수가 입력되었는지 확인하는 함수 => 재사용을 위해 함수로 구현하는 것이 합리적이다.
    while True:
        try:
            numberInput = int(float(input(prompt))) # 실수형 숫자를 입력받음 -> 입력받은 숫자는 반드시 정수형 변환해줘야 함
            return numberInput
        except ValueError:
            print("Invalid number input.")

def inputExpression(prompt):
    while True:
        try:
            expression = input(prompt).split()
            if len(expression) != 3:
                print("Invalid Expression.")
                continue
            a = int(float(expression[0]))
            b = int(float(expression[2]))
            oper = expression[1]
            return a, b, oper
        except ValueError:
            print("Invalid Expression.")        

# [보너스 과제] 문자열 수식 입력 방식 계산기 기능 추가
    #  사용자가 한 줄로 수식을 입력하면 해당 수식을 해석하여 계산 결과를 출력하는 기능

    # ✅ 구현 요구사항
        # 사용자 입력 형식: "숫자 연산자 숫자" 형태 (공백 포함) => 예) Enter expression: 2 + 3
        # 연산자는 하나만 허용 => 연산자 우선 순위를 고려하지 않아도 된다.
        # 허용 연산자: +, -, *, /
        # 예외 처리 포함:
            # 잘못된 입력 형식 => 우선, 숫자 연산자 숫자 형태가 아니라면 잘못된 입력 형식이다.
            # 0으로 나누는 경우

def main():
    a, b, oper = inputExpression("Enter expression: ") # 2 + 3

    # print(expression) # ['2', '+', '3'] => 리스트 형태

    # 1. len(expression) != 3 이면 잘못된 입력 형식이다 ⭐⭐ => 첫번째 평가 피드백!! 주석 작성해두고 실제로 구현하는 것을 잊어버림 ⭐⭐
    # 2. expression[0], expression[2]이 숫자가 아니라면, 잘못된 입력 형식이다.
    # 3. expression[1]이 허용 연산자가 아니라면, 잘못된 입력 형식이다.

    # a = inputNumber("Enter the first number : ")
    # b = inputNumber("Enter the second number : ")
    # oper = input("Enter the operator [ + or - or * or / ] : ")

    if oper == '+':
        answer = add(a, b)
    elif oper == '-':
        answer = subtract(a, b)
    elif oper == '*':
        answer = multiply(a, b)
    elif oper == '/':
        answer = divide(a, b)
        if (answer == None): # b == 0이면 에러 메세지만을 출력. result가 없기 때문에 출력하지 말 것 -> return을 쓰면 print(f'Result: {answer}')를 실행하지 않는다.
            return
    else:
        print("Invalid Expression.") # 잘못된 연산자는 "Invalid operator." 출력 
        return

    print(f'Result: {float(answer)}')

if __name__ == "__main__":
    main()