import sys
import qsharp

qsharp.packages.add("Microsoft.Quantum.Numerics")
qsharp.reload()
from GroversTutorial import FactorizeWithGrovers2
import matplotlib.pyplot as plt
import numpy as np


def freq(number: int, experiment_iter: int) -> dict:
    # Instantiate variables
    frequency = {}
    results = []

    # Run experiment_iter times the Q# operation.
    for i in range(experiment_iter):
        print(f"Experiment: {i} of {experiment_iter}")
        results.append(FactorizeWithGrovers2.simulate(number=number))

    # Store the results in a dictionary
    for i in results:
        if i in frequency:
            frequency[i] = frequency[i] + 1
        else:
            frequency[i] = 1

    # Sort and print the results
    frequency = dict(reversed(sorted(frequency.items(), key=lambda item: item[1])))
    return frequency


def main():

    # Instantiate variables
    experiment_iter = int(sys.argv[2])
    number = int(sys.argv[1])

    frequency = freq(number, experiment_iter)
    print("Output,  Frequency")
    for k, v in frequency.items():
        print(f"{k:<8} {v}")

    # Plot an histogram with the results
    plt.bar(frequency.keys(), frequency.values())
    plt.xlabel("Output")
    plt.ylabel("Frequency of the outputs")
    plt.title(
        f"Outputs for Grover's factoring. N={number}, {experiment_iter} iterations"
    )
    plt.xticks(np.arange(1, 33, 2.0))
    plt.show()


if __name__ == "__main__":
    main()
