"""SQLAlchemy ORM models — mirrors the spec schema (§2.3 & §5.1) exactly."""
from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from sqlalchemy import (BigInteger, Boolean, DateTime, Float, ForeignKey, Index,
                        Integer, String, Text, UniqueConstraint)
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Supplier(Base):
    __tablename__ = "suppliers"
    __table_args__ = (
        Index("idx_suppliers_status", "status"),
        Index("idx_suppliers_country", "country"),
    )

    supplier_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    company_name_en: Mapped[Optional[str]] = mapped_column(String(500))
    company_name_fa: Mapped[Optional[str]] = mapped_column(String(500))
    website_url: Mapped[str] = mapped_column(String(2000), unique=True)
    alternate_urls: Mapped[Optional[List[str]]] = mapped_column(ARRAY(Text))
    discovery_method: Mapped[Optional[str]] = mapped_column(String(100))
    discovery_date: Mapped[Optional[datetime]] = mapped_column(DateTime, default=datetime.now)
    httrack_mirror_path: Mapped[Optional[str]] = mapped_column(String(1000))
    httrack_project_name: Mapped[Optional[str]] = mapped_column(String(200))
    httrack_last_mirror: Mapped[Optional[datetime]] = mapped_column(DateTime)
    httrack_last_update: Mapped[Optional[datetime]] = mapped_column(DateTime)
    httrack_mirror_size_bytes: Mapped[Optional[int]] = mapped_column(BigInteger)
    httrack_total_files: Mapped[Optional[int]] = mapped_column(Integer)
    httrack_custom_flags: Mapped[Optional[str]] = mapped_column(Text)
    requires_playwright: Mapped[bool] = mapped_column(Boolean, default=False)
    last_crawled: Mapped[Optional[datetime]] = mapped_column(DateTime)
    crawl_frequency_hrs: Mapped[int] = mapped_column(Integer, default=24)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    verification_score: Mapped[Optional[float]] = mapped_column(Float)
    supplier_type: Mapped[Optional[str]] = mapped_column(String(100))
    # Crawl profile + catalogue format classification (fix guide §6.3 / remediation §7):
    # static_html | paginated_database | pdf_excel_catalogue | js_catalogue |
    # login_required | no_public_catalogue | blocked
    crawl_profile: Mapped[Optional[str]] = mapped_column(String(50), default="static_html")
    catalog_type: Mapped[Optional[str]] = mapped_column(String(50))
    expected_catalogue_type: Mapped[Optional[str]] = mapped_column(String(50))
    expected_pagination: Mapped[Optional[str]] = mapped_column(String(50))
    requires_login: Mapped[bool] = mapped_column(Boolean, default=False)
    robots_status: Mapped[Optional[str]] = mapped_column(String(50))
    last_http_status: Mapped[Optional[int]] = mapped_column(Integer)
    last_successful_product_count: Mapped[Optional[int]] = mapped_column(Integer)
    partial_reason: Mapped[Optional[str]] = mapped_column(String(300))
    city: Mapped[Optional[str]] = mapped_column(String(200))
    province: Mapped[Optional[str]] = mapped_column(String(200))
    country: Mapped[str] = mapped_column(String(10), default="IR")
    phone_numbers: Mapped[Optional[List[str]]] = mapped_column(ARRAY(Text))
    email_addresses: Mapped[Optional[List[str]]] = mapped_column(ARRAY(Text))
    specializations: Mapped[Optional[List[str]]] = mapped_column(ARRAY(Text))
    has_online_catalog: Mapped[Optional[bool]] = mapped_column(Boolean)
    catalog_url: Mapped[Optional[str]] = mapped_column(String(2000))
    catalog_entry_points: Mapped[Optional[List[str]]] = mapped_column(ARRAY(Text))
    total_products: Mapped[int] = mapped_column(Integer, default=0)
    status: Mapped[str] = mapped_column(String(50), default="active")
    notes: Mapped[Optional[str]] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)

    offerings: Mapped[List["SupplierOffering"]] = relationship(back_populates="supplier")
    mirror: Mapped[Optional["HTTrackMirror"]] = relationship(back_populates="supplier", uselist=False)


class Molecule(Base):
    __tablename__ = "molecules"
    __table_args__ = (
        Index("idx_molecules_cas", "cas_number"),
        Index("idx_molecules_formula", "molecular_formula"),
    )

    molecule_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Real InChIKey (27 chars) when a structure is known; NULL otherwise.
    # Non-InChI fallback identifiers MUST NOT live here — see source_identity.
    inchi_key: Mapped[Optional[str]] = mapped_column(String(27), unique=True)
    # Deterministic dedup identity: valid InChIKey > normalized CAS >
    # supplier+product-code > stable 27-char fallback hash. Never exposed
    # as an InChIKey in APIs/CSVs.
    source_identity: Mapped[str] = mapped_column(String(128), unique=True)
    # Explicit organic classification (§ organic_classifier.py)
    organic_status: Mapped[str] = mapped_column(String(20), default="unknown")  # true|false|unknown
    organic_reason: Mapped[Optional[str]] = mapped_column(String(50))  # structure|cas_resolution|name_resolution|manual
    organic_confidence: Mapped[Optional[float]] = mapped_column(Float)
    organic_lookup_error: Mapped[Optional[str]] = mapped_column(String(300))
    classification_review_required: Mapped[bool] = mapped_column(Boolean, default=False)
    iupac_name: Mapped[Optional[str]] = mapped_column(Text)
    common_names: Mapped[Optional[List[str]]] = mapped_column(ARRAY(Text))
    persian_names: Mapped[Optional[List[str]]] = mapped_column(ARRAY(Text))
    cas_number: Mapped[Optional[str]] = mapped_column(String(20))
    molecular_formula: Mapped[Optional[str]] = mapped_column(String(200))
    molecular_weight: Mapped[Optional[float]] = mapped_column(Float)
    canonical_smiles: Mapped[Optional[str]] = mapped_column(Text)
    inchi: Mapped[Optional[str]] = mapped_column(Text)
    pubchem_cid: Mapped[Optional[int]] = mapped_column(BigInteger)
    ec_number: Mapped[Optional[str]] = mapped_column(String(20))
    boiling_point: Mapped[Optional[str]] = mapped_column(String(100))
    melting_point: Mapped[Optional[str]] = mapped_column(String(100))
    density: Mapped[Optional[str]] = mapped_column(String(100))
    appearance: Mapped[Optional[str]] = mapped_column(Text)
    ghs_pictograms: Mapped[Optional[List[str]]] = mapped_column(ARRAY(Text))
    hazard_statements: Mapped[Optional[List[str]]] = mapped_column(ARRAY(Text))
    signal_word: Mapped[Optional[str]] = mapped_column(String(20))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)

    offerings: Mapped[List["SupplierOffering"]] = relationship(back_populates="molecule")


class SupplierOffering(Base):
    __tablename__ = "supplier_offerings"
    __table_args__ = (
        UniqueConstraint("molecule_id", "supplier_id", "supplier_product_code",
                         name="uq_offering"),
        Index("idx_offerings_supplier", "supplier_id"),
        Index("idx_offerings_molecule", "molecule_id"),
        Index("idx_offerings_available", "is_currently_available"),
    )

    offering_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    molecule_id: Mapped[int] = mapped_column(ForeignKey("molecules.molecule_id"))
    supplier_id: Mapped[int] = mapped_column(ForeignKey("suppliers.supplier_id"))
    supplier_product_code: Mapped[Optional[str]] = mapped_column(String(200))
    brand: Mapped[Optional[str]] = mapped_column(String(200))
    grade: Mapped[str] = mapped_column(String(100))
    purity: Mapped[Optional[str]] = mapped_column(String(100))
    purity_numeric: Mapped[Optional[float]] = mapped_column(Float)
    pack_sizes: Mapped[Optional[dict]] = mapped_column(JSONB)
    price_min: Mapped[Optional[float]] = mapped_column(Float)
    price_max: Mapped[Optional[float]] = mapped_column(Float)
    currency: Mapped[Optional[str]] = mapped_column(String(10))
    availability_status: Mapped[Optional[str]] = mapped_column(String(50))
    product_url: Mapped[Optional[str]] = mapped_column(String(2000))
    httrack_source_file: Mapped[Optional[str]] = mapped_column(String(2000))
    date_first_seen: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    date_last_verified: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    date_last_changed: Mapped[Optional[datetime]] = mapped_column(DateTime)
    is_currently_available: Mapped[bool] = mapped_column(Boolean, default=True)
    extraction_confidence: Mapped[Optional[float]] = mapped_column(Float)
    raw_page_hash: Mapped[Optional[str]] = mapped_column(String(64))

    molecule: Mapped[Molecule] = relationship(back_populates="offerings")
    supplier: Mapped[Supplier] = relationship(back_populates="offerings")


class HTTrackMirror(Base):
    __tablename__ = "httrack_mirrors"
    __table_args__ = (Index("idx_mirrors_supplier", "supplier_id"),)

    mirror_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    supplier_id: Mapped[int] = mapped_column(ForeignKey("suppliers.supplier_id"), unique=True)
    mirror_path: Mapped[str] = mapped_column(String(1000))
    project_name: Mapped[Optional[str]] = mapped_column(String(200))
    httrack_profile: Mapped[Optional[str]] = mapped_column(String(100))
    initial_mirror_date: Mapped[Optional[datetime]] = mapped_column(DateTime)
    last_update_date: Mapped[Optional[datetime]] = mapped_column(DateTime)
    total_files: Mapped[Optional[int]] = mapped_column(Integer)
    html_files: Mapped[Optional[int]] = mapped_column(Integer)
    pdf_files: Mapped[Optional[int]] = mapped_column(Integer)
    excel_files: Mapped[Optional[int]] = mapped_column(Integer)
    mirror_size_bytes: Mapped[Optional[int]] = mapped_column(BigInteger)
    last_changes_json: Mapped[Optional[dict]] = mapped_column(JSONB)
    files_new_last_run: Mapped[Optional[int]] = mapped_column(Integer)
    files_modified_last_run: Mapped[Optional[int]] = mapped_column(Integer)
    files_removed_last_run: Mapped[Optional[int]] = mapped_column(Integer)
    httrack_return_code: Mapped[Optional[int]] = mapped_column(Integer)
    httrack_flags_used: Mapped[Optional[str]] = mapped_column(Text)
    uses_playwright_fallback: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)

    supplier: Mapped[Supplier] = relationship(back_populates="mirror")


class CrawlRunState(Base):
    """Persisted crawl-run/task state (remediation §2/§4).

    Lets /api/v1/coverage report real queued/running counts instead of zeros,
    and lets latest-run logic be timestamp-driven rather than ad hoc.
    """
    __tablename__ = "crawl_run_state"
    __table_args__ = (Index("idx_run_state_supplier", "supplier_id"),
                      Index("idx_run_state_state", "state"))

    run_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    supplier_id: Mapped[Optional[int]] = mapped_column(ForeignKey("suppliers.supplier_id"))
    task_id: Mapped[Optional[str]] = mapped_column(String(64))
    state: Mapped[str] = mapped_column(String(20), default="queued")  # queued|running|success|partial|failed|skipped
    reason: Mapped[Optional[str]] = mapped_column(String(300))
    queued_at: Mapped[Optional[datetime]] = mapped_column(DateTime)
    started_at: Mapped[Optional[datetime]] = mapped_column(DateTime)
    finished_at: Mapped[Optional[datetime]] = mapped_column(DateTime)


class RejectedCatalogueItem(Base):
    """Audit trail for every parser candidate that did NOT enter the database.

    Nothing is silently discarded: rejected entries are retained with their
    raw fields and the rejection stage/reason so they can be re-processed
    when parsing or classification policy improves (§4.2 of the fix guide).
    """
    __tablename__ = "rejected_catalogue_items"
    __table_args__ = (Index("idx_rejected_supplier", "supplier_id"),)

    rejection_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    supplier_id: Mapped[Optional[int]] = mapped_column(ForeignKey("suppliers.supplier_id"))
    source_file: Mapped[Optional[str]] = mapped_column(String(2000))
    source_url: Mapped[Optional[str]] = mapped_column(String(2000))
    raw_title: Mapped[Optional[str]] = mapped_column(Text)
    raw_description: Mapped[Optional[str]] = mapped_column(Text)
    cas_number: Mapped[Optional[str]] = mapped_column(String(20))
    molecular_formula: Mapped[Optional[str]] = mapped_column(String(200))
    canonical_smiles: Mapped[Optional[str]] = mapped_column(Text)
    grade: Mapped[Optional[str]] = mapped_column(String(100))
    purity: Mapped[Optional[str]] = mapped_column(String(100))
    brand: Mapped[Optional[str]] = mapped_column(String(200))
    extraction_method: Mapped[Optional[str]] = mapped_column(String(50))
    rejection_stage: Mapped[str] = mapped_column(String(30))  # grade|validation|organic|database_sync
    rejection_reason: Mapped[Optional[str]] = mapped_column(String(300))
    rejected_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)


class CrawlLog(Base):
    __tablename__ = "crawl_log"
    __table_args__ = (Index("idx_crawl_logs_supplier", "supplier_id"),)

    log_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    supplier_id: Mapped[Optional[int]] = mapped_column(ForeignKey("suppliers.supplier_id"))
    mirror_id: Mapped[Optional[int]] = mapped_column(ForeignKey("httrack_mirrors.mirror_id"))
    crawl_start: Mapped[Optional[datetime]] = mapped_column(DateTime)
    crawl_end: Mapped[Optional[datetime]] = mapped_column(DateTime)
    crawl_type: Mapped[Optional[str]] = mapped_column(String(50))
    pages_crawled: Mapped[Optional[int]] = mapped_column(Integer)
    products_found: Mapped[Optional[int]] = mapped_column(Integer)
    products_new: Mapped[Optional[int]] = mapped_column(Integer)
    products_updated: Mapped[Optional[int]] = mapped_column(Integer)
    products_removed: Mapped[Optional[int]] = mapped_column(Integer)
    httrack_duration_sec: Mapped[Optional[float]] = mapped_column(Float)
    parse_duration_sec: Mapped[Optional[float]] = mapped_column(Float)
    errors: Mapped[Optional[dict]] = mapped_column(JSONB)
    status: Mapped[Optional[str]] = mapped_column(String(50))
    partial_reason: Mapped[Optional[str]] = mapped_column(String(300))


class OfferingHistory(Base):
    __tablename__ = "offering_history"

    history_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    offering_id: Mapped[Optional[int]] = mapped_column(Integer)
    molecule_id: Mapped[Optional[int]] = mapped_column(Integer)
    supplier_id: Mapped[Optional[int]] = mapped_column(Integer)
    change_type: Mapped[Optional[str]] = mapped_column(String(50))
    old_values: Mapped[Optional[dict]] = mapped_column(JSONB)
    new_values: Mapped[Optional[dict]] = mapped_column(JSONB)
    detected_via: Mapped[Optional[str]] = mapped_column(String(100))
    changed_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
