import os
import xml.etree.ElementTree as ET
import json

def build_ui_map():
    print(">>> ZADANIE 5.3: BUDOWA MAPY SELEKTOROW (UI MAPPING) <<<")
    layout_dir = "../Artefakt02/decompiled_apk/res/layout/"
    output_file = "53_selectors.json"

    if not os.path.exists(layout_dir):
        print(f"BLAD: Folder layoutow nie istnieje: {layout_dir}")
        return

    ui_map = {
        "metadata": {"source": "decompiled_apk", "block": "5.3"},
        "selectors": {}
    }

    for file_name in os.listdir(layout_dir):
        if file_name.endswith(".xml"):
            try:
                tree = ET.parse(os.path.join(layout_dir, file_name))
                root = tree.getroot()
                for element in root.iter():
                    res_id = element.attrib.get(
                        '{http://schemas.android.com/apk/res/android}id')
                    if res_id:
                        clean_id = res_id.split('/')[-1]
                        business_name = clean_id.upper()
                        ui_map["selectors"][business_name] = clean_id
            except:
                continue

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(ui_map, f, indent=4)

    print(f"[OK] Zmapowano {len(ui_map['selectors'])} unikalnych elementow UI.")
    print(f"Artefakt zapisany: {output_file}")

if __name__ == "__main__":
    build_ui_map()