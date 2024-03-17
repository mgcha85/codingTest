from collections import deque
from itertools import product
from copy import copy


# 가능한 모든 숫자 조합을 만들어 목표 숫자를 만들 수 있는지 확인

def can_make_target_with_numbers(numbers, M, W):
    str_numbers = [str(number) for number in numbers if number != 0]  # 0이 아닌 숫자만 사용
    for length in range(1, M + 1):
        for combination in product(str_numbers, repeat=length):
            if int("".join(combination)) == W:
                return len("".join(combination))  # 조합으로 만든 숫자의 길이 반환
    return float('inf')

# 연산 함수 정의
def operate(a, op, b):
    if op == '+': return a + b
    elif op == '-': return a - b
    elif op == '*': return a * b
    elif op == '/' and b != 0: return a // b
    else: return None

def min_touches(numbers: list[str], operators: list[str], M: int, W: int):
    if str(W) in numbers: # 목표 숫자와 동일한 숫자를 바로 사용할 수 있는 경우
        return 1
    
    numbers_int = set(map(int, numbers))
    offset = 1

    while True:
        offset += 1

        if offset >= M: return -1
        numbers_add = list([''.join(numbers) for numbers in product(numbers, repeat=offset)])
        if str(W) in numbers_add:
            return offset
        
        numbers_int_add = set(map(int, numbers_add))
        numbers_int = numbers_int.union(numbers_int_add)

        # BFS 초기화
        queue = deque()
        for num in numbers_int:
            queue.append((num, len(str(num))))  # (현재 값, 터치 횟수)
        visited = copy(numbers_int)

        while queue:
            current, touches = queue.popleft()

            for op in operators:
                for num in numbers_int:
                    if touches + len(str(num)) + 1 > M: continue  # 현재 숫자, 연산자, 다음 숫자를 고려한 터치 횟수
                    result = operate(current, op, num)
                    if result is not None and 0 <= result <= 999 and result not in visited:
                        new_touches = touches + len(str(num)) + 1
                        if result == W: return new_touches + 1
                        queue.append((result, new_touches))
                        visited.add(result)


# 파일로부터 입력 읽기
def read_input_from_file(filename):
    with open(filename, 'r') as file:
        T = int(file.readline().strip())
        results = []
        for _ in range(T):
            N, O, M = file.readline().strip().split()
            numbers = list(file.readline().strip().split())
            operators_input = list(file.readline().strip().split())
            W = int(file.readline().strip())

            operator_map = {'1': '+', '2': '-', '3': '*', '4': '/'}
            operators = [operator_map[o] for o in operators_input]
            
            result = min_touches(numbers, operators, int(M), W)
            results.append(result)
        return results


# 결과 출력
def print_results(results):
    for i, result in enumerate(results, start=1):
        print(f"#{i} {result}")


# 입력 파일 이름
filename = "input.txt"
results = read_input_from_file(filename)
print_results(results)
