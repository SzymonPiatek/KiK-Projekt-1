import string

ALPHABET = string.ascii_uppercase  # alfabet jawny: A-Z (26 liter)


class InvalidKeyError(ValueError):
    """Zgłaszany, gdy klucz podany przez użytkownika jest niepoprawny."""


def parse_key(raw_key: str) -> int:
    """Zamienia tekst wpisany przez użytkownika na klucz (liczbę całkowitą)."""
    raw_key = raw_key.strip()

    if not raw_key:
        raise InvalidKeyError("Klucz nie może być pusty.")

    try:
        return int(raw_key)
    except ValueError:
        raise InvalidKeyError(
            f"Klucz musi być liczbą całkowitą (podano: '{raw_key}')."
        ) from None


def build_cipher_alphabet(key: int) -> str:
    """Buduje alfabet szyfrowy: alfabet jawny przesunięty cyklicznie o key."""
    # Modulo sprawia, że działają też liczby ujemne i większe niż 26
    shift = key % len(ALPHABET)
    return ALPHABET[shift:] + ALPHABET[:shift]


def build_translation_table(source: str, target: str) -> dict[int, int]:
    """Tworzy tablicę dla str.translate (litery wielkie i małe)."""
    table = str.maketrans(source, target)
    table.update(str.maketrans(source.lower(), target.lower()))
    return table


def encrypt(text: str, key: int) -> str:
    """Szyfruje tekst: alfabet jawny -> alfabet szyfrowy."""
    cipher_alphabet = build_cipher_alphabet(key)
    return text.translate(build_translation_table(ALPHABET, cipher_alphabet))


def decrypt(text: str, key: int) -> str:
    """Deszyfruje tekst: alfabet szyfrowy -> alfabet jawny."""
    cipher_alphabet = build_cipher_alphabet(key)
    return text.translate(build_translation_table(cipher_alphabet, ALPHABET))


def ask_for_text(prompt: str) -> str:
    """Prosi o niepusty tekst, powtarzając pytanie aż do skutku."""
    while True:
        text = input(prompt)
        if text.strip():
            return text
        print("Błąd: tekst nie może być pusty. Spróbuj ponownie.")


def ask_for_key() -> int:
    """Prosi o klucz, powtarzając pytanie aż do podania poprawnego."""
    while True:
        try:
            return parse_key(input("Podaj klucz (liczba całkowita): "))
        except InvalidKeyError as error:
            print(f"Błąd: {error}")


def run_operation(operation, title: str) -> None:
    """Wspólny przebieg szyfrowania i deszyfrowania: tekst, klucz, wynik."""
    print(f"\n--- {title} ---")
    text = ask_for_text("Podaj tekst: ")
    key = ask_for_key()
    print(f"\nWynik: {operation(text, key)}")


def main() -> None:
    """Punkt wejścia programu (na razie pusty szkielet)."""
    print("Kryptosystem - szyfr podstawieniowy")


if __name__ == "__main__":
    main()
