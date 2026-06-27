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
length = 20              

sequence = lfsr(seed, taps, length)

print("Initial Seed:", seed)
print(" Sequence:")
print("".join(map(str, sequence)))