#!/usr/bin/env python3
"""Extract two independent text signals and rendered evidence from a PDF.

Evidence A: PyMuPDF logical text when installed, otherwise pdftotext.
Evidence B: Tesseract fas+eng OCR over 160-220 DPI grayscale rendering.
Display evidence: compact JPEG per page for optional self-contained HTML.
All work is resumable and local; no network calls are made.
"""
from __future__ import annotations
import argparse, concurrent.futures as cf, json, os, shutil, subprocess, tempfile
from pathlib import Path
from common import normalize_persian, sha256


def require(binary: str):
    if not shutil.which(binary):
        raise SystemExit(f"missing required binary: {binary}")


def page_count(pdf: Path) -> int:
    out = subprocess.check_output(["pdfinfo", str(pdf)], text=True, errors="replace")
    for line in out.splitlines():
        if line.startswith("Pages:"):
            return int(line.split(":", 1)[1])
    raise RuntimeError("pdfinfo did not report page count")


def pymupdf_text(pdf: Path):
    try:
        import fitz
    except ImportError:
        return None
    doc = fitz.open(pdf)
    return [p.get_text("text", sort=True) for p in doc]


def poppler_text(pdf: Path, n: int, work: Path):
    all_txt = work / "pdftotext.txt"
    subprocess.run(["pdftotext", "-layout", str(pdf), str(all_txt)], check=True, timeout=max(60, n * 2))
    pages = all_txt.read_text("utf-8", errors="replace").split("\f")
    if pages and not pages[-1].strip(): pages.pop()
    if len(pages) != n:
        # Page-by-page fallback prevents leading/trailing form-feed drift.
        pages = []
        for i in range(1, n + 1):
            f = work / f"pdftotext-{i:04d}.txt"
            subprocess.run(["pdftotext", "-f", str(i), "-l", str(i), "-layout", str(pdf), str(f)],
                           check=True, timeout=30)
            pages.append(f.read_text("utf-8", errors="replace"))
    return pages


def render_display(pdf: Path, out: Path, dpi: int, quality: int):
    out.mkdir(parents=True, exist_ok=True)
    if list(out.glob("page-*.jpg")): return
    subprocess.run(["pdftoppm", "-jpeg", "-r", str(dpi), "-jpegopt",
                    f"quality={quality},optimize=y", str(pdf), str(out / "page")], check=True)
    # Normalize Poppler's variable zero padding.
    for i, f in enumerate(sorted(out.glob("page-*.jpg")), 1):
        target = out / f"page-{i:04d}.jpg"
        if f != target: f.rename(target)


def ocr_one(pdf: Path, i: int, out: Path, dpi: int, langs: str):
    target = out / f"page-{i:04d}.txt"
    if target.exists(): return i
    out.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=out) as td:
        stem = Path(td) / "page"
        subprocess.run(["pdftoppm", "-f", str(i), "-l", str(i), "-r", str(dpi),
                        "-gray", "-png", "-singlefile", str(pdf), str(stem)],
                       check=True, timeout=90, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(["tesseract", str(stem) + ".png", str(stem), "-l", langs, "--psm", "6"],
                       check=True, timeout=90, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        target.write_text(Path(str(stem) + ".txt").read_text("utf-8", errors="replace"), "utf-8")
    return i


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf", type=Path); ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--ocr-dpi", type=int, default=180); ap.add_argument("--display-dpi", type=int, default=82)
    ap.add_argument("--jpeg-quality", type=int, default=60); ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--langs", default="fas+eng")
    args = ap.parse_args(); args.pdf = args.pdf.resolve(); args.out.mkdir(parents=True, exist_ok=True)
    for b in ("pdfinfo", "pdftotext", "pdftoppm", "tesseract"): require(b)
    if not args.pdf.is_file(): raise SystemExit("PDF not found")
    n = page_count(args.pdf)
    logical = pymupdf_text(args.pdf) or poppler_text(args.pdf, n, args.out)
    if len(logical) != n: raise RuntimeError(f"logical extraction count {len(logical)} != PDF pages {n}")
    display = args.out / "display"; ocr = args.out / "ocr"
    render_display(args.pdf, display, args.display_dpi, args.jpeg_quality)
    with cf.ThreadPoolExecutor(max_workers=max(1, args.workers)) as ex:
        list(ex.map(lambda i: ocr_one(args.pdf, i, ocr, args.ocr_dpi, args.langs), range(1, n + 1)))
    records = []
    for i in range(1, n + 1):
        records.append({"page": i, "logical_raw": logical[i-1],
                        "ocr_raw": (ocr / f"page-{i:04d}.txt").read_text("utf-8", errors="replace"),
                        "logical_normalized": normalize_persian(logical[i-1]),
                        "ocr_normalized": normalize_persian((ocr / f"page-{i:04d}.txt").read_text("utf-8", errors="replace")),
                        "image": f"display/page-{i:04d}.jpg"})
    (args.out / "evidence.json").write_text(json.dumps(records, ensure_ascii=False, indent=2), "utf-8")
    manifest = {"pdf": str(args.pdf), "pdf_sha256": sha256(args.pdf), "pages": n,
                "logical_engine": "PyMuPDF" if pymupdf_text(args.pdf) is not None else "pdftotext",
                "ocr_engine": f"tesseract {args.langs}", "ocr_dpi": args.ocr_dpi,
                "display_dpi": args.display_dpi, "display_images": len(list(display.glob("*.jpg")))}
    (args.out / "extraction_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), "utf-8")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
if __name__ == "__main__": main()
