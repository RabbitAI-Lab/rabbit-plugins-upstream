#!/usr/bin/env python3
"""resolve_names.py — resolve a list of molecule names to SMILES via PubChem.

Usage:
  python3 resolve_names.py <names.txt> <out.csv> [missing.txt]

Notes (debugged 2026-08-03):
  - PUG REST batch POST returns 404 for name->CID; per-name GET works.
  - The JSON property is "ConnectivitySMILES" (or "CanonicalSMILES" when
    canonicalization is available) — check both keys.
  - Unicode names (beta, alpha, primes, dashes) need ASCII-ification.
  - Retries with backoff per name; failures go to missing.txt with reasons.
"""
import argparse, csv, json, sys, time, urllib.parse, urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import debug_utils as du

BASE = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"

BASE = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"
ASCII_MAP = {
    "β": "beta", "α": "alpha", "δ": "delta", "γ": "gamma", "ε": "epsilon",
    "ω": "omega", "μ": "mu", "θ": "theta", "π": "pi", "σ": "sigma",
    "′": "'", "’": "'", "–": "-", "—": "-", "−": "-", "º": "", "°": "",
}


def get(url, timeout=40):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode()


def asciify(nm):
    out = nm
    for k, v in ASCII_MAP.items():
        out = out.replace(k, v)
    return out


def fetch_props(name):
    """-> (smiles, formula, mw) or None; tries original + asciified name."""
    for cand in (name, asciify(name)):
        q = urllib.parse.quote(cand)
        for attempt in range(3):
            try:
                url = (f"{BASE}/compound/name/{q}/"
                       "property/CanonicalSMILES,MolecularFormula,MolecularWeight/JSON")
                d = json.loads(get(url))
                p = d["PropertyTable"]["Properties"][0]
                smi = p.get("CanonicalSMILES") or p.get("ConnectivitySMILES")
                if smi:
                    return smi, p.get("MolecularFormula", ""), p.get("MolecularWeight", "")
                return None
            except Exception as e:
                du.LOG.debug("name %r (cand %r) attempt %d: %s %s", name, cand, attempt, type(e).__name__, e)
                time.sleep(0.9 + attempt * 0.7)
    return None


def main(names_file, out_csv, missing_csv=None, debug=False, log_file=None):
    du.setup_logging(debug=debug, log_file=log_file)
    du.install_exception_hook()
    log = du.LOG
    du.require_file(names_file, "names file")
    names = [ln.strip() for ln in open(names_file, encoding="utf-8") if ln.strip()]
    seen = set()
    uniq = [n for n in names if not (n in seen or seen.add(n))]
    log.info("%d unique names", len(uniq))
    rows, missing = [], []
    for i, nm in enumerate(uniq, 1):
        res = fetch_props(nm)
        if res:
            rows.append((nm,) + res)
        else:
            missing.append(nm)
        if i % 50 == 0:
            log.info("  %d/%d resolved %d", i, len(uniq), len(rows))
        time.sleep(0.25)
    with open(out_csv, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["name", "smiles", "formula", "mw"])
        w.writerows(rows)
    mfile = missing_csv or out_csv.replace(".csv", "_missing.txt")
    with open(mfile, "w") as f:
        f.write("\n".join(missing))
    log.info("DONE: %d resolved -> %s; %d missing -> %s", len(rows), out_csv, len(missing), mfile)
    if missing:
        print("MISSING:", ", ".join(missing)[:400], flush=True)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("names")
    ap.add_argument("out_csv")
    ap.add_argument("missing_csv", nargs="?")
    ap.add_argument("--debug", action="store_true")
    ap.add_argument("--log-file", default=None)
    a = ap.parse_args()
    main(a.names, a.out_csv, a.missing_csv, debug=a.debug, log_file=a.log_file)
