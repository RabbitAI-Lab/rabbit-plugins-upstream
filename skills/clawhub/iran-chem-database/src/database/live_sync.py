"""LiveSyncEngine — change-driven database sync (spec §5.2).

New molecules INSERT; changed price/availability UPDATE + history; products gone
from the mirror are marked discontinued. hts-changes.json drives selective
re-parsing so the DB reflects current supplier catalog state.

Identity policy (fix guide §3 + v2.4.0 dedup hardening):
  * a real InChIKey lives in Molecule.inchi_key;
  * every other record gets a deterministic source_identity (CAS > supplier+code
    > 27-char fallback hash built from a NORMALIZED title);
  * CROSS-IDENTITY UNIFICATION: when a record's own identity is not found, the
    engine looks the molecule up by real InChIKey and then by normalized CAS
    and MERGES into the existing row instead of creating a duplicate — this is
    what prevents "the same molecule twice" in exports (e.g. one listing with
    a resolved structure and another CAS-only listing of the same chemical);
  * offerings are keyed by (molecule, supplier, supplier_product_code) — two
    product codes for the same chemical become TWO offerings, never one
    overwriting the other, and the code is persisted.
"""
from __future__ import annotations

import logging
from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.database.identity import (build_source_identity, identity_strength,
                                   normalize_cas)
from src.database.models import (Molecule, OfferingHistory, RejectedCatalogueItem,
                                 SupplierOffering)

logger = logging.getLogger(__name__)


class LiveSyncEngine:
    def __init__(self, session: Session):
        self.db = session

    # ── molecule upsert with cross-identity merge ──────────────────────────
    def upsert_molecule(self, record: dict, supplier_id: int) -> str:
        """Insert-or-update a molecule + its offering. Returns 'new' | 'updated'.

        Lookup order: source_identity → real InChIKey → normalized CAS.
        Matching on InChIKey/CAS merges the record into the existing row so the
        same chemical never appears twice in molecule-shaped exports.
        """
        source_identity, inchi_key = build_source_identity(record, supplier_id)
        cas = normalize_cas(record.get("cas_number"))

        molecule = self.db.execute(
            select(Molecule).where(Molecule.source_identity == source_identity)
        ).scalar_one_or_none()

        merged = False
        if molecule is None and inchi_key:
            molecule = self.db.execute(
                select(Molecule).where(Molecule.inchi_key == inchi_key)
            ).scalar_one_or_none()
            merged = molecule is not None
        if molecule is None and cas:
            molecule = self.db.execute(
                select(Molecule).where(Molecule.cas_number == cas)
            ).scalar_one_or_none()
            merged = molecule is not None

        if molecule is None:
            molecule = Molecule(
                source_identity=source_identity,
                inchi_key=inchi_key,
                iupac_name=record.get("iupac_name") or record.get("title"),
                common_names=[record["common_name"]] if record.get("common_name") else None,
                persian_names=[record["persian_name"]] if record.get("persian_name") else None,
                cas_number=cas or None,
                molecular_formula=record.get("molecular_formula"),
                molecular_weight=record.get("molecular_weight"),
                canonical_smiles=record.get("canonical_smiles"),
                inchi=record.get("inchi"),
                pubchem_cid=record.get("pubchem_cid"),
                organic_status=record.get("organic_status") or "unknown",
                organic_reason=record.get("organic_reason"),
                organic_confidence=record.get("organic_confidence"),
                organic_lookup_error=record.get("organic_lookup_error"),
                classification_review_required=bool(record.get("classification_review_required")),
                ghs_pictograms=record.get("ghs_pictograms"),
                hazard_statements=record.get("hazard_statements"),
                signal_word=record.get("signal_word"),
            )
            self.db.add(molecule)
            self.db.flush()
            result = "new"
        else:
            # Enrich/upgrade an existing row (merge path included).
            changed = False
            if merged and identity_strength(source_identity) > identity_strength(molecule.source_identity):
                # upgrade to the stronger identity (CAS→InChIKey, fallback→CAS, …)
                other = self.db.execute(
                    select(Molecule).where(Molecule.source_identity == source_identity)
                ).scalar_one_or_none()
                if other is None:
                    molecule.source_identity = source_identity
                    changed = True
            for col, key in (
                ("inchi_key", "inchi_key"),
                ("canonical_smiles", "canonical_smiles"), ("inchi", "inchi"),
                ("molecular_formula", "molecular_formula"),
                ("molecular_weight", "molecular_weight"),
                ("pubchem_cid", "pubchem_cid"),
                ("iupac_name", "iupac_name"),
            ):
                if not getattr(molecule, col) and record.get(key):
                    setattr(molecule, col, record[key])
                    changed = True
            # CAS is filled ONLY from a checksum-valid value
            if not molecule.cas_number and cas:
                molecule.cas_number = cas
                changed = True
            if record.get("organic_status") and molecule.organic_status == "unknown":
                molecule.organic_status = record["organic_status"]
                molecule.organic_reason = record.get("organic_reason")
                molecule.organic_confidence = record.get("organic_confidence")
                molecule.organic_lookup_error = record.get("organic_lookup_error")
                molecule.classification_review_required = bool(record.get("classification_review_required"))
                changed = True
            if changed:
                molecule.updated_at = datetime.now()
            result = "updated"

        self._upsert_offering(molecule, record, supplier_id)
        return result

    # ── offering upsert keyed by product code ──────────────────────────────
    def _upsert_offering(self, molecule: Molecule, record: dict, supplier_id: int) -> None:
        product_code = (record.get("supplier_product_code") or record.get("product_code")
                        or record.get("sku") or "")
        product_code = str(product_code)[:200] if product_code else ""

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
        if product_code:
            values["supplier_product_code"] = product_code
        if record.get("package"):
            values["pack_sizes"] = {"package": str(record["package"])[:200]}

        stmt = select(SupplierOffering).where(
            SupplierOffering.molecule_id == molecule.molecule_id,
            SupplierOffering.supplier_id == supplier_id,
        )
        if product_code:
            stmt = stmt.where(SupplierOffering.supplier_product_code == product_code)
        existing = self.db.execute(stmt).scalar_one_or_none()

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

    def record_rejection(self, record: dict, stage: str, reason: str,
                         supplier_id: int | None = None) -> None:
        """Persist a rejected candidate so nothing is silently dropped (§4.2)."""
        self.db.add(RejectedCatalogueItem(
            supplier_id=supplier_id or record.get("supplier_id"),
            source_file=record.get("source_file"),
            source_url=record.get("product_url"),
            raw_title=record.get("title") or record.get("name"),
            raw_description=record.get("description"),
            cas_number=record.get("cas_number"),
            molecular_formula=record.get("molecular_formula"),
            canonical_smiles=record.get("canonical_smiles"),
            grade=record.get("grade"),
            purity=record.get("purity"),
            brand=record.get("brand"),
            extraction_method=record.get("_extraction_method"),
            rejection_stage=stage,
            rejection_reason=reason[:300],
        ))

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
