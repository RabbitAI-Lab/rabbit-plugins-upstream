#!/usr/bin/env python3
"""
run_data_layers.py — ORCHESTRATOR for the 7 supplemental data layers.
Runs all sources, prints a unified JSON report + composite data-confidence,
and writes data/data_layers_report.json. Honest: any UNVERIFIED source is
flagged, never faked.

Layers:
  [1] COT (CFTC)            -> data_sources_cot.py
  [2] Intraday 4H           -> data_sources_intraday.py
  [3] Volume / Order Flow   -> data_sources_volume.py
  [4] News Sentiment (NLP)  -> data_sources_news_rss.py
  [5] Options Put/Call      -> data_sources_options.py
  [6] Retail Sentiment      -> data_sources_retail.py
  [7] Central Bank Buying   -> data_sources_central_bank.py
"""
import json, sys, os, importlib.util

SCRIPT_DIR = os.path.dirname(__file__)

def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(SCRIPT_DIR, name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def main():
    results = {}
    # [2] intraday
    try:
        results["intraday"] = load("data_sources_intraday").run("4h")[0]
    except Exception as e:
        results["intraday"] = {"status": "ERROR", "reason": str(e)}
    # [3] volume
    try:
        results["volume"] = load("data_sources_volume").run()
    except Exception as e:
        results["volume"] = {"status": "ERROR", "reason": str(e)}
    # [4] news
    try:
        results["news"] = load("data_sources_news_rss").run()
    except Exception as e:
        results["news"] = {"status": "ERROR", "reason": str(e)}
    # [5] options
    try:
        results["options"] = load("data_sources_options").run()
    except Exception as e:
        results["options"] = {"status": "ERROR", "reason": str(e)}
    # [6] retail
    try:
        results["retail"] = load("data_sources_retail").run()
    except Exception as e:
        results["retail"] = {"status": "ERROR", "reason": str(e)}
    # [7] central bank
    try:
        results["central_bank"] = load("data_sources_central_bank").run()
    except Exception as e:
        results["central_bank"] = {"status": "ERROR", "reason": str(e)}
    # [1] COT
    try:
        results["cot"] = load("data_sources_cot").run()
    except Exception as e:
        results["cot"] = {"status": "ERROR", "reason": str(e)}

    # ---- composite data-confidence ----
    verified = sum(1 for k, v in results.items() if isinstance(v, dict) and v.get("status") == "OK")
    total = len(results)
    # weight: intraday/volume/news/options/cbank count more than cot/retail (which are often blocked)
    core = ["intraday", "volume", "news", "options", "central_bank"]
    core_ok = sum(1 for k in core if results.get(k, {}).get("status") == "OK")
    confidence = round(core_ok / len(core), 2)

    summary = {
        "symbol": "XAU/USD",
        "layers_total": total,
        "layers_verified": verified,
        "core_confidence": confidence,
        "unverified": [k for k, v in results.items() if isinstance(v, dict) and v.get("status") != "OK"],
        "note": "COT & retail often UNVERIFIED without Firecrawl/keys — non-blocking; core 5 must pass for high confidence.",
    }
    report = {"summary": summary, "layers": results,
              "_ts": __import__("time").time()}
    out = os.path.join(SCRIPT_DIR, "..", "data", "data_layers_report.json")
    try:
        json.dump(report, open(out, "w"), indent=2)
    except Exception:
        pass
    return report

if __name__ == "__main__":
    r = main()
    print(json.dumps(r, indent=2))
