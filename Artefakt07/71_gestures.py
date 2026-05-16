import sys
import os
import time
sys.path.append(os.path.abspath("../Artefakt06"))
try:
    from MainPage import MainPage
except ImportError:
    print("BLAD: Nie znaleziono MainPage.py w ../Artefakt06/")
    sys.exit(1)

class GestureAutomator(MainPage):
    """
    MODUL GESTOW (Layer 4): Rozszerzenie Page Objectu o fizyke dotyku.
    """
    def scroll_down_logic(self, start_y=0.8, end_y=0.2, duration_ms=1000):
        """
        Symulacja gestu SCROLL DOWN (procentowo).
        """
        print(f"[GESTURE] Start Swipe: Y={start_y} -> End Y={end_y} (t={duration_ms}ms)")
        if duration_ms < 200:
            return "BLAD: Gest zbyt szybki - grozi brakiem reakcji UI (Flick)."
        return f"SUKCES: Przewinieto liste o {int((start_y - end_y)*100)}% wysokosci ekranu."

    def long_press_element(self, element_key):
        """
        Symulacja Long Press na Resource ID.
        """
        selector = self.find_id(element_key)
        if selector:
            return f"SUKCES: Wykonano LONG PRESS (2s) na elemencie: {selector}"
        return f"BLAD: Nie odnaleziono elementu {element_key} w mapie selektorow."

if __name__ == "__main__":
    ga = GestureAutomator()
    print(">>> ZADANIE 7.1: TESTY FIZYKI DOTYKU <<<")
    print("-" * 30)
    print(ga.scroll_down_logic(duration_ms=800))
    print(ga.long_press_element("LIST_ITEM"))
    print("-" * 30)