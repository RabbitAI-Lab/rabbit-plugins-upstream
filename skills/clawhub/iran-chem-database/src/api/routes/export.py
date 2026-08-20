"""Export endpoint — CSV / JSON / SDF."""
from __future__ import annotations

import csv
import io

from fastapi import APIRouter, Depends
from fastapi.responses import Response
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.database.models import Molecule, Supplier, SupplierOffering
from src.database.session import get_db_session

router = APIRouter(prefix="/api/v1/export", tags=["export"])


def get_db() -> Session:
    db = get_db_session()
    try:
        yield db
    finally:
        db.close()


@router.get("")
def export(format: str = "json", db: Session = Depends(get_db)):
    molecules = db.execute(select(Molecule)).scalars().all()
    offerings = db.execute(select(SupplierOffering)).scalars().all()
    suppliers = {s.supplier_id: s for s in db.execute(select(Supplier)).scalars().all()}

    if format == "csv":
        buf = io.StringIO()
        writer = csv.writer(buf)
        writer.writerow(["InChIKey", "IUPAC Name", "CAS", "Formula", "MW", "SMILES",
                         "Supplier", "Grade", "Purity", "Price Min", "Currency", "Available"])
        for o in offerings:
            mol = next((m for m in molecules if m.molecule_id == o.molecule_id), None)
            sup = suppliers.get(o.supplier_id)
            writer.writerow([
                mol.inchi_key if mol else "", mol.iupac_name if mol else "",
                mol.cas_number if mol else "", mol.molecular_formula if mol else "",
                mol.molecular_weight if mol else "", mol.canonical_smiles if mol else "",
                sup.company_name_en if sup else "", o.grade, o.purity,
                o.price_min, o.currency, o.is_currently_available,
            ])
        return Response(buf.getvalue(), media_type="text/csv",
                        headers={"Content-Disposition": "attachment; filename=iran_chem_db_export.csv"})

    if format == "sdf":
        blocks = []
        for m in molecules:
            if m.canonical_smiles:
                try:
                    from rdkit import Chem
                    mol = Chem.MolFromSmiles(m.canonical_smiles)
                    if mol:
                        mol.SetProp("_Name", m.iupac_name or m.inchi_key)
                        mol.SetProp("CAS", m.cas_number or "")
                        blocks.append(Chem.MolToMolBlock(mol))
                except Exception:  # noqa: BLE001
                    continue
        return Response("\n".join(blocks) + "\n", media_type="chemical/x-mdl-sdfile")

    # JSON (default)
    data = []
    for m in molecules:
        data.append({
            "inchi_key": m.inchi_key, "iupac_name": m.iupac_name,
            "cas_number": m.cas_number, "molecular_formula": m.molecular_formula,
            "molecular_weight": m.molecular_weight, "canonical_smiles": m.canonical_smiles,
            "inchi": m.inchi, "pubchem_cid": m.pubchem_cid,
        })
    return {"export_date": None, "total_molecules": len(molecules), "molecules": data}
