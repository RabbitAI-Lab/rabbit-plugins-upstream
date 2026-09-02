"""Tests for HTML product parsing on LOCAL mirror fixtures."""
from pathlib import Path

from conftest import FIXTURES
from src.parser.html_parser import HTMLProductParser


def test_parse_product_page():
    parser = HTMLProductParser()
    file_path = str(FIXTURES / "sample_supplier_mirror/www.example-chem.ir/catalog/product-1.html")
    molecules = parser.parse_file(file_path, supplier_id=1)
    assert len(molecules) >= 1
    # JSON-LD product block is present
    titles = " ".join(m.get("title", "") for m in molecules)
    assert "Ethanol" in titles
    # CAS extracted from table
    cas_values = [m.get("cas_number", "") for m in molecules if m.get("cas_number")]
    assert "64-17-5" in cas_values


def test_parse_persian_page():
    parser = HTMLProductParser()
    file_path = str(FIXTURES / "sample_supplier_mirror/www.example-chem.ir/catalog/product-2.html")
    molecules = parser.parse_file(file_path, supplier_id=2)
    assert molecules, "Persian page should yield at least one molecule"
    text = " ".join(str(m.get("title", "")) for m in molecules)
    assert "سولفوریک" in text or "اسید" in text
