from input import input_str

bits_list = input_str.splitlines()


def get_most_common(bits_list_):
    sum_of_bits = [0] * 12

    for bits in bits_list_:
        for index, bit in enumerate(bits):
            sum_of_bits[index] += int(bit)

    most_common_bits = [round(float(bit) / len(bits_list_)) for bit in sum_of_bits]
    return most_common_bits


epsilon_b = []
eps_list = bits_list
gam_list = bits_list


eps_final = None
gam_final = None


for index in range(12):

    new_eps_list = []

    e_m = get_most_common(eps_list)
    for bits in eps_list:
        if int(bits[index]) == e_m[index]:
            new_eps_list.append(bits)
    eps_list = new_eps_list

    if len(eps_list) == 1:
        eps_final = eps_list[0]
        break

for index in range(12):

    new_gam_list = []

    g_m = get_most_common(gam_list)
    for bits in gam_list:
        if int(bits[index]) != g_m[index]:
            new_gam_list.append(bits)
    gam_list = new_gam_list

    if len(gam_list) == 1:
        gam_final = gam_list[0]
        break

eps_bits = [int(_) for _ in eps_final]
gam_bits = [int(_) for _ in gam_final]

eps_bits.reverse()
gam_bits.reverse()

epsilon = 0
gamma = 0
for index, bit in enumerate(eps_bits):
    epsilon += (2 ** index) * bit

for index, bit in enumerate(gam_bits):
    gamma += (2 ** index) * bit

print(epsilon * gamma)
