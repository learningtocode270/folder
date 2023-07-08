def main():
    height = get_height()
    c = 1
    while c <= height:
        print(" " * (height - c), end="")

        print("#" * (height - (height - c)), end="")

        print("  ", end = "")

        print("#" * (height - (height - c)), end="")

        print("")
        c += 1


def get_height():
    while True:
        try:
            n = int(input("Height: "))

            # Only allow values greater than 0 and less than or equal to 8
            if (8 >= n > 0):
                return n
        except ValueError:
            print('not a valid number')


main()