# basic.py

from math import pi


def collatz(n):
    sequence = [n]
    if n < 1:
        return []
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = (3 * n + 1) / 2
        sequence.append(n)
    return sequence


def main():
    prompt = int(
        input("Please chose a positive integer to plug into the Collatz function: ")
    )
    print(
        f"If you plug in {prompt} into the Collatz function you get the following sequence: {collatz(prompt)}."
    )


if __name__ == "__main__":
    main()
