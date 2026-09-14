"""v2.16 regression tests (strategy pillars P1.2, P3.1, P3.3, P5.1, F4).

Covers: the market-verified seed baseline, CID dedupe at admission,
the one-command export-verified pipeline, provenance hashing, the
provider hop chain (graceful no-AI degradation), and the exhaustive
relay failover with per-host method cache.
"""
import csv
import hashlib
import json
import re
import os
import sys
import tempfile

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils import seed_db  # noqa: E402
from src.utils.ai_hopchain import (NoHopError, _extract_json_array,   # noqa: E402
                                   normalize_batch)
from src.crawler.free_access_engine import FreeAccessEngine  # noqa: E402
from tools.export_verified import (cas_checksum_valid, merge_by_cid,   # noqa: E402
                                   provenance_hash, run, OUTPUT_COLUMNS)

SEED_DIR = seed_db.SEED_DIR
MARKET_CSV = seed_db.MARKET_VERIFIED_CSV


# ---------------------------------------------------------------------------
# seed baseline
# ---------------------------------------------------------------------------

def test_market_verified_seed_loads():
    assert os.path.exists(MARKET_CSV)
    meta = seed_db.load_seed_manifest(MARKET_CSV)
    assert meta.get("rows") == 873  # v2.17: 651 + 224 new molecules
    rows = []
    with open(MARKET_CSV, encoding="utf-8", newline="") as fh:
        r = csv.reader(fh)
        next(r)
        header = next(r)
        rows = [dict(zip(header, x)) for x in r if len(x) == len(header)]
    assert len(rows) == 873
    cids = [x["pubchem_cid"].strip() for x in rows if x["pubchem_cid"].strip()]
    assert len(cids) == len(set(cids)), "market-verified seed must be CID-unique"
    iks = [x["inchi_key"].strip() for x in rows if x["inchi_key"].strip()]
    assert len(iks) == len(set(iks)), "seed must be InChIKey-unique"
    # v2.17: 29 carbonless rows previously mislabelled confirmed_organic are
    # now explicitly flagged inorganic instead of being shipped as organic.
    assert all(x["organic_status"] in ("confirmed_organic", "inorganic")
               for x in rows)
    assert sum(1 for x in rows
               if x["organic_status"] == "confirmed_organic") == 844
    for x in rows:
        has_c = re.search(r"C(?![a-z])", x["molecular_formula"])
        if x["organic_status"] == "confirmed_organic":
            assert has_c, f"organic row without element C: {x['molecular_formula']}"
        else:
            assert not has_c
    # v2.16 backfill: every row carries a category
    assert all(x["category"].strip() for x in rows)


def test_merged_baseline_counts_and_identity_keys():
    rows = seed_db.load_seed_rows()
    assert len(rows) >= 1000  # 873 + expanded/legacy/inorganic after merges
    keys = [seed_db._row_key(r) for r in rows]
    assert len(keys) == len(set(keys)), "identity keys must be unique"
    # F5: name variants are preserved, not dropped
    multi = [r for r in rows
             if len([v for v in (r.get("name_variants") or "").split("; ")
                     if v]) > 1]
    assert len(multi) > 100


def test_env_example_shipped():
    """An env template must ship, and it must carry the placeholder literals
    install.sh checks for. The ClawHub registry strips leading-dot files from
    published artifacts, so env.example (the non-dotfile twin) is the one that
    actually survives; accept either so source and release both pass."""
    root = os.path.abspath(os.path.join(os.path.dirname(MARKET_CSV),
                                        os.pardir, os.pardir))
    candidates = [os.path.join(root, ".env.example"),
                  os.path.join(root, "env.example")]
    present = [c for c in candidates if os.path.exists(c)]
    assert present, "neither .env.example nor env.example is present"
    for c in present:
        txt = open(c, encoding="utf-8").read()
        assert "DB_PASSWORD=change-this-to-a-long-random-password" in txt, c
        assert "SEARCH_API_KEY=" in txt, c


# ---------------------------------------------------------------------------
# P1.2 — CID dedupe at admission
# ---------------------------------------------------------------------------


def test_merge_by_cid_zero_same_cid():
    rows = [
        {"molecule": "L-Ascorbic Acid", "common_name": "L-Ascorbic Acid",
         "cas": "50-81-7", "pubchem_cid": "54670067",
         "inchi_key": "A", "formula": "C6H8O7", "suppliers": "S1",
         "source_urls": "u1", "evidence_text": "e1"},
        {"molecule": "Vitamin C", "common_name": "Vitamin C",
         "cas": "50-81-7", "pubchem_cid": "54670067",
         "inchi_key": "B", "formula": "C6H8O7", "suppliers": "S2",
         "source_urls": "u2", "evidence_text": "e2"},
        {"molecule": "Unrelated", "common_name": "Unrelated",
         "cas": "", "pubchem_cid": "", "inchi_key": "C",
         "formula": "C9H8O4", "suppliers": "S3", "source_urls": "u3",
         "evidence_text": "e3"},
    ]
    merged = merge_by_cid(rows)
    assert len(merged) == 2
    cids = [m.get("pubchem_cid") for m in merged if m.get("pubchem_cid")]
    assert len(cids) == len(set(cids)), "output must have zero same-CID rows"
    # evidence/suppliers unioned, name variants preserved
    asc = next(m for m in merged if m.get("pubchem_cid") == "54670067")
    assert "S1" in asc["suppliers"] and "S2" in asc["suppliers"]
    assert "L-Ascorbic Acid" in asc["name_variants"]
    assert "Vitamin C" in asc["name_variants"]


# ---------------------------------------------------------------------------
# P3.1/P3.3 — one-command export + provenance hash
# ---------------------------------------------------------------------------

def test_provenance_hash_reproducible():
    r = {"evidence_text": "ملامین ۹۹٪", "evidence_url": "https://x.ir/p1",
         "pubchem_cid": "7955"}
    h1 = provenance_hash(r)
    h2 = provenance_hash(dict(r))
    assert h1 == h2
    assert h1 == hashlib.sha256(
        "ملامین ۹۹٪|https://x.ir/p1|7955".encode("utf-8")).hexdigest()


def test_cas_checksum():
    assert cas_checksum_valid("50-81-7")      # ascorbic acid
    assert cas_checksum_valid("67-64-1")      # acetone
    assert not cas_checksum_valid("108-78-3")  # model typo (bad digit)
    assert not cas_checksum_valid("abc")


def test_export_verified_reproduces_market_verified(tmp_path):
    out_path = str(tmp_path / "verified.csv")

    class A:  # minimal argparse namespace
        files = [MARKET_CSV]
        out = out_path
        include_unknown = False
        enforce_country = False

    assert run(A) == 0
    with open(out_path, encoding="utf-8", newline="") as fh:
        r = csv.reader(fh)
        meta = json.loads(next(r)[0][len("# export_metadata:"):].strip()
                         .strip('"').replace('""', '"'))
        header = next(r)
        rows = [dict(zip(header, x)) for x in r]
    # v2.17: the 29 flagged-inorganic seed rows are correctly rejected by the
    # organic gate, so the verified export is 844 of the 873 seed rows.
    assert meta["rows"] == 844
    assert len(rows) == 844
    assert meta["rejected"] == 29
    cids = [x["pubchem_cid"] for x in rows if x["pubchem_cid"]]
    assert len(cids) == len(set(cids))
    # every row carries a provenance hash that recomputes
    for x in rows[:20]:
        assert x["provenance_hash"] == hashlib.sha256(
            "|".join([x["evidence_text"].strip(), x["evidence_url"].strip(),
                      x["pubchem_cid"]]).encode("utf-8")).hexdigest()
    assert set(OUTPUT_COLUMNS) <= set(header)


def test_export_verified_rejects_to_sidecar(tmp_path):
    """Gates never silently discard: rejected rows go to <out>.rejected.csv."""
    src = tmp_path / "in.csv"
    src.write_text(
        '# export_metadata: {"rows": 2}\n'
        'molecule_name,common_name,cas_number,pubchem_cid,inchi_key,'
        'molecular_formula,molecular_weight,canonical_smiles,organic_status,'
        'category,grade,supplier_name,supplier_platform,availability_status,'
        'evidence_url,evidence_text,identity_method,source_type,record_date\n'
        'Ethanol,ethanol,64-17-5,702,XYZ,C2H6O,46.07,,confirmed_organic,'
        'organic_reagent,,,S,,https://x/1,e,i,s,2026-08-23\n'
        'Sodium Hydroxide,sodium hydroxide,1310-73-2,173,ABC,NaOH,40.00,'
        ',inorganic,organic_reagent,,,S,,https://x/2,e,i,s,2026-08-23\n',
        encoding="utf-8")
    out_path = str(tmp_path / "out.csv")

    class A:
        files = [str(src)]
        out = out_path
        include_unknown = False
        enforce_country = False

    assert run(A) == 0
    assert os.path.exists(out_path + ".rejected.csv")
    rej = open(out_path + ".rejected.csv", encoding="utf-8").read()
    assert "not_confirmed_organic" in rej
    assert "Sodium Hydroxide" in rej
    main_txt = open(out_path, encoding="utf-8").read()
    assert "Sodium Hydroxide" not in main_txt
    assert "Ethanol" in main_txt


# ---------------------------------------------------------------------------
# P5.1 — provider hop chain
# ---------------------------------------------------------------------------

def test_extract_json_array_tolerant():
    assert _extract_json_array('noise [{"item":1,"name":"x"}] tail') == \
        [{"item": 1, "name": "x"}]
    assert _extract_json_array('```json\n[{"item": 1}]\n```') == [{"item": 1}]
    assert _extract_json_array("no json here") is None


def test_normalize_batch_no_ai_never_invents(monkeypatch, tmp_path):
    monkeypatch.setenv("ICDB_ROUTER", str(tmp_path / "missing_router.py"))
    for var in ("GEMINI_API_KEY", "MISTRAL_API_KEY", "OPENROUTER_API_KEY",
                "LLM7_API_KEY"):
        monkeypatch.delenv(var, raising=False)
    from src.utils import ai_hopchain
    # stub the router resolver too (it falls back to a real workspace path)
    monkeypatch.setattr(ai_hopchain, "_router_path", lambda: None)
    ai_hopchain._DEAD_HOPS.clear()
    out = normalize_batch(["melamine 500g"], batch=1, pacing=0.0)
    assert out["results"][0]["name"] is None
    assert out["none_rate"] == 1.0
    assert out["failed_batches"] >= 1


def test_normalize_batch_parses_numbered_json(monkeypatch, tmp_path):
    monkeypatch.setenv("ICDB_ROUTER", str(tmp_path / "missing_router.py"))
    for var in ("GEMINI_API_KEY", "MISTRAL_API_KEY", "OPENROUTER_API_KEY",
                "LLM7_API_KEY"):
        monkeypatch.delenv(var, raising=False)
    from src.utils import ai_hopchain
    ai_hopchain._DEAD_HOPS.clear()

    def fake_hop(texts, system, timeout, max_tokens=1024):
        return ('```json\n[{"item": 1, "name": "melamine", '
                '"cas": "108-78-1", "confidence": 0.9}, '
                '{"item": 2, "name": "NONE"}]\n```')

    monkeypatch.setattr(ai_hopchain, "HOPS",
                          [("fake", fake_hop)])
    out = normalize_batch(["a", "b"], batch=2, pacing=0.0)
    assert out["results"][0]["name"] == "melamine"
    assert out["results"][0]["cas"] == "108-78-1"
    assert out["results"][1]["name"] is None
    assert out["none_rate"] == 0.5


def test_normalize_batch_value_field(monkeypatch, tmp_path):
    monkeypatch.setenv("ICDB_ROUTER", str(tmp_path / "missing_router.py"))
    for var in ("GEMINI_API_KEY", "MISTRAL_API_KEY", "OPENROUTER_API_KEY",
                "LLM7_API_KEY"):
        monkeypatch.delenv(var, raising=False)
    from src.utils import ai_hopchain
    ai_hopchain._DEAD_HOPS.clear()

    def fake_hop(texts, system, timeout, max_tokens=1024):
        return '[{"item": 1, "category": "vitamin"}]'

    monkeypatch.setattr(ai_hopchain, "HOPS", [("fake", fake_hop)])
    out = normalize_batch(["x"], batch=1, pacing=0.0, value_field="category")
    assert out["results"][0]["name"] == "vitamin"


# ---------------------------------------------------------------------------
# F4 — exhaustive relay failover + per-host method cache
# ---------------------------------------------------------------------------

def _mocked_engine():
    eng = FreeAccessEngine(tempfile.mkdtemp())

    def make(m, ok):
        def relay(url, output_dir):
            return {"method": m, "saved": 2 if ok else 0,
                    "error": None if ok else "SimulatedError"}
        return relay

    for m, ok in (("jina", False), ("wayback", False), ("commoncrawl", True),
                  ("spn2", True), ("translate", True), ("archive_today", True),
                  ("screenshot", True)):
        setattr(eng, f"fetch_via_{m}", make(m, ok))
    return eng


def test_failover_ordered_stop_on_success_and_cache():
    eng = _mocked_engine()
    cache = tempfile.mktemp(suffix=".json")
    r1 = eng.fetch_with_failover("https://x.ir/", "/tmp", host_key="x.ir",
                                 cache_path=cache)
    assert r1["method_used"] == "commoncrawl"
    tried1 = [k for k in r1 if isinstance(r1[k], dict)]
    assert tried1 == ["jina", "wayback", "commoncrawl"]
    # cached method is tried first on the next run
    r2 = eng.fetch_with_failover("https://x.ir/p2", "/tmp", host_key="x.ir",
                                 cache_path=cache)
    assert r2["method_used"] == "commoncrawl"
    tried2 = [k for k in r2 if isinstance(r2[k], dict)]
    assert tried2 == ["commoncrawl"]
    assert json.load(open(cache))["x.ir"]["method"] == "commoncrawl"


def test_failover_all_failed():
    eng = _mocked_engine()
    for m in ("jina", "wayback", "commoncrawl", "spn2", "translate",
              "archive_today", "screenshot"):
        setattr(eng, f"fetch_via_{m}",
                (lambda u, o: {"method": m, "saved": 0, "error": "X"}))
    r = eng.fetch_with_failover("https://dead.ir/", "/tmp", host_key="dead.ir")
    assert r["method_used"] is None
    assert r["total_saved"] == 0
