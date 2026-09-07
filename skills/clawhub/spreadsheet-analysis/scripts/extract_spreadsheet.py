#!/usr/bin/env python3
import csv, json, os, re, sys, zipfile
from xml.etree import ElementTree as ET

if len(sys.argv) != 2: raise SystemExit("用法: extract_spreadsheet.py FILE.xlsx|FILE.csv")
path = sys.argv[1]; ext = os.path.splitext(path)[1].lower()
if not os.path.isfile(path) or os.path.getsize(path) > 10 * 1024 * 1024: raise SystemExit("表格不存在或超过 10 MB。")
rows = []
if ext == ".csv":
    try:
        with open(path, encoding="utf-8-sig", newline="") as f:
            for number, row in enumerate(csv.reader(f), 1): rows.append(("CSV", number, row))
    except UnicodeDecodeError: raise SystemExit("CSV 必须使用 UTF-8 编码。")
elif ext == ".xlsx":
    try:
        with zipfile.ZipFile(path) as z:
            ns = {"m":"http://schemas.openxmlformats.org/spreadsheetml/2006/main", "r":"http://schemas.openxmlformats.org/officeDocument/2006/relationships"}
            shared = []
            if "xl/sharedStrings.xml" in z.namelist():
                sr = ET.fromstring(z.read("xl/sharedStrings.xml")); shared = ["".join(t.text or "" for t in si.iter("{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t")) for si in sr]
            wb = ET.fromstring(z.read("xl/workbook.xml")); rels = ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
            relmap = {x.attrib["Id"]: x.attrib["Target"] for x in rels}
            for sheet in wb.find("m:sheets", ns):
                name = sheet.attrib.get("name", "Sheet"); target = relmap[sheet.attrib["{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"]]
                target = target.lstrip("/"); target = target if target.startswith("xl/") else "xl/" + target
                root = ET.fromstring(z.read(target))
                for row in root.findall(".//m:sheetData/m:row", ns):
                    vals = []
                    for c in row.findall("m:c", ns):
                        ref = c.attrib.get("r", "?"); value = c.findtext("m:v", default="", namespaces=ns)
                        if c.attrib.get("t") == "s" and value.isdigit(): value = shared[int(value)]
                        elif c.attrib.get("t") == "inlineStr": value = "".join(t.text or "" for t in c.findall(".//m:t", ns))
                        column = re.sub(r'\d+$', '', ref)
                        if value != "": vals.append(f"{column}={value}")
                    rows.append((name, int(row.attrib.get("r", len(rows)+1)), vals, True))
    except Exception: raise SystemExit("XLSX 无法解析，可能已损坏或加密。")
else: raise SystemExit("仅支持 XLSX 和 CSV。")
segments, total = [], 0
for item in rows:
    sheet, number, values = item[:3]
    if not values: continue
    if len(item) == 3: values = [f"{chr(65+i)}={v}" for i, v in enumerate(values) if v != ""]
    text = " | ".join(values); total += len(text)
    segments.append({"location": f"{sheet}!第{number}行", "text": text})
    if len(segments) > 2000 or total > 120000: raise SystemExit("表格内容超过限制。")
if total < 20: raise SystemExit("表格没有足够的可读取内容。")
name = re.sub(r'[\x00-\x1f\\/]+', '-', os.path.basename(path))[:180]
print(json.dumps({"name": name, "total_characters": total, "segments": segments}, ensure_ascii=False))
