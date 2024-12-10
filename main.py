import json
from typing import List, Dict

# Datei: weihnachtsgeschenke_manager.py

class WeihnachtsgeschenkeManager:
    def __init__(self, db_file: str = "weihnachtsgeschenke.json"):
        """Initialisiert den Manager und lädt Daten aus der JSON-Datenbank."""
        self.db_file = db_file
        self.data = self.lade_daten()

    def lade_daten(self) -> Dict:
        """Lädt Daten aus der JSON-Datei."""
        try:
            with open(self.db_file, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def speichere_daten(self):
        """Speichert Daten in der JSON-Datei."""
        with open(self.db_file, "w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)

    def add_beschenkter(self, name: str):
        """Fügt einen neuen Beschenkten hinzu."""
        if name not in self.data:
            self.data[name] = []
            self.speichere_daten()
            print(f"Beschenkter '{name}' hinzugefügt.")
        else:
            print(f"Beschenkter '{name}' existiert bereits.")

    def add_geschenk(self, name: str, geschenk: str):
        """Fügt ein Geschenk für einen Beschenkten hinzu."""
        if name in self.data:
            self.data[name].append(geschenk)
            self.speichere_daten()
            print(f"Geschenk '{geschenk}' für '{name}' hinzugefügt.")
        else:
            print(f"Beschenkter '{name}' nicht gefunden. Bitte zuerst hinzufügen.")

    def zeige_alle(self):
        """Zeigt alle Beschenkten und ihre Geschenke."""
        if not self.data:
            print("Keine Einträge gefunden.")
        else:
            for name, geschenke in self.data.items():
                print(f"\n{name}:")
                for i, geschenk in enumerate(geschenke, start=1):
                    print(f"  {i}. {geschenk}")

    def loesche_geschenk(self, name: str, index: int):
        """Löscht ein Geschenk basierend auf dem Index."""
        if name in self.data and 0 <= index < len(self.data[name]):
            entfernt = self.data[name].pop(index)
            self.speichere_daten()
            print(f"Geschenk '{entfernt}' entfernt.")
        else:
            print(f"Ungültiger Index oder Beschenkter '{name}' nicht gefunden.")

    def loesche_beschenkter(self, name: str):
        """Löscht einen Beschenkten und alle zugehörigen Geschenke."""
        if name in self.data:
            del self.data[name]
            self.speichere_daten()
            print(f"Beschenkter '{name}' und alle Geschenke gelöscht.")
        else:
            print(f"Beschenkter '{name}' nicht gefunden.")

# Konsolenschnittstelle
def main():
    manager = WeihnachtsgeschenkeManager()

    while True:
        print("\nWeihnachtsgeschenke Manager")
        print("1. Beschenkten hinzufügen")
        print("2. Geschenk hinzufügen")
        print("3. Alle Einträge anzeigen")
        print("4. Geschenk löschen")
        print("5. Beschenkten löschen")
        print("6. Beenden")

        try:
            auswahl = int(input("Wähle eine Option: "))
        except ValueError:
            print("Ungültige Eingabe. Bitte eine Zahl eingeben.")
            continue

        if auswahl == 1:
            name = input("Name des Beschenkten: ").strip()
            manager.add_beschenkter(name)
        elif auswahl == 2:
            name = input("Name des Beschenkten: ").strip()
            geschenk = input("Geschenk: ").strip()
            manager.add_geschenk(name, geschenk)
        elif auswahl == 3:
            manager.zeige_alle()
        elif auswahl == 4:
            name = input("Name des Beschenkten: ").strip()
            try:
                index = int(input("Index des Geschenks (beginnend bei 1): ")) - 1
                manager.loesche_geschenk(name, index)
            except ValueError:
                print("Ungültiger Index.")
        elif auswahl == 5:
            name = input("Name des Beschenkten: ").strip()
            manager.loesche_beschenkter(name)
        elif auswahl == 6:
            print("Auf Wiedersehen!")
            break
        else:
            print("Ungültige Auswahl.")

if __name__ == "__main__":
    main()
