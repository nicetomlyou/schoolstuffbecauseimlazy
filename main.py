import sys
import os
cwd = os.getcwd()
sys.path.append(str(cwd) + '/MathAnalStuff/')

from rowecheloncalculator import recmain
from matrixdeterminant import mdmain

sys.path.append(str(cwd) + '/English2Acc/')
from vocabscaper import vsmain


def main():
    choice = input("What would you like to go to? Type Help to see options.")
    if choice.lower() == "help":
        choice = input("Type 'math' to go to the math section. Type 'english' to go to the language section.Type "
                       "'back' to go to the beginning.")
        if choice.lower() == "math":
            choice = input("Type '1' to go to Row Echelon Calculator. Type '2' to go to Matrix Determinant "
                           "calculator. Type 'back' to go to the beginning.")

            if choice == "back":
                main()
            if choice == "1":
                recmain()
            if choice == "2":
                mdmain()
            else:
                print("no proper option selected, going back to main menu.")
                main()
        if choice.lower() == "english":
            choice = input("Type '1' to go to Vocab Scraper. Type 'back' to go to the beginning.")
            if choice == "1":
                vsmain()
            if choice == "back":
                main()
            else:
                print("no proper option selected, going back to main menu.")
                main()
    if choice.lower() == "rec":
        recmain()
    if choice.lower() == "md":
        mdmain()
    if choice.lower() == "vs":
        vsmain()
    else:
        print("no proper option selected, going back to main menu.")
        main()
while True:
    main()

