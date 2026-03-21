# Open_Source_Homework_1
Dies ist ein einfaches Python-Projekt im Rahmen des 1. Homework Assignments zur VU Open Source Energy System Modeling. 
Dieses Projekt ist Open Source unter der MIT Lizenz [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

## Beschreibung des Projekts
Dieses Projekt enthält drei Funktionen zur Temperaturumrechnung und -bewertung:
- `celsius_to_fahrenheit()`: Umrechnung von Celsius in Fahrenheit
- `fahrenheit_to_celsius()`: Umrechnung von Fahrenheit in Celsius
- `ist_warm()`: Bewertung, ob eine Temperatur als "warm" (über 20°C) gilt

### Funktionen im Detail
#### "celsius_to_fahrenheit(celsius)"
Rechnet eine Temperatur von Celsius in Fahrenheit um.
- **Input:** Temperatur in Celsius (float)
- **Output:** Temperatur in Fahrenheit (float)
- **Beispiel:** "celsius_to_fahrenheit(25)" → "77.00"

#### "fahrenheit_to_celsius(fahrenheit)"
Rechnet eine Temperatur von Fahrenheit in Celsius um.
- **Input:** Temperatur in Fahrenheit (float)
- **Output:** Temperatur in Celsius (float)
- **Beispiel:** "fahrenheit_to_celsius(77)" → "25.00"

#### "ist_warm(temperatur, einheit="celsius")"
Prüft, ob eine Temperatur (Input) über 20°C liegt.
- **Input:** Temperatur (float), Einheit (str, optional: "celsius" oder "fahrenheit")
- **Output:** Boolean (True wenn warm, False wenn nicht warm)
- **Beispiel:** "ist_warm(25)" → "True", "ist_warm(15)" → "False"

# Installation
## 1. Repository klonen
Im Terminal den Pfad zum Ordner eingeben, danach: git clone https://github.com/turndel/Open_Source_Homework_1.git [Name des Ordners]

## 2. Virtuelle Umgebung erstellen
Terminal öffnen und folgende Commands eingeben: 
1. python -m venv .venv 
2. - source .venv/bin/activate  (Auf macOS/Linux)
   - .venv\Scripts\activate.bat (für Windows CMD)
   - .venv\Scripts\Activate.ps1 (für Windows PowerShell)
  
## 3. Requirements installieren
pip install -r requirements.txt

## 4. Projekt im Entwicklermodus installieren
pip install -e .

## Verwendung über Terminal (Kommandozeile)
Das Projekt enthält ein Kommandozeile-Interface (`cli.py`) für schnelle Berechnungen direkt im Terminal.

Über Terminal sieht es dann so aus:
### Celsius zu Fahrenheit
python cli.py 25 --von c --operation to_f

### Fahrenheit zu Celsius
python cli.py 77 --von f --operation to_c

### Prüfen ob warm (Celsius)
python cli.py 25 --operation warm

### Prüfen ob warm (Fahrenheit)
python cli.py 70 --von f --operation warm

### Voraussetzung, Hinweis
Stellen Sie sicher, dass Sie sich im Projektverzeichnis befinden und die virtuelle Umgebung aktiviert ist:
Im Terminal: 
- cd /Ihr-Pfad-zum-Ordner/Open_Source_Homework_1
- source .venv/bin/activate (...)

# Anmerkungen
#### Als Hilfswerkzeug zur Entwicklung dieses Projekts, sowie zum Verständnis, wurde KI verwendet.
