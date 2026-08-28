"""Tests for the extended parsers (guide §5): JSON-LD fields, DOCX, JSON API."""
import io
import json
import zipfile
from pathlib import Path

from bs4 import BeautifulSoup

from src.parser.docx_parser import DOCXCatalogParser
from src.parser.html_parser import HTMLProductParser
from src.parser.json_catalogue_parser import JSONCatalogueParser


# ── JSON-LD extended fields ────────────────────────────────────────────────
def test_jsonld_additional_property():
    html = """
    <script type="application/ld+json">
    {"@type":"Product","name":"Ethanol absolute",
     "description":"CAS 64-17-5 purity 99.9% ACS Reagent",
     "sku":"1.00983.1000",
     "additionalProperty":[{"name":"CAS Number","value":"64-17-5"},
                            {"name":"Purity","value":"99.9%"}],
     "offers":{"price":"1850000","priceCurrency":"IRR",
               "availability":"https://schema.org/InStock"}}
    </script>
    """
    mols = HTMLProductParser()._parse_json_ld(BeautifulSoup(html, "lxml"))
    assert mols and mols[0]["cas_number"] == "64-17-5"
    assert mols[0]["purity"] == "99.9%"
    assert mols[0]["sku"] == "1.00983.1000"
    assert mols[0]["availability"] == "InStock"
    assert mols[0]["currency"] == "IRR"
    assert mols[0]["grade"] == "ACS"
    assert mols[0]["price"] == 1850000.0


def test_jsonld_description_fallback():
    html = ('<script type="application/ld+json">'
            '{"@type":"Product","name":"Acetone","description":"99.5% pure, CAS 67-64-1, HPLC grade"}'
            '</script>')
    mols = HTMLProductParser()._parse_json_ld(BeautifulSoup(html, "lxml"))
    assert mols[0]["cas_number"] == "67-64-1"
    assert mols[0]["purity"] == "99.5%"
    assert mols[0]["grade"] == "HPLC"


# ── DOCX parser ────────────────────────────────────────────────────────────
def _make_docx(rows, path):
    """Build a minimal docx with a 3-column table using only stdlib."""
    from xml.sax.saxutils import escape
    cells_xml = []
    for row in rows:
        cells = "".join(
            f"<w:tc><w:p><w:r><w:t>{escape(c)}</w:t></w:r></w:p></w:tc>" for c in row)
        cells_xml.append(f"<w:tr>{cells}</w:tr>")
    doc = ('<?xml version="1.0"?>'
           '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
           '<w:body><w:tbl>' + "".join(cells_xml) + '</w:tbl></w:body></w:document>')
    with zipfile.ZipFile(path, "w") as zf:
        zf.writestr("[Content_Types].xml", "")
        zf.writestr("word/document.xml", doc)


def test_docx_parser_extracts_cas(tmp_path):
    p = tmp_path / "catalog.docx"
    _make_docx([
        ["Ethanol", "64-17-5", "99.9% ACS Reagent", "1850000 تومان"],
        ["Acetone", "67-64-1", "HPLC Grade", ""],
    ], str(p))
    mols = DOCXCatalogParser().parse_file(str(p), supplier_id=3)
    assert len(mols) >= 2
    cas = {m.get("cas_number") for m in mols}
    assert "64-17-5" in cas and "67-64-1" in cas
    eth = next(m for m in mols if m.get("cas_number") == "64-17-5")
    assert eth["purity"] == "99.9%"
    assert eth["grade"] == "ACS"
    assert eth["price"] == 1850000.0


# ── JSON catalogue parser ──────────────────────────────────────────────────
def test_json_catalogue_list_shape(tmp_path):
    p = tmp_path / "api.json"
    p.write_text(json.dumps([
        {"title": "Methanol", "cas": "67-56-1", "price": "450000", "in_stock": True},
        {"name": "Acetonitrile", "cas_number": "75-05-8"},
    ]), encoding="utf-8")
    mols = JSONCatalogueParser().parse_file(str(p), supplier_id=5)
    assert len(mols) == 2
    assert mols[0]["cas_number"] == "67-56-1"
    assert mols[0]["price"] == 450000.0
    assert mols[1]["cas_number"] == "75-05-8"


def test_json_catalogue_data_envelope(tmp_path):
    p = tmp_path / "gql.json"
    p.write_text(json.dumps({"data": {"products": [
        {"name_en": "Ethanol", "CAS": "64-17-5", "grade": "Extra pure",
         "code": "100983", "price_toman": "735000"}
    ]}}), encoding="utf-8")
    mols = JSONCatalogueParser().parse_file(str(p), supplier_id=5)
    assert len(mols) == 1
    assert mols[0]["cas_number"] == "64-17-5"
    assert mols[0]["supplier_product_code"] == "100983"
    assert mols[0]["grade"] == "Extra pure"


def test_json_catalogue_ignores_garbage(tmp_path):
    p = tmp_path / "notcat.json"
    p.write_text(json.dumps({"settings": {"theme": "dark"}}), encoding="utf-8")
    assert JSONCatalogueParser().parse_file(str(p), supplier_id=5) == []


# ── JS catalogue detection (pure functions) ────────────────────────────────
def test_api_hint_detection():
    from src.crawler.js_catalogue import JSCatalogueEngine
    e = JSCatalogueEngine("/tmp")
    assert e.page_has_api_hints('<script>fetch("/api/products?page=1")</script>')
    assert e.page_has_api_hints("<div>graphql endpoint</div>")
    assert not e.page_has_api_hints("<html><body>static catalog table</body></html>")


def test_api_endpoint_extraction():
    from src.crawler.js_catalogue import JSCatalogueEngine
    e = JSCatalogueEngine("/tmp")
    html = ('<script>const r = await fetch("https://shop.ir/api/v2/products?page=1");</script>'
            '<script>axios.get("https://shop.ir/wp-json/wc/v3/products")</script>')
    urls = e.detect_catalogue_api(html)
    assert any("api/v2/products" in u for u in urls)
    assert any("wp-json/wc/v3/products" in u for u in urls)
