"""Streamlit dashboard — search UI + HTTrack mirror monitor panel (spec §6.2).

Run: streamlit run src/dashboard/app.py --server.port=8501
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import streamlit as st  # noqa: E402
from sqlalchemy import select  # noqa: E402

from src.config import get_config  # noqa: E402
from src.database.models import HTTrackMirror, Molecule, Supplier, SupplierOffering  # noqa: E402
from src.database.queries import global_stats, search_molecules  # noqa: E402
from src.database.session import get_db_session  # noqa: E402

st.set_page_config(page_title="Iran Chemical Database", layout="wide")
st.title("🧪 Iran Chemical Database — Research-Grade Molecules")
st.caption("HTTrack-powered live crawling system")


@st.cache_resource
def db_session():
    return get_db_session()


def main() -> None:
    cfg = get_config()
    db = db_session()

    tabs = st.tabs(["Search", "Molecules", "Suppliers", "HTTrack Mirror Monitor", "Statistics"])

    with tabs[0]:
        q = st.text_input("Search (name / CAS / formula / SMILES — EN or FA)")
        if q:
            rows, total = search_molecules(db, q, None, None, None, None, None, None, 1, 25)
            st.write(f"{total} result(s)")
            for m in rows:
                st.markdown(f"**{m.iupac_name or m.inchi_key}** — CAS `{m.cas_number}` · "
                            f"{m.molecular_formula} · {m.molecular_weight} g/mol")

    with tabs[1]:
        rows, total = search_molecules(db, None, None, None, None, None, None, None, 1, 100)
        data = [{"InChIKey": m.inchi_key, "Name": m.iupac_name, "CAS": m.cas_number,
                 "Formula": m.molecular_formula, "MW": m.molecular_weight}
                for m in rows]
        st.dataframe(data)

    with tabs[2]:
        suppliers = db.execute(select(Supplier)).scalars().all()
        data = [{"ID": s.supplier_id, "Name (EN)": s.company_name_en, "Name (FA)": s.company_name_fa,
                 "URL": s.website_url, "City": s.city, "Status": s.status,
                 "Verified": s.is_verified, "Products": s.total_products,
                 "Last crawl": s.last_crawled}
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
        s = global_stats(db)
        st.metric("Molecules", s["total_molecules"])
        st.metric("Suppliers", s["total_suppliers"])
        st.metric("Active suppliers", s["active_suppliers"])
        st.metric("Offerings", s["total_offerings"])
        st.metric("Available", s["available_offerings"])


if __name__ == "__main__":
    main()
