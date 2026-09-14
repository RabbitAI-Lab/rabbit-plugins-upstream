"""fix-guide migration: identity / organic / audit / coverage columns

Revision for the "incomplete CSV exports" fix guide:
  * Molecule.inchi_key becomes nullable (real InChIKeys only);
  * Molecule.source_identity added (unique, NOT NULL) — CAS-only records and
    fallback identities insert successfully instead of overflowing VARCHAR(27);
  * Molecule.organic_status / organic_reason / organic_confidence;
  * RejectedCatalogueItem audit table (rejections are never silently dropped);
  * Supplier.crawl_profile / catalog_type;
  * CrawlLog.partial_reason.

Works on BOTH fresh and existing databases: on a fresh database (no
`molecules` table yet) the full current schema is created via
Base.metadata.create_all; on an existing database only additive ALTERs run.
"""
from alembic import op
import sqlalchemy as sa

# standalone root revision (the project had no prior migration chain)
revision = "0002_fix_guide"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    has_molecules = sa.inspect(bind).has_table("molecules")

    if not has_molecules:
        # Fresh install: create the complete, fixed schema.
        from src.database.models import Base
        Base.metadata.create_all(bind)
        return

    # Existing install: additive, idempotent changes.
    for stmt in (
        "ALTER TABLE molecules ALTER COLUMN inchi_key DROP NOT NULL",
        "ALTER TABLE molecules ADD COLUMN IF NOT EXISTS source_identity VARCHAR(128)",
        "ALTER TABLE molecules ADD COLUMN IF NOT EXISTS organic_status VARCHAR(20) DEFAULT 'unknown'",
        "ALTER TABLE molecules ADD COLUMN IF NOT EXISTS organic_reason VARCHAR(50)",
        "ALTER TABLE molecules ADD COLUMN IF NOT EXISTS organic_confidence FLOAT",
        "ALTER TABLE suppliers ADD COLUMN IF NOT EXISTS crawl_profile VARCHAR(50) DEFAULT 'static_html'",
        "ALTER TABLE suppliers ADD COLUMN IF NOT EXISTS catalog_type VARCHAR(50)",
        "ALTER TABLE crawl_log ADD COLUMN IF NOT EXISTS partial_reason VARCHAR(300)",
    ):
        op.execute(stmt)

    # Backfill source_identity from the legacy inchi_key values (which were
    # real InChIKeys where present and fallback hashes elsewhere).
    op.execute(
        "UPDATE molecules SET source_identity = inchi_key "
        "WHERE source_identity IS NULL AND inchi_key IS NOT NULL"
    )
    # Any remaining NULL source_identity (shouldn't happen) gets a stable filler.
    op.execute(
        "UPDATE molecules SET source_identity = 'legacy-mol-' || molecule_id::text "
        "WHERE source_identity IS NULL"
    )
    op.execute("ALTER TABLE molecules ALTER COLUMN source_identity SET NOT NULL")
    op.execute("CREATE UNIQUE INDEX IF NOT EXISTS uq_molecules_source_identity "
               "ON molecules (source_identity)")
    op.execute("CREATE UNIQUE INDEX IF NOT EXISTS uq_molecules_inchi_key "
               "ON molecules (inchi_key) WHERE inchi_key IS NOT NULL")

    op.execute(
        "CREATE TABLE IF NOT EXISTS rejected_catalogue_items ("
        "  rejection_id SERIAL PRIMARY KEY,"
        "  supplier_id INTEGER,"
        "  source_file VARCHAR(2000),"
        "  source_url VARCHAR(2000),"
        "  raw_title TEXT,"
        "  raw_description TEXT,"
        "  cas_number VARCHAR(20),"
        "  molecular_formula VARCHAR(200),"
        "  canonical_smiles TEXT,"
        "  grade VARCHAR(100),"
        "  purity VARCHAR(100),"
        "  brand VARCHAR(200),"
        "  extraction_method VARCHAR(50),"
        "  rejection_stage VARCHAR(30) NOT NULL,"
        "  rejection_reason VARCHAR(300),"
        "  rejected_at TIMESTAMP DEFAULT now()"
        ")"
    )
    op.execute("CREATE INDEX IF NOT EXISTS idx_rejected_supplier "
               "ON rejected_catalogue_items (supplier_id)")


def downgrade() -> None:
    # Additive columns are kept (dropping unique columns would destroy data);
    # only the audit table is dropped.
    bind = op.get_bind()
    if sa.inspect(bind).has_table("rejected_catalogue_items"):
        op.drop_table("rejected_catalogue_items")
