import string

ALPHABET = string.ascii_uppercase  # alfabet jawny: A-Z (26 liter)
MIN_KEYWORD_LENGTH = 8             # minimalna długość słowa kluczowego


class InvalidKeyError(ValueError):
    """Zgłaszany, gdy klucz podany przez użytkownika jest niepoprawny."""


def main() -> None:
    """Punkt wejścia programu (na razie pusty szkielet)."""
    print("Kryptosystem - szyfr podstawieniowy")


if __name__ == "__main__":
    main()
