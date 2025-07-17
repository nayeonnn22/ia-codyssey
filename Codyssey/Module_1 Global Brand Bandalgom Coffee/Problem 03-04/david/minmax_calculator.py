# 문제 04 - 수행 과제 02
# 최소값 최대값 프로그램 구현하기

# 입력된 숫자들 중 최소값(minimum) 과 최대값(maximum) 을 출력하는 프로그램을 작성한다.

def inputNumbers():
    while True:
        try:
            numbers = input().split()
            for i in range(len(numbers)):
                numbers[i] = float(numbers[i]) # 여기서 float으로 형변환을 할 때 예외가 발생할 수 있다. 정수가 아닌 실수만 입력되면 된다.
            return numbers
        except ValueError:
            print("Invalid input.")

def findMinMax(numbersList):
    minValue, maxValue = numbersList[0], numbersList[0]

    for i in numbersList:
        if i < minValue: # 만일 현재의 minValue보다 작은 값이 발견되면, 해당 값을 minValue 값에 넣는다
            minValue = i
        if i > maxValue:
            maxValue = i

    return minValue, maxValue

def main():
    # 1. 숫자들을 한 줄에 공백을 기준으로 입력받는다. -> split() 활용
    # 1-1. 예외 처리 : 숫자 이외의 값이 입력될 경우 "Invalid input."을 출력한다.
    numbers = inputNumbers()

    # print(numbers)
    # print(type(numbers[0]))

    # 2. 입력된 숫자 중 최대값, 최소값을 구한다.
    minvalue, maxValue = findMinMax(numbers)

    # 3. 최대값과 최소값을 출력한다.
    print(f"Min: {minvalue}, Max: {maxValue}")

# 구현 방식 및 기술 요구사항
    # Python 내장 함수 min()과 max() 사용을 금지한다.
    # 숫자로 변환 시 float()를 사용한다.


if __name__ == "__main__":
    main()