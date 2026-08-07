#!/usr/bin/env python3
# pdf2md.py — PDF → Markdown，确定性提取优先，OCR 兜底，输出质量指标 JSON
#
# 用法：
#   pdf2md.py 输入.pdf [-o 输出.md] [--engine auto|pdftotext|markitdown|ocr]
#             [--dpi 300] [--lang chi_sim+eng] [--first N] [--last M]
#
# 引擎策略（auto，默认）：
#   有文字层 → pdftotext -layout（保表格列对齐）→ 质量不达标换 markitdown → 再不行 OCR
#   无文字层（扫描件）→ 直接 tesseract OCR
# stdout 输出一行 JSON 摘要（engine/pages/chars/cjk_ratio/warnings…），日志走 stderr。

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path

CJK_RE = re.compile(r"[　-〿一-鿿＀-￯]")
CID_RE = re.compile(r"\(cid:\d+\)")
LANG_TOKEN_RE = re.compile(r"^[A-Za-z0-9_/-]+$")

# 质量红线：低于该密度视为提取失败（很可能是扫描件或乱码）
MIN_CHARS_PER_PAGE = 40
MAX_GARBAGE_RATIO = 0.03
MIN_DPI = 72
MAX_DPI = 600


def log(msg):
    print(msg, file=sys.stderr, flush=True)


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def need(tool, hint):
    if not shutil.which(tool):
        raise RuntimeError(f"缺少依赖 {tool}，安装：{hint}")


def pdf_info(pdf):
    need("pdfinfo", "brew install poppler")
    r = run(["pdfinfo", str(pdf)])
    if r.returncode != 0:
        raise RuntimeError(f"pdfinfo 失败：{r.stderr.strip()[:200]}")
    pages = 0
    encrypted = False
    m = re.search(r"^Pages:\s+(\d+)", r.stdout, re.M)
    if m:
        pages = int(m.group(1))
    if re.search(r"^Encrypted:\s+yes", r.stdout, re.M):
        encrypted = True
    return pages, encrypted


def font_count(pdf):
    need("pdffonts", "brew install poppler")
    r = run(["pdffonts", str(pdf)])
    if r.returncode != 0:
        raise RuntimeError(f"pdffonts 失败：{r.stderr.strip()[:200]}")
    lines = [l for l in r.stdout.splitlines()[2:] if l.strip()]
    return len(lines)


def metrics(text, pages):
    stripped = re.sub(r"\s", "", text)
    chars = len(stripped)
    cjk = len(CJK_RE.findall(stripped))
    cid = len(CID_RE.findall(text))
    fffd = text.count("�")
    return {
        "chars": chars,
        "cjk_ratio": round(cjk / max(chars, 1), 3),
        "cid_count": cid,
        "replacement_chars": fffd,
        "garbage_ratio": round((cid * 8 + fffd) / max(chars, 1), 4),
        "chars_per_page": round(chars / max(pages, 1), 1),
    }


def quality_ok(m):
    return m["chars_per_page"] >= MIN_CHARS_PER_PAGE and m["garbage_ratio"] <= MAX_GARBAGE_RATIO


def extract_pdftotext(pdf, first, last):
    need("pdftotext", "brew install poppler")
    cmd = ["pdftotext", "-layout"]
    if first:
        cmd += ["-f", str(first)]
    if last:
        cmd += ["-l", str(last)]
    cmd += [str(pdf), "-"]
    r = run(cmd)
    if r.returncode != 0:
        raise RuntimeError(f"pdftotext 失败：{r.stderr.strip()[:200]}")
    raw_pages = r.stdout.split("\f")
    if raw_pages and not raw_pages[-1].strip():
        raw_pages.pop()
    start = first or 1
    parts, sparse = [], []
    for i, p in enumerate(raw_pages):
        pgno = start + i
        body = p.strip()
        if len(re.sub(r"\s", "", body)) < 20:
            sparse.append(pgno)
        if body:
            parts.append(f"<!-- 第 {pgno} 页 -->\n\n{body}")
    return "\n\n".join(parts), sparse


def extract_markitdown(pdf, first, last):
    if first or last:
        raise RuntimeError("markitdown 不支持页码范围，请用 pdftotext 或 ocr 引擎")
    need("markitdown", "uv tool install 'markitdown[pdf]'")
    r = run(["markitdown", str(pdf)])
    if r.returncode != 0:
        raise RuntimeError(f"markitdown 失败：{r.stderr.strip()[:200]}")
    return r.stdout, None


def validate_page_options(first, last):
    if first is not None and first < 1:
        raise RuntimeError("--first 必须是正整数")
    if last is not None and last < 1:
        raise RuntimeError("--last 必须是正整数")
    if first is not None and last is not None and last < first:
        raise RuntimeError("--last 不能小于 --first")


def validate_dpi(dpi):
    if dpi < MIN_DPI or dpi > MAX_DPI:
        raise RuntimeError(f"--dpi 必须在 {MIN_DPI}-{MAX_DPI} 之间")


def installed_tesseract_langs():
    r = run(["tesseract", "--list-langs"])
    if r.returncode != 0:
        raise RuntimeError(f"tesseract --list-langs 失败：{r.stderr.strip()[:200]}")
    lines = [line.strip() for line in r.stdout.splitlines() if line.strip()]
    return {line for line in lines if not line.startswith("List of available languages")}


def validate_lang(lang):
    parts = [part for part in lang.split("+") if part]
    if not parts or "+".join(parts) != lang:
        raise RuntimeError("--lang 必须是 tesseract 语言代码，多个代码用 + 连接")
    bad_tokens = [part for part in parts if not LANG_TOKEN_RE.fullmatch(part)]
    if bad_tokens:
        raise RuntimeError(f"--lang 包含非法语言代码：{bad_tokens}")
    installed = installed_tesseract_langs()
    missing = [part for part in parts if part not in installed]
    if missing:
        raise RuntimeError(f"tesseract 缺少语言包 {missing}，安装：brew install tesseract-lang")


def extract_ocr(pdf, first, last, dpi, lang):
    need("tesseract", "brew install tesseract tesseract-lang")
    need("pdftoppm", "brew install poppler")
    validate_dpi(dpi)
    validate_lang(lang)
    with tempfile.TemporaryDirectory() as td:
        cmd = ["pdftoppm", "-r", str(dpi), "-gray", "-png"]
        if first:
            cmd += ["-f", str(first)]
        if last:
            cmd += ["-l", str(last)]
        cmd += [str(pdf), f"{td}/pg"]
        r = run(cmd)
        if r.returncode != 0:
            raise RuntimeError(f"pdftoppm 失败：{r.stderr.strip()[:200]}")
        imgs = sorted(
            Path(td).glob("pg-*.png"),
            key=lambda p: int(re.search(r"-(\d+)\.png$", p.name).group(1)),
        )
        if not imgs:
            raise RuntimeError("pdftoppm 未产出任何页面图片")
        parts = []
        for n, img in enumerate(imgs, 1):
            pgno = int(re.search(r"-(\d+)\.png$", img.name).group(1))
            rr = run(["tesseract", str(img), "stdout", "-l", lang])
            if rr.returncode != 0:
                raise RuntimeError(f"tesseract 第 {pgno} 页失败：{rr.stderr.strip()[:200]}")
            parts.append(f"<!-- 第 {pgno} 页（OCR） -->\n\n{rr.stdout.strip()}")
            if n % 10 == 0 or n == len(imgs):
                log(f"OCR 进度：{n}/{len(imgs)}")
        return "\n\n".join(parts), None


def main():
    ap = argparse.ArgumentParser(description="PDF → Markdown，确定性提取优先，OCR 兜底")
    ap.add_argument("input", help="输入 PDF 路径")
    ap.add_argument("-o", "--output", help="输出 .md 路径（默认与输入同名同目录）")
    ap.add_argument("--engine", choices=["auto", "pdftotext", "markitdown", "ocr"], default="auto")
    ap.add_argument("--dpi", type=int, default=300, help="OCR 渲染分辨率（默认 300）")
    ap.add_argument("--lang", default="chi_sim+eng", help="tesseract 语言（默认 chi_sim+eng）")
    ap.add_argument("--first", type=int, help="起始页")
    ap.add_argument("--last", type=int, help="结束页")
    args = ap.parse_args()

    pdf = Path(args.input).expanduser().resolve()
    if not pdf.is_file():
        sys.exit(f"文件不存在：{pdf}")
    try:
        validate_page_options(args.first, args.last)
        validate_dpi(args.dpi)
    except RuntimeError as e:
        sys.exit(str(e))
    with pdf.open("rb") as f:
        header = f.read(1024)
    if b"%PDF" not in header:
        print(json.dumps({"error": "not_a_pdf", "hint": "文件头无 %PDF，可能是伪 PDF（纯文本或 zip 打包），先用 file 命令鉴别"}, ensure_ascii=False))
        sys.exit(2)

    total_pages, encrypted = pdf_info(pdf)
    fonts = font_count(pdf)
    eff_pages = (args.last - (args.first or 1) + 1) if args.last else (total_pages or 1)

    warnings = []
    if encrypted:
        warnings.append("PDF 已加密，提取可能失败或不全（可先 qpdf --decrypt 处理）")

    if args.engine == "auto":
        if fonts == 0:
            order = ["ocr"]
            warnings.append("无内嵌字体，判定为扫描件，直接 OCR")
        else:
            order = ["pdftotext", "markitdown", "ocr"]
    else:
        order = [args.engine]

    extractors = {
        "pdftotext": lambda: extract_pdftotext(pdf, args.first, args.last),
        "markitdown": lambda: extract_markitdown(pdf, args.first, args.last),
        "ocr": lambda: extract_ocr(pdf, args.first, args.last, args.dpi, args.lang),
    }

    attempts = {}
    engine_used = text = sparse = None
    for eng in order:
        log(f"尝试引擎：{eng}")
        try:
            t, sp = extractors[eng]()
        except RuntimeError as e:
            warnings.append(f"{eng}：{e}")
            continue
        m = metrics(t, eff_pages)
        attempts[eng] = (t, sp, m)
        if len(order) == 1 or quality_ok(m):
            engine_used, text, sparse = eng, t, sp
            break
        warnings.append(
            f"{eng} 质量不达标（chars/page={m['chars_per_page']}，garbage_ratio={m['garbage_ratio']}），换下一引擎"
        )

    if engine_used is None:
        if not attempts:
            print(json.dumps({"error": "all_engines_failed", "warnings": warnings}, ensure_ascii=False))
            sys.exit(3)
        engine_used = max(attempts, key=lambda k: attempts[k][2]["chars"])
        text, sparse, _ = attempts[engine_used]
        warnings.append(f"所有引擎质量均不达标，选用相对最优的 {engine_used}；关键内容建议视觉抽查")

    m = metrics(text, eff_pages)
    is_ocr = engine_used == "ocr"
    if is_ocr:
        warnings.append("OCR 产物：引用其中的关键数字（金额、比例）前，必须回原 PDF 视觉复核")
    if sparse:
        warnings.append(
            f"{len(sparse)} 页几乎无文字（如第 {sparse[:8]} 页），可能是扫描页，需对这些页单独 --engine ocr 或视觉读取"
        )

    out = Path(args.output).expanduser().resolve() if args.output else pdf.with_suffix(".md")
    out.parent.mkdir(parents=True, exist_ok=True)
    frontmatter = (
        "---\n"
        f"source: {pdf}\n"
        f"engine: {engine_used}\n"
        f"pages: {total_pages}\n"
        f"ocr: {str(is_ocr).lower()}\n"
        f"converted_at: {datetime.now().isoformat(timespec='seconds')}\n"
        "---\n\n"
    )
    out.write_text(frontmatter + text, encoding="utf-8")

    print(json.dumps({
        "output": str(out),
        "engine": engine_used,
        "pages": total_pages,
        "ocr": is_ocr,
        **m,
        "sparse_pages": (sparse or [])[:20],
        "warnings": warnings,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
