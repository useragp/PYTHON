klucz = 3    # podaj klucz
oryginal = "WARSZAWKA"    # podaj oryginalną wiadomość
zaszyfrowany = ""    #zaszyfrowana wiadomość (zostanie wyświetlona)

for literka in oryginal:
    index = ord(literka)
    x = index + (klucz%26)         #decymalna reprezentacja zaszyfrowanej literki

# duże literki
    if index in range(65, 91):
        if x > 90:
            x-=26


# małe literki
    elif index in range(97, 123):
        if x > 122:
            x-=26

    zaszyfrowany += chr(x)
print(zaszyfrowany)
