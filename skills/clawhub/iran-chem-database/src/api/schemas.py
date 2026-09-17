"""Pydantic response/request models for the API."""
from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class PackSize(BaseModel):
    size: str
    unit: str
    price: Optional[float] = None


class OfferingOut(BaseModel):
    offering_id: int
    supplier_id: int
    supplier_name: Optional[str] = None
    brand: Optional[str] = None
    grade: str
    purity: Optional[str] = None
    purity_numeric: Optional[float] = None
    pack_sizes: Optional[dict] = None
    price_min: Optional[float] = None
    price_max: Optional[float] = None
    currency: Optional[str] = None
    availability_status: Optional[str] = None
    product_url: Optional[str] = None
    is_currently_available: Optional[bool] = None


class MoleculeOut(BaseModel):
    molecule_id: int
    source_identity: str
    # Real InChIKey only (None when the record has no resolved structure)
    inchi_key: Optional[str] = None
    organic_status: str = "unknown"
    organic_reason: Optional[str] = None
    organic_confidence: Optional[float] = None
    iupac_name: Optional[str] = None
    common_names: Optional[List[str]] = None
    persian_names: Optional[List[str]] = None
    cas_number: Optional[str] = None
    molecular_formula: Optional[str] = None
    molecular_weight: Optional[float] = None
    canonical_smiles: Optional[str] = None
    inchi: Optional[str] = None
    pubchem_cid: Optional[int] = None
    appearance: Optional[str] = None
    ghs_pictograms: Optional[List[str]] = None
    hazard_statements: Optional[List[str]] = None
    signal_word: Optional[str] = None
    offerings: List[OfferingOut] = []


class SupplierOut(BaseModel):
    supplier_id: int
    company_name_en: Optional[str] = None
    company_name_fa: Optional[str] = None
    website_url: str
    supplier_type: Optional[str] = None
    city: Optional[str] = None
    province: Optional[str] = None
    status: Optional[str] = None
    is_verified: Optional[bool] = None
    verification_score: Optional[float] = None
    total_products: Optional[int] = None
    last_crawled: Optional[str] = None


class StatsOut(BaseModel):
    total_molecules: int
    total_suppliers: int
    active_suppliers: int
    total_offerings: int
    available_offerings: int


class MirrorOut(BaseModel):
    mirror_id: int
    supplier_id: int
    mirror_path: str
    project_name: Optional[str] = None
    total_files: Optional[int] = None
    html_files: Optional[int] = None
    pdf_files: Optional[int] = None
    excel_files: Optional[int] = None
    mirror_size_bytes: Optional[int] = None
    last_update_date: Optional[str] = None
    files_new_last_run: Optional[int] = None
    files_modified_last_run: Optional[int] = None
    files_removed_last_run: Optional[int] = None
    httrack_return_code: Optional[int] = None
    uses_playwright_fallback: Optional[bool] = None


class TriggerMirrorRequest(BaseModel):
    supplier_id: int
