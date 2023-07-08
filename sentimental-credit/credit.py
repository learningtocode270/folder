def main():
    number = input("Number: ")

    n = algo(number)
    if n == False:
        return

    z = correctLength(number)
    if z != True:
        print("INVALID")

    x = firstDigits(number)

    y = int(x)

    if ((y // 10) == 4):
        print("VISA")


    amex = [37, 34]
    mastercard = [51, 52, 53, 54, 55]

    if y in amex:
        print("AMEX")

    if y in mastercard:
        print("MASTERCARD")
    else:
        print("INVALID")

def algo(number):
    sum_of_set1 = 0
    sum_of_set2 = 0

    odd_digits = number[-2 :: -2]
    even_digits = number[-1 :: -2]

    ### print(odd_digits)
    ### print(even_digits)

    d = int(len(odd_digits))
    e = int(len(even_digits))

    list_of_products = []

    for i in range(d):
        list_of_products.append(int(odd_digits[i]) * 2)

    ### print(list_of_products)

    str_list = "".join(str(x) for x in list_of_products)
    length = len(str_list)

    for v in range(length):
        sum_of_set1 += int(str_list[v])

    for j in range(e):
        sum_of_set2 += int(even_digits[j])

    ### print(sum_of_set1)
    ### print(sum_of_set2)
    ### print(sum_of_set1 + sum_of_set2)

    if (sum_of_set1 + sum_of_set2) % 10 == 0:
        return True
    else:
        print("INVALID")
        return False


def firstDigits(number):
    while (int(number) > 100):
        number = int(number) // 10
    return str(number)

def correctLength(number):
    allowed = [15, 16, 13]
    if len(number) in allowed:
        return True
main()