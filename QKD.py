import numpy as np


def prepare_qubits(num_qubits):
    return np.random.randint(0, 4, num_qubits)


def measure_qubits(qubits):
    random_bases = np.random.randint(0, 2, len(qubits))
    measurements = []

    for idx, qubit in enumerate(qubits):
        if random_bases[idx] == qubit % 2:
            measurements.append(qubit // 2)
        else:
            measurements.append(-1)
    return random_bases, measurements


def compare_bases_and_filter_key(sender_bases, receiver_bases, receiver_results):
    filtered_key = []
    for i in range(len(sender_bases)):
        if sender_bases[i] == receiver_bases[i]:
            filtered_key.append(receiver_results[i])
    return filtered_key


def main():
    num_qubits = 100

    # Alice prepares qubits and sends them to Bob
    alice_qubits = prepare_qubits(num_qubits)

    # Bob measures the qubits received
    bob_bases, bob_measurements = measure_qubits(alice_qubits)

    # Alice and Bob compare bases and filter their keys
    alice_bases = [qubit % 2 for qubit in alice_qubits]
    shared_key = compare_bases_and_filter_key(
        alice_bases, bob_bases, bob_measurements)

    print("Alice's qubits: ", alice_qubits)
    print("Bob's bases:    ", bob_bases)
    print("Bob's measurements: ", bob_measurements)
    print("Shared key:     ", shared_key)


if __name__ == "__main__":
    main()
