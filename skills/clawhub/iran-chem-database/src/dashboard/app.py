"""Streamlit dashboard — search UI + mirror monitor + observability (remediation §9).

Panels: Search, Molecules, Suppliers, Mirrors, Coverage & Jobs, Rejections,
Reconciliation, Export readiness. Run:
  streamlit run src/dashboard/app.py --server.port=8501
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import streamlit as st  # noqa: E402
from sqlalchemy import desc, select  # noqa: E402

from src.api.coverage_logic import coverage_snapshot  # noqa: E402
from src.config import get_config  # noqa: E402
from src.database.models import (CrawlRunState, HTTrackMirror,  # noqa: E402
                                 RejectedCatalogueItem, Supplier)
from src.database.queries import search_molecules  # noqa: E402
from src.database.session import get_db_session  # noqa: E402

st.set_page_config(page_title="Iran Chemical Database", layout="wide")
st.title("🧪 Iran Chemical Database")
st.caption("Best-effort index of Iranian chemical supplier offerings — "
           "coverage is measured, not assumed. Installation provides software, "
           "not a populated dataset.")


@st.cache_resource
def db_session():
    return get_db_session()


def main() -> None:
    cfg = get_config()
    db = db_session()
    mode = (cfg.as_dict().get("parsing", {}) or {}).get("inclusion_mode", "all_identifiable_catalogue")
    st.info(f"Active inclusion policy: **{mode}**")

    tabs = st.tabs(["Search", "Molecules", "Suppliers", "Mirrors",
                    "Coverage & Jobs", "Rejections", "Reconciliation"])

    with tabs[0]:
        q = st.text_input("Search (name / CAS / formula / SMILES — EN or FA)")
        if q:
            rows, total = search_molecules(db, q, None, None, None, None, None, None, None, 1, 25)
            st.write(f"{total} result(s) — paginated view; use /api/v1/export for full CSV")
            for m in rows:
                st.markdown(f"**{m.iupac_name or m.inchi_key}** — CAS `{m.cas_number}` · "
                            f"{m.molecular_formula} · {m.molecular_weight} g/mol · "
                            f"organic: `{m.organic_status}`")

    with tabs[1]:
        rows, total = search_molecules(db, None, None, None, None, None, None, None, None, 1, 100)
        data = [{"Source identity": m.source_identity, "InChIKey": m.inchi_key or "",
                 "Name": m.iupac_name, "CAS": m.cas_number,
                 "Formula": m.molecular_formula, "MW": m.molecular_weight,
                 "Organic": m.organic_status, "Organic reason": m.organic_reason,
                 "Review?": m.classification_review_required}
                for m in rows]
        st.dataframe(data)
        st.caption(f"Showing first page only ({len(data)} of {total}). "
                   "`organic_status=true` means CONFIRMED organic — unknown rows are unresolved, not inorganic.")

    with tabs[2]:
        suppliers = db.execute(select(Supplier)).scalars().all()
        data = [{"ID": s.supplier_id, "Name (EN)": s.company_name_en, "Name (FA)": s.company_name_fa,
                 "URL": s.website_url, "Profile": s.crawl_profile, "Status": s.status,
                 "Robots": s.robots_status, "HTTP": s.last_http_status,
                 "Products": s.total_products, "Last good count": s.last_successful_product_count,
                 "Partial reason": s.partial_reason, "Last crawl": s.last_crawled}
                for s in suppliers]
        st.dataframe(data)

    with tabs[3]:
        st.subheader("HTTrack Mirror Monitor")
        mirrors = db.execute(select(HTTrackMirror)).scalars().all()
        for m in mirrors:
            with st.expander(f"{m.project_name or m.mirror_path} (files: {m.total_files})"):
                st.write(f"Path: `{m.mirror_path}`")
                st.write(f"HTML: {m.html_files} · PDF: {m.pdf_files} · Excel: {m.excel_files}")
                st.write(f"Size: {m.mirror_size_bytes} bytes · Last update: {m.last_update_date}")
                st.write(f"New: {m.files_new_last_run} · Modified: {m.files_modified_last_run} · "
                         f"Removed: {m.files_removed_last_run}")
                st.write(f"htrack return code: {m.httrack_return_code} · "
                         f"Playwright fallback: {m.uses_playwright_fallback}")

    with tabs[4]:
        cov = coverage_snapshot(db)
        s = cov["suppliers"]
        st.subheader("Supplier crawl status")
        st.write(s)
        st.metric("Configured suppliers", s["configured"])
        c1, c2, c3, c4, c5, c6 = st.columns(6)
        c1.metric("Success", s["success"]); c2.metric("Partial", s["partial"])
        c3.metric("Failed", s["failed"]); c4.metric("Queued", s["queued"])
        c5.metric("Running", s["running"]); c6.metric("Not started", s["not_started"])
        r = cov["records"]
        st.subheader("Records")
        st.write({k: r[k] for k in ("accepted_molecules", "offerings", "rejected_grade",
                                    "rejected_validation", "organic_true", "organic_false",
                                    "organic_unknown")})
        st.subheader("Export readiness")
        st.write(cov["export_readiness"])
        st.subheader("Task queue (persisted run states)")
        runs = db.execute(select(CrawlRunState).order_by(desc(CrawlRunState.run_id)).limit(30)).scalars().all()
        st.dataframe([{"run": x.run_id, "supplier": x.supplier_id, "state": x.state,
                       "reason": x.reason, "queued": x.queued_at,
                       "started": x.started_at, "finished": x.finished_at} for x in runs])

    with tabs[5]:
        st.subheader("Rejection audit (nothing silently dropped)")
        by_stage = st.selectbox("Stage", ["all", "grade", "validation", "database_sync"])
        q = select(RejectedCatalogueItem).order_by(desc(RejectedCatalogueItem.rejection_id)).limit(200)
        if by_stage != "all":
            q = q.where(RejectedCatalogueItem.rejection_stage == by_stage)
        rows = db.execute(q).scalars().all()
        st.dataframe([{"supplier": r.supplier_id, "title": (r.raw_title or "")[:60],
                       "stage": r.rejection_stage, "reason": r.rejection_reason,
                       "at": r.rejected_at} for r in rows])

    with tabs[6]:
        st.subheader("Per-supplier reconciliation funnel")
        from src.api.routes.observability import reconciliation as _rec
        data = _rec(db)
        st.dataframe(data["suppliers"])


if __name__ == "__main__":
    main()
