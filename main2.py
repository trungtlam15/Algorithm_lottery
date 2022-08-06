
def fibonacci_sequence(number1,number2,limit):
    new_list = []
    if number1 > limit or number2 > limit:
        return
    next_number = number1 + number2
    new_list.append(next_number)
    print(new_list)
    fibonacci_sequence(number2,next_number,limit)

if __name__ == '__main__':
    number1 = 1
    number2 = 1
    limit = 50
    fibonacci_sequence(number1,number2,limit)

