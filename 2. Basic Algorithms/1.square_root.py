"""
Finding the Square Root of an Integer

Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is O(log(n))

"""


def sqrt(number):

    if number < 0:
        imaginary_root = True
        value = -1
    else:
        imaginary_root = False
        value = 1

    if number == 0:
        return 0

    while True:
        if not imaginary_root:
            if round(number/value) == value:
                return value
            elif round(number/value) > value:
                value += (round(number/value) - value) //2
            else:
                value -= (value - round(number/value))//2
        else:
            if round(number/value) == -1 * value: # because division of two negative numbers returns a positive
                return complex(0, -1 * value)
            elif round(number/value) < value:
                value += (round(number/value) + value) //2
            else:
                value -= (value + round(number/value))//2


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (60 == sqrt(3600)) else "Fail")

print ("Pass" if  (complex(0, 1) == sqrt(-1)) else "Fail")
print ("Pass" if  (complex(0, 5) == sqrt(-25)) else "Fail")
print ("Pass" if  (complex(0, 5) == sqrt(-27)) else "Fail")
