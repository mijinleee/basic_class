X = int(input())  # 영수증에 적힌 총 금액
N = int(input())  # 영수증에 적힌 구매한 물건의 종류의 수

total_price = 0  # 물건의 가격과 개수로 계산한 총 금액
for i in range(N):
    a, b = map(int, input().split())
    total_price += a * b

if total_price == X:
    print("Yes")
else:
    print("No")