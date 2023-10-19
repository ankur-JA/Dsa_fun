                                #      *
                                #     **
                                #    ***
                                #   ****
                                #  ***** by gearhed

def pattern(n):
    for i in range(1, n + 1):
        # Print spaces
        print(" " * (n - i), end="")

        # Print stars
        print("* " * i)




n = int(input())
pattern(n)