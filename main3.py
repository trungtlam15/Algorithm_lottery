
def solution(list):
    count_odd = 0
    for i in list:
        count_odd += i%2
    print("number of odd: ",count_odd)

    count_even = len(list) - count_odd
    print("number of even: ",count_even)

if __name__ == '__main__':

    list = [1, 4, 7, 9, 10, 15, 40]
    solution(list)