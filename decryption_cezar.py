klucz = 3
oryginal = ""
zaszyfrowany = "zduvcdznd"

for literka in zaszyfrowany:
    index = ord(literka)
    x = index - (klucz%26)  #decymalna reprezentacja odszyfrowanej literki

    #duże literki
    if index in range(65, 91):
        if x < 65:
            x += 26


    # #małe literki
    elif index in range(97, 123):
        if x < 97:
            x += 26


    oryginal += chr(x)
print(oryginal)