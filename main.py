import array
import math
import os

Num = array.array('f')
FirstDiff = array.array('f')
SecondDiff = array.array('f')
ThirdDiff = array.array('f')
CommonRatio = array.array('f')


def ResetData():
    Num.clear()
    FirstDiff.clear()
    SecondDiff.clear()
    ThirdDiff.clear()
    CommonRatio.clear()


def get_sequence():
    n = int(input("How many numbers do you want to enter? "))

    for _ in range(n):
        val = int(input("Enter a number: "))
        Num.append(val)

    print("Final array:", Num)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
 

def display_nth_term(message):
    print("* Nth TERM *") 
    print(" = " + message)


def Calculate_First_Diff():
    for i in range(len(Num) - 1):
        FirstDiff.append(Num.index(i + 1) - Num.index(i))


def Calculate_Second_Diff():
    for i in range(len(FirstDiff) - 1):
        SecondDiff.append(FirstDiff.index(i + 1) - FirstDiff.index(i))


def Calculate_Third_Diff():
    for i in range(len(SecondDiff) - 1):
        ThirdDiff.append(SecondDiff.index(i + 1) - SecondDiff.index(i))


def Calculate_Common_Ratio():
    for i in range(len(Num) - 1):
        CommonRatio.append(Num.index(i + 1) / Num.index(i))


def It_Is_Linear_Sequence():
    FirstDiffSame = True

    for i in range(len(FirstDiff) - 1):
        if FirstDiff.index(i) != FirstDiff.index(i + 1):
            FirstDiffSame = False
            break

    if FirstDiffSame:
        return True
    else:
        return False


def It_Is_Quadratic_Sequence():
    SecondDiffSame = True

    for i in range(len(SecondDiff) - 1):
        if SecondDiff.index(i) != SecondDiff.index(i + 1):
            SecondDiffSame = False
            break

    if SecondDiffSame:
        return True
    else:
        return False

     
def It_Is_Cubic_Sequence():
    ThirdDiffSame = True

    for i in range(len(ThirdDiff) - 1):
        if ThirdDiff.index(i) != ThirdDiff.index(i + 1):
            ThirdDiffSame = False
            break

    if ThirdDiffSame:
        return True
    else:
        return False


def It_Is_Geometric_Sequence():
    CommonRatioSame = True

    for i in range(len(CommonRatio) - 1):
        if CommonRatio.index(i) != CommonRatio.index(i + 1):
            CommonRatioSame = False
            break

    if CommonRatioSame:
        return True
    else:
        return False


def Get_Linear_nth_term():
    d = FirstDiff.index(0)
    a = Num.index(0)
    nth_term = ""

    if d == 1:
        nth_term = "n"
    else:
        nth_term = str(d) + "n"

    if (a - d) > 0:
        nth_term = nth_term + "+" + str(a - d)
    else:
        if (a - d) != 0 and (a - d < 0):
            nth_term = nth_term + str(a - d)

    return nth_term


def Get_Quadratic_nth_term():
    a = SecondDiff[0] / 2.0
    b = FirstDiff[0] - (3.0 * a)
    c = Num[0] - (a + b)
    nth_term = ""

    if a == 1:
        nth_term = "n^2"
    elif a == -1:
        nth_term = "-n^2"
    else:
        nth_term = str(a)

    if b == 1:
        nth_term = nth_term + "+n"
    elif b == -1:
        nth_term = nth_term + "-n"
    elif b > 1:
        nth_term = nth_term + "+" + str(b) + "n"
    else:
        if b < -1:
            nth_term = nth_term + str(b) + "n"

    if c < 0:
        nth_term = nth_term + str(c)
    else:
        if c != 0:
            nth_term = nth_term + "+" + str(c)
    
    return nth_term


def Get_Cubic_nth_term():
    a = ThirdDiff[0] / 6.0
    b = (SecondDiff[0] - (12.0 * a)) / 2.0
    c = FirstDiff[0] - (3.0 * b) - (7.0 * a)
    d = Num[0] - (a + b + c)
    nth_term = ""

    if a == 1:
        nth_term = "n^3"
    elif a == -1:
        nth_term =  "-n^3"
    else:
        nth_term = str(a) + "n^3"
    if b == 1:
        nth_term = nth_term + "+n^2"
    elif b == -1:
        nth_term = nth_term + "-n^2"
    elif b > 1:
        nth_term = nth_term  + "+" + str(b) + "n^2"
    else:
        if b < -1:
            nth_term = nth_term + str(b) + "n^2"

    if c == 1:
        nth_term = nth_term + "+n"
    elif c == -1:
        nth_term = nth_term + "-n"
    elif c > 1:
        nth_term = nth_term + "+" + str(c) + "n"
    else:
        if c < -1:
            nth_term = nth_term + str(c) + "n"

    if d < 0:
        nth_term = nth_term + str(d)
    else:
        if d != 0:
            nth_term = nth_term + "+" + str(d)

    return nth_term


def Get_Goemetric_nth_term():
    pass

   
if __name__ == "__main__":
    
    ResetData()

    get_sequence()

    Calculate_First_Diff() 

    Calculate_Second_Diff()
    Calculate_Third_Diff()
    Calculate_Common_Ratio()

    if It_Is_Linear_Sequence():
        display_nth_term(Get_Linear_nth_term())

    elif It_Is_Quadratic_Sequence():
        display_nth_term(Get_Quadratic_nth_term())

    elif It_Is_Cubic_Sequence():
        display_nth_term(Get_Cubic_nth_term())

    elif It_Is_Geometric_Sequence():
        # display_nth_term(Get_Goemetric_nth_term())
        display_nth_term("Feature Unavailable")

    else:
        display_nth_term("Generator Failed")