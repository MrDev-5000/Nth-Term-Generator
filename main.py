import numpy as np
import os
import subprocess


def InitData():
    global FirstDiff
    FirstDiff = np.empty(np.size(Sequence) - 1)  if np.size(Sequence) > 1 else np.array([])

    global SecondDiff
    SecondDiff = np.empty(np.size(FirstDiff) - 1) if np.size(FirstDiff) > 1 else np.array([])

    global ThirdDiff
    ThirdDiff = np.empty(np.size(SecondDiff) - 1) if np.size(SecondDiff) > 1 else np.array([])

    global CommonRatio
    CommonRatio = np.empty(np.size(Sequence) - 1) if np.size(Sequence) > 1 else np.array([])


def get_sequence():
    Num = []
    while True:
        n = int(input("How many numbers do you want to enter? ")) 
        if n > 1:
            break
        else:
            print("Insufficent number , pls provide at least 2 numbers")

    for _ in range(n):
        val = int(input("Enter a number: "))
        Num.append(val)

    global Sequence
    Sequence = np.array(Num)
    print("Entered Sequence:", Sequence)


def clearConsole():
    command = 'cls' if os.name == 'nt' else 'clear'
    subprocess.run(command, shell=True)


def display_nth_term(message):
    print("* Nth TERM *") 
    print(" = " + message)


def Calculate_First_Diff():
    FirstDiff = np.diff(Sequence)
    print(f"First diff {FirstDiff}")
        

def Calculate_Second_Diff():
    try:
        SecondDiff = np.diff(FirstDiff)
    except ValueError:
        pass


def Calculate_Third_Diff():
    try:
        ThirdDiff = np.diff(SecondDiff)
    except ValueError:
        pass


def Calculate_Common_Ratio(Sequence):
    _Sequence = np.asanyarray (Sequence)
    Sequence = _Sequence[1:] / _Sequence[:-1]


def It_Is_Linear_Sequence():
    FirstDiffSame = True

    for i in range(np.size(FirstDiff)-1):
        if FirstDiff[i] != FirstDiff[i + 1]:
            FirstDiffSame = False
            break

    if FirstDiffSame:
        return True
    else:
        return False


def It_Is_Quadratic_Sequence():
    SecondDiffSame = True

    for i in range(np.size(SecondDiff) - 1):
        if SecondDiff[i] != SecondDiff[i + 1]:
            SecondDiffSame = False
            break

    if SecondDiffSame:
        return True
    else:
        return False

     
def It_Is_Cubic_Sequence():
    ThirdDiffSame = True

    for i in range(np.size(ThirdDiff) - 1):
        if ThirdDiff[i] != ThirdDiff[i + 1]:
            ThirdDiffSame = False
            break

    if ThirdDiffSame:
        return True
    else:
        return False


def It_Is_Geometric_Sequence():
    CommonRatioSame = True

    for i in range(np.size(CommonRatio) - 1):
        if CommonRatio[i] != CommonRatio[i + 1]:
            CommonRatioSame = False
            break

    if CommonRatioSame:
        return True
    else:
        return False


def Get_Linear_nth_term():
    d = FirstDiff[0]
    a = Sequence[0]
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
    c = Sequence[0] - (a + b)
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
    d = Sequence[0] - (a + b + c)
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

    get_sequence()
    InitData()

    Calculate_First_Diff() 

    Calculate_Second_Diff()
    Calculate_Third_Diff()
    Calculate_Common_Ratio(Sequence)

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