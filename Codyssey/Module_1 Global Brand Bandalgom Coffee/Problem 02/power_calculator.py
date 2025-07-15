# ✅ 2. 제곱 계산 프로그램 구현하기 - power_calculator.py
# Python을 사용하여 제곱 계산 프로그램을 구현한다.

# Python 파일명: power_calculator.py

# 구현 요구사항:
    # 사용자로부터 숫자와 제곱할 횟수(지수)를 입력받음
    # 입력받은 숫자를 지정한 횟수만큼 거듭제곱한 결과 출력
    # Python의 내장 연산자 ** 또는 pow() 함수 사용 금지
    # 반복문을 사용하여 직접 제곱 계산 구현
    # 숫자는 float(), 지수는 int()로 형변환

# power라는 사용자 정의 함수를 구현한다.
def power(number: float, exponent: int) -> float:
    answer = 1
    for i in range(abs(exponent)): # 반복문을 사용하여 직접 제곱 계산을 구현한다
        answer = answer * number

    # exponent가 정수가 들어올 수 있다는 것은 음수도 가능하다는 의미이다.
    if exponent < 0:
        answer = 1 / answer

    return answer

# 사용자 입력 예시:
# Enter number: 3
# Enter exponent: 4

# 출력 형식:
# Result: 81

# 예외 처리: <try except>
# 숫자 입력이 숫자형이 아닐 경우 "Invalid number input." 출력
# 지수 입력이 정수가 아닐 경우 "Invalid exponent input." 출력

def main():
    while True:
        try:
            numberInput = input("Enter number: ")
            numberInput = float(numberInput) # 숫자는 float으로 형변환
            break
        except ValueError:
            print("Invalid number input.")
    
    while True:
        try:
            exponentInput = input("Enter exponent: ")
            exponentInput = int(exponentInput) # 지수는 int로 형변환
            break
        except ValueError:
            print("Invalid exponent input.")

    answer = power(numberInput, exponentInput)

    if answer == int(answer): # answer가 정수이면 int로 형변환하여 출력
        print(f'Result: {int(answer)}')
    else: # answer가 정수가 아니면 float 상태 그대로 출력
        print(f'Result: {answer}')

# 프로그램의 실행 로직:
# if __name__ == "__main__":
#     main()

if __name__ == "__main__":
    main()

# 테스트 방식:
# Visual Studio Code에서 power_calculator.py 파일을 열고 터미널에서 python power_calculator.py 명령어로 실행한다