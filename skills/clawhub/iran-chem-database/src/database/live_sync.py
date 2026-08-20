"""LiveSyncEngine — change-driven database sync (spec §5.2).

New molecules INSERT; changed price/availability UPDATE + history; products gone
from the mirror are marked discontinued. hts-changes.json drives selective
re-parsing so the DB reflects current supplier catalog state.
"""
from __future__ import annotations

import logging
from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.database.models import Molecule, OfferingHistory, SupplierOffering

logger = logging.getLogger(__name__)


class LiveSyncEngine:
    def __init__(self, session: Session):
        self.db = session

    def upsert_molecule(self, record: dict, supplier_id: int) -> str:
        """Insert-or-update a molecule + its offering. Returns 'new' | 'updated'."""
        inchi_key = record.get("inchi_key") or record.get("inchiKey")
        if not inchi_key:
            # Stable, deterministic fallback key (do NOT use hash() — it is
            # randomized per process via PYTHONHASHSEED and would break dedup
            # across runs).
            import hashlib
            basis = (str(record.get("cas_number") or "") + "|" +
                     str(record.get("title") or "") + "|" +
                     str(record.get("molecular_formula") or ""))
            inchi_key = "fallback-" + hashlib.sha256(basis.encode("utf-8")).hexdigest()[:20]

        molecule = self.db.execute(
            select(Molecule).where(Molecule.inchi_key == inchi_key)
        ).scalar_one_or_none()

        if molecule is None:
            molecule = Molecule(
                inchi_key=inchi_key,
                iupac_name=record.get("iupac_name") or record.get("title"),
                common_names=[record["common_name"]] if record.get("common_name") else None,
                persian_names=[record["persian_name"]] if record.get("persian_name") else None,
                cas_number=record.get("cas_number"),
                molecular_formula=record.get("molecular_formula"),
                molecular_weight=record.get("molecular_weight"),
                canonical_smiles=record.get("canonical_smiles"),
                inchi=record.get("inchi"),
                pubchem_cid=record.get("pubchem_cid"),
                ghs_pictograms=record.get("ghs_pictograms"),
                hazard_statements=record.get("hazard_statements"),
                signal_word=record.get("signal_word"),
            )
            self.db.add(molecule)
            self.db.flush()
            result = "new"
        else:
            result = "updated"

        self._upsert_offering(molecule, record, supplier_id)
        return result

    def _upsert_offering(self, molecule: Molecule, record: dict, supplier_id: int) -> None:
        existing = self.db.execute(
            select(SupplierOffering).where(
                SupplierOffering.molecule_id == molecule.molecule_id,
                SupplierOffering.supplier_id == supplier_id,
            )
        ).scalar_one_or_none()

        values = {
            "grade": record.get("grade") or "unspecified",
            "purity": record.get("purity"),
            "purity_numeric": record.get("purity_numeric"),
            "brand": record.get("brand"),
            "price_min": record.get("price_min") or record.get("price"),
            "currency": record.get("currency", "IRR"),
            "availability_status": record.get("availability_status", "In Stock"),
            "product_url": record.get("product_url"),
            "httrack_source_file": record.get("source_file"),
            "extraction_confidence": record.get("extraction_confidence"),
            "raw_page_hash": record.get("raw_page_hash"),
            "is_currently_available": True,
            "date_last_verified": datetime.now(),
        }

        if existing is None:
            offering = SupplierOffering(
                molecule_id=molecule.molecule_id, supplier_id=supplier_id, **values
            )
            self.db.add(offering)
        else:
            old = {k: getattr(existing, k) for k in values if getattr(existing, k) != values[k]}
            if old:
                self.db.add(OfferingHistory(
                    offering_id=existing.offering_id,
                    molecule_id=molecule.molecule_id,
                    supplier_id=supplier_id,
                    change_type="update",
                    old_values=old,
                    new_values={k: values[k] for k in old},
                    detected_via="httrack_update",
                ))
                existing.date_last_changed = datetime.now()
            for k, v in values.items():
                setattr(existing, k, v)

    def mark_discontinued(self, supplier_id: int, removed_files: list[str]) -> int:
        """Mark offerings sourced from removed mirror files as discontinued."""
        count = 0
        for f in removed_files:
            offerings = self.db.execute(
                select(SupplierOffering).where(
                    SupplierOffering.supplier_id == supplier_id,
                    SupplierOffering.httrack_source_file == f,
                )
            ).scalars().all()
            for offering in offerings:
                if offering.is_currently_available:
                    offering.is_currently_available = False
                    offering.date_last_changed = datetime.now()
                    self.db.add(OfferingHistory(
                        offering_id=offering.offering_id,
                        molecule_id=offering.molecule_id,
                        supplier_id=supplier_id,
                        change_type="discontinued",
                        detected_via="httrack_changes_json",
                    ))
                    count += 1
        return count

    def commit(self) -> None:
        self.db.commit()
