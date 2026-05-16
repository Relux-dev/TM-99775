import json
import os

def run_descriptive_validation():
    print(">>> ZADANIE 5.5: GENEROWANIE RAPORTU FEEDBACKU DLA DEWELOPERA <<<")

    try:
        with open("51_caps.json", "r") as f:
            caps = json.load(f)
        with open("53_selectors.json", "r") as f:
            ui_map = json.load(f)
    except FileNotFoundError as e:
        print(f"BLAD: Brak pliku — {e}")
        return

    current_pkg = caps.get("appPackage") or caps.get("appium:appPackage")
    feedback_report = []

    if current_pkg == "io.appium.android.apis":
        feedback_report.append({
            "feature": "Identyfikacja Aplikacji",
            "status": "ZGODNY",
            "message": f"Pakiet {current_pkg} poprawnie zmapowany."
        })
    else:
        feedback_report.append({
            "feature": "Identyfikacja Aplikacji",
            "status": "DO POPRAWY",
            "message": f"Wykryto {current_pkg}, sprawdz konfiguracje manifestu."
        })

    target_element = "ACCESSIBILITY"
    if target_element in ui_map["selectors"]:
        feedback_report.append({
            "feature": "Dostepnosc UI",
            "status": "ZGODNY",
            "message": f"Element {target_element} jest dostepny w layoutach."
        })
    else:
        available = list(ui_map['selectors'].keys())[:3]
        feedback_report.append({
            "feature": "Dostepnosc UI",
            "status": "INFORMACJA",
            "message": f"Nie odnaleziono '{target_element}'. Dostepne: {available}."
        })

    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<test_report project="Appium_Audit">\n'

    print("\n--- FEEDBACK DLA TWORCOW APLIKACJI ---")
    for item in feedback_report:
        print(f"[{item['status']}] {item['feature']}: {item['message']}")
        xml += f'  <issue feature="{item["feature"]}" status="{item["status"]}">{item["message"]}</issue>\n'
    xml += '</test_report>'

    with open("55_result.xml", "w", encoding="utf-8") as f:
        f.write(xml)

    print(f"\n[INFO] Blok 5 zakonczony. Raport opisowy gotowy: 55_result.xml")

if __name__ == "__main__":
    run_descriptive_validation()