def make_negative(number):
    if number >= 0:
        final_number = (number - number) - number
        return final_number
    else:
        return number


print(make_negative(1)) # return -1
print(make_negative(-5)) # return -5
print(make_negative(0))  # return 0
print(make_negative(5))  # return -5
print(make_negative(10))  # return -5
