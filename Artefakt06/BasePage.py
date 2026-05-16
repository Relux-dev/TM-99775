import json
import os

class BasePage:
    def __init__(self, selectors_path="../Artefakt05/53_selectors.json"):
        self.selectors_path = selectors_path
        self.selectors = {}
        self._load_selectors()

    def _load_selectors(self):
        if not os.path.exists(self.selectors_path):
            print(f"BLAD: Brak pliku zasobow w {self.selectors_path}")
            return
        try:
            with open(self.selectors_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.selectors = data.get("selectors", {})
                print(f"[BASE_PAGE] Pomyslnie zainicjalizowano mape: {len(self.selectors)} elementow.")
        except Exception as e:
            print(f"BLAD PARSOWANIA: {e}")

    def find_id(self, business_key):
        resource_id = self.selectors.get(business_key)
        if not resource_id:
            print(f"OSTRZEZENIE: Brak klucza '{business_key}' w mapie selektorow!")
        return resource_id

if __name__ == "__main__":
    bp = BasePage()
    test_key = "ADD"
    print(f"Weryfikacja klucza '{test_key}': {bp.find_id(test_key)}")