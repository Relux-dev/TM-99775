import os
import xml.etree.ElementTree as ET

def analyze_manifest():
    print(">>> ZADANIE 5.2: ANALIZA MANIFESTU (POLACZENIE Z ARTEFAKTEM 02) <<<")
    manifest_path = "../Artefakt02/decompiled_apk/AndroidManifest.xml"
    output_path = "52_inspection.log"

    if not os.path.exists(manifest_path):
        print(f"BLAD: Nie znaleziono manifestu w: {manifest_path}")
        return

    tree = ET.parse(manifest_path)
    root = tree.getroot()

    package = root.attrib.get('package')
    permissions = [
        elem.attrib.get('{http://schemas.android.com/apk/res/android}name')
        for elem in root.findall('uses-permission')
    ]
    activities = [
        elem.attrib.get('{http://schemas.android.com/apk/res/android}name')
        for elem in root.findall('.//activity')
    ]

    report = [
        "=== ARTEFAKT 5.2: RAPORT ANALIZY SYSTEMOWEJ ===",
        f"Pakiet glowny: {package}",
        f"Liczba Activity: {len(activities)}",
        "",
        "Kluczowe Uprawnienia (Co aplikacja chce robic?):"
    ]
    report.extend([f"- {p}" for p in permissions[:5]])

    final_report = "\n".join(report)
    print(final_report)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(final_report)

    print(f"\n[OK] Sukces! Artefakt zapisany jako: {output_path}")

if __name__ == "__main__":
    analyze_manifest()