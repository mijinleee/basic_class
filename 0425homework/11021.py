T = int(input())  # 테스트 케이스 개수 입력

for i in range(1, T+1):
    A, B = map(int, input().split())
    print(f"Case #{i}: {A+B}")