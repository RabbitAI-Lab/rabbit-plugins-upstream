#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
extract.py —— 保险计划书分析大师·文件提取器

从上传的计划书/条款/利益演示文件中抽取结构化表格与文本，供分析引擎使用。

支持格式（本 WorkBuddy 环境自带带库 Python 解释器，已验证可用）：
  - Excel  : .xlsx / .xls   -> openpyxl
  - Word   : .docx          -> python-docx
  - PDF    : .pdf           -> pdfplumber

输出：默认 JSON（含 sheets/tables/pages 与文本内容），加 --md 输出 Markdown。

自动定位与自装：若当前 python 缺解析库，会先尝试 PYTHONPATH / 同级或上层
pylibs / 标准 venv 的 site-packages，再尝试用 pip 自装 openpyxl/python-docx/
pdfplumber，最后尝试重执行 WorkBuddy 自带带库 venv python（与 markitdown 同目录
的 python.exe）；仍失败则提示改用对话追问/粘贴参数或手动 pip install。

用法：
  python extract.py 计划书.xlsx
  python extract.py 计划书.pdf --md
  python extract.py 条款.docx > out.json
"""
import sys, os, json, argparse

# ---------- 自动定位带库解释器（缺库时重执行） ----------
def _find_lib_python():
    import shutil
    md = shutil.which("markitdown")
    if md:
        cand = os.path.join(os.path.dirname(os.path.abspath(md)), "python.exe")
        if os.path.exists(cand):
            return cand
    home = os.path.expanduser("~")
    cand = os.path.join(home, ".workbuddy", "binaries", "python",
                        "envs", "default", "Scripts", "python.exe")
    if os.path.exists(cand):
        return cand
    return None

def _extend_syspath_for_libs():
    """导入失败时的回退：把常见带库目录加入 sys.path 再试一次。"""
    cands = []
    pp = os.environ.get("PYTHONPATH", "")
    cands += [p for p in pp.split(os.pathsep) if p]
    here = os.path.dirname(os.path.abspath(__file__))
    cands.append(os.path.join(here, "pylibs"))
    cands.append(os.path.join(here, "..", "..", "pylibs"))
    home = os.path.expanduser("~")
    cands.append(os.path.join(home, ".workbuddypro", "binaries", "python",
                              "envs", "default", "Lib", "site-packages"))
    for c in cands:
        if os.path.isdir(c):
            sys.path.insert(0, c)

# 注意：库导入在各函数内惰性进行；本模块被 import 时不触发重执行。
# 仅在作为 CLI 运行（main）时做库定位/重执行，见 _ensure_libs()。

def _try_pip_install_libs():
    """缺库时尝试用当前解释器的 pip 自装依赖。

    在用户本机（非沙箱）通常可用；沙箱可能拦截写入而静默失败，此时交由后续回退处理。
    """
    try:
        import subprocess
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "--quiet",
             "openpyxl", "python-docx", "pdfplumber"],
            check=False, timeout=180,
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        try:
            import importlib
            importlib.invalidate_caches()
        except Exception:
            pass
        return True
    except Exception:
        return False


def _ensure_libs():
    """CLI 运行时确保解析库可用：扩展 sys.path -> 自装依赖 -> 重执行带库 venv。

    自愈顺序保证在用户本机（venv 为空或缺少库时）也能自动补全依赖后正常运行。
    """
    try:
        import openpyxl, docx, pdfplumber  # noqa: F401
        return
    except ImportError:
        pass
    # 1) 扩展 sys.path 回退（PYTHONPATH / 同级或上层 pylibs / 标准 venv site-packages）
    _extend_syspath_for_libs()
    try:
        import openpyxl, docx, pdfplumber  # noqa: F401
        return
    except ImportError:
        pass
    # 2) 自装依赖（用户本机可行）
    if _try_pip_install_libs():
        try:
            import openpyxl, docx, pdfplumber  # noqa: F401
            return
        except ImportError:
            pass
    # 3) 重执行带库 venv python（与 markitdown 同目录的 python.exe）
    py = _find_lib_python()
    if py and os.path.abspath(py) != os.path.abspath(sys.executable):
        os.execv(py, [py, os.path.abspath(__file__)] + sys.argv[1:])
    sys.stderr.write(
        "缺少解析库 openpyxl/python-docx/pdfplumber，且自动安装与带库解释器均不可用。\n"
        "请先运行：pip install openpyxl python-docx pdfplumber\n"
        "或改用对话追问/粘贴参数方式提供数据。\n")
    sys.exit(3)


# ---------- 各格式提取 ----------
def extract_xlsx(path):
    import openpyxl
    wb = openpyxl.load_workbook(path, data_only=True)
    sheets = {}
    for ws in wb.worksheets:
        rows = []
        for r in ws.iter_rows(values_only=True):
            rows.append([("" if v is None else v) for v in r])
        sheets[ws.title] = rows
    return {"sheets": sheets}


def extract_docx(path):
    import docx
    d = docx.Document(path)
    paras = [p.text for p in d.paragraphs if p.text.strip()]
    tables = []
    for t in d.tables:
        tables.append([[c.text for c in row.cells] for row in t.rows])
    return {"paragraphs": paras, "tables": tables}


def extract_pdf(path):
    import pdfplumber
    pages = []
    with pdfplumber.open(path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text() or ""
            tbls = []
            for tb in page.extract_tables():
                tbls.append([[("" if c is None else str(c)) for c in row]
                             for row in tb])
            pages.append({"page": i + 1, "text": text, "tables": tbls})
    return {"pages": pages}


# ---------- Markdown 渲染（便于人读/核对） ----------
def to_md(kind, data):
    lines = []
    if kind == "xlsx":
        for name, rows in data["sheets"].items():
            lines.append(f"## 工作表：{name}（{len(rows)} 行）\n")
            for row in rows:
                cells = [str(c).replace("\n", " ") for c in row]
                lines.append("| " + " | ".join(cells) + " |")
            lines.append("")
    elif kind == "docx":
        if data["paragraphs"]:
            lines.append("## 正文段落\n")
            lines += [p for p in data["paragraphs"]]
            lines.append("")
        for i, t in enumerate(data["tables"]):
            lines.append(f"## 表格 {i + 1}（{len(t)} 行）\n")
            for row in t:
                lines.append("| " + " | ".join(str(c).replace("\n", " ") for c in row) + " |")
            lines.append("")
    elif kind == "pdf":
        for p in data["pages"]:
            lines.append(f"## 第 {p['page']} 页\n")
            if p["text"].strip():
                lines.append(p["text"])
                lines.append("")
            for i, t in enumerate(p["tables"]):
                lines.append(f"### 表格 {i + 1}\n")
                for row in t:
                    lines.append("| " + " | ".join(str(c).replace("\n", " ") for c in row) + " |")
                lines.append("")
    return "\n".join(lines)


def main():
    _ensure_libs()
    ap = argparse.ArgumentParser(description="保险计划书文件提取器")
    ap.add_argument("file", help="xlsx / docx / pdf 路径")
    ap.add_argument("--md", action="store_true", help="输出 Markdown 而非 JSON")
    args = ap.parse_args()

    ext = os.path.splitext(args.file)[1].lower()
    if ext in (".xlsx", ".xls"):
        data = extract_xlsx(args.file); kind = "xlsx"
    elif ext == ".docx":
        data = extract_docx(args.file); kind = "docx"
    elif ext == ".pdf":
        data = extract_pdf(args.file); kind = "pdf"
    else:
        sys.stderr.write(f"不支持的格式: {ext}\n")
        sys.exit(2)

    if args.md:
        print(to_md(kind, data))
    else:
        print(json.dumps({"kind": kind, "source": args.file, "data": data},
                         ensure_ascii=False))


if __name__ == "__main__":
    try:
        from _feedback_hook import install; install()
    except Exception:
        pass
    main()
