"""Tests for PDF catalog parsing (local files only)."""
import pytest

from src.parser.pdf_parser import PDFCatalogParser


def _make_pdf(path):
    import pymupdf
    doc = pymupdf.open()
    page = doc.new_page()
    page.insert_text((72, 72), "Catalog\nEthanol CAS 64-17-5 ACS Reagent 99.9%\nMethanol CAS 67-56-1 HPLC")
    doc.save(str(path))
    doc.close()


def test_parse_pdf_catalog(tmp_path):
    pdf = tmp_path / "catalog.pdf"
    _make_pdf(pdf)
    parser = PDFCatalogParser()
    molecules = parser.parse_file(str(pdf), supplier_id=1)
    cas_values = {m.get("cas_number") for m in molecules}
    assert "64-17-5" in cas_values
    assert "67-56-1" in cas_values


def test_parse_missing_pdf_returns_empty():
    parser = PDFCatalogParser()
    assert parser.parse_file("/nonexistent.pdf", 1) == []
