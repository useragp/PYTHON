klucz = "c"
oryginal = ""
zaszyfrowany = "!!!&%!"

def xor(x, y):
    if x == y:
        return 0
    else:
        return 1

def bitowo(litera):
    return bin(ord(litera)).lstrip("0b").zfill(7)

dl = 0
for literka in zaszyfrowany:
    if dl == len(klucz):
        dl = 0

    literka_oryginal = ''
    for i in range(7):
        literka_oryginal_bitowo = xor(int(bitowo(literka)[i]), int(bitowo(klucz[dl])[i]))
        literka_oryginal += str(literka_oryginal_bitowo)

    oryginal += chr(int(literka_oryginal, 2))
    dl += 1

print(oryginal)




