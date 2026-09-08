#!/usr/bin/env python3
"""Session-grounded, reviewed generation of tables/cards/mnemonics/review/quiz/bank.
Supports conservative defaults and --maximum mode. All additions retain source refs.

v1.3.0 — robust provider-JSON coercion:
  * accepts a bare JSON array or object;
  * coerces Persian/Arabic page references and answer labels;
  * accepts well-formed subsets instead of failing on under-counts;
  * drops bare-letter flashcard answers instead of shipping them;
  * retries quiz/scenario sections with a focused pass when the combined
    --maximum schema is truncated by a smaller provider.
"""
from __future__ import annotations
import argparse, concurrent.futures as cf, json
from pathlib import Path
from common import (call_provider, extract_json, load_provider_config,
                    coerce_ref, coerce_answer, is_bare_answer, strip_option_prefix,
                    consensus_pick, dedupe_items, stable_sort_items, write_json,
                    log_line, DEFAULT_SEED)

SYSTEM = '''شما طراح آموزشی پزشکی و متخصص موضوع منبع هستید. فقط از متن جلسه استفاده کنید. محتوای فارسی دقیق، غیرتکراری، امتحان‌محور و بالینی بسازید. املا، نیم‌فاصله و نشانه‌گذاری کامل باشد. نام علمی لازم را داخل پرانتز حفظ کنید. هر سؤال چهار گزینه و دقیقاً یک پاسخ درست داشته باشد. ارجاع باید واقعاً به صفحهٔ منبع مرتبط باشد. داده یا دوز اختراع نکنید. خروجی فقط JSON معتبر باشد.'''

# Contract reminders that the old schema omitted; models otherwise return
# «صفحهٔ ۳» references, «الف» answer labels and bare-letter flashcard answers.
_CONTRACT = ('مهم: مقدار "ref" باید عدد صحیح شمارهٔ صفحه باشد (مثلاً 5)، نه متن «صفحهٔ ۵». '
             'مقدار "answer" فقط یکی از حروف A یا B یا C یا D باشد. '
             'پاسخ فلش‌کارت ("a") باید جملهٔ کامل باشد، نه یک حرف.')


def validate(d, s, e, want):
    """Coerce a provider response into the strict internal contract.

    Never raises on shape/count/style mismatches that can be recovered: invalid
    items are dropped, counts are capped to the requested maximum (subsets are
    accepted), and references/answers are normalized. Raises only when nothing
    valid remains (so the caller can fail over to the next provider).
    """
    # models sometimes return a bare array instead of {"flash": [...]}
    if isinstance(d, list):
        d = {"flash": d}
    if not isinstance(d, dict):
        raise ValueError("response is not an object or array")

    out = {"tables": [], "flash": [], "mnemonics": [], "review": [], "quiz": [], "bank": []}

    for t in d.get("tables", []) or []:
        if not isinstance(t, dict):
            continue
        h = t.get("headers") or []
        rows = t.get("rows") or []
        if not (2 <= len(h) <= 4) or len(rows) < 4:
            continue
        rows = [r for r in rows if isinstance(r, list) and len(r) == len(h)][:10]
        if len(rows) < 4:
            continue
        out["tables"].append({"caption": str(t.get("caption", "")),
                              "headers": [str(x) for x in h],
                              "rows": [[str(c) for c in r] for r in rows]})

    for x in d.get("flash", []) or []:
        if not isinstance(x, dict):
            continue
        q, a = str(x.get("q", "")).strip(), str(x.get("a", "")).strip()
        if not q or is_bare_answer(a):
            continue
        out["flash"].append({"q": q, "a": a, "ref": coerce_ref(x.get("ref"), s, e)})

    for x in d.get("mnemonics", []) or []:
        if not isinstance(x, dict):
            continue
        title, text = str(x.get("title", "")).strip(), str(x.get("text", "")).strip()
        if not title or not text:
            continue
        out["mnemonics"].append({"title": title, "text": text,
                                 "ref": coerce_ref(x.get("ref"), s, e)})

    for x in d.get("review", []) or []:
        if not isinstance(x, dict):
            continue
        text = str(x.get("text", "")).strip()
        if not text:
            continue
        out["review"].append({"text": text, "ref": coerce_ref(x.get("ref"), s, e)})

    for key in ("quiz", "bank"):
        for x in d.get(key, []) or []:
            if not isinstance(x, dict):
                continue
            opts = [strip_option_prefix(o) for o in (x.get("options") or [])]
            ans = coerce_answer(x.get("answer"))
            if len(opts) != 4 or not ans:
                continue
            out[key].append({"q": str(x.get("q", "")), "options": opts, "answer": ans,
                             "why": str(x.get("why", "")), "ref": coerce_ref(x.get("ref"), s, e)})

    if not any(out.values()):
        raise ValueError("no valid items in provider response")

    # cap to requested maximum; subsets are accepted (no under-count failure)
    for k, n in want.items():
        out[k] = out[k][:n]
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("corrected", type=Path)
    ap.add_argument("sessions", type=Path)
    ap.add_argument("--providers", type=Path, default=None,
                    help="optional providers.json; omit to auto-discover from environment")
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--maximum", action="store_true")
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--consensus", type=int, default=1, metavar="N",
                    help="ask N different models for the same session and keep "
                         "what they agree on (default 1 = single model). N>=2 "
                         "makes results reproducible across model families.")
    ap.add_argument("--min-votes", type=int, default=1,
                    help="with --consensus N, drop items fewer than this many "
                         "models produced (2 = strict cross-model agreement)")
    a = ap.parse_args()
    a.out.mkdir(parents=True, exist_ok=True)

    d = {int(k): v for k, v in json.loads(a.corrected.read_text()).items()}
    sessions = json.loads(a.sessions.read_text())["sessions"]
    providers = load_provider_config(a.providers)
    want = {"tables": 3 if a.maximum else 1, "flash": 10 if a.maximum else 4,
            "mnemonics": 4 if a.maximum else 1, "review": 10 if a.maximum else 4,
            "quiz": 5 if a.maximum else 2, "bank": 4 if a.maximum else 1}

    def one(job):
        i, sess = job
        s, e = int(sess["start"]), int(sess["end"])
        name = sess["name"]
        cache = a.out / f"session-{i+1:03d}.json"
        if cache.exists():
            return json.loads(cache.read_text())
        source = "\n\n".join(f"صفحه {p} — {d[p]['title']}\n{d[p]['text']}" for p in range(s, e + 1))

        def ask(prompt, tokens, skip=0):
            """Ask the provider chain, starting at an offset so that a
            --consensus run hits a DIFFERENT model family each time."""
            last = None
            for off in range(len(providers)):
                p = providers[(i + skip + off) % len(providers)]
                try:
                    return validate(extract_json(call_provider(p, prompt, SYSTEM, tokens)), s, e, want), p["name"]
                except Exception as exc:
                    last = exc
            return None, (type(last).__name__ if last else "unknown")

        def ask_consensus(prompt, tokens):
            """N-way self-consistency across model families.

            The identical prompt goes to N distinct providers; items that more
            than one model produced are ranked first (semantic matching, not
            string equality), so the pack reflects what the models AGREE the
            source says rather than one model's idiosyncrasies.
            """
            n = max(1, min(a.consensus, len(providers)))
            if n == 1:
                return ask(prompt, tokens)
            packs, names = [], []
            for k in range(n):
                pack, name = ask(prompt, tokens, skip=k)
                if pack:
                    packs.append(pack)
                    names.append(name)
            if not packs:
                return None, "all providers failed"
            merged = {}
            for key in want:
                merged[key] = stable_sort_items(dedupe_items(consensus_pick(
                    [p.get(key, []) for p in packs],
                    min_votes=a.min_votes if len(packs) >= a.min_votes else 1)))[: want[key]]
            log_line("consensus merged", session=i + 1, models=len(packs),
                     kept={k: len(v) for k, v in merged.items() if v})
            return merged, "+".join(names) + f" (consensus×{len(packs)})"

        schema = (
            f"جلسه: {name}، صفحات {s} تا {e}. دقیقاً JSON زیر را بساز:\n"
            f'{{"tables":[{want["tables"]} جدول caption,headers,rows با ۴ تا ۱۰ ردیف],'
            f'"flash":[{want["flash"]} شیء q,a,ref],'
            f'"mnemonics":[{want["mnemonics"]} شیء title,text,ref],'
            f'"review":[{want["review"]} شیء text,ref],'
            f'"quiz":[{want["quiz"]} شیء q,options چهارگانه,answer,why,ref],'
            f'"bank":[{want["bank"]} سناریوی q,options چهارگانه,answer,why,ref]}}.\n'
            f"همهٔ موارد متمایز باشند. {_CONTRACT}\n\n{source}"
        )
        content, primary_name = ask_consensus(schema, 16000)
        if content is None:
            raise RuntimeError(f"session {i+1}: all providers failed")

        # Focused fallback for sections the combined schema omitted (small
        # providers truncate the large --maximum response, leaving quiz/bank
        # empty). Ask for those sections on their own.
        for section, label, tokens in (("quiz", "سؤال چهارگزینه‌ای", 8000),
                                       ("bank", "سناریوی بالینی", 8000)):
            if want[section] and not content[section]:
                foc = (
                    f"جلسه: {name}، صفحات {s} تا {e}. فقط «{label}» را بساز. دقیقاً JSON:\n"
                    f'{{"{section}":[{want[section]} مورد q,options(آرایهٔ ۴ گزینه),answer,why,ref]}}.\n'
                    f"همهٔ موارد متمایز باشند. {_CONTRACT}\n\n{source}"
                )
                extra, _ = ask(foc, tokens)
                if extra and extra[section]:
                    content[section] = extra[section]

        review = ("ساختار و تعداد را حفظ کن و خطای علمی، زبان، پاسخ، گزینه، تکرار و ارجاع را با متن منبع اصلاح کن. "
                  + _CONTRACT + " فقط JSON:\n" + json.dumps(content, ensure_ascii=False) + "\n\n" + source)
        reviewer = providers[(i + 1) % len(providers)]
        model = primary_name
        try:
            content = validate(extract_json(call_provider(reviewer, review, SYSTEM, 18000)), s, e, want)
            model = reviewer["name"]
        except Exception:
            model = f"{primary_name} (primary retained)"

        obj = {"session": i + 1, "name": name, "start": s, "end": e, "model": model, "content": content}
        cache.write_text(json.dumps(obj, ensure_ascii=False, indent=2), "utf8")
        return obj

    with cf.ThreadPoolExecutor(max_workers=a.workers) as ex:
        result = list(ex.map(one, enumerate(sessions)))

    write_json(a.out / "all.json", result)
    totals = {k: sum(len(x["content"][k]) for x in result) for k in want}
    print(json.dumps({"sessions": len(result), "totals": totals}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
