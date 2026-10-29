## Kryptosystem - szyfr podstawieniowy
Program konsolowy w Pythonie do szyfrowania i deszyfrowania tekstu szyfrem
podstawieniowym.

## Klucz
Klucz podaje użytkownik jako liczbę całkowitą (także ujemną). Alfabet
szyfrowy jest przesunięty cyklicznie o tę liczbę.

## Uruchomienie
Wymagany Python 3.10 lub nowszy.

python main.py


### Menu

> =========== SZYFR PODSTAWIENIOWY ===========
> 1. Szyfruj tekst
> 2. Deszyfruj tekst
> 0. Wyjście


Po wybraniu opcji 1 lub 2 program prosi o tekst i klucz, a następnie
wypisuje wynik.

Jak działa szyfr
Litera z alfabetu jawnego (A-Z) jest zamieniana na literę o tej samej
pozycji w alfabecie szyfrowym. Dla klucza 3:

jawny:    ABCDEFGHIJKLMNOPQRSTUVWXYZ
szyfrowy: DEFGHIJKLMNOPQRSTUVWXYZABC


Wielkość liter jest zachowywana.
Znaki spoza A-Z (spacje, cyfry, interpunkcja, polskie znaki) nie są zmieniane.
Klucze różniące się o wielokrotność 26 dają ten sam wynik (np. 3 i 29).

Przykład: Hello, World! z kluczem 3 daje Khoor, Zruog!.

Obsługa błędów
Pusty tekst - program prosi o ponowne wpisanie.
Klucz pusty lub niebędący liczbą całkowitą (np. abc, 3.5) - komunikat
o błędzie i ponowne pytanie o klucz.
Nieprawidłowa opcja w menu - komunikat i powrót do menu.
Ctrl+C / Ctrl+D - program kończy się bez śladu stosu.