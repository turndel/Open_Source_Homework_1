import sys, argparse

from src.temperaturen.temperaturen import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    ist_warm
)

def main():
    parser = argparse.ArgumentParser(description='Temperatur Umrechnungen')
    parser.add_argument('wert', type=float, help='Temperaturwert')
    parser.add_argument('--von', choices=['c', 'f'], default='c',
                       help='Einheit: c (Celsius) oder f (Fahrenheit)')
    parser.add_argument('--operation', choices=['to_f', 'to_c', 'warm'], 
                       default='to_f', help='Operation')

    args = parser.parse_args()

    if args.operation == 'to_f':
        if args.von == 'f':
            print("Fehler: Kann nicht von Fahrenheit zu Fahrenheit umrechnen")
            sys.exit(1)
        ergebnis = celsius_to_fahrenheit(args.wert)
        print(f"{args.wert}°C = {ergebnis:.2f}°F")

    elif args.operation == 'to_c':
        if args.von == 'c':
            print("Fehler: Kann nicht von Celsius zu Celsius umrechnen")
            sys.exit(1)
        ergebnis = fahrenheit_to_celsius(args.wert)
        print(f"{args.wert}°F = {ergebnis:.2f}°C")

    elif args.operation == 'warm':
        einheit = 'celsius' if args.von == 'c' else 'fahrenheit'
        if ist_warm(args.wert, einheit):
            print(f"{args.wert}°{args.von.upper()} ist warm!")
        else:
            print(f"{args.wert}°{args.von.upper()} ist nicht warm.")

if __name__ == "__main__":
    main()