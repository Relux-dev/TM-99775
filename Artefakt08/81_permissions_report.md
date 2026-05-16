# AUDYT BEZPIECZENSTWA: MANIFEST SCANNER
**Raport wykonany przez:** Michal 99775
**Data:** 16.05.2026

---

## 1. Zawartosc RiskyPermission.xml

Zidentyfikowano nastepujace wpisy krytyczne:

- **Debuggable:** true (WYSOKIE RYZYKO - Aplikacja podatna na inzynierie wsteczna).
- **Permissions:** Wykryto uprawnienia dajace dostep do sieci (INTERNET) oraz pamieci zewnetrznej.

## 2. Interpretacja Inzynierska

Z punktu widzenia bezpieczenstwa, najowazniejszym problemem jest flaga debuggable.
Pozwala ona na uzycie komendy adb jdwp do sledzenia procesow aplikacji przez osoby niepowolane.

## 3. Akcja korygujaca

Zaleca sie wdrozenie skryptu do procesu CI/CD (np. w Jenkins/GitHub Actions),
ktory bedzie automatycznie blokowal buildy jesli RiskyPermission.xml wykaze flage debuggable="true".

**Podpis:** Michal 99775
**Data:** 16.05.2026