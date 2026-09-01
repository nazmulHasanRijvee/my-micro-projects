import time
import os

print(f"{'Timer':^{40}}")
print("-" * 40)
# Header alignment


def errormanage(y="none"):

    while True:
        try:
            x = int(input("Enter the" + y))
        except ValueError:
            print("Invalid input! Please enter a number.\n")
            continue

        return x


def timing():

    d = errormanage(" hour.\n")

    b = errormanage(" minute.\n")

    c = errormanage(" second.\n")

    while c >= 0:
        print(f"{d} : {b} : {c}")

        time.sleep(1)
        os.system("cls")

        c -= 1

        if b == 0 and d != 0:
            d -= 1
            b = 59

        elif c == 0 and b != 0:
            b -= 1
            c = 59

    else:
        print("Time's up!")


while True:
    a = input("Do you want to set a timer?  :- ").lower()

    if a in "yes":
        timing()

    elif a in "no":
        print("Exiting the program. Thank you for using this program.")
        break

    else:
        print("Invalid input!. Please enter yes or no.")
        continue
