# 📱 Testowanie Aplikacji Mobilnych — Portfolio Laboratoryjne (TM-99775)

Kompletny, semestralny projekt z automatyzacji testów aplikacji mobilnych w modelu **Cloud-Ready / Headless** — od konteneryzacji środowiska, przez automatyzację UI (Appium) i analizę bezpieczeństwa, aż po testy API i pełny pipeline CI/CD z raportowaniem Allure.

**Uczelnia:** Uniwersytet WSB Merito Wrocław · **Przedmiot:** Testowanie aplikacji mobilnych
**Prowadzący:** mgr Mariusz Dworniczak
**Autor:** Michał · **Nr albumu:** 99775
**Aplikacja testowa:** ApiDemos (Android)

---

## 🧰 Stack technologiczny

| Obszar | Technologie |
| :--- | :--- |
| Język | Python 3.10+ |
| Automatyzacja UI | Appium 2.x (UiAutomator2) |
| Testy API | `requests`, `jsonschema` |
| Framework testowy | `pytest` |
| Infrastruktura | Docker, Docker Compose |
| Raportowanie | Allure Framework |
| Analiza statyczna | ADB, apktool, skanery własne (MobSF-style) |
| CI/CD | `pipeline.py` (One-Click) |

---

## 📁 Struktura repozytorium

| Folder | Blok | Temat |
| :--- | :--- | :--- |
| `Artefakt01` | 1 | Środowisko, struktura repo i pierwszy „push” |
| `Artefakt02` | 2 | ADB i statyczna analiza APK |
| `Artefakt03` | 3 | Docker-Compose i serwer Appium |
| `Artefakt04` / `Artefakt05` | 4–5 | Inspektor, lokalizatory i pierwszy skrypt |
| `Artefakt06` | 6 | Page Object Model (POM) |
| `Artefakt07` | 7 | Gesty i testy przerwań |
| `Artefakt08` | 8 | Statyczna analiza bezpieczeństwa |
| `Artefakt09` | 9 | Testowanie API dla Mobile |
| `Artefakt10` | 10 | Raportowanie i automatyzacja (CI/CD) |

---

## 📅 Przebieg laboratorium (Bloki 1–10)

### 🔹 Blok 1 — Środowisko i pierwszy „push” (`Artefakt01`)
Konfiguracja repozytorium Git i podstaw konteneryzacji. Zbudowany minimalny obraz Docker (Alpine) z `ENTRYPOINT` wypisującym identyfikator studenta, a następnie wykonany pierwszy build i `git push`.
**Wniosek:** Obrazy Docker dają powtarzalne, izolowane środowisko niezależne od systemu hosta — eliminują „piekło zależności” i pozwalają stawiać/usuwać środowisko jedną komendą.

### 🔹 Blok 2 — ADB i statyczna analiza APK (`Artefakt02`)
Dekompilacja pliku `.apk` (apktool) i analiza jego wnętrza: `AndroidManifest.xml`, zasoby, struktura archiwum (`zip_structure.txt`).
**Wniosek:** Analiza statyczna pozwala ocenić uprawnienia i zawartość aplikacji bez jej uruchamiania — tanio i szybko, jeszcze przed testami dynamicznymi.

### 🔹 Blok 3 — Docker-Compose i serwer Appium (`Artefakt03`)
Uruchomienie silnika **Appium 2.x** w kontenerze za pomocą `docker-compose.yaml` (port 4723), z odseparowaniem od systemu operacyjnego hosta.

### 🔹 Bloki 4–5 — Inspektor, lokalizatory i pierwszy skrypt (`Artefakt05`)
Praca z Appium Inspectorem i budowa pierwszej sesji automatycznej (`step1`–`step5`): definicja capabilities (`51_caps.json`), lokalizatory **Resource-ID i XPath** (`53_selectors.json`), nawiązanie sesji oraz zapis wyniku (`55_result.xml`).

### 🔹 Blok 6 — Page Object Model (`Artefakt06`)
Wdrożenie wzorca **POM** (`BasePage.py`, `MainPage.py`) oddzielającego logikę testu od szczegółów UI, z audytem architektury (`64_audit_report.md`).
**Wniosek:** Selektory trzymane w plikach JSON pozwalają przy zmianie UI poprawić **jeden plik zamiast wielu testów** — szacowane skrócenie czasu naprawy o ~80%.

### 🔹 Blok 7 — Gesty i testy przerwań (`Artefakt07`)
Symulacja gestów (scroll, swipe, long-press), testy przerwań systemowych (połączenie przychodzące, okna dialogowe), zarządzanie stanem (obrót ekranu) oraz synchronizacja przez **Explicit Wait**. Raport stabilności: `75_stress_report.md`.
**Wniosek:** Explicit Wait skrócił czas egzekucji o ~8,5 s względem sztywnego `time.sleep`, a aplikacja poprawnie obsługuje cykl `onPause → onResume`.

### 🔹 Blok 8 — Statyczna analiza bezpieczeństwa (`Artefakt08`)
Pełny audyt bezpieczeństwa: skaner manifestu (`81`), wyszukiwarka twardo zakodowanych sekretów (`82`), audyt bibliotek pod kątem CVE (`83`) i scoring ryzyka (`84`).
**Wynik audytu (`85_final_audit.md`):** Security Score **0/100 — REJECTED**; wykryto m.in. `debuggable="true"`, hardcoded `password` oraz podatną bibliotekę (CVE-2015-7501, RCE).

### 🔹 Blok 9 — Testowanie API dla Mobile (`Artefakt09`)
Testy warstwy backendowej (headless) z biblioteką `requests`:
- `91_api_setup.py` — połączenie z API i weryfikacja kodu **200 OK**
- `92_crud_test.py` — tworzenie zasobu (POST), kod **201 Created**
- `93_schema_test.py` — walidacja kontraktu **JSON Schema** (typy danych)
- `94_negative_test.py` — testy negatywne (404, obsługa błędów 4xx/5xx)
- `95_hybrid_test.py` — scenariusz hybrydowy **API + Appium**
**Wniosek:** Testy API wyłapują błędy na styku App ↔ Backend w milisekundach, zanim uruchomimy wolniejsze testy UI.

### 🔹 Blok 10 — Raportowanie i automatyzacja CI/CD (`Artefakt10`) 🏆
Zamiana surowych logów w **interaktywne raporty Allure** oraz automatyzacja całego cyklu:
- `test_101_allure_init.py` — inicjalizacja Allure (kroki, severity, status Passed/Failed)
- `test_102_meta_reporting.py` — struktura biznesowa **Epic → Feature → Story**
- `test_103_attachments.py` — dowody wizualne (załączniki: screenshot + JSON)
- `pipeline.py` — **One-Click pipeline**: `docker up` → `pytest` → `allure generate` → `docker down`

---

## 🚀 Uruchomienie

### Wymagania
Python 3.10+, Git, Docker Desktop oraz Allure CLI (+ Java 8+ dla Allure).

```bash
git clone https://github.com/Relux-dev/TM-99775.git
cd TM-99775
python -m pip install requests jsonschema pytest allure-pytest Appium-Python-Client
```
> Windows: `python` · macOS/Linux: `python3`

### Serwer Appium (Docker)
```bash
cd Artefakt09          # lub Artefakt03
docker compose up -d   # serwer Appium na porcie 4723
```

### Testy API (Blok 9)
```bash
cd Artefakt09
python 91_api_setup.py
python 92_crud_test.py
python 93_schema_test.py
python 94_negative_test.py
python 95_hybrid_test.py
```

### Pipeline + raport Allure (Blok 10)
```bash
cd Artefakt10
python pipeline.py            # pełny cykl CI/CD (uruchamiać z folderu Artefakt10)
allure serve allure-results   # interaktywny raport w przeglądarce
```

---

## ✍️ Autor

**Michał** — nr albumu **99775**
Repozytorium: [github.com/Relux-dev/TM-99775](https://github.com/Relux-dev/TM-99775)
