import math

def integerToRoman(A):
    romansDict = \
        {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
            5000: "G",
            10000: "H"
        }

    tmp = 1
    while A >= tmp:
        tmp *= 10

    tmp /= 10

    res = ""

    while A:


        lastNum = int(A / tmp)

        if lastNum <= 3:
            res += (romansDict[tmp] * lastNum)
        elif lastNum == 4:
            res += (romansDict[tmp] +
                    romansDict[tmp * 5])
        elif 5 <= lastNum <= 8:
            res += (romansDict[tmp * 5] +
                    (romansDict[tmp] * (lastNum - 5)))
        elif lastNum == 9:
            res += (romansDict[tmp] +
                    romansDict[tmp * 10])

        A = math.floor(A % tmp)
        tmp /= 10

    return res



print("Roman value for the integer is:"
      + str(integerToRoman(3549)))




def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


