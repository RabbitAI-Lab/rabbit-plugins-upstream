#!/usr/bin/env python3
"""extract_dual_ocr.py v2 (v1.4.0) — recall-first dual extraction for Persian PDFs.

Evidence A: PyMuPDF logical text (fallback pdftotext).
Evidence B: Tesseract OCR — PRECISION ENGINE:
  - adaptive DPI (300 base, 400 retry for low-confidence pages)
  - preprocessing: grayscale -> autocontrast -> median denoise -> Sauvola
    adaptive binarization -> projection-profile deskew (+-6 deg)
  - PSM ENSEMBLE (auto psm 3 + block psm 6) merged at WORD level by box overlap:
    a word found by ANY pass survives (recall-first), confidence = best, votes
    counted; disagreement flags the word for review
  - Persian repairs at word level: Arabic->Persian chars (ي->ی ك->ک), Arabic->
    Persian digits in Persian context, ZWNJ preserved, conservative rejoin of
    over-split fragments (gap < 0.30 x median glyph advance)
  - text-layer triage: pages whose logical text is dense skip the ensemble
    (single verification pass) -> speed; coverage still reported
Outputs (resumable, local, no network):
  evidence.json           legacy fields (compat) + per-page coverage stats +
                          low_conf_words [{w,conf,bbox}] for token-gated repair
  recall_report.json      per-page: logical/ocr/union word counts, missing-risk
  extraction_manifest.json
Token economy: downstream LLM correction should use ONLY low_conf_words and
missing-risk pages (documented in SKILL.md) instead of whole pages.
"""
from __future__ import annotations
import argparse, concurrent.futures as cf, json, os, re, shutil, statistics, subprocess, tempfile
from pathlib import Path

from common import normalize_persian, sha256

PERSIAN_DIGITS = "۰۱۲۳۴۵۶۷۸۹"
ARABIC_DIGITS = "٠١٢٣٤٥٦٧٨٩"
AR2FA = {"ي": "ی", "ك": "ک", "ة": "ه", "ۀ": "هٔ", "أ": "ا", "إ": "ا", "ؤ": "و", "ٱ": "ا"}
ZWNJ = "\u200c"


def auto_workers(requested: int, per_instance_mb: int = 650) -> int:
    """Cap parallel tesseracts by available RAM (tessdata_best LSTM ~0.5-0.7 GB
    per instance; OOM kills lose the whole page batch)."""
    try:
        for line in open("/proc/meminfo"):
            if line.startswith("MemAvailable"):
                avail_mb = int(line.split()[1]) // 1024
                return max(1, min(requested, avail_mb // per_instance_mb))
    except Exception:
        pass
    return max(1, requested)


def require(binary: str):
    if not shutil.which(binary):
        raise SystemExit(f"missing required binary: {binary}")


# ─────────────────────────── PDF plumbing (unchanged) ───────────────────────
def page_count(pdf: Path) -> int:
    out = subprocess.check_output(["pdfinfo", str(pdf)], text=True, errors="replace")
    for line in out.splitlines():
        if line.startswith("Pages:"):
            return int(line.split(":", 1)[1])
    raise RuntimeError("pdfinfo did not report page count")


def pymupdf_text(pdf: Path):
    try:
        import pymupdf
    except ImportError:
        try:
            import fitz as pymupdf  # legacy name
        except ImportError:
            return None
    doc = pymupdf.open(pdf)
    return [p.get_text("text", sort=True) for p in doc]


def page_images_area(pdf: Path):
    """Fraction of each page covered by raster images (triage signal)."""
    try:
        import pymupdf
    except ImportError:
        try:
            import fitz as pymupdf
        except ImportError:
            return None
    out = []
    doc = pymupdf.open(pdf)
    for p in doc:
        area = p.rect.get_area()
        img = 0.0
        try:
            for b in p.get_image_info():
                r = b.get("bbox")
                if r:
                    img += max(0.0, (r[2] - r[0]) * (r[3] - r[1]))
        except Exception:
            pass
        out.append(min(1.0, img / area) if area else 0.0)
    return out


def poppler_text(pdf: Path, n: int, work: Path):
    all_txt = work / "pdftotext.txt"
    subprocess.run(["pdftotext", "-layout", str(pdf), str(all_txt)], check=True, timeout=max(60, n * 2))
    pages = all_txt.read_text("utf-8", errors="replace").split("\f")
    if pages and not pages[-1].strip():
        pages.pop()
    if len(pages) != n:
        pages = []
        for i in range(1, n + 1):
            f = work / f"pdftotext-{i:04d}.txt"
            subprocess.run(["pdftotext", "-f", str(i), "-l", str(i), "-layout", str(pdf), str(f)],
                           check=True, timeout=30)
            pages.append(f.read_text("utf-8", errors="replace"))
    return pages


def render_display(pdf: Path, out: Path, dpi: int, quality: int):
    out.mkdir(parents=True, exist_ok=True)
    if list(out.glob("page-*.jpg")):
        return
    subprocess.run(["pdftoppm", "-jpeg", "-r", str(dpi), "-jpegopt",
                    f"quality={quality},optimize=y", str(pdf), str(out / "page")], check=True)
    for i, f in enumerate(sorted(out.glob("page-*.jpg")), 1):
        target = out / f"page-{i:04d}.jpg"
        if f != target:
            f.rename(target)


# ─────────────────────────── preprocessing (pure PIL/numpy) ─────────────────
def _sauvola(img, window=25, k=0.34):
    """Chunked Sauvola (low memory: full-res cumsums in float32 + row-band math)."""
    import numpy as np
    from PIL import Image
    a = np.asarray(img.convert("L"), dtype=np.float32)
    h, w = a.shape
    r = window // 2
    ii = a.cumsum(0, dtype=np.float32).cumsum(1, dtype=np.float32)
    ii2 = (a * a).cumsum(0, dtype=np.float32).cumsum(1, dtype=np.float32)
    pad = np.zeros((1, w), np.float32)
    ii0 = np.vstack([pad, ii]); ii20 = np.vstack([pad, ii2])   # row -1 = 0
    out = np.empty((h, w), np.uint8)
    xx = np.arange(w)[None, :]
    x0 = np.clip(xx - r, 0, w - 1); x1 = np.clip(xx + r, 0, w - 1)
    col_cnt = (x1 - x0 + 1).astype(np.float32)
    for yA in range(0, h, 256):                                 # row bands
        yB = min(h, yA + 256)
        yy = np.arange(yA, yB)[:, None]
        ry0 = np.clip(yy - r, 0, h - 1); ry1 = np.clip(yy + r, 0, h - 1)
        row_cnt = (ry1 - ry0 + 1).astype(np.float32)
        cnt = row_cnt * col_cnt
        # windowed sums via integral images (row indices shifted by +1 for pad)
        s = (ii0[ry1 + 1, x1] - ii0[ry0, x1] - ii0[ry1 + 1, x0] + ii0[ry0, x0])
        s2 = (ii20[ry1 + 1, x1] - ii20[ry0, x1] - ii20[ry1 + 1, x0] + ii20[ry0, x0])
        mean = s / cnt
        var = np.maximum(s2 / cnt - mean * mean, 0.0)
        thr = mean * (1.0 + k * (np.sqrt(var) / 128.0 - 1.0))
        out[yA:yB] = (a[yA:yB] > thr) * 255
    return Image.fromarray(out)  # background 255, text 0 (dark text on white)


def _deskew(img, max_angle=10.0):
    """Skew estimated on a 1/4-scale copy (fast, low memory); one full-res rotate."""
    import numpy as np
    g = img.convert("L")
    small = g.resize((max(1, g.width // 4), max(1, g.height // 4)))
    if (np.asarray(small) < 128).sum() < 20:
        return g, 0.0
    best, best_score = 0.0, -1.0
    for ang in [x * 0.5 for x in range(-int(max_angle * 2), int(max_angle * 2) + 1)]:
        rot = small.rotate(ang, expand=False, fillcolor=255, resample=3)
        prof = (np.asarray(rot) < 128).sum(1).astype(np.float64)
        score = float((prof * prof).sum())
        if score > best_score:
            best_score, best = score, ang
    if abs(best) < 0.1:
        return g, 0.0
    return g.rotate(best, expand=False, fillcolor=255, resample=3), best


def preprocess(png: Path, out_png: Path, binarize=True, deskew=True, denoise=True):
    from PIL import Image, ImageFilter, ImageOps
    img = Image.open(png)
    img = ImageOps.autocontrast(img.convert("L"))
    if denoise:
        img = img.filter(ImageFilter.MedianFilter(3))
    angle = 0.0
    if deskew:
        img, angle = _deskew(img)
    if binarize:
        img = _sauvola(img)
    img.save(out_png)
    return angle


# ─────────────────────────── OCR ensemble ───────────────────────────────────
TSV_COLS = ["level", "page", "block", "par", "line", "word", "left", "top", "width", "height", "conf", "text"]


def tesseract_tsv(img: Path, base: Path, langs: str, psm: int, timeout: int = 300):
    env = dict(os.environ)
    env["OMP_THREAD_LIMIT"] = "1"
    env.setdefault("TESSDATA_PREFIX", "")
    cmd = ["tesseract", str(img), str(base), "-l", langs, "--psm", str(psm), "--oem", "1",
           "-c", "preserve_interword_spaces=1", "tsv"]
    r = subprocess.run(cmd, check=True, capture_output=True, text=True, timeout=timeout, env=env)
    tsv = base.with_suffix(".tsv")
    words = []
    if tsv.exists():
        for ln in tsv.read_text("utf-8", errors="replace").splitlines()[1:]:
            f = ln.split("\t")
            if len(f) < 12:
                continue
            try:
                conf = float(f[10])
            except ValueError:
                continue
            txt = f[11].strip()
            if not txt or conf < 0:            # conf -1 = non-word row
                continue
            l, t, w, h = int(f[6]), int(f[7]), int(f[8]), int(f[9])
            words.append({"t": txt, "conf": conf, "box": (l, t, w, h), "psm": psm})
    return words


def _iou(a, b):
    ax, ay, aw, ah = a; bx, by, bw, bh = b
    if min(aw * ah, bw * bh) < 4:            # 1x1 artifacts: near-identical => match
        return 1.0 if abs(ax - bx) <= 2 and abs(ay - by) <= 2 else 0.0
    x0, y0 = max(ax, bx), max(ay, by)
    x1, y1 = min(ax + aw, bx + bw), min(ay + ah, by + bh)
    inter = max(0, x1 - x0) * max(0, y1 - y0)
    return inter / (aw * ah + bw * bh - inter + 1e-9)


def merge_word_sets(passes):
    """Recall-first union: a word survives if ANY pass found it. Boxes matched by
    IoU >= 0.4 (same physical word) -> keep highest-conf text, count votes."""
    merged = []
    for words in passes:
        for w in words:
            hit = None
            for m in merged:
                if _iou(m["box"], w["box"]) >= 0.4 and _sameish(m["t"], w["t"]):
                    hit = m
                    break
            if hit is None:
                m = {"t": w["t"], "conf": w["conf"], "box": w["box"], "votes": 1,
                     "psms": {w["psm"]}, "agree": True}
                merged.append(m)
                continue
            hit["votes"] += 1
            hit["psms"].add(w["psm"])
            if w["conf"] > hit["conf"]:
                hit.update(t=w["t"], conf=w["conf"], box=w["box"])
    for m in merged:
        if m["votes"] == 1 and m["conf"] < 85:
            m["agree"] = False                      # single low-conf detection -> review
    # stray-mark filter (precision, recall-safe): 1-char single-vote very-low-conf
    merged = [m for m in merged if not (m["votes"] == 1 and m["conf"] < 20 and len(m["t"]) <= 1 and not _looks_persian(m["t"]))]
    merged.sort(key=lambda m: (m["box"][1], m["box"][0]))
    return merged


def _sameish(a: str, b: str) -> bool:
    a2, b2 = a.replace(ZWNJ, ""), b.replace(ZWNJ, "")
    if a2 == b2:
        return True
    if abs(len(a2) - len(b2)) > 2:
        return False
    same = sum(x == y for x, y in zip(a2, b2))
    return same / max(len(a2), len(b2), 1) >= 0.5


def repair_word(t: str) -> str:
    t = "".join(AR2FA.get(c, c) for c in t)
    t = "".join(PERSIAN_DIGITS[ARABIC_DIGITS.index(c)] if c in ARABIC_DIGITS else c for c in t)
    return t


def rejoin_fragments(merged, page_width):
    """Tesseract over-splits Persian words (ligature/ZWNJ boundaries). Rejoin
    fragments on the SAME line when the gap < 0.25 x median glyph height."""
    if len(merged) < 2:
        return merged
    heights = [m["box"][3] for m in merged]
    med = statistics.median(heights) or 1.0   # gap scale = glyph HEIGHT (persian chars are narrow)
    out, i = [], 0
    for m in merged:
        if out:
            p = out[-1]
            # vertical overlap (same visual line, any direction)
            vov = min(p["box"][1] + p["box"][3], m["box"][1] + m["box"][3]) - max(p["box"][1], m["box"][1])
            same_line = vov > 0.4 * min(p["box"][3], m["box"][3])
            # direction-agnostic horizontal gap (RTL-safe): distance between boxes
            gap = max(p["box"][0], m["box"][0]) - min(p["box"][0] + p["box"][2], m["box"][0] + m["box"][2])
            if same_line and 0 <= gap < 0.25 * med and _looks_persian(p["t"].rstrip(ZWNJ)[-1:]) and _looks_persian(m["t"].lstrip(ZWNJ)[:1]):
                if m["box"][0] >= p["box"][0]:     # m to the RIGHT => m PRECEDES p in RTL reading
                    p["t"] = m["t"] + p["t"]
                    x0 = p["box"][0]
                else:                               # m to the LEFT => m FOLLOWS p
                    p["t"] = p["t"] + m["t"]
                    x0 = m["box"][0]
                p["conf"] = min(p["conf"], m["conf"])
                x1 = max(p["box"][0] + p["box"][2], m["box"][0] + m["box"][2])
                p["box"] = (x0, p["box"][1], x1 - x0, max(p["box"][3], m["box"][3]))
                continue
        out.append(dict(m))
    return out


def _looks_persian(ch: str) -> bool:
    return bool(re.match(r"[\u0600-\u06FF]", ch or ""))


def _is_rtl(tokens):
    fa = sum(1 for t in tokens if _looks_persian(t[:1] if t else ""))
    return fa > len(tokens) / 2 if tokens else False


def words_to_text(merged):
    """Reading-order reconstruction: vertical-overlap line grouping, then
    within-line ordering by direction (RTL: right-to-left = descending x)."""
    if not merged:
        return ""
    items = sorted(merged, key=lambda m: (m["box"][1], m["box"][0]))
    lines, cur = [], [items[0]]
    for m in items[1:]:
        cy0, ch = cur[-1]["box"][1], cur[-1]["box"][3]
        my0, mh = m["box"][1], m["box"][3]
        overlap = min(cy0 + ch, my0 + mh) - max(cy0, my0)
        same = overlap > 0.35 * min(ch, mh) or abs((cy0 + ch / 2) - (my0 + mh / 2)) < 0.5 * max(ch, mh)
        if same:
            cur.append(m)
        else:
            lines.append(cur)
            cur = [m]
    lines.append(cur)
    out = []
    for ln in lines:
        toks = [w["t"] for w in (sorted(ln, key=lambda w: -w["box"][0]) if _is_rtl([w["t"] for w in ln])
                                 else sorted(ln, key=lambda w: w["box"][0]))]
        out.append(" ".join(toks))
    return "\n".join(out)


# ─────────────────────────── per-page driver ────────────────────────────────
def ocr_page(pdf: Path, i: int, out: Path, dpi: int, langs: str, mode: str, min_conf: float = 65.0):
    """mode: 'verify' (single psm3 pass) or 'full' (psm ensemble + retry@400).
    Returns per-page dict; caches tsvs for resume."""
    out.mkdir(parents=True, exist_ok=True)
    passes, angle = [], 0.0
    with tempfile.TemporaryDirectory(dir=out) as td:
        td = Path(td)
        stem = td / "page"
        def render(d):
            subprocess.run(["pdftoppm", "-f", str(i), "-l", str(i), "-r", str(d),
                            "-gray", "-png", "-singlefile", str(pdf), str(stem)],
                           check=True, timeout=180, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            prep = td / "prep.png"
            nonlocal angle
            angle = preprocess(stem.with_suffix(".png"), prep)
            return prep
        prep = render(dpi)
        psms = [3] if mode == "verify" else [3, 6]
        for psm in psms:
            words = tesseract_tsv(prep, td / f"p{psm}", langs, psm)
            passes.append(words)
        # scale ensemble: fas LSTM reads ~20-25px glyph lines best (trained on
        # ~96-150 dpi scans); a 0.55x pass recovers words lost at full 300 dpi
        if mode == "full":
            from PIL import Image
            small = td / "small.png"
            im = Image.open(prep)
            im.resize((max(1, int(im.width * 0.55)), max(1, int(im.height * 0.55))),
                      Image.LANCZOS).save(small)
            for psm in (3, 4):
                passes.append(tesseract_tsv(small, td / f"s{psm}", langs, psm))
        merged = merge_word_sets(passes)
        mean_conf = statistics.mean([w["conf"] for w in merged]) if merged else 0.0
        retried = False
        if mode == "full" and dpi < 400 and (mean_conf < min_conf or not merged):
            prep = render(400)
            passes2 = [tesseract_tsv(prep, td / f"hi{p}", langs, p) for p in psms]
            m2 = merge_word_sets(passes + passes2)
            if (statistics.mean([w["conf"] for w in m2]) if m2 else 0) > mean_conf + 3:
                merged, mean_conf, retried = m2, statistics.mean([w["conf"] for w in m2]), True
        merged = rejoin_fragments(merged, None)
        for m in merged:
            m["t"] = repair_word(m["t"])
        text = words_to_text(merged)
        page = {"page": i, "dpi": 400 if retried else dpi, "mode": mode,
                "deskew_deg": round(angle, 2), "n_words": len(merged),
                "mean_conf": round(mean_conf, 1),
                "low_conf_words": [{"w": m["t"], "conf": round(m["conf"], 0),
                                    "bbox": list(m["box"]), "votes": m["votes"]}
                                   for m in merged if m["conf"] < 60 or not m["agree"]][:400],
                "text": text}
    (out / f"page-{i:04d}.txt").write_text(page["text"], "utf-8")
    (out / f"page-{i:04d}.json").write_text(json.dumps(page, ensure_ascii=False), "utf-8")
    return page


# ─────────────────────────── coverage / reporting ───────────────────────────
def token_set(text: str):
    toks = normalize_persian(text).split()
    return {repair_word(t).strip(".,؛،:؛؟!()[]«»\"'") for t in toks if t.strip()}


def coverage(i, logical, ocr):
    L, O = token_set(logical or ""), token_set(ocr or "")
    union = L | O
    only_l, only_o = L - O, O - L
    missing_risk = "none"
    if L and len(only_l) / max(1, len(L)) > 0.10:
        missing_risk = "high"          # >10% of text-layer words unseen by OCR
    elif L and only_l:
        missing_risk = "low"
    return {"page": i, "logical_words": len(L), "ocr_words": len(O), "union_words": len(union),
            "words_only_in_logical": sorted(only_l)[:80], "words_only_in_ocr": len(only_o),
            "missing_risk": missing_risk}


# ─────────────────────────── main ───────────────────────────────────────────
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf", type=Path); ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--ocr-dpi", type=int, default=300); ap.add_argument("--display-dpi", type=int, default=82)
    ap.add_argument("--jpeg-quality", type=int, default=60); ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--langs", default="fas+eng")
    ap.add_argument("--ocr-mode", choices=["auto", "full", "verify", "fast"], default="auto",
                    help="auto=triage per page | full=ensemble everywhere | verify=1 pass | fast=alias verify")
    args = ap.parse_args(); args.pdf = args.pdf.resolve(); args.out.mkdir(parents=True, exist_ok=True)
    for b in ("pdfinfo", "pdftotext", "pdftoppm", "tesseract"): require(b)
    if not args.pdf.is_file(): raise SystemExit("PDF not found")
    n = page_count(args.pdf)
    logical = pymupdf_text(args.pdf) or poppler_text(args.pdf, n, args.out)
    if len(logical) != n: raise RuntimeError(f"logical extraction count {len(logical)} != PDF pages {n}")
    img_area = page_images_area(args.pdf) or [1.0] * n
    display = args.out / "display"; ocr = args.out / "ocr"
    render_display(args.pdf, display, args.display_dpi, args.jpeg_quality)

    def mode_for(i):
        if args.ocr_mode != "auto":
            return "verify" if args.ocr_mode in ("verify", "fast") else "full"
        dense_text = len(token_set(logical[i - 1])) >= 60
        return "verify" if (dense_text and img_area[i - 1] < 0.15) else "full"

    jobs = [(i, mode_for(i)) for i in range(1, n + 1)
            if not (ocr / f"page-{i:04d}.json").exists()]
    n_workers = auto_workers(args.workers)
    if n_workers != args.workers:
        print(f"[mem-guard] workers {args.workers} -> {n_workers} (RAM cap, ~650MB/tesseract)", flush=True)
    with cf.ThreadPoolExecutor(max_workers=n_workers) as ex:
        futs = {ex.submit(ocr_page, args.pdf, i, ocr, args.ocr_dpi, args.langs, m): i for i, m in jobs}
        for f in cf.as_completed(futs):
            f.result()

    records, covs = [], []
    for i in range(1, n + 1):
        pj = json.loads((ocr / f"page-{i:04d}.json").read_text("utf-8"))
        ocr_txt = pj["text"]
        cov = coverage(i, logical[i - 1], ocr_txt)
        covs.append(cov)
        records.append({"page": i, "logical_raw": logical[i-1], "ocr_raw": ocr_txt,
                        "logical_normalized": normalize_persian(logical[i-1]),
                        "ocr_normalized": normalize_persian(ocr_txt),
                        "ocr_mean_conf": pj["mean_conf"], "ocr_mode": pj["mode"], "ocr_dpi": pj["dpi"],
                        "ocr_low_conf_words": pj["low_conf_words"],
                        "missing_risk": cov["missing_risk"],
                        "image": f"display/page-{i:04d}.jpg"})
    (args.out / "evidence.json").write_text(json.dumps(records, ensure_ascii=False, indent=2), "utf-8")
    (args.out / "recall_report.json").write_text(json.dumps(covs, ensure_ascii=False, indent=2), "utf-8")
    risky = [c["page"] for c in covs if c["missing_risk"] != "none"]
    low_conf_pages = [r["page"] for r in records if r["ocr_mean_conf"] < 65]
    manifest = {"pdf": str(args.pdf), "pdf_sha256": sha256(args.pdf), "pages": n,
                "logical_engine": "PyMuPDF" if pymupdf_text(args.pdf) is not None else "pdftotext",
                "ocr_engine": f"tesseract {args.langs} ensemble[psm3+psm6] adaptive-dpi "
                              f"sauvola+deskew (v1.4.0 engine)",
                "ocr_dpi": args.ocr_dpi, "display_dpi": args.display_dpi,
                "display_images": len(list(display.glob("*.jpg"))),
                "missing_risk_pages": risky, "low_conf_pages": low_conf_pages,
                "token_hint": "repair prompts should use ocr_low_conf_words + missing_risk pages only"}
    (args.out / "extraction_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), "utf-8")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
