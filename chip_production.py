
def max_chips(H, W, wafer):
    """
    Calculate the maximum number of chips that can be produced from a given wafer.

    Args:
    - H: The height of the wafer.
    - W: The width of the wafer.
    - wafer: A 2D list representing the wafer, where 0 indicates a usable area and 1 indicates an unusable area.

    Returns:
    - The maximum number of 2x2 chips that can be produced from the wafer.
    """
    max_chips = 0

    # Iterate through the wafer to find all possible 2x2 areas.
    for i in range(H - 1):
        for j in range(W - 1):
            # Check if the current 2x2 area is usable for chip production.
            if wafer[i][j] == 0 and wafer[i][j+1] == 0 and wafer[i+1][j] == 0 and wafer[i+1][j+1] == 0:
                # If usable, increment the max_chips count.
                max_chips += 1
                # Mark the area as used by setting it to 1.
                wafer[i][j], wafer[i][j+1], wafer[i+1][j], wafer[i+1][j+1] = 1, 1, 1, 1

    return max_chips


if __name__ == "__main__":
    filename = "input2.txt"
    with open(filename, 'r') as file:
        T = int(file.readline().strip())  # 테스트 케이스 개수
        for t in range(1, T+1):
            H, W = map(int, file.readline().strip().split())  # 세로길이 H, 가로길이 W
            wafer = [list(map(int, file.readline().strip().split())) for _ in range(H)]  # 웨이퍼 정보
            result = max_chips(H, W, wafer)  # 최대 생산 가능한 칩의 개수 계산
            print(f"#{t} {result}")  # 결과 출력
