def find_min_cpus(packets, max_cpus=5, max_time=10):
    for cpu_count in range(1, max_cpus + 1):
        # 각 CPU의 현재 작업 완료 시간 초기화
        cpu_end_times = [0] * cpu_count
        for packet in packets:
            arrival_time, length = packet
            # 가능한 CPU 중 가장 먼저 빈 CPU 선택
            cpu_index = min(range(cpu_count), key=lambda i: max(cpu_end_times[i], arrival_time))
            start_time = max(cpu_end_times[cpu_index], arrival_time)
            end_time = start_time + length
            # 패킷 처리 시간이 10초를 넘는지 확인
            if end_time - arrival_time > max_time:
                break
            cpu_end_times[cpu_index] = end_time
        else:
            # 모든 패킷을 조건 내에서 처리할 수 있는 경우
            return cpu_count
    # 5개의 CPU를 사용해도 조건을 만족할 수 없는 경우
    return -1

# 입력 및 출력 처리
T = int(input())
for t in range(1, T+1):
    N = int(input())
    packets = [tuple(map(int, input().split())) for _ in range(N)]
    result = find_min_cpus(packets)
    print(f"#{t} {result}")
