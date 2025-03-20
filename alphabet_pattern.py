def print_alphabet_pattern(letter):
    """Prints the pattern for a given uppercase alphabet letter."""

    if letter == 'A':
        for row in range(7):
            for col in range(5):
                if (col % 4 == 0 and row != 0) or ((row == 0 or row == 3) and (col > 0 and col < 4)):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    elif letter == 'B':
        for row in range(7):
            for col in range(5):
                if col == 0 or (col == 4 and (row != 0 and row != 3 and row != 6)) or ((row == 0 or row == 3 or row == 6) and (col > 0 and col < 4)):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

    elif letter == 'C':
        for row in range(7):
            for col in range(5):
                if col == 0 or ((row == 0 or row == 6) and (col > 0)):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    elif letter == 'D':
        for row in range(7):
            for col in range(5):
                if col == 0 or (col == 4 and row != 0 and row != 6) or ((row == 0 or row == 6) and (col>0 and col<4)):
                  print("*", end="")
                else:
                  print(" ", end="")
            print()
    elif letter == 'E':
        for row in range(7):
            for col in range(5):
                if col == 0 or row == 0 or row == 3 or row == 6:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    elif letter == 'F':
        for row in range(7):
            for col in range(5):
                if col == 0 or row == 0 or row == 3:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    elif letter == 'G':
        for row in range(7):
            for col in range(5):
                if col == 0 or ((row == 0 or row == 6) and (col > 0 and col < 4)) or (col == 4 and (row > 2 and row < 6)) or (row == 3 and (col > 2)):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    elif letter == 'H':
        for row in range(7):
            for col in range(5):
                if col == 0 or col == 4 or row == 3:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    elif letter == 'I':
        for row in range(7):
            for col in range(5):
                if col == 2 or row == 0 or row == 6:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    elif letter == 'J':
        for row in range(7):
            for col in range(5):
                if col == 2 or row == 0 or (row == 6 and col<3) or (col == 0 and row > 3):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    elif letter == 'K':
        for row in range(7):
            for col in range(5):
                if col == 0 or (row + col == 4) or (row - col == 2):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    elif letter == 'L':
        for row in range(7):
            for col in range(5):
                if col == 0 or row == 6:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    elif letter == 'M':
        for row in range(7):
            for col in range(7):
                if col == 0 or col == 6 or (row == col and (col > 0 and col < 4)) or (row + col == 6 and (col > 2 and col < 6)):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    elif letter == 'N':
        for row in range(7):
            for col in range(7):
                if col == 0 or col == 6 or row == col:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    elif letter == 'O':
        for row in range(7):
            for col in range(5):
                if (col == 0 or col == 4) and (row != 0 and row != 6) or ((row == 0 or row == 6) and (col > 0 and col < 4)):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    elif letter == 'P':
        for row in range(7):
            for col in range(5):
                if col == 0 or (col == 4 and row < 4 and row > 0) or (row == 0 or row == 3) and (col > 0 and col < 4):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    elif letter == 'Q':
        for row in range(7):
            for col in range(6):
                if ((col == 0 or col == 4) and (row != 0 and row != 6)) or ((row == 0 or row == 6) and (col > 0 and col < 4)) or (row==4 and col == 3) or(row==5 and col ==4) or (row==6 and col==5):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    elif letter == 'R':
        for row in range(7):
            for col in range(5):
                if col == 0 or (col == 4 and row < 4 and row > 0) or (row == 0 or row == 3) and (col > 0 and col < 4) or row-col==2:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    elif letter == 'S':
        for row in range(7):
            for col in range(5):
                if ((row == 0 or row == 3 or row == 6) and col > 0 and col < 4) or (col == 0 and (row > 0 and row < 3)) or (col == 4 and (row > 3 and row < 6)):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    elif letter == 'T':
        for row in range(7):
            for col in range(5):
                if row == 0 or col == 2:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    elif letter == 'U':
        for row in range(7):
            for col in range(5):
                if (col == 0 or col == 4) and row != 6 or (row == 6 and col > 0 and col < 4):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    elif letter == 'V':
        for row in range(7):
            for col in range(7):
                if (row==col and col < 4) or (row+col==6 and col >2):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    elif letter == 'W':
        for row in range(7):
            for col in range(7):
                if col == 0 or col == 6 or (row + col == 6 and col<4) or (row==col and col>2):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    elif letter == 'X':
        for row in range(7):
            for col in range(7):
                if row == col or row + col == 6:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    elif letter == 'Y':
        for row in range(7):
            for col in range(7):
                if (row == col and col < 3) or (row + col == 6 and col > 3) or (col == 3 and row > 2):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    elif letter == 'Z':
        for row in range(5):
            for col in range(5):
                if row == 0 or row == 4 or col + row == 4 :
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    else:
      print("Invalid Letter")

def main():
    letter = input("Enter an uppercase letter (A-Z) to print its pattern: ").upper()
    print_alphabet_pattern(letter)


if __name__ == "__main__":
    main()