def max_chips(H, W, wafer):
    chips = 0
    for i in range(H-1):
        for j in range(W-1):
            # 현재 위치에서 2x2 칩이 가능한지 확인
            if wafer[i][j] == 0 and wafer[i+1][j] == 0 and wafer[i][j+1] == 0 and wafer[i+1][j+1] == 0:
                # 칩으로 만들 수 있는 영역을 찾으면 칩 개수를 증가
                chips += 1
                # 찾은 영역을 사용 불가능하게 변경 (이 부분은 주어진 문제 조건에 따라 조정 필요)
                wafer[i][j] = wafer[i+1][j] = wafer[i][j+1] = wafer[i+1][j+1] = 1
    return chips


if __name__ == "__main__":
    filename = "input2.txt"
    with open(filename, 'r') as file:
        T = int(file.readline().strip())  # 테스트 케이스의 개수
        for t in range(1, T+1):
            H, W = map(int, file.readline().strip().split())
            wafer = [list(map(int, file.readline().strip().split())) for _ in range(H)]  # 웨이퍼 정보 변경
            # 최대 생산 가능한 칩의 개수 계산
            result = max_chips(H, W, wafer)
            print(f"#{t} {result}")
