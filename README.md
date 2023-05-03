# Quantum Cryptography: Quantum Key Distribution (QKD)
Quantum cryptography is a technique that leverages the principles of quantum mechanics to ensure secure communication between two parties. The most well-known quantum cryptography protocol is Quantum Key Distribution (QKD), which allows two parties to generate a shared, secret encryption key in a way that is resistant to eavesdropping. QKD relies on the fundamental properties of quantum mechanics, such as superposition and entanglement, to achieve this level of security.

The most famous QKD protocol is the BB84 protocol, which was proposed by Charles Bennett and Gilles Brassard in 1984. Here's a brief overview of how the BB84 protocol works:

1. The sender (Alice) prepares a series of qubits (quantum bits) in random polarization states. These qubits can be photons polarized either horizontally, vertically, or diagonally (at 45 or 135 degrees).

2. Alice sends the qubits to the receiver (Bob) through a quantum channel, such as an optical fiber.

3. Bob measures the received qubits using a random selection of polarization filters. He records the results without knowing whether his choice of filters matched the original polarization states used by Alice.

4. Alice and Bob then communicate over a classical channel (like a phone call or a secure internet connection) to compare the filters used by Bob during the measurements. They discard the results where the filters didn't match.

5. If the remaining results match, Alice and Bob can use them to generate a shared secret key. This key can be used to encrypt and decrypt messages using classical encryption algorithms.

![Alt text](Media/Screenshot%202023-05-03%20000836.png)

In this script, the qubits are represented as integers (0, 1, 2, or 3) instead of actual quantum states.

The security of QKD lies in the fact that any attempt by an eavesdropper (Eve) to intercept and measure the qubits will unavoidably disturb their quantum states due to the no-cloning theorem and Heisenberg's uncertainty principle. Alice and Bob can detect this disturbance by comparing a subset of their measurement results. If they detect eavesdropping, they can discard the key and try again.

Quantum cryptography is currently used in a limited number of applications, mainly due to the technical challenges and the need for specialized equipment. However, as quantum technologies advance, it's expected that quantum cryptography will become more widely used to secure communications, especially in critical infrastructure, financial institutions, and government systems.


### Let's illustrate the process with an example:

1. Alice prepares qubits and sends them to Bob:

```
Alice's qubits: H, V, D, A, H, V (H = horizontal, V = vertical, D = diagonal, A = anti-diagonal)

```

2. Bob measures qubits using random bases:

```
Bob's bases:    R, R, D, D, R, D (R = rectilinear basis, D = diagonal basis)
Bob's measurements: H, V, -, D, H, -

```

(Here, "-" indicates that Bob's choice of basis didn't match Alice's, so the result is discarded.)

3. Alice and Bob compare bases and identify the matching ones:

```
Alice's bases: R, R, D, D, R, D
Bob's bases:   R, R, D, D, R, D
Matching positions: 1, 2, 3, 4, 5 (using 1-based indexing)

```

4. Alice and Bob generate the shared secret key using the remaining results (i.e., the results corresponding to the matching positions):

```
Alice's key: 0, 1, 1, 1, 0 (0 = H, 1 = V; we ignore the results for D and A)
Bob's key:   0, 1, 1, 1, 0

```

Since Alice and Bob now have the same shared secret key, they can use it to encrypt and decrypt messages using classical encryption algorithms like AES or Triple-DES. The security of this key relies on the fundamental properties of quantum mechanics, which prevent an eavesdropper:))) from obtaining the key without being detected.


