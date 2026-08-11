"""
Light-mode SEC guidance extractor: self-contained, no ES / Ollama / RAG infra.

Fetches the most recent 10-K or 10-Q for a ticker directly from EDGAR, chunks
the filing in memory, ranks passages with BM25, and asks Claude (or OpenAI) to
answer with inline citations.

Trades ~20% answer quality vs the heavy pipeline for zero-infra setup — good
enough for a single-ticker one-off lookup. For 100+ tickers/day, use the heavy
pipeline (mode=heavy, requires SEC_PIPELINE_DIR).
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path
from urllib.parse import urljoin

try:
    import requests
except ImportError:
    print("ERROR: `requests` is required. Install: pip install -r requirements.txt")
    sys.exit(1)

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("ERROR: `beautifulsoup4` is required. Install: pip install -r requirements.txt")
    sys.exit(1)

try:
    from rank_bm25 import BM25Okapi
except ImportError:
    print("ERROR: `rank_bm25` is required. Install: pip install -r requirements.txt")
    sys.exit(1)

UA = os.environ.get(
    "SEC_GUIDANCE_UA",
    "sec-guidance-skill contact@example.com",
)
HEADERS = {"User-Agent": UA}
CACHE_DIR = Path.home() / ".cache" / "sec-guidance"
CHUNK_CHARS = 1500
CHUNK_OVERLAP = 200
DEFAULT_TOP_K = 8

GUIDANCE_QUERIES = [
    "What is management's guidance and outlook for future revenue and earnings?",
    "What forward-looking statements did management make about future performance expectations?",
    "What did management say about expected gross margins and profitability going forward?",
    "What new product launches, services, or business expansions did management project or plan?",
    "What macroeconomic conditions, risks, or uncertainties did management highlight for upcoming quarters?",
]


def _cache_path(key: str) -> Path:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    safe = re.sub(r"[^a-zA-Z0-9._-]", "_", key)
    return CACHE_DIR / safe


def _lookup_cik(ticker: str) -> str | None:
    """Resolve ticker → 10-digit CIK from SEC's bulk file, cached."""
    cache = _cache_path("company_tickers.json")
    if not cache.exists() or (time.time() - cache.stat().st_mtime) > 86400:
        r = requests.get("https://www.sec.gov/files/company_tickers.json",
                         headers=HEADERS, timeout=30)
        r.raise_for_status()
        cache.write_bytes(r.content)
    data = json.loads(cache.read_text())
    for rec in data.values():
        if rec.get("ticker", "").upper() == ticker.upper():
            return f"{int(rec['cik_str']):010d}"
    return None


def _latest_filing(cik: str, form: str) -> dict | None:
    """Return {accession, filing_date, primary_doc_url} for the most recent form."""
    r = requests.get(f"https://data.sec.gov/submissions/CIK{cik}.json",
                     headers=HEADERS, timeout=30)
    r.raise_for_status()
    recent = r.json().get("filings", {}).get("recent", {})
    forms = recent.get("form", [])
    dates = recent.get("filingDate", [])
    accs = recent.get("accessionNumber", [])
    docs = recent.get("primaryDocument", [])
    form_norm = form.replace("-", "").upper()
    for f, d, acc, doc in zip(forms, dates, accs, docs):
        if f.replace("-", "").upper() == form_norm:
            acc_nodash = acc.replace("-", "")
            url = (f"https://www.sec.gov/Archives/edgar/data/"
                   f"{int(cik)}/{acc_nodash}/{doc}")
            return {"accession": acc, "filing_date": d, "primary_doc_url": url}
    return None


def _fetch_and_extract_text(url: str, filing_key: str) -> str:
    """Fetch primary doc, strip HTML/XBRL, return plain text. Cached per filing."""
    cache = _cache_path(f"filing__{filing_key}.txt")
    if cache.exists():
        return cache.read_text()
    r = requests.get(url, headers=HEADERS, timeout=60)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    for tag in soup(["script", "style", "meta", "link"]):
        tag.decompose()
    # Inject paragraph breaks before block-level tags so text isn't a wall
    for block in soup.find_all(["p", "div", "tr", "li", "h1", "h2", "h3", "h4", "h5", "h6"]):
        block.insert_before("\n\n")
    text = soup.get_text(" ")
    # Collapse whitespace but keep paragraph breaks
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    # Strip XBRL namespace noise lines
    lines = [ln for ln in text.split("\n")
             if not re.match(r"^(xmlns|xbrli:|iso4217:|us-gaap:)", ln.strip())]
    text = "\n".join(lines)
    cache.write_text(text)
    return text


def _chunk(text: str, size: int = CHUNK_CHARS, overlap: int = CHUNK_OVERLAP) -> list[str]:
    chunks = []
    i = 0
    n = len(text)
    while i < n:
        chunks.append(text[i:i + size])
        if i + size >= n:
            break
        i += size - overlap
    return chunks


def _bm25_topk(query: str, chunks: list[str], k: int) -> list[tuple[int, float, str]]:
    tokenized = [re.findall(r"\w+", c.lower()) for c in chunks]
    bm25 = BM25Okapi(tokenized)
    q_tok = re.findall(r"\w+", query.lower())
    scores = bm25.get_scores(q_tok)
    ranked = sorted(enumerate(scores), key=lambda x: -x[1])[:k]
    return [(idx, float(score), chunks[idx]) for idx, score in ranked]


def _pick_llm() -> tuple[str, str]:
    """Return (provider, model). Prefer Anthropic, fall back to OpenAI."""
    if os.environ.get("ANTHROPIC_API_KEY"):
        return "anthropic", os.environ.get("SEC_GUIDANCE_MODEL", "claude-sonnet-4-6")
    if os.environ.get("OPENAI_API_KEY"):
        return "openai", os.environ.get("SEC_GUIDANCE_MODEL", "gpt-4o-mini")
    print("ERROR: No LLM API key found. Set ANTHROPIC_API_KEY or OPENAI_API_KEY.")
    sys.exit(1)


def _ask_llm(query: str, passages: list[tuple[int, float, str]],
             provider: str, model: str) -> str:
    """Send prompt + numbered passages to the LLM, return answer text."""
    context = "\n\n".join(
        f"[{i + 1}] (chunk #{idx}, bm25={score:.2f})\n{text}"
        for i, (idx, score, text) in enumerate(passages)
    )
    system = ("You are a financial analyst extracting forward-looking guidance "
              "from SEC filings. Answer the question using ONLY the numbered "
              "passages below. Cite passages inline as [1], [2], etc. If the "
              "passages don't contain the answer, say so — do not speculate.")
    user = f"QUESTION: {query}\n\nPASSAGES:\n{context}"
    if provider == "anthropic":
        try:
            import anthropic
        except ImportError:
            print("ERROR: `anthropic` SDK required. pip install anthropic")
            sys.exit(1)
        client = anthropic.Anthropic()
        resp = client.messages.create(
            model=model, max_tokens=1024, system=system,
            messages=[{"role": "user", "content": user}],
        )
        return resp.content[0].text
    if provider == "openai":
        try:
            import openai
        except ImportError:
            print("ERROR: `openai` SDK required. pip install openai")
            sys.exit(1)
        client = openai.OpenAI()
        resp = client.chat.completions.create(
            model=model, max_tokens=1024,
            messages=[{"role": "system", "content": system},
                      {"role": "user", "content": user}],
        )
        return resp.choices[0].message.content
    raise RuntimeError(f"Unknown provider: {provider}")


def run_light(ticker: str, form: str, top_k: int, custom_query: str | None) -> None:
    print(f"\n{'='*64}")
    print(f"  SEC GUIDANCE (light mode) | {ticker.upper()} {form.upper()}")
    print(f"{'='*64}\n")

    cik = _lookup_cik(ticker)
    if not cik:
        print(f"ERROR: no CIK found for ticker {ticker}")
        sys.exit(1)

    filing = _latest_filing(cik, form)
    if not filing:
        print(f"ERROR: no {form} filing found for {ticker} (CIK {cik})")
        sys.exit(1)

    print(f"Filing: {form} {filing['filing_date']}  accession={filing['accession']}")
    print(f"URL: {filing['primary_doc_url']}\n")

    filing_key = f"{ticker.upper()}_{form.replace('-','')}_{filing['accession']}"
    text = _fetch_and_extract_text(filing['primary_doc_url'], filing_key)
    chunks = _chunk(text)
    print(f"Extracted {len(text):,} chars → {len(chunks)} chunks\n")

    provider, model = _pick_llm()
    print(f"LLM: {provider}/{model}\n")

    queries = [custom_query] if custom_query else GUIDANCE_QUERIES
    for i, query in enumerate(queries, 1):
        print(f"[{i}/{len(queries)}] {query}")
        print("─" * 64)
        try:
            passages = _bm25_topk(query, chunks, top_k)
            if not passages:
                print("  No candidate passages.\n")
                continue
            answer = _ask_llm(query, passages, provider, model)
            print(answer)
            print("\nSources (chunk index / BM25 score):")
            for j, (idx, score, _) in enumerate(passages, 1):
                print(f"  [{j}] chunk #{idx}  score={score:.2f}")
            print()
        except Exception as e:
            print(f"  ERROR: {e}\n")

    print(f"{'='*64}\nDone.")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Light-mode SEC guidance extractor")
    p.add_argument("--ticker", default="AAPL")
    p.add_argument("--form", default="10-Q", choices=["10-Q", "10-K"])
    p.add_argument("--top-k", type=int, default=DEFAULT_TOP_K)
    p.add_argument("--query", help="Single custom question (skips the 5 default queries)")
    args = p.parse_args()
    run_light(args.ticker, args.form, args.top_k, args.query)
