""" from testing_code import square """

""" def test_sqaure():
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9")
 """
from testing_sqaure_fn import test_sqaure

def test_sqaure():
    try:
        assert test_sqaure(-3) == 9
    except AssertionError:
        print("-3 Squared was not 9 ")

    try:
        assert test_sqaure(-2) == 4
    except AssertionError:
        print("-2 squared was not 4")
    try:
        assert test_sqaure(0) == 0
    except AssertionError:
        print("0 squared was not 0")


def main():
   """  x = int(input("Enter any integer")) """
   test_sqaure()

if __name__ == "__main__":
    main()