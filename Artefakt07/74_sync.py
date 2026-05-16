import sys
import os
import time
sys.path.append(os.path.abspath("../Artefakt06"))
from MainPage import MainPage

class SyncManager(MainPage):
    """
    MODUL SYNCHRONIZACJI (Layer 4): Inteligentne czekanie na UI.
    """
    def wait_for_element_and_click(self, business_key, timeout=10):
        """
        Symulacja profesjonalnego Explicit Wait (WebDriverWait).
        """
        selector = self.find_id(business_key)
        if not selector:
            return f"BLAD: Brak klucza '{business_key}' w mapie!"
        print(f"[SYNC] Rozpoczynam oczekiwanie na: {selector} (max {timeout}s)")
        start_time = time.time()
        found = False
        # W rzeczywistym Appium:
        # element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(...))
        time.sleep(1.5)
        found = True
        end_time = time.time()
        duration = round(end_time - start_time, 2)
        if found:
            return f"SUKCES: Element '{selector}' odnaleziony i klikniety po {duration}s."
        return f"TIMEOUT: Element '{selector}' nie pojawil sie w ciagu {timeout}s!"

if __name__ == "__main__":
    sm = SyncManager()
    print(">>> ZADANIE 7.4: TESTY SYNCHRONIZACJI DYNAMICZNEJ <<<")
    print("-" * 50)
    print(sm.wait_for_element_and_click("ADD"))
    print(sm.wait_for_element_and_click("NON_EXISTENT_BUTTON"))
    print("-" * 50)