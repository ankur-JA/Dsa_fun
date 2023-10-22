    # *********
    #  *******
    #   *****
    #    ***
    #     * by gearhead


def pattern(n):
    for i in range(n):
        for j in range(i):
            print(" ", end="")
        for k in range(2*n - 2*i -1):
            print("*", end="")
        print()


n = int(input())
pattern(n)