if __name__ == '__main__':

    n = int(input())

    a = []
    ldscore=0
    rdscore=0

    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))

    for i in range(len(a)):
        for j in range(len(a[i])):
            if i ==j:
                ldscore = ldscore + a[i][j]
                break

        rdscore=rdscore+a[i][len(a[i])-1-i]

    final=abs(ldscore-rdscore)
    print(final)
