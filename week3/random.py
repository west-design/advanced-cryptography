def lfsr(seed, taps, length):
    register = seed.copy()
    sequence = []
    for _ in range(length):
        output = register[-1]
        sequence.append(output)
        feedback = 0
        for tap in taps:
            feedback ^= register[tap]
        register = [feedback] + register[:-1]
    return sequence
seed = [1, 0, 1, 1]
taps = [0, 1]
length = 100
sequence = lfsr(seed, taps, length)
ones = sequence.count(1)
zeros = sequence.count(0)
print("Sequence:")
print("".join(map(str, sequence)))
print("Total Bits :", length)
print("Number of Ones :", ones)
print("Number of Zeros:", zeros)
if abs(ones - zeros) <= 10:
    print("Result: The sequence appears random.")
else:
    print("Result: The sequence may not be sufficiently random.")