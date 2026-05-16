# RAPORT ANALIZY WYCIEKOW (SECRETS)
**Student:** Michal
**Indeks:** 99775
**Data raportu:** 16.05.2026

---

## 1. Trzy najbardziej grozne znaleziska (High Risk)

1. **[URL_Endpoint] -> http://www.example.com/lala/foobar@example.com**
   - Uzasadnienie: Zawiera adres e-mail w sciezce URL, co sugeruje wyciek danych uzytkownika
     lub twardo zakodowane poswiadczenia testowe.

2. **[Potential_Secret] -> password**
   - Uzasadnienie: Obecnosc tego slowa w strings.xml sugeruje, ze deweloper mogl tam zapisac
     domyslne haslo do bazy lub uslugi.

3. **[Potential_Secret] -> reset_password_warning**
   - Uzasadnienie: Moze wskazywac na lokalne przechowywanie mechanizmow resetu hasla,
     ktore moga zostac zmanipulowane.

## 2. Trzy znaleziska typu False Positive (Low/No Risk)

1. **[URL_Endpoint] -> http://www.google.com**
   - Uzasadnienie: Standardowy adres URL wyszukiwarki, uzywany do testowania lacznosci.

2. **[API_Key_Format] -> table_layout_1_triple_star**
   - Uzasadnienie: Mimo ze pasuje do wzorca dlugiego ciagu, jest to nazwa identyfikatora elementu UI.

3. **[API_Key_Format] -> abc_font_family_display_3_material**
   - Uzasadnienie: Nazwa zasobu systemowego zwiazanego z czcionkami biblioteki Material Design.

---

## Wnioski koncowe

Automatyczne skanowanie RegEx jest skuteczne, ale wymaga manualnej weryfikacji inzyniera,
poniewaz skrypt nie rozumie kontekstu biznesowego aplikacji.