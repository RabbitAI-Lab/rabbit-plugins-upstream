#!/usr/bin/env python3
import json, os, re, sys, zipfile
from xml.etree import ElementTree as ET

if len(sys.argv) != 2: raise SystemExit("用法: extract_word.py FILE.docx")
path = sys.argv[1]
if not os.path.isfile(path) or os.path.getsize(path) > 10 * 1024 * 1024: raise SystemExit("DOCX 不存在或超过 10 MB。")
try:
    with zipfile.ZipFile(path) as z:
        if len(z.infolist()) > 500 or "word/document.xml" not in z.namelist(): raise ValueError()
        raw = z.read("word/document.xml")
except Exception: raise SystemExit("文件不是有效的 DOCX，可能已损坏或加密。")
if len(raw) > 8 * 1024 * 1024: raise SystemExit("DOCX 正文超过解析限制。")
root = ET.fromstring(raw)
ns = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
segments, total = [], 0
for p in root.iter(ns + "p"):
    text = "".join((node.text or "") if node.tag == ns + "t" else ("\t" if node.tag == ns + "tab" else "\n") for node in p.iter() if node.tag in (ns + "t", ns + "tab", ns + "br")).strip()
    if not text: continue
    total += len(text); segments.append({"location": f"第 {len(segments)+1} 段", "text": text})
    if len(segments) > 2000 or total > 120000: raise SystemExit("DOCX 内容超过限制。")
if total < 20: raise SystemExit("DOCX 没有足够的可读取文字。")
name = re.sub(r'[\x00-\x1f\\/]+', '-', os.path.basename(path))[:180]
print(json.dumps({"name": name, "total_characters": total, "segments": segments}, ensure_ascii=False))
