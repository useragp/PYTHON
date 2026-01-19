import random
lista = []
parzyste = []

for _ in range(50):
    liczba = (random.randint(-100,100))
    lista.append(liczba)
    if liczba % 2 == 0:
        parzyste.append(liczba)

print("Lista liczb:\t", lista)
print("Liczby przyste:\t", parzyste)

decyzja = input("\nJeśli chcesz przemożyć te liczby przez 3: \t\twpisz 1.\nJeśli chcesz podnieść te liczby do kwadratu: \twpisz 2.\n")
zwrot_decyzji = []

for l in parzyste:
    if decyzja == "1":
        zwrot_decyzji.append(l * 3)
    elif decyzja == "2":
        zwrot_decyzji.append(l**2)
    else:
        print("NIEPROPRAWNA LICZBA")

print("\nPo decyzji:\t", zwrot_decyzji)
print("Posortowana lista:\t", sorted(zwrot_decyzji))
print("Zsumowana lista:", sum(zwrot_decyzji))