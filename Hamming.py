import re
import random

POZYCJE = [1, 2, 4, 8, 16]

def binarnie(tekst: str) -> str:        # zamiana wiadomosci wejsciowej na postac binarna (8 bitowa)
    binarnie = ""
    for literka in tekst:
        binarnie += bin(ord(literka)).lstrip("0b").zfill(8)
    return binarnie

def bloki(wiadomosc: str) -> list[str]:             # z wiadomosci w postaci binarnej - bloki 16-sto bitowe
    bloki = re.findall('.{1,16}', wiadomosc)  #zwraca listę kolejnych fragmentów tekstu o długości max 16 znaków.
    return bloki

def dodaj_bity_kontrolne(wiadomosc :str) -> list[str]:

    wynik = []
    i = 0

    for x in range(len(wiadomosc)+len(POZYCJE)):
        if x+1 in POZYCJE:
            i += 1
            wynik.append('0')        # dodaje bit kontrolny - "0"
        else:
            wynik.append(wiadomosc[x-i])     # uzupełnia - dodaje kolejne bity wiadomości

    return wynik

def obliczanie_bitow_kontrolnych(wiadomosc: list[str]):  # obliczanie wartości bitów kontrolnych
    POZYCJE = [1, 2, 4, 8, 16]
    wynik = wiadomosc.copy()

    '''
    dla każdej pozycji np. 4 --> 4 liczy, 4 pomija 
    pętla tworzy wskaźnik p, który kontroluje ile bitów liczyć, a ile pomijać
    jeśli p > 0 i != 0 --> znajduje się w sekwencji "LICZ" i z każdą iteracją zmniejsza się o 1.
    Gdy p == 0 --> skończyła się sekwencja "LICZ" i p znajduje się na sekwencji "POMIŃ" skąd "przechodzi" przez kolejne
    bity aż będzie == 0. Wtedy wraca do sekwencji "LICZ"
    '''

    for pozycja in POZYCJE:
        p = pozycja     # "wskaznik" -> 'p' bitów licz 'p' pomiń
        ile_jedynek = 0

        for bit in range(p, len(wiadomosc) + 1):
            if p > 0:
                if bit != pozycja:                       # nie liczy samego bitu kontrolnego
                    if wiadomosc[bit - 1] == '1':
                        ile_jedynek+=1
                p -= 1
                if p == 0:
                    p -= pozycja + 1
            if p < 0:                       # sekcja "POMIŃ"
                p += 1
                if p == 0:
                    p = pozycja

        wynik[pozycja - 1] = '1' if ile_jedynek % 2 == 1 else '0'               #parzysta - 0, nieparzysta - 1

    return wynik

def kodowanie_wiadomosci(bloki) -> list[str]:    # łączenie bloków zakodowanej wiadomości (z bitami kontrolnymi)
    # -> w jedną listę "bitów"

    zakodowana_wiadomosc = []

    for blok in bloki:
        blok_i_bity_kontrolne = obliczanie_bitow_kontrolnych(dodaj_bity_kontrolne(blok))
        for znak in blok_i_bity_kontrolne:
            zakodowana_wiadomosc.append(znak)
    return zakodowana_wiadomosc

def string(lista: list[str]) -> str:    #zamiana/łączenie listy znaków w string
    s = "".join(lista)
    return s

def wprowadzenie_bledu(wiadomosc: list[str]) -> list[str]:
    # losuje pozycję na której wprowadzony zostanie błąd, zamieniam bit i zwracam gotową wiadomość z błędem

    wiadomosc_z_bledem = wiadomosc.copy()
    bit = random.randint(0, len(wiadomosc_z_bledem)-1)
    print("Pozycja z błędem:\t", bit + 1)
    wiadomosc_z_bledem[bit] = "1" if wiadomosc_z_bledem[bit] == "0" else "0"

    return wiadomosc_z_bledem

def znajdz_blad(wiadomosc: list[str]):
    # 1  obliczanie poprawnych wartości bitów kontrolnych
    wiadomosc_poprawne_bity_kontrolne = obliczanie_bitow_kontrolnych(wiadomosc)

    # 2 które bity kontrolne się nie zgadzają
    syndrom = ""
    for p in reversed(POZYCJE):  # p16 p8 p4 p2 p1
        if wiadomosc[p - 1] != wiadomosc_poprawne_bity_kontrolne[p - 1]:
            syndrom += "1"
        else:
            syndrom += "0"

    s = int(syndrom, 2)
    # print(syndrom, "\t", s)

    return s

def korekcja_bledu(wiadomosc : list[str], pozycja:int) -> list[str]:
    wynik = []
    for i in range(len(wiadomosc)):
        if i == pozycja-1:
            wynik.append("1") if wiadomosc[i] == "0" else wynik.append("0")
        else:
            wynik.append(wiadomosc[i])
    return wynik

# "Czysta" wiadomość -> bez bitów kontrolnych
def wiadomosc_bez_K(wiadomosc):
    wynik = []
    for i in range(len(wiadomosc)):
        if i+1 not in POZYCJE:
            wynik.append(wiadomosc[i])
    return wynik

print()

def wyniki(wiadomosc_wejsciowa):

  #1 wiadomość w formacie binarnym-----"
    Wiadomosc_Binarnie = binarnie(wiadomosc_wejsciowa)
    print("Binarnie:\t", binarnie(wiadomosc_wejsciowa))

    #2 wiadomość w formacie binarnym podzielona na bloki 16-bitowe-----")
    Bloki = bloki(Wiadomosc_Binarnie)
    print("Bloki:\t\t", Bloki)

    #3 kodowanie wiadomosci - [dodawanie i obliczanie wartości bitów kontrolnych]-----")
    Zakodowana_wiadomosc = kodowanie_wiadomosci(Bloki)
    print("Zakodowana wiadomosc:\t", string(Zakodowana_wiadomosc))

    #4 wprowadzanie bledu-----
    print("\n ---------  WPROWADZANIE BLEDU  ---------")
    Wiadomosc_blad = wprowadzenie_bledu(Zakodowana_wiadomosc)       # wiadomosc z błędem -> list[str]
    print("Wiadomosc z błędem:\t\t", string(Wiadomosc_blad))

    #5 pozycja z błędem-----")
    print("\n ---------  KORYGOWANIE BLEDU  ---------")
    Pozycja_bledu = znajdz_blad(Wiadomosc_blad)

    print("Pozycja błędu:\t", Pozycja_bledu)

  #6 korygowanie błędu-----")
    Poprawiona_wiadomosc = korekcja_bledu(Wiadomosc_blad, Pozycja_bledu)
    print("Poprawiona wiadomość:\t", string(Poprawiona_wiadomosc))
    Wiadomosc_bez_bitow_kontrolnych = wiadomosc_bez_K(Poprawiona_wiadomosc)
    print("WIADOMOŚĆ:\t", string(Wiadomosc_bez_bitow_kontrolnych))


wiadomosc_wejsciowa = "ha"


wyniki(wiadomosc_wejsciowa)
print("=================================================")


