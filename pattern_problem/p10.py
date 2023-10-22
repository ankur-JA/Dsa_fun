    #      *
    #     * *
    #    * * *
    #   * * * *
    #  * * * * * by gearhead

def patter(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end="")
        for k in range(i+1):
            print("* ", end="")
        print()


n = int(input())
patter(n)