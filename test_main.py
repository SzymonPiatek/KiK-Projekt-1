import pytest
from unittest.mock import patch

from main import (
    InvalidKeyError,
    parse_key,
    build_cipher_alphabet,
    encrypt,
    decrypt,
    ask_for_text,
    ask_for_key,
    main
)


class TestParseKey:
    @pytest.mark.parametrize("raw_key, expected", [
        ("1", 1),
        ("  5  ", 5),
        ("-3", -3),
        ("0", 0),
        ("12345", 12345),
    ])
    def test_parse_key_valid(self, raw_key, expected):
        assert parse_key(raw_key) == expected

    @pytest.mark.parametrize("raw_key", [
        "",
        "   ",
        "abc",
        "1.5",
        "3a",
    ])
    def test_parse_key_invalid(self, raw_key):
        with pytest.raises(InvalidKeyError):
            parse_key(raw_key)


class TestCipherAlphabet:
    @pytest.mark.parametrize("key, expected", [
        (0, "ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
        (1, "BCDEFGHIJKLMNOPQRSTUVWXYZA"),
        (3, "DEFGHIJKLMNOPQRSTUVWXYZABC"),
        (26, "ABCDEFGHIJKLMNOPQRSTUVWXYZ"),  # Pełen obrót
        (27, "BCDEFGHIJKLMNOPQRSTUVWXYZA"),  # Powyżej 26
        (-1, "ZABCDEFGHIJKLMNOPQRSTUVWXY"),  # Ujemne
        (-27, "ZABCDEFGHIJKLMNOPQRSTUVWXY"),
    ])
    def test_build_cipher_alphabet(self, key, expected):
        assert build_cipher_alphabet(key) == expected


class TestEncryptionDecryption:
    @pytest.mark.parametrize("text, key, expected", [
        ("HELLO", 3, "KHOOR"),
        ("hello", 3, "khoor"),
        ("Hello, World! 123", 3, "Khoor, Zruog! 123"), # Znaki interpunkcyjne i cyfry
        ("abc", 0, "abc"),
        ("Python", -1, "Oxsgnm"),
    ])
    def test_encrypt(self, text, key, expected):
        assert encrypt(text, key) == expected

    @pytest.mark.parametrize("text, key, expected", [
        ("KHOOR", 3, "HELLO"),
        ("khoor", 3, "hello"),
        ("Khoor, Zruog! 123", 3, "Hello, World! 123"),
        ("abc", 0, "abc"),
        ("Oxsgnm", -1, "Python"),
    ])
    def test_decrypt(self, text, key, expected):
        assert decrypt(text, key) == expected

    def test_encryption_decryption_symmetry(self):
        original = "Secret Message! @2023"
        key = 14
        encrypted = encrypt(original, key)
        decrypted = decrypt(encrypted, key)
        assert decrypted == original


class TestUserInputRequests:
    @patch("builtins.input", side_effect=["", "   ", "Valid Text"])
    def test_ask_for_text(self, mock_input):
        # Powinno zignorować dwa pierwsze puste wejścia i zwrócić trzecie
        result = ask_for_text("Podaj tekst: ")
        assert result == "Valid Text"
        assert mock_input.call_count == 3

    @patch("builtins.input", side_effect=["abc", "", "3.14", "7"])
    def test_ask_for_key(self, mock_input):
        # Powinno ignorować błędy (tekst, puste, float) i zwrócić poprawny int
        result = ask_for_key()
        assert result == 7
        assert mock_input.call_count == 4


class TestMainApplicationLoop:
    @patch("builtins.input", side_effect=["0"])
    @patch("builtins.print")
    def test_main_exit(self, mock_print, mock_input):
        # Test wyjścia z programu (opcja 0)
        main()
        mock_print.assert_any_call("Do widzenia!")

    @patch("builtins.input", side_effect=["invalid", "0"])
    @patch("builtins.print")
    def test_main_invalid_option(self, mock_print, mock_input):
        # Test podania nieprawidłowej opcji w menu
        main()
        mock_print.assert_any_call("Błąd: nieprawidłowa opcja. Wpisz 1, 2 lub 0.")

    @patch("builtins.input", side_effect=["1", "Tajny tekst", "3", "0"])
    @patch("builtins.print")
    def test_main_encrypt_flow(self, mock_print, mock_input):
        # Przepływ: wybór szyfrowania (1) -> tekst -> klucz -> wyjście (0)
        main()
        mock_print.assert_any_call("\nWynik: Wdmqb whnvw")

    @patch("builtins.input", side_effect=["2", "Wdmqb whnvw", "3", "0"])
    @patch("builtins.print")
    def test_main_decrypt_flow(self, mock_print, mock_input):
        # Przepływ: wybór deszyfrowania (2) -> tekst -> klucz -> wyjście (0)
        main()
        mock_print.assert_any_call("\nWynik: Tajny tekst")
