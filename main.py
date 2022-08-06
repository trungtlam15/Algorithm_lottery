import random


def lottery(number, lucky_draw):
    if number == lucky_draw:
        return 0
    elif number > lucky_draw:
        return 1
    else:
        return 2


def check(from_number, to_number, lucky_draw):
    mid_number = int((from_number + to_number) / 2)
    result = lottery(mid_number, lucky_draw)
    print("try with mid_number: ", mid_number)
    if result == 0:
        print(">>>bingooooo!!!!!")
    elif result == 1:
        check(from_number, mid_number, lucky_draw)
    else:
        check(mid_number, to_number, lucky_draw)


if __name__ == '__main__':
    from_number = 0
    to_number = 100

    lucky_draw = random.randint(from_number, to_number + 1)
    print('lucky draw:', lucky_draw)

    check(from_number, to_number, lucky_draw)


