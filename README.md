# 🐍 Python Projects – Cryptography & Error Detection

Repozytorium zawiera projekty w Pythonie związane z:
- kryptografią
- operacjami bitowymi
- wykrywaniem i korekcją błędów

Kod pokazuje praktyczne zrozumienie algorytmów oraz pracy na danych binarnych.

---

## 🚀 Kluczowe umiejętności

- Python (operacje na stringach i bitach)
- Implementacja algorytmów kryptograficznych
- Kodowanie i dekodowanie danych
- Debugowanie i analiza błędów
- Myślenie algorytmiczne

---

## 📂 Projekty

### 🧠 Hamming.py (Kod Hamminga)
Implementacja kodu Hamminga do wykrywania i korekcji błędów w transmisji danych.

**Funkcjonalności:**
- konwersja tekstu do postaci binarnej (8-bit)
- podział wiadomości na bloki 16-bitowe
- dodawanie bitów kontrolnych
- obliczanie bitów parzystości
- symulacja błędu (losowa zmiana bitu)
- wykrywanie pozycji błędu (syndrom)
- korekcja błędu
- odzyskiwanie oryginalnej wiadomości

👉 Pokazuje:
- zaawansowaną logikę
- operacje na bitach
- zrozumienie transmisji danych i kontroli błędów

---

### 🔐 szyfr_cezara.py
Implementacja klasycznego szyfru Cezara.

**Funkcjonalności:**
- przesuwanie liter o zadany klucz
- obsługa dużych i małych liter (ASCII)
- zabezpieczenie przed wyjściem poza zakres alfabetu

👉 Pokazuje: manipulacje znakami, logikę warunkową, podstawy kryptografii.

---
### 🔐 decryption_cezar.py
Implementacja deszyfrowania szyfru Cezara.

**Funkcjonalności:**
- przesunięcie znaków o klucz
- obsługa dużych i małych liter (ASCII)
- zabezpieczenie przed wyjściem poza zakres alfabetu

👉 Pokazuje:
- pracę na znakach i ASCII
- logikę warunkową
- podstawy kryptografii

---

### 🔐 szyfr_xor.py
Implementacja szyfrowania XOR z użyciem klucza.

**Funkcjonalności:**
- konwersja znaków do postaci binarnej
- operacje bitowe (XOR)
- cykliczne użycie klucza
- konwersja binarna → znak

👉 Pokazuje:
- operacje bitowe
- zrozumienie szyfrowania symetrycznego
- pracę na poziomie bitów

---

### 🔐 decryption_xor.py
Deszyfrowanie wiadomości zaszyfrowanej szyfrem XOR z kluczem.

**Funkcjonalności:**
- konwersja liter do postaci binarnej 7-bitowej
- operacje bitowe XOR
- cykliczne użycie klucza
- dekodowanie binarnego ciągu do znaków

👉 Pokazuje: operacje bitowe, logikę algorytmiczną, symetryczne szyfrowanie.

---

## ⚙️ Technologie
- Python 3
- Standard Library (re, random)

---

## ▶️ Uruchomienie

```bash
git clone https://github.com/useragp/PYTHON.git
cd PYTHON
python nazwa_pliku.py
