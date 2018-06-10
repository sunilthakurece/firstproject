def plusminus(ar):
    Pnos = 0
    Nnos = 0
    znos = 0
    for i in ar:
        if i > 0:
            Pnos = Pnos + 1
        elif i < 0:
            Nnos = Nnos + 1
        else:
            znos = znos + 1
    print(round(Pnos / x, 6))
    print(round(Nnos / x, 6))
    print(round(znos / x, 6))
x = int(input())
y = list(map(int, input().rstrip().split()))
plusminus(y)