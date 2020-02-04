niz = "CTGCTACACGTCAGATAGTAGTACAGTCTGCACGTCTGTGCAGCACACAGTGAGTGCGTCTGTGCGTGCATCAGTCGTCACTGACTCA"

print("Dolžina sekvence: %i" % len(niz))
print("DNK format: " + niz)
print(niz[0:1])
niz = "A" + niz

# Pretvarjanje DNK format v Binarni format
pretvorba = []
for i in range(len(niz)):
    if niz[i] == 'A':
        pretvorba.append(str(0))
    elif niz[i] == 'C':
        pretvorba.append(str(0))
    elif niz[i] == 'T':
        pretvorba.append(str(1))
    elif niz[i] == 'G':
        pretvorba.append(str(1))

# Pretvorjeni podatki v listu
print(pretvorba)

# Pretvorjeni podatki združeni v niz
skupen_niz = "".join(pretvorba)
print("Binarni format: " + skupen_niz)

# Pretvorba podatkov iz Binarnega formata v ASCII format (besede)
skupen_niz = skupen_niz[2:]
skupen_niz = -len(skupen_niz) % 8 * '0' + skupen_niz

for j in range(1):
    bloki = (skupen_niz[(i + j):(i + 8 + j)] for i in range(0, len(skupen_niz), 8))
    prevod = ''.join(chr(int(char, 2)) for char in bloki)
    print(' ')
    print('ASCII format: ' + prevod)
