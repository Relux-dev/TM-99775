import json
import os

def setup_integrated_session():
    print(">>> ZADANIE 5.4: INTEGRACJA ARTEFAKTOW (STABLE BUILD) <<<")
    caps_path = "51_caps.json"
    selectors_path = "53_selectors.json"
    log_path = "54_session.log"

    if not os.path.exists(caps_path) or not os.path.exists(selectors_path):
        print("BLAD: Brak wymaganych plikow JSON. Uruchom najpierw step1 i step3.")
        return

    with open(caps_path, 'r') as f:
        caps_data = json.load(f)
    with open(selectors_path, 'r') as f:
        ui_map = json.load(f)

    app_pkg = caps_data.get("appPackage") or caps_data.get("appium:appPackage")
    app_act = caps_data.get("appActivity") or caps_data.get("appium:appActivity")
    dev_name = caps_data.get("deviceName") or caps_data.get("appium:deviceName")

    if not app_pkg or not app_act:
        status_msg = "FAILED: Missing appPackage or appActivity in JSON!"
    else:
        status_msg = "READY TO CONNECT"

    session_info = (
        "=== ARTEFAKT 5.4: SESSION READINESS REPORT ===\n"
        f"Target App    : {app_pkg}\n"
        f"Main Activity : {app_act}\n"
        f"Device        : {dev_name}\n"
        f"UI Elements   : {len(ui_map['selectors'])} loaded\n"
        f"Status        : {status_msg}"
    )

    print(session_info)

    with open(log_path, "w", encoding="utf-8") as f:
        f.write(session_info)

if __name__ == "__main__":
    setup_integrated_session()