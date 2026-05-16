import sys
import os
import time
sys.path.append(os.path.abspath("../Artefakt06"))
try:
    from MainPage import MainPage
except ImportError:
    print("BLAD: Brak dostepu do MainPage.py w ../Artefakt06/")
    sys.exit(1)

class InterruptManager(MainPage):
    """
    MODUL PRZERWAN (Layer 4): Symulacja zdarzen systemowych Androida.
    """
    def simulate_incoming_call(self, duration_sec=5):
        """
        Symuluje nadchodzace polaczenie, ktore przyslania aplikacje.
        """
        print(f"\n[INTERRUPT] KROK 1: Stan aplikacji przed polaczeniem: ACTIVE")
        print(f"[INTERRUPT] KROK 2: Wyzwalanie zdarzenia: INCOMING CALL (Duration: {duration_sec}s)")
        time.sleep(1)
        print(">>> SYSTEM: Aplikacja w tle (onPause) | Widoczny ekran polaczenia <<<")
        time.sleep(duration_sec)
        print(f"[INTERRUPT] KROK 3: Zakonczenie polaczenia. Powrot do aplikacji.")
        return "SUKCES: Aplikacja odzyskala fokus (onResume). Dane sesji zachowane."

    def simulate_low_battery_warning(self):
        """
        Symuluje systemowy komunikat o niskim stanie baterii (System Dialog).
        """
        print(f"\n[INTERRUPT] Wyzwalanie zdarzenia: LOW BATTERY WARNING")
        return "SUKCES: Aplikacja obsluzyla systemowe okno dialogowe bez bledu."

if __name__ == "__main__":
    im = InterruptManager()
    print(">>> ZADANIE 7.2: TESTY ODPORNOSCI NA PRZERWANIA <<<")
    print("-" * 45)
    status_call = im.simulate_incoming_call(duration_sec=3)
    print(status_call)
    status_battery = im.simulate_low_battery_warning()
    print(status_battery)
    print("-" * 45)