"""Calculator V2"""
def main():
    """Calculator V2"""
    number = int(input())
    count = len(str(number))
    count_1 = 1
    count_9 = 9
    tap_num = 0
    if number == 1:
        print(1)
        quit()
    for i in range(1, count):
        howmany = (count_9 - count_1)+1
        tap_num += howmany * i
        count_1 = int(str(count_1) + "0")
        count_9 = int(str(count_9) + "9")
    last_count = ((number - count_1) + 1) * count
    total = (tap_num + last_count) + number
    print(total)
    print(total)
    print(total)
    print(total)
main()
