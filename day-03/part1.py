from input import input_str

bits_list = input_str.splitlines()
sum_of_bits = [0] * 12

for bits in bits_list:
    print(type(bits))
    for index, bit in enumerate(bits):
        sum_of_bits[index] += int(bit)

sum_of_bits = [round(bit / len(bits_list)) for bit in sum_of_bits]


print(sum_of_bits)
sum_of_bits.reverse()
print(sum_of_bits)

epsilon = 0
gamma = 0


for index, bit in enumerate(sum_of_bits):
    epsilon += (2 ** index) * bit
    gamma += (2 ** index) * ((bit + 1) % 2)

print(epsilon * gamma)
