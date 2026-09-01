#!/usr/bin/env python3
"""forge.py — the single, deterministic entrypoint every agent runtime can call.

Why this file exists
--------------------
v1.3 exposed nine scripts with nine different argument shapes. Any agent that
wanted to use the skill had to hand-write glue, and each runtime wrote it
differently — which is exactly how "the same skill" starts producing different
results. v1.5.0 puts one contract in front of all of them:

    python3 scripts/forge.py <command> [--json] [options]
    echo '{"command":"run","pdf":"a.pdf"}' | python3 scripts/forge.py --stdin

Contract guarantees
-------------------
* **stdout is data only.** With ``--json`` (or ``--stdin``) stdout is exactly
  one JSON document. All progress/diagnostics go to stderr. Safe to pipe.
* **Exit codes are stable.**
      0  success
      1  contract/QA failure (the work ran, the result is not acceptable)
      2  usage error (bad arguments)
      3  missing dependency (poppler/tesseract/python module)
      4  no usable model provider
      5  interrupted / timeout
* **Idempotent + resumable.** Every stage caches; re-running a completed stage
  is a no-op that returns the previous result.
* **Deterministic.** Temperature 0, fixed seed, canonical JSON, stable
  ordering, cross-model dedupe — see ``docs/MODEL_COMPATIBILITY.md``.
* **Model-agnostic.** Providers are auto-discovered from the environment;
  ``FORGE_MOCK=1`` gives a fully offline, network-free run for CI.

Commands
--------
  describe    machine-readable capability manifest (no side effects)
  doctor      environment + provider diagnosis; ``--json`` for a report
  selftest    offline test suite (no network, no keys)
  extract     PDF -> dual-OCR evidence
  correct     evidence -> reconstructed pages
  sessions    reconstructed pages -> session candidates
  enrich      pages + sessions -> study aids
  verify      independent flashcard answer verification
  build       -> self-contained offline HTML
  audit       fidelity metrics
  qa          QA gates over the built HTML
  package     verified ZIP + SHA-256
  run         the whole pipeline (pauses at session review unless --auto-sessions)
  compat      cross-model compatibility matrix
  reproduce   run the same contract on N models and report agreement
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from common import canonical_json, write_json, log_line          # noqa: E402
import model_adapters as MA                                       # noqa: E402

EXIT_OK, EXIT_CONTRACT, EXIT_USAGE, EXIT_DEPS, EXIT_NOPROVIDER, EXIT_INTERRUPT = 0, 1, 2, 3, 4, 5
VERSION = "1.5.1"


# ──────────────────────────────────────────────────────────────────────────
def _out(payload: dict, as_json: bool) -> None:
    if as_json:
        print(canonical_json(payload))
    else:
        print(canonical_json(payload))


def _run(args: list, cwd: Path | None = None) -> int:
    log_line("exec", cmd=" ".join(str(a) for a in args[:4]) + " …")
    return subprocess.call([sys.executable] + [str(a) for a in args], cwd=str(cwd or ROOT))


# ── describe ───────────────────────────────────────────────────────────────
def cmd_describe(a) -> int:
    manifest = json.loads((ROOT / "agent-manifest.json").read_text("utf-8")) \
        if (ROOT / "agent-manifest.json").exists() else {}
    _out(manifest or {"name": "persian-pdf-studyguide-forge", "version": VERSION}, True)
    return EXIT_OK


# ── doctor ─────────────────────────────────────────────────────────────────
def cmd_doctor(a) -> int:
    import importlib.util
    bins = {b: shutil.which(b) for b in
            ("python3", "pdfinfo", "pdftotext", "pdftoppm", "tesseract", "node", "zip")}
    mods = {m: bool(importlib.util.find_spec(m)) for m in ("fitz", "bs4", "PIL")}
    langs: list = []
    if bins["tesseract"]:
        try:
            r = subprocess.run(["tesseract", "--list-langs"], capture_output=True, text=True)
            langs = [x.strip() for x in r.stdout.splitlines()[1:] if x.strip()]
        except Exception:
            pass
    provs = MA.discover_providers(a.providers, include_mock=True)
    net_ok = any(p.dialect != "mock" for p in provs)
    required_ok = all(bins[b] for b in ("pdfinfo", "pdftotext", "pdftoppm", "tesseract")) \
        and {"fas", "eng"}.issubset(set(langs))
    report = {
        "schema": "forge.doctor/1",
        "skill": "persian-pdf-studyguide-forge",
        "version": VERSION,
        "python": sys.version.split()[0],
        "binaries": bins,
        "python_modules": mods,
        "tesseract_languages": langs,
        "providers": [{"name": p.name, "dialect": p.dialect, "model": p.model,
                       "source": p.notes or "config"} for p in provs],
        "provider_count": len([p for p in provs if p.dialect != "mock"]),
        "offline_mock_available": True,
        "extraction_ready": required_ok,
        "model_ready": net_ok or os.environ.get("FORGE_MOCK") == "1",
        "cache_dir": str(MA.cache_dir()),
        "install_hints": {
            "debian": "sudo apt-get install -y poppler-utils tesseract-ocr tesseract-ocr-fas tesseract-ocr-eng zip",
            "macos": "brew install poppler tesseract tesseract-lang",
            "python": f"{sys.executable} -m pip install -r requirements.txt",
            "offline": "export FORGE_MOCK=1   # run the whole pipeline with no keys",
            "keys": "export ANY OF: OPENAI_API_KEY ANTHROPIC_API_KEY GEMINI_API_KEY "
                    "GROQ_API_KEY OPENROUTER_API_KEY MISTRAL_API_KEY COHERE_API_KEY "
                    "DEEPSEEK_API_KEY XAI_API_KEY TOGETHER_API_KEY OLLAMA_HOST",
        },
    }
    report["verdict"] = ("READY" if required_ok and report["model_ready"]
                         else "DEGRADED" if required_ok or report["model_ready"]
                         else "NOT_READY")
    _out(report, True)
    if not report["model_ready"]:
        return EXIT_NOPROVIDER
    return EXIT_OK if required_ok else EXIT_DEPS


# ── selftest ───────────────────────────────────────────────────────────────
def cmd_selftest(a) -> int:
    rc = _run([HERE / "self_test.py"])
    return EXIT_OK if rc == 0 else EXIT_CONTRACT


# ── compat ─────────────────────────────────────────────────────────────────
def cmd_compat(a) -> int:
    provs = MA.discover_providers(a.providers, include_mock=a.mock,
                                  only=a.only.split(",") if a.only else None)
    if not provs:
        _out({"error": "no usable provider", "hint": "set an API key or FORGE_MOCK=1"}, True)
        return EXIT_NOPROVIDER
    report = MA.compat_matrix(provs, timeout=a.timeout)
    if a.out:
        write_json(a.out, report)
    _out(report, True)
    return EXIT_OK if report["verdict"] == "READY" else EXIT_CONTRACT


# ── reproduce ──────────────────────────────────────────────────────────────
_REPRO_SYSTEM = ("You are a strict JSON generator for a Persian study-guide pipeline. "
                 "Output only valid JSON. Never add prose, markdown or reasoning.")
_REPRO_PROMPT = (
    'From the source below produce exactly this JSON:\n'
    '{"flash":[3 objects with q,a,ref],"quiz":[2 objects with q,options(4),answer(A-D),why,ref]}\n'
    'ref must be an integer page number. Answers must be full statements.\n\n'
    'صفحه 1 — مقدمه\nحافظهٔ کوتاه‌مدت ظرفیتی حدود هفت واحد دارد و بدون مرور حدود سی ثانیه دوام می‌آورد.\n\n'
    'صفحه 2 — رمزگردانی\nرمزگردانی معنایی ماندگارترین نوع رمزگردانی در حافظهٔ بلندمدت است.\n')


def cmd_reproduce(a) -> int:
    """Run the identical contract on every available model and measure whether
    the *intended result* — a schema-valid, page-grounded, deduplicated pack —
    is reproduced. This is the acceptance test for model-agnosticism."""
    from reasoning_team_enrich import validate
    provs = MA.discover_providers(a.providers, include_mock=a.mock,
                                  only=a.only.split(",") if a.only else None)
    if not provs:
        _out({"error": "no usable provider"}, True)
        return EXIT_NOPROVIDER
    provs = provs[: a.limit]
    want = {"tables": 0, "flash": 3, "mnemonics": 0, "review": 0, "quiz": 2, "bank": 0}
    rows, packs = [], []
    import concurrent.futures as cf

    def one(p):
        t0 = time.time()
        row = {"provider": p.name, "dialect": p.dialect, "model": p.model,
               "ok": False, "contract_valid": False, "counts": {}, "error": "",
               "latency_s": 0.0, "finish": ""}
        try:
            reply = MA.call_model(p, _REPRO_PROMPT, _REPRO_SYSTEM, max_tokens=2500,
                                  json_mode=True, seed=7, retries=3, use_cache=not a.no_cache)
            row["ok"], row["finish"], row["model"] = True, reply.finish, reply.model
            pack = validate(reply.json(), 1, 2, want)
            row["contract_valid"] = True
            row["counts"] = {k: len(v) for k, v in pack.items() if v}
            return row, pack
        except Exception as exc:
            row["error"] = f"{type(exc).__name__}: {exc}"[:200]
            return row, None
        finally:
            row["latency_s"] = round(time.time() - t0, 2)

    with cf.ThreadPoolExecutor(max_workers=min(6, len(provs))) as ex:
        for row, pack in ex.map(one, provs):
            rows.append(row)
            if pack:
                packs.append(pack)

    from common import consensus_pick, stable_sort_items, dedupe_items
    agreed = {}
    for key in ("flash", "quiz"):
        merged = consensus_pick([p.get(key, []) for p in packs])
        agreed[key] = stable_sort_items(dedupe_items(merged))
    valid = [r for r in rows if r["contract_valid"]]
    report = {
        "schema": "forge.reproducibility/1",
        "skill_version": VERSION,
        "models_tried": len(rows),
        "models_contract_valid": len(valid),
        "reproducibility_rate": round(len(valid) / len(rows), 3) if rows else 0.0,
        "verdict": ("REPRODUCIBLE" if len(valid) >= 2 or (len(valid) == 1 == len(rows))
                    else "INSUFFICIENT"),
        "consensus_counts": {k: len(v) for k, v in agreed.items()},
        "models": sorted(rows, key=lambda r: (not r["contract_valid"], r["latency_s"])),
        "consensus_pack": agreed if a.include_pack else "omitted (use --include-pack)",
    }
    if a.out:
        write_json(a.out, report)
    _out(report, True)
    return EXIT_OK if valid else EXIT_CONTRACT


# ── pipeline stages ────────────────────────────────────────────────────────
def _pv(a):
    return ["--providers", str(a.providers)] if getattr(a, "providers", None) else []


def cmd_extract(a) -> int:
    return _run([HERE / "extract_dual_ocr.py", a.pdf, "--out", Path(a.work) / "extraction"])


def cmd_correct(a) -> int:
    return _run([HERE / "reasoning_team_correct.py", Path(a.work) / "extraction/evidence.json",
                 "--out", Path(a.work) / "corrections"] + _pv(a))


def cmd_sessions(a) -> int:
    return _run([HERE / "detect_session_candidates.py", Path(a.work) / "corrections/final.json",
                 "--out", Path(a.work) / "session_candidates.json"])


def cmd_enrich(a) -> int:
    cmd = [HERE / "reasoning_team_enrich.py", Path(a.work) / "corrections/final.json",
           Path(a.work) / "sessions.json", "--out", Path(a.work) / "enrichment"] + _pv(a)
    if a.maximum:
        cmd.append("--maximum")
    return _run(cmd)


def cmd_verify(a) -> int:
    return _run([HERE / "verify_flashcards.py", Path(a.work) / "corrections/final.json",
                 Path(a.work) / "enrichment/all.json",
                 "--out", Path(a.work) / "enrichment/all.verified.json"] + _pv(a))


def cmd_build(a) -> int:
    enr = Path(a.work) / "enrichment/all.verified.json"
    if not enr.exists():
        enr = Path(a.work) / "enrichment/all.json"
    return _run([HERE / "build_selfcontained_html.py", Path(a.work) / "corrections/final.json",
                 Path(a.work) / "extraction", enr,
                 "--output", Path(a.work) / "studyguide.html", "--title", a.title])


def cmd_audit(a) -> int:
    return _run([HERE / "fidelity_audit.py", Path(a.work) / "extraction/evidence.json",
                 Path(a.work) / "corrections/final.json", "--out", Path(a.work) / "fidelity.json"])


def cmd_qa(a) -> int:
    return _run([HERE / "qa_gates.py", Path(a.work) / "studyguide.html"])


def cmd_package(a) -> int:
    return _run([HERE / "verify_zip.py", a.work, Path(a.work) / "final-studyguide.zip"])


def _sessions_from_candidates(cand: Path, work: Path) -> list:
    """Turn detector output into a valid sessions.json body.

    The detector emits *candidate start pages*; enrichment needs contiguous
    {name, start, end} ranges covering every page. When the detector finds no
    boundary (short documents, non-standard headers) the whole document becomes
    one session rather than failing — an honest, reviewable default.
    """
    data = json.loads(cand.read_text("utf-8"))
    raw = data.get("candidates", data.get("sessions", [])) if isinstance(data, dict) else data
    final = json.loads((work / "corrections/final.json").read_text("utf-8"))
    pages = sorted(int(k) for k in final)
    lo, hi = (pages[0], pages[-1]) if pages else (1, 1)

    if raw and isinstance(raw[0], dict) and "start" in raw[0] and "end" in raw[0]:
        return [{"name": str(s.get("name") or f"جلسهٔ {i+1}"),
                 "start": int(s["start"]), "end": int(s["end"])}
                for i, s in enumerate(raw)]

    starts = sorted({int(c["page"]) for c in raw if isinstance(c, dict) and c.get("page")})
    if not starts or starts[0] > lo:
        starts = [lo] + starts
    out = []
    for i, st in enumerate(starts):
        end = (starts[i + 1] - 1) if i + 1 < len(starts) else hi
        if end < st:
            continue
        name = next((str(c.get("suggested_name") or "").strip()
                     for c in raw if isinstance(c, dict) and c.get("page") == st), "")
        title = str(final.get(str(st), {}).get("title", "")).strip()
        out.append({"name": name or title or f"جلسهٔ {i+1}", "start": st, "end": end})
    return out or [{"name": "کل سند", "start": lo, "end": hi}]


def cmd_run(a) -> int:
    work = Path(a.work)
    work.mkdir(parents=True, exist_ok=True)
    stages = [("extract", cmd_extract), ("correct", cmd_correct), ("sessions", cmd_sessions)]
    results = {}
    for name, fn in stages:
        rc = fn(a)
        results[name] = rc
        if rc != 0:
            _out({"stage_failed": name, "exit": rc, "results": results}, True)
            return EXIT_CONTRACT
    sess = work / "sessions.json"
    if not sess.exists():
        cand = work / "session_candidates.json"
        if a.auto_sessions and cand.exists():
            items = _sessions_from_candidates(cand, work)
            write_json(sess, {"sessions": items, "reviewed": False,
                              "note": "AUTO-ACCEPTED boundaries (--auto-sessions). "
                                      "These were NOT human-reviewed; the guide "
                                      "must be marked unreviewed."})
            log_line("sessions auto-accepted (unreviewed)", count=len(items))
        else:
            _out({"status": "PAUSED_FOR_SESSION_REVIEW",
                  "review_file": str(work / "session_candidates.json"),
                  "create_file": str(sess),
                  "template": "templates/sessions.example.json",
                  "continue_with": f"python3 scripts/forge.py enrich --work {work}"
                                   f" && python3 scripts/forge.py build --work {work}"
                                   f" --title '{a.title}'",
                  "or_skip_review": "re-run with --auto-sessions (marks the guide as unreviewed)",
                  "results": results}, True)
            return EXIT_OK
    for name, fn in (("enrich", cmd_enrich), ("verify", cmd_verify), ("build", cmd_build),
                     ("audit", cmd_audit), ("qa", cmd_qa), ("package", cmd_package)):
        if name == "verify" and a.no_verify:
            continue
        rc = fn(a)
        results[name] = rc
        if rc != 0 and name not in ("verify",):
            _out({"stage_failed": name, "exit": rc, "results": results}, True)
            return EXIT_CONTRACT
    _out({"status": "COMPLETE", "results": results,
          "html": str(work / "studyguide.html"),
          "zip": str(work / "final-studyguide.zip"),
          "fidelity": str(work / "fidelity.json")}, True)
    return EXIT_OK


COMMANDS = {
    "describe": cmd_describe, "doctor": cmd_doctor, "selftest": cmd_selftest,
    "compat": cmd_compat, "reproduce": cmd_reproduce,
    "extract": cmd_extract, "correct": cmd_correct, "sessions": cmd_sessions,
    "enrich": cmd_enrich, "verify": cmd_verify, "build": cmd_build,
    "audit": cmd_audit, "qa": cmd_qa, "package": cmd_package, "run": cmd_run,
}


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        prog="forge.py", description="Persian PDF StudyGuide Forge — universal agent entrypoint",
        formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__)
    ap.add_argument("command", nargs="?", choices=sorted(COMMANDS), help="stage to run")
    ap.add_argument("--stdin", action="store_true",
                    help="read a JSON job object from stdin instead of argv")
    ap.add_argument("--json", action="store_true", default=True,
                    help="emit JSON on stdout (default; always true)")
    ap.add_argument("--pdf", help="source PDF (authorized material only)")
    ap.add_argument("--work", default="work", help="workspace directory (default: work)")
    ap.add_argument("--title", default="راهنمای مطالعه", help="study guide title")
    ap.add_argument("--providers", help="optional providers.json (else auto-discover)")
    ap.add_argument("--maximum", action="store_true", help="maximum enrichment mode")
    ap.add_argument("--auto-sessions", action="store_true",
                    help="accept detected session boundaries without human review")
    ap.add_argument("--no-verify", action="store_true", help="skip flashcard verification")
    ap.add_argument("--mock", action="store_true", help="include the offline mock provider")
    ap.add_argument("--only", help="comma-separated provider/dialect filter")
    ap.add_argument("--limit", type=int, default=8, help="max providers for compat/reproduce")
    ap.add_argument("--timeout", type=int, default=60)
    ap.add_argument("--no-cache", action="store_true")
    ap.add_argument("--include-pack", action="store_true",
                    help="include the consensus pack in the reproducibility report")
    ap.add_argument("--out", help="write the report to this path")
    ap.add_argument("--version", action="version", version=f"persian-pdf-studyguide-forge {VERSION}")
    return ap


def main(argv: list) -> int:
    ap = build_parser()
    a = ap.parse_args(argv)
    if a.stdin:
        try:
            job = json.load(sys.stdin)
        except Exception as exc:
            _out({"error": f"invalid JSON on stdin: {exc}"}, True)
            return EXIT_USAGE
        for k, v in job.items():
            setattr(a, k.replace("-", "_"), v)
        a.command = job.get("command", a.command)
    if not a.command:
        ap.print_help(sys.stderr)
        return EXIT_USAGE
    if a.mock:
        os.environ["FORGE_MOCK"] = "1"
    if a.command in ("extract", "run") and not a.pdf:
        _out({"error": "--pdf is required for this command"}, True)
        return EXIT_USAGE
    try:
        return COMMANDS[a.command](a)
    except KeyboardInterrupt:
        _out({"error": "interrupted"}, True)
        return EXIT_INTERRUPT
    except MA.ModelError as exc:
        _out({"error": str(exc), "kind": "model"}, True)
        return EXIT_NOPROVIDER
    except FileNotFoundError as exc:
        _out({"error": str(exc), "kind": "missing_input"}, True)
        return EXIT_DEPS


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
