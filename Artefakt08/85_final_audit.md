# RAPORT Z AUDYTU BEZPIECZENSTWA: APIDEMOS
**Data:** 16.05.2026
**Audytor:** Michal 99775
**Projekt:** Mobilny System Demonstracyjny (Android)

---

## 1. OCENA KONCOWA (SECURITY SCORE)
**WYNIK:** 0/100
**STATUS:** REJECTED

---

## 2. KLUCZOWE OBSZARY RYZYKA

### A. Konfiguracja Systemowa (Zadanie 8.1)
**Problem:** Flaga debuggable="true" w AndroidManifest.xml.
**Wplyw:** Umozliwia napastnikowi podpiecie debuggera i kradziez danych z pamieci ulotnej.

### B. Wycieki Danych (Zadanie 8.2)
**Problem:** Wykryto twardo zakodowane slowa kluczowe (np. password) w zasobach strings.xml.
**Wplyw:** Ryzyko przejecia konta testowego lub dostepu do niepublicznych endpointow.

### C. Biblioteki Zewnetrzne (Zadanie 8.3)
**Problem:** Uzycie org.apache.commons w wersji 1.0.0.
**Wplyw:** Podatnosc CVE-2015-7501 (CRITICAL) pozwalajaca na zdalne wykonanie kodu na urzadzeniu uzytkownika.

---

## 3. MAPA DROGOWA NAPRAWCZA (REMEDIATION)

1. **[PRIORYTET 1]:** Aktualizacja biblioteki org.apache.commons do najnowszej bezpiecznej wersji.
2. **[PRIORYTET 1]:** Wylaczenie trybu debugowania w wersji produkcyjnej (Release build).
3. **[PRIORYTET 2]:** Przeniesienie wszystkich wrazliwych ciagow znakow ze strings.xml
   do bezpiecznego magazynu kluczy (Android Keystore).

---

## WNIOSKI KONCOWE

Aplikacja w obecnym stanie nie moze zostac opublikowana.
Poziom ryzyka zwiazanego z bibliotekami firm trzecich oraz bledna konfiguracja manifestu
jest zbyt wysoki dla bezpiecznego uzytkowania.

**Decyzja:** NO-GO
**Audytor:** Michal 99775