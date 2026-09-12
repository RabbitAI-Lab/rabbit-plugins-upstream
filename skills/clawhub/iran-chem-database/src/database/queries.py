"""Typed query helpers for the API layer."""
from __future__ import annotations

from sqlalchemy import func, or_, select
from sqlalchemy.orm import Session, selectinload

from src.database.models import Molecule, Supplier, SupplierOffering


def search_molecules(db: Session, query: str | None = None, cas: str | None = None,
                     formula: str | None = None, grade: str | None = None,
                     supplier_id: int | None = None, min_purity: float | None = None,
                     available: bool | None = None, organic_status: str | None = None,
                     page: int = 1, limit: int = 20):
    # Eager-load offerings (+ their suppliers) to avoid N+1 queries in the API layer.
    stmt = (select(Molecule)
            .distinct()
            .join(SupplierOffering, SupplierOffering.molecule_id == Molecule.molecule_id)
            .options(selectinload(Molecule.offerings).selectinload(SupplierOffering.supplier)))
    if query:
        like = f"%{query}%"
        stmt = stmt.where(or_(
            Molecule.iupac_name.ilike(like),
            Molecule.cas_number.ilike(like),
            Molecule.molecular_formula.ilike(like),
            Molecule.canonical_smiles.ilike(like),
            Molecule.inchi_key.ilike(like),
        ))
    if cas:
        stmt = stmt.where(Molecule.cas_number == cas)
    if formula:
        stmt = stmt.where(Molecule.molecular_formula.ilike(f"%{formula}%"))
    if grade:
        stmt = stmt.where(SupplierOffering.grade.ilike(f"%{grade}%"))
    if supplier_id:
        stmt = stmt.where(SupplierOffering.supplier_id == supplier_id)
    if min_purity is not None:
        stmt = stmt.where(SupplierOffering.purity_numeric >= min_purity)
    if available is not None:
        stmt = stmt.where(SupplierOffering.is_currently_available == available)
    if organic_status and organic_status != "all":
        stmt = stmt.where(Molecule.organic_status == organic_status)
    total = db.execute(select(func.count()).select_from(stmt.subquery())).scalar_one()
    rows = db.execute(stmt.offset((page - 1) * limit).limit(limit)).scalars().all()
    return rows, total


def list_suppliers(db: Session, status: str | None = None, page: int = 1, limit: int = 50):
    stmt = select(Supplier)
    count_stmt = select(func.count()).select_from(Supplier)
    if status:
        stmt = stmt.where(Supplier.status == status)
        count_stmt = count_stmt.where(Supplier.status == status)
    total = db.execute(count_stmt).scalar_one()
    rows = db.execute(stmt.offset((page - 1) * limit).limit(limit)).scalars().all()
    return rows, total


def global_stats(db: Session) -> dict:
    from src.api.coverage_logic import coverage_snapshot
    cov = coverage_snapshot(db)
    return {
        "total_molecules": cov["records"]["accepted_molecules"],
        "total_suppliers": cov["suppliers"]["configured"],
        "active_suppliers": db.execute(
            select(func.count()).select_from(Supplier).where(Supplier.status == "active")
        ).scalar_one(),
        "total_offerings": cov["records"]["offerings"],
        "available_offerings": db.execute(
            select(func.count()).select_from(SupplierOffering)
            .where(SupplierOffering.is_currently_available.is_(True))
        ).scalar_one(),
        "rejected_grade": cov["records"]["rejected_grade"],
        "rejected_validation": cov["records"]["rejected_validation"],
        "organic_true": cov["records"]["organic_true"],
        "organic_false": cov["records"]["organic_false"],
        "organic_unknown": cov["records"]["organic_unknown"],
        "coverage": cov["suppliers"],
        "export_readiness": cov["export_readiness"],
    }
