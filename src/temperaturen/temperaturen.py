# FUNKTION ZUR TEMPERATUR-UMRECHNUNG

# Rechnet Celsius in Fahrenheit um.
def celsius_to_fahrenheit(celsius):

    # Args:
    # Celsius: Temperatur in Celsius
    # Returns: Temperatur in Fahrenheit

    temp_fahr = (celsius * 9/5) + 32
    print(f"{celsius:.2f}°C entspricht {temp_fahr:.2f}°F")
    return(temp_fahr)


# Rechnet Fahrenheit in Celsius um.
def fahrenheit_to_celsius(fahrenheit):

    # Args:
    # Fahrenheit: Temperatur in Fahrenheit
    # Returns: Temperatur in Celsius

    temp_cels = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit:.2f}°F entspricht {temp_cels:.2f}°C")
    return(temp_cels)


# Prüft ob eine Temperatur als "warm" gilt (über 20°C).
def ist_warm(temperatur, einheit="celsius"):

    # Args:
    # temperatur: Die Temperatur als Zahlenwert
    # einheit: "celsius" oder "fahrenheit" (Standard: celsius)
    # Returns:
    # True wenn Temperatur warm (>20°C), sonst False

    # Ist die Einheit in Fahrenheit, soll sie zu Celsius umgewandelt werden.
    if einheit == "fahrenheit":
        temperatur_celsius = fahrenheit_to_celsius(temperatur)
    else:
        temperatur_celsius = temperatur

    # Ist die Temperatur zu hoch, oder unterhalb der Grenze?
    if temperatur_celsius > 20:
        print(f"{temperatur_celsius:.2f}°C ist warm. Ich brauch Wasser!")
        return True

    elif temperatur_celsius >= 0:  # Alles zwischen 0 und 20 (inklusive 20)
        print(f"{temperatur_celsius:.2f}°C ist nicht warm. Kein Wasser nötig.")
        return False

    else:  # temperatur_celsius < 0
        print(f"{temperatur_celsius:.2f}°C ist kalt. Brrrrr!")
        return False