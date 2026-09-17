"""Tests for Excel/CSV catalog parsing + column mapping."""
from src.parser.excel_parser import ExcelCatalogParser


def _make_csv(path):
    path.write_text(
        "Product Name,CAS Number,Grade,Purity,Price\n"
        "Ethanol,64-17-5,ACS Reagent,99.9%,500000\n"
        "Acetone,67-64-1,HPLC Grade,99.5%,300000\n",
        encoding="utf-8",
    )


def test_parse_csv(tmp_path):
    csv_path = tmp_path / "catalog.csv"
    _make_csv(csv_path)
    parser = ExcelCatalogParser()
    molecules = parser.parse_file(str(csv_path), supplier_id=1)
    assert len(molecules) == 2
    assert molecules[0]["cas_number"] == "64-17-5"
    assert molecules[0]["grade"] == "ACS Reagent"
    assert molecules[0]["price"] == 500000.0
    assert molecules[0]["purity_numeric"] == 99.9


def test_detect_column_mapping():
    cols = ["Product Name", "CAS Number", "Molecular Formula", "Purity", "Price (IRR)"]
    mapping = ExcelCatalogParser.detect_column_mapping(cols)
    assert mapping["name"] == "Product Name"
    assert mapping["cas"] == "CAS Number"
    assert mapping["formula"] == "Molecular Formula"
    assert mapping["purity"] == "Purity"
    assert mapping["price"] == "Price (IRR)"
