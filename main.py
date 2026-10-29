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


def main() -> None:
    """Punkt wejścia programu (na razie pusty szkielet)."""
    print("Kryptosystem - szyfr podstawieniowy")


if __name__ == "__main__":
    main()
