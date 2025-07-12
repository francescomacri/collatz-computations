from math import pi
import matplotlib.pyplot as plt


def collatz(n):
    sequence = [n]
    if n < 1:
        return []
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (3 * n + 1) // 2
        sequence.append(n)
    return sequence


def plot_sequence(seq, start_n):
    plt.figure(figsize=(8, 4))
    plt.plot(range(len(seq)), seq, marker="o")

    plt.yscale("log")  # Set y-axis to logarithmic scale

    plt.title(f"Collatz Sequence for n = {start_n} (Logarithmic Scale)")
    plt.xlabel("Step Index")
    plt.ylabel("Sequence Value (log scale)")
    plt.grid(True, which="both", ls="--")
    plt.tight_layout()
    plt.show()


def main():
    prompt = int(
        input("Please choose a positive integer to plug into the Collatz function: ")
    )
    seq = collatz(prompt)
    print(
        f"If you plug in {prompt} into the Collatz function you get the following sequence:\n{seq}"
    )
    if seq:
        plot_sequence(seq, prompt)


if __name__ == "__main__":
    main()
