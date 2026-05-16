from BasePage import BasePage

class MainPage(BasePage):
    def __init__(self):
        super().__init__()
        print("[MAIN_PAGE] Ekran glowny zainicjalizowany.")

    def navigate_to_add_content(self):
        selector = self.find_id("ADD")
        if selector:
            return f"SUKCES: Wykonano klikniecie w element UI o ID: '{selector}'"
        return "BLAD: Nie mozna nawigowac - brak selektora 'ADD' w mapie!"

    def get_main_title_status(self):
        selector = self.find_id("TITLE")
        if selector:
            return f"SUKCES: Odnaleziono naglowek strony (ID: {selector}). Status: Widoczny."
        return "INFORMACJA: Element 'TITLE' nie jest zdefiniowany dla tego ekranu."

    def perform_search_action(self, query):
        selector = self.find_id("SEARCH_BUTTON")
        if selector:
            return f"SUKCES: Wpisano '{query}' do pola {selector} i zatwierdzono."
        return f"BLAD: Przycisk wyszukiwania nie zostal zmapowany."

if __name__ == "__main__":
    main_page = MainPage()
    print("-" * 30)
    print(main_page.navigate_to_add_content())
    print(main_page.get_main_title_status())
    print("-" * 30)