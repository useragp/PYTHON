klucz = "c"
oryginal = "BCDEF"
zaszyfrowany = ""

def xor(x, y):
    if x == y:
        return 0
    else:
        return 1

def bitowo(litera):
    return bin(ord(litera)).lstrip("0b").zfill(7)

dl = 0  # długość klucza
for literka in oryginal:
    if dl == len(klucz):
        dl = 0              # "pętla" - klucz

    zaszyfrowana_literka = ""
    for i in range(7):      #  długość binarnej reprezentacji literki
        bit = xor(int(bitowo(literka)[i]), int(bitowo(klucz[dl])[i])) #bit zaszyfrowanego tekstu
        zaszyfrowana_literka += str(bit)

    zaszyfrowany += chr(int(zaszyfrowana_literka, 2))   #zaszyfrowana literka z binarnego na decymalny
    dl += 1  # następna literka klucza

print(zaszyfrowany)





