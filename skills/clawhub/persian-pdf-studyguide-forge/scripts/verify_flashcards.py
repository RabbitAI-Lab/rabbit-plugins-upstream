#!/usr/bin/env python3
"""Independent post-hoc verification of flashcard answers (added v1.3.0).

A different model from the generator confirms or corrects each flashcard answer
strictly against the card's source page. Cards whose answer cannot be
determined from the page are dropped rather than invented. The input enrichment
file is never modified — a new pack file is written instead, so the operator
can diff and audit before building the HTML.

Usage:
  python3 scripts/verify_flashcards.py work/corrections/final.json \\
      work/enrichment/all.json --providers providers.json \\
      --out work/enrichment/all.verified.json [--all] [--workers 4]

By default only suspicious cards are verified: answers that are bare letters
(or empty) and multiple-choice-phrased questions («کدام…»). Pass --all to
verify every flashcard.
"""
import argparse, concurrent.futures as cf, json, threading
from pathlib import Path
from common import (call_provider, extract_json, load_provider_config,
                    normalize_persian, is_bare_answer)

VERIFY_SYSTEM = "تو مصحح آموزشی فارسی هستی و فقط از متن صفحهٔ منبع استفاده می‌کنی."


def _answer_prompt(q, proposed, page, page_text):
    return (
        f"سؤال و پاسخ پیشنهادی و متن صفحهٔ منبع را داده‌ام. بررسی کن که آیا پاسخ دقیقاً از متن صفحهٔ {page} "
        f"پشتیبانی می‌شود و به سؤال مربوط است.\n"
        f"- اگر درست است، همان پاسخ را (مختصر و دقیق) بنویس.\n"
        f"- اگر اشتباه یا نامربوط است، پاسخ درست را از متن صفحه استخراج کن.\n"
        f"- اگر سؤال به گزینه‌هایی اشاره دارد که در متن نیست و پاسخ قابل تشخیص نیست، فقط بنویس: نامشخص.\n"
        f"خروجی فقط JSON:\n{{\"answer\": \"...\"}}\n\n"
        f"سؤال: {q}\nپاسخ پیشنهادی: {proposed}\n\nمتن صفحهٔ {page}:\n{page_text[:6000]}"
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("corrected", type=Path)
    ap.add_argument("enrichment", type=Path)
    ap.add_argument("--providers", type=Path, default=None,
                    help="optional providers.json; omit to auto-discover from environment")
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--all", action="store_true",
                    help="verify every flashcard, not just suspicious ones")
    ap.add_argument("--workers", type=int, default=4)
    a = ap.parse_args()

    corrected = {int(k): v for k, v in json.loads(a.corrected.read_text()).items()}
    packs = json.loads(a.enrichment.read_text())
    providers = load_provider_config(a.providers)
    if not providers:
        raise SystemExit("no configured provider has its api_key_env set")

    jobs = []
    for pi, p in enumerate(packs):
        s, e = int(p["start"]), int(p["end"])
        for fi, card in enumerate(p["content"].get("flash", [])):
            q = str(card.get("q", ""))
            ans = str(card.get("a", ""))
            suspicious = is_bare_answer(ans) or "کدام" in q
            if not (a.all or suspicious):
                continue
            ref = card.get("ref")
            try:
                page = min(e, max(s, int(ref)))
            except (TypeError, ValueError):
                page = s
            jobs.append((pi, fi, q, ans, page))

    print(json.dumps({"flashcards_to_verify": len(jobs), "providers": len(providers)},
                     ensure_ascii=False))

    counter = {"n": 0}
    lock = threading.Lock()

    def next_idx():
        with lock:
            idx = counter["n"] % len(providers)
            counter["n"] += 1
        return idx

    def one(job):
        pi, fi, q, proposed, page = job
        page_text = corrected[page]["text"]
        for k in range(len(providers)):
            p = providers[(next_idx() + k) % len(providers)]
            try:
                obj = extract_json(call_provider(p, _answer_prompt(q, proposed, page, page_text),
                                                 VERIFY_SYSTEM, 600, timeout=180))
                ans = normalize_persian(str(obj.get("answer", "")))
                if ans and not is_bare_answer(ans) and ans != "نامشخص":
                    return pi, fi, ans
            except Exception:
                continue
        return pi, fi, ""

    with cf.ThreadPoolExecutor(max_workers=a.workers) as ex:
        results = list(ex.map(one, jobs))

    kept = dropped = 0
    for pi, fi, ans in results:
        if ans:
            packs[pi]["content"]["flash"][fi]["a"] = ans
            kept += 1
        else:
            packs[pi]["content"]["flash"][fi] = None
            dropped += 1
    for p in packs:
        p["content"]["flash"] = [f for f in p["content"]["flash"] if f is not None]

    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(packs, ensure_ascii=False, indent=2), "utf8")
    print(json.dumps({"verified_kept": kept, "dropped": dropped, "output": str(a.out)},
                     ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
