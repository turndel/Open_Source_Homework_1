# Test-Code zur Überprüfung des Codes
import os
import sys

# Füge den Hauptordner zum Python-Pfad hinzu
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Jetzt kann importiert werden
from src.temperaturen.temperaturen import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    ist_warm,
)


# Testen der jeweiligen Funktionen
def test_celsius_to_fahrenheit():

    """ Testet die Celsius->Fahrenheit Umrechnung. """
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert round(celsius_to_fahrenheit(20), 2) == 68.00

def test_fahrenheit_to_celsius():

    """ Testet die Fahrenheit->Celsius Umrechnung. """
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    assert round(fahrenheit_to_celsius(68), 2) == 20.00

def test_ist_warm():

    """ Testet die Warm-Erkennung. """
    assert ist_warm(25) is True   # Warm
    assert ist_warm(20) is False  # Grenze: nicht warm

    assert ist_warm(15) is False  # Nicht warm
    assert ist_warm(-5) is False  # Kalt
    assert ist_warm(70, "fahrenheit") is True  # Warm in Fahrenheit
