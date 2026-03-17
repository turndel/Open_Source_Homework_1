# Open_Source_Homework_1

Dies ist ein einfaches Python-Projekt im Rahmen des 1. Homework Assignments zur VU Open Source Energy System Modeling. 

## Beschreibung des Projekts

Dieses Projekt enthält drei Funktionen zur Temperaturumrechnung und -bewertung:
- Umrechnung von Celsius in Fahrenheit, bzw.
- Umrechnung von Fahrenheit in Celsius  
- Bewertung, ob eine Temperatur als "warm" oder "kalt" gilt (abhängig von der angegebenen Temperatur)

## Funktionen im Detail

### "celsius_to_fahrenheit(celsius)"
Rechnet eine Temperatur von Celsius in Fahrenheit um.
- **Input:** Temperatur in Celsius (float)
- **Output:** Temperatur in Fahrenheit (float)
- **Beispiel:** "celsius_to_fahrenheit(25)" → "77.00"

### "fahrenheit_to_celsius(fahrenheit)"
Rechnet eine Temperatur von Fahrenheit in Celsius um.
- **Input:** Temperatur in Fahrenheit (float)
- **Output:** Temperatur in Celsius (float)
- **Beispiel:** "fahrenheit_to_celsius(77)" → "25.00"

### "ist_warm(temperatur, einheit="celsius")"
Prüft, ob eine Temperatur (Input) über 20°C liegt.
- **Input:** Temperatur (float), Einheit (str, optional: "celsius" oder "fahrenheit")
- **Output:** Boolean (True wenn warm, False wenn nicht warm)
- **Beispiel:** "ist_warm(25)" → "True", "ist_warm(15)" → "False"
