"""remediation migration: run states, supplier/molecule observability fields

Additive-only changes for the remediation release (v2.3.0):
  * crawl_run_state table (persisted queued/running/terminal states);
  * suppliers: expected_catalogue_type, expected_pagination, requires_login,
    robots_status, last_http_status, last_successful_product_count,
    partial_reason;
  * molecules: organic_lookup_error, classification_review_required.

Fresh databases get the full schema; existing databases get additive ALTERs.
"""
from alembic import op
import sqlalchemy as sa

revision = "0003_remediation"
down_revision = "0002_fix_guide"
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    has_molecules = sa.inspect(bind).has_table("molecules")

    if not has_molecules:
        from src.database.models import Base
        Base.metadata.create_all(bind)
        return

    for stmt in (
        "ALTER TABLE molecules ADD COLUMN IF NOT EXISTS organic_lookup_error VARCHAR(300)",
        "ALTER TABLE molecules ADD COLUMN IF NOT EXISTS classification_review_required BOOLEAN DEFAULT false",
        "ALTER TABLE suppliers ADD COLUMN IF NOT EXISTS expected_catalogue_type VARCHAR(50)",
        "ALTER TABLE suppliers ADD COLUMN IF NOT EXISTS expected_pagination VARCHAR(50)",
        "ALTER TABLE suppliers ADD COLUMN IF NOT EXISTS requires_login BOOLEAN DEFAULT false",
        "ALTER TABLE suppliers ADD COLUMN IF NOT EXISTS robots_status VARCHAR(50)",
        "ALTER TABLE suppliers ADD COLUMN IF NOT EXISTS last_http_status INTEGER",
        "ALTER TABLE suppliers ADD COLUMN IF NOT EXISTS last_successful_product_count INTEGER",
        "ALTER TABLE suppliers ADD COLUMN IF NOT EXISTS partial_reason VARCHAR(300)",
    ):
        op.execute(stmt)

    op.execute(
        "CREATE TABLE IF NOT EXISTS crawl_run_state ("
        "  run_id SERIAL PRIMARY KEY,"
        "  supplier_id INTEGER,"
        "  task_id VARCHAR(64),"
        "  state VARCHAR(20) NOT NULL DEFAULT 'queued',"
        "  reason VARCHAR(300),"
        "  queued_at TIMESTAMP,"
        "  started_at TIMESTAMP,"
        "  finished_at TIMESTAMP"
        ")"
    )
    op.execute("CREATE INDEX IF NOT EXISTS idx_run_state_supplier ON crawl_run_state (supplier_id)")
    op.execute("CREATE INDEX IF NOT EXISTS idx_run_state_state ON crawl_run_state (state)")


def downgrade() -> None:
    bind = op.get_bind()
    if sa.inspect(bind).has_table("crawl_run_state"):
        op.drop_table("crawl_run_state")
