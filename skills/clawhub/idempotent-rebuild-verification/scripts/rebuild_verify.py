#!/usr/bin/env python3
"""rebuild_verify.py — 哈希钉扎重建工作区的验证/分类/提取工具 v2.0.0

纯标准库、离线、确定性。JSON 输出（stdout=数据, stderr=错误），退出码：
  0 全部正常 · 2 输入错误 · 3 检测到漂移/缺失/不一致

命令：
  verify FILE --want HEX [--want-size N]   单文件漂移分类（良性质漂移 vs 真损坏）
  manifest MANIFEST [--root DIR]           批量校验 `path sha256 [size]` 清单
  pins RUNBOOK.md                          提取 runbook 中的 sha256 钉扎
  extract-steps RUNBOOK.md [--lang L] [--write-steps DIR]
                                           CommonMark 正确的代码块/步骤提取（处理嵌套围栏）
  wipe-audit DIR                           快照擦除后状态判定（正常 vs 异常）
  gen-fixtures DIR                         生成确定性合成测试夹具（无网络、无 PHI）

核心领域事实（2026-09-06 依据核对）：
  - POSIX XCU 命令替换：$(cmd) 会移除替换末尾的 1..N 个换行（嵌入的保留）。
    因此 `loader set "$(cat f)"` 后回写 f 会丢失尾部换行 -> 钉扎哈希假警报（良性质漂移）。
  - heredoc `cat > f <<'EOF'` 内容恒以 \\n 结尾。
  - CommonMark §4.5 围栏代码块：闭合围栏须同字符且长度>=开栏；```bash 块内再出现 ```
    即为闭合 -> 朴素按围栏切分 runbook 会静默截断载荷。
  - 快照擦除：排除目录（build/node_modules/dist/...）在轮间消失，普通文件存活 ->
    "脚本在、产物不在" 是擦除后正常态。

本工具只做完整性/状态判定，不修改任何被验证文件；不联网。
"""
import argparse
import hashlib
import json
import os
import re
import sys

TOOL = "rebuild-verify v2.0.0"

# 本环境快照排除目录（workspace 文档化列表；按环境可加）
SNAPSHOT_EXCLUDED = [
    "build", "node_modules", "dist", "out", "target", "__pycache__",
    ".venv", ".npm", ".cache", ".local", ".next", ".nuxt", ".output",
    ".parcel-cache", ".pytest_cache", ".ruff_cache", ".svelte-kit", ".tox",
    ".turbo", ".mypy_cache", "coverage", ".arena",
]

# 症状 -> 需重跑的步骤（固定路由表，内嵌于代码）
STEP_ROUTER = {
    "toolchain_missing": "重跑 toolchain 安装步骤（cmake/g++ 等缺失）",
    "shim_missing": "重跑 shim 步骤（沙箱 stdin 关闭时注意 npx --yes）",
    "compile_artifacts_missing": "重跑 compile 步骤（build/ 属快照排除目录，擦除后正常缺失）",
    "model_missing": "重跑 model 下载步骤（*.gguf/*.bin 缺失）",
    "skill_count_dropped": "重跑 mass-install 步骤（幂等，可安全重跑）",
    "script_hash_mismatch": "先运行 verify 分类（良性漂移时重跑 writer 步骤，勿盲目重贴）",
}

HTML_MARKERS = (b"404", b"error", b"not found", b"access denied")


def err(msg, code=2, **extra):
    out = {"status": "error", "tool": TOOL, "error": msg}
    out.update(extra)
    print(json.dumps(out, ensure_ascii=False), file=sys.stderr)
    sys.exit(code)


def emit(obj):
    print(json.dumps(obj, ensure_ascii=False))


def sha256_hex(b):
    return hashlib.sha256(b).hexdigest()


def read_file(path, quiet=False):
    try:
        with open(path, "rb") as f:
            return f.read()
    except OSError as e:
        if quiet:
            return None
        err("无法读取文件: %s" % e, 2, path=path)


def count_trailing_newlines(data, byte=b"\n"):
    n = 0
    for b in reversed(data):
        if b == byte[0]:
            n += 1
        else:
            break
    return n


def looks_like_html(data):
    head = data[:256].lstrip()[:16].lower()
    if head.startswith(b"<!doctype html") or head.startswith(b"<html"):
        return True
    if len(data) < 4096:
        low = data[:4096].lower()
        # 关键词分支要求 < > 标签上下文：纯文本含 "error" 不算 HTML 错误页
        return b"<" in low and b">" in low and any(m in low for m in HTML_MARKERS)
    return False


# ── verify：漂移分类状态机 ─────────────────────────────────────────────────
def classify(data, want, want_size):
    """返回 (status, klass, detail, next_action)。status: ok/benign/warn/error。"""
    got = sha256_hex(data)
    d = {"size": len(data), "got_sha256": got, "want_sha256": want, "want_size": want_size}
    if want is None and want_size is not None:
        if len(data) == want_size:
            d["size_only"] = True
            return "ok", "size_ok", d, "尺寸匹配；建议补钉 sha256（%s）" % got
        return "error", "size_mismatch", d, "尺寸不符（%d != %d）：先 diff 再决定重写" % (len(data), want_size)
    if not want:
        return "error", "no_criteria", d, "需要 --want HEX 或 --want-size N"
    if got == want:
        return "ok", "ok", d, "无需动作：哈希匹配"
    # 1) 尾部换行归一化族（$(cat) 往返 / printf 补一个 \n / heredoc 单 \n）
    core = data.rstrip(b"\n")
    variants = {"strip_all": sha256_hex(core), "single_nl": sha256_hex(core + b"\n")}
    match = None
    for k, v in variants.items():
        if v == want:
            match = k
            break
    if match:
        n = count_trailing_newlines(data)
        d.update(trailing_newlines=n, normalized_match=match)
        if match == "strip_all" and n == 0:
            hint = "文件被 $(cat ...) 往返剥离了全部尾部换行且未补回（POSIX 命令替换语义）"
        elif match == "single_nl" and n == 1:
            hint = "文件多了一个尾部换行（写入端补 \n 而钉扎为无 \n 形式）"
        else:
            hint = "尾部换行数量不同（当前 %d 个；钉扎形式=%s）" % (n, match)
        return "benign", "trailing_newline_drift", d, \
            "良性质漂移，勿盲目重贴：重跑 *writer* 步骤恢复钉扎形式。%s" % hint
    # 2) CRLF 归一化（编辑器往返）
    lf = data.replace(b"\r\n", b"\n")
    if lf != data and sha256_hex(lf) == want:
        d.update(crlf_count=data.count(b"\r\n"), normalized_match="crlf_to_lf")
        return "benign", "crlf_drift", d, \
            "良性质漂移：行尾 CRLF vs 钉扎 LF；转换或按 CRLF 形式重新钉扎"
    # 3) HTML 错误页（下载失败：404/错误页被当成功写入）
    if looks_like_html(data):
        d.update(magic=data[:16].hex())
        return "error", "html_error_page", d, \
            "这是 HTML 错误页而非目标内容：URL/仓库路径或认证错误，重新下载并断言字节数"
    # 4) 截断（heredoc 粘贴中断）
    if want_size is not None and len(data) < want_size * 0.9:
        d.update(size_delta=len(data) - want_size, ends_with_newline=data.endswith(b"\n"))
        return "error", "truncated_paste", d, \
            "疑似截断（%d < %d*0.9）：删除后整块重贴，勿在尾部续写" % (len(data), want_size)
    # 5) 同尺寸内容变更
    if want_size is not None and len(data) == want_size:
        d.update(magic=data[:16].hex())
        return "error", "content_change", d, \
            "同尺寸哈希不符：内容被改；与新鲜写出做 diff 定位差异"
    # 6) 其他
    d.update(magic=data[:16].hex(),
             trailing_newlines=count_trailing_newlines(data),
             size_delta=(len(data) - want_size) if want_size is not None else None)
    return "warn", "unknown", d, \
        "未归类漂移：用 diff/xxd 对比新鲜写出的同内容文件后再处置"


def cmd_verify(args):
    data = read_file(args.file)
    want = args.want.lower() if args.want else None
    if want:
        if not re.fullmatch(r"[0-9a-f]{64}", want):
            err("--want 需要 64 位十六进制 sha256", 2, got=args.want)
    status, klass, detail, action = classify(data, want, args.want_size)
    detail["file"] = args.file
    emit({"command": "verify", "status": status, "class": klass,
          "tool": TOOL, "next_action": action, "detail": detail})
    sys.exit(0 if status == "ok" else (3 if status in ("benign", "warn", "error") else 2))


# ── manifest ───────────────────────────────────────────────────────────────
def parse_manifest(text, root):
    entries = []
    for i, line in enumerate(text.splitlines(), 1):
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        parts = s.split()
        if len(parts) < 2:
            err("清单第 %d 行格式错误: %r（需 `path sha256 [size]`）" % (i, s), 2)
        path, h = parts[0], parts[1].lower()
        if not re.fullmatch(r"[0-9a-f]{64}", h):
            err("清单第 %d 行哈希非法: %r" % (i, parts[1]), 2)
        size = int(parts[2]) if len(parts) > 2 else None
        p = path if os.path.isabs(path) else os.path.join(root, path)
        entries.append({"line": i, "path": p, "rel": path, "sha256": h, "size": size})
    return entries


def cmd_manifest(args):
    text = read_file(args.manifest).decode("utf-8", errors="replace")
    root = os.path.abspath(args.root or os.path.dirname(os.path.abspath(args.manifest)))
    entries = parse_manifest(text, root)
    ok, drifted, missing = [], [], []
    for e in entries:
        data = read_file(e["path"], quiet=True)
        if data is None:
            missing.append({"rel": e["rel"], "line": e["line"]})
            continue
        status, klass, detail, action = classify(data, e["sha256"], e["size"])
        rec = {"rel": e["rel"], "class": klass, "status": status, "next_action": action}
        if status == "ok":
            ok.append(rec)
        else:
            drifted.append(rec)
    out = {"command": "manifest", "tool": TOOL, "root": root, "total": len(entries),
           "n_ok": len(ok), "n_drifted": len(drifted), "n_missing": len(missing),
           "ok": [r["rel"] for r in ok], "drifted": drifted, "missing": missing,
           "status": "ok" if not drifted and not missing else "drift"}
    emit(out)
    sys.exit(0 if not drifted and not missing else 3)


# ── pins ──────────────────────────────────────────────────────────────────
PIN_PATTERNS = [
    re.compile(r"sha256\s+must\s+be\s*:\s*([0-9a-fA-F]{64})"),
    re.compile(r"must\s+be\s+sha256\s*:\s*([0-9a-fA-F]{64})"),
    re.compile(r"sha256\s*:\s*([0-9a-fA-F]{64})"),
]


def cmd_pins(args):
    text = read_file(args.file).decode("utf-8", errors="replace")
    lines = text.splitlines()
    fenced_lines = set()
    for b in extract_blocks(lines):
        for k in range(b["start"] - 2, b["end"] + 1):  # 开栏..闭栏（含）
            fenced_lines.add(k + 1)
    pins, heading = [], ""
    for i, line in enumerate(lines, 1):
        in_fence = i in fenced_lines
        if not in_fence:
            h = re.match(r"^(#{1,6})\s+(.*)", line)
            if h:
                heading = h.group(2).strip()
        m = None
        for pat in PIN_PATTERNS:
            m = pat.search(line)
            if m:
                break
        if not m:
            continue
        ref = None
        r = re.search(r"`([^`]+\.\w+)`", line)
        if r:
            ref = r.group(1)
        else:
            for j in range(i - 2, max(-1, i - 5), -1):
                if j < 0:
                    break
                r = re.search(r"(?:cat|tee)\s+>?>?\s*([^\s|;&<]+)\s*<<", lines[j])
                if r:
                    ref = r.group(1)
                    break
                r = re.search(r"(?:sha256sum|md5sum|diff)\s+([`~]?(?:~/|\.{1,2}/)?[\w./-]+\.\w+)", lines[j])
                if r:
                    tok = r.group(1).strip("`~")
                    if lines[j].rstrip().endswith(tok) and lines[j].find(tok) > 0 and lines[j][lines[j].find(tok) - 1] == "~":
                        tok = "~" + tok
                    ref = tok
                    break
                r = re.search(r"(?:write|writes|written|file|path|to|into)\s+(?:the\s+)?[`~]?"
                              r"((?:~/|\.{1,2}/)?[\w./-]+\.\w+)", lines[j])
                if r:
                    ref = r.group(1)
                    break
        pins.append({"line": i, "sha256": m.group(1).lower(), "heading": heading,
                     "referenced_file": ref, "in_code_fence": in_fence,
                     "raw": line.strip()[:160]})
    emit({"command": "pins", "tool": TOOL, "file": args.file, "n_pins": len(pins), "pins": pins})
    sys.exit(0)


# ── extract-steps（CommonMark 围栏语义）────────────────────────────────────
FENCE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})\s*(.*)$")
HEREDOC_RE = re.compile(r"^\s*(?:cat|tee)\b[^|;&]*?<<-?\s*['\"]?([A-Za-z_][A-Za-z0-9_-]*)['\"]?")


def fence_indent_ok(ln):
    """CommonMark 缩进规则：Tab 展开到下一个 4 列；围栏行缩进上限 3 列。"""
    col = 0
    for ch in ln:
        if ch == " ":
            col += 1
        elif ch == "\t":
            col += 4 - (col % 4)
        else:
            break
    return col <= 3


def extract_blocks(lines):
    """返回 [{start, end, lang, unterminated, content}]。
    1-based：start=内容首行, end=内容末行（闭合围栏行=end+1；未闭合时 end=文档末行）。content 不含围栏行。"""
    blocks, i, n = [], 0, len(lines)
    while i < n:
        m = FENCE_RE.match(lines[i])
        if m:
            fence_char = m.group(1)[0]
            fence_len = len(m.group(1))
            info = m.group(2).strip()
            lang = info.split()[0].lower() if info else ""
            start = i + 2  # 内容首行（1-based）；开栏行 = start-1
            j = i + 1
            closed = False
            while j < n:
                ln = lines[j]
                s = ln.strip()
                if len(s) >= fence_len and set(s) == {fence_char} and fence_indent_ok(ln):
                    closed = True
                    break
                j += 1
            end = j  # 1-based 末行 = j（闭合围栏行），未闭合 = n
            blocks.append({"start": start, "end": j, "lang": lang,
                           "unterminated": not closed,
                           "content": lines[i + 1: j]})
            i = j + 1 if closed else n
        else:
            i += 1
    return blocks


def heredocs_in(content_lines):
    found, open_ = [], None
    for k, ln in enumerate(content_lines):
        s = ln.strip()
        m = HEREDOC_RE.match(ln)
        if m and not s.startswith("#"):
            label = m.group(1)
            open_ = {"label": label, "at_line": k + 1, "terminated": False,
                     "dash": bool(re.search(r"<<-\s*['\"]?" + re.escape(label), ln))}
            found.append(open_)
            continue
        if open_ and not open_["terminated"]:
            term = (s == open_["label"]) or (open_["dash"] and re.fullmatch(r"\t*" + re.escape(open_["label"]), ln.rstrip()))
            if term:
                open_["terminated"] = True
                open_ = None
    return found


def step_status(b):
    if b["unterminated"]:
        return "suspect", "代码块未闭合（CommonMark: 内容延伸到文档末尾）——按显式行范围切割，勿直接执行"
    for h in b.get("heredocs", []):
        if not h["terminated"]:
            return "suspect", ("heredoc 标签 %s 未找到终止行（可能被内嵌围栏提前截断）——按显式行范围切割，勿直接执行" % h["label"])
    return "ok", "结构完整"


def cmd_extract(args):
    text = read_file(args.file).decode("utf-8", errors="replace")
    lines = text.splitlines()
    blocks = extract_blocks(lines)
    steps = []
    for idx, b in enumerate(blocks, 1):
        blang = b["lang"] or "text"
        if args.lang and args.lang != "all" and blang != args.lang:
            continue
        content = b["content"]
        hds = heredocs_in(content)
        st, why = step_status({**b, "heredocs": hds})
        payload = ("\n".join(content) + "\n") if content else ""
        steps.append({"index": idx, "lang": blang,
                      "start_line": b["start"], "end_line": b["end"],
                      "bytes": len(payload.encode("utf-8")),
                      "unterminated": b["unterminated"],
                      "heredocs": hds, "status": st, "why": why,
                      "sha256": sha256_hex(payload.encode("utf-8")) if content else None})
    suspect = [s["index"] for s in steps if s["status"] == "suspect"]
    out = {"command": "extract-steps", "tool": TOOL, "file": args.file,
           "n_steps": len(steps), "suspect": suspect,
           "next_action": ("有疑似截断步骤 %s：按显式行范围人工切割后再执行" % suspect)
                           if suspect else "全部步骤结构完整", "steps": steps}
    if args.write_steps:
        os.makedirs(args.write_steps, exist_ok=True)
        manifest = []
        for s in steps:
            b = next(b for b in blocks if b["start"] == s["start_line"] and b["end"] == s["end_line"])
            name = "step_%02d.%s" % (s["index"], {"bash": "sh", "sh": "sh", "shell": "sh",
                                                    "python": "py"}.get(s["lang"], "txt"))
            p = os.path.join(args.write_steps, name)
            payload = "\n".join(b["content"]) + ("\n" if b["content"] else "")
            with open(p, "w", encoding="utf-8", newline="") as f:
                f.write(payload)
            manifest.append({"index": s["index"], "file": name, "bytes": s["bytes"],
                             "sha256": s["sha256"], "status": s["status"]})
        with open(os.path.join(args.write_steps, "steps.json"), "w", encoding="utf-8") as f:
            json.dump(manifest, f, ensure_ascii=False, indent=1)
        out["written"] = args.write_steps
    emit(out)
    sys.exit(0)


# ── wipe-audit ─────────────────────────────────────────────────────────────
def snapshot_excluded():
    """快照排除目录清单。RV_SNAPSHOT_EXCLUDED 环境变量（空白/逗号/分号/冒号分隔）覆盖内置值。"""
    env = os.environ.get("RV_SNAPSHOT_EXCLUDED", "").strip()
    if env:
        return frozenset(x.strip() for x in re.split(r"[,;:\s]+", env) if x.strip())
    return SNAPSHOT_EXCLUDED


def cmd_wipe(args):
    root = os.path.abspath(args.dir)
    counts = {"excluded_dirs_present": [], "scripts": [], "bins": [], "models": [], "shim": []}
    n_entries = 0
    for dirpath, dirnames, filenames in os.walk(root):
        if n_entries > 5000:
            break
        n_entries += len(dirnames) + len(filenames)
        rel = os.path.relpath(dirpath, root)
        for fn in filenames:
            fp = os.path.join(dirpath, fn)
            if fn in ("Makefile",) or fn.endswith((".sh", ".py")):
                counts["scripts"].append(os.path.relpath(fp, root))
            if fn.endswith((".gguf", ".safetensors")) or (fn.endswith(".bin") and "model" in fp.lower()):
                counts["models"].append(os.path.relpath(fp, root))
        bin_hits = [dn for dn in dirnames
                    if os.path.basename(os.path.normpath(dirpath)) == "bin"
                    and dirpath != os.path.join(root, "bin")]
        for dn in bin_hits:
            dp = os.path.join(dirpath, dn)
            for x in os.listdir(dp)[:20]:
                counts["bins"].append(os.path.relpath(os.path.join(dp, x), root))
        for dn in dirnames:
            if dn in snapshot_excluded():
                counts["excluded_dirs_present"].append(os.path.relpath(os.path.join(dirpath, dn), root))
        if rel in (".", ""):
            for special in (".shim",):
                if os.path.isdir(os.path.join(dirpath, special)):
                    counts["shim"].append(special)
            if os.path.isdir(os.path.join(dirpath, "node_modules", ".bin")):
                counts["shim"].append("node_modules/.bin")
    ex_set = set(os.path.basename(p) for p in counts["excluded_dirs_present"])
    has_scripts = bool(counts["scripts"])
    has_artifacts = bool(counts["excluded_dirs_present"]) or bool(counts["bins"]) or bool(counts["models"])
    actions = []
    if not has_scripts and not has_artifacts:
        verdict = "clean"
        next_action = "空工作区/未开始构建"
    elif has_scripts and not has_artifacts:
        verdict = "normal_post_wipe"
        if not counts["bins"]:
            actions.append(STEP_ROUTER["compile_artifacts_missing"])
        if not counts["models"]:
            actions.append(STEP_ROUTER["model_missing"])
        if not counts["shim"]:
            actions.append(STEP_ROUTER["shim_missing"])
        next_action = "快照擦除后正常态：脚本存活、排除目录产物消失；仅需重跑产物步骤（见 next_actions）"
    elif has_scripts and has_artifacts:
        verdict = "pre_wipe_or_full"
        next_action = "完整状态（未擦除或已重建）：无需动作"
    else:
        verdict = "scripts_missing_too"
        next_action = "异常：产物还在但脚本消失——先恢复脚本（git/备份），再谈重跑"
    out = {"command": "wipe-audit", "tool": TOOL, "root": root, "verdict": verdict,
           "next_action": next_action, "next_actions": actions,
           "present": {
               "excluded_dirs": sorted(ex_set),
               "scripts": counts["scripts"][:20], "n_scripts": len(counts["scripts"]),
               "bins": counts["bins"][:20], "n_bins": len(counts["bins"]),
               "models": counts["models"][:10], "shim": counts["shim"]},
           "entries_scanned": n_entries}
    emit(out)
    sys.exit(0 if verdict != "scripts_missing_too" else 3)


# ── gen-fixtures（确定性合成夹具）──────────────────────────────────────────
CANONICAL_LINE = "Rebuild canonical prompt line {n:03d} - hash-pinned content for triage tests."


def make_canonical(total=1116):
    """确定性构造：正文行 + 最后一行补齐，整体恰好 total 字节且以单个 \\n 结尾。"""
    body, n = b"", 1
    while True:
        cand = CANONICAL_LINE.format(n=n).encode("ascii") + b"\n"
        if len(body) + len(cand) > total - 1:
            break
        body += cand
        n += 1
    last_len = total - 1 - len(body)
    filler = CANONICAL_LINE.format(n=n).encode("ascii")
    if len(filler) >= last_len:
        filler = filler[: last_len]
    else:
        filler = filler + b" " * (last_len - len(filler))
    return body + filler + b"\n"


def make_html404():
    page = (b"<html>\n<head><title>404 Not Found</title></head>\n"
            b"<body><center><h1>404 Not Found</h1></center>\n"
            b"<hr><center>nginx/1.24.0</center>\n</body>\n</html>\n")
    return page


def cmd_genfixtures(args):
    root = os.path.abspath(args.dir)
    os.makedirs(root, exist_ok=True)
    canon = make_canonical(1116)
    assert len(canon) == 1116 and canon.endswith(b"\n") and not canon.endswith(b"\n\n")
    fixtures = {
        "canonical.txt": canon,
        "drift_no_nl.txt": canon[:-1],                      # 1115B：$(cat) 往返
        "drift_3nl.txt": canon + b"\n\n",                   # 1118B：多两个 \n
        "truncated.txt": canon[:500],                       # 截断
        "html404.txt": make_html404(),                      # 下载失败页
        "same_size_diff.txt": canon[:100] + bytes([canon[100] + 1]) + canon[101:],
        "crlf.txt": canon.replace(b"\n", b"\r\n"),
    }
    assert not fixtures["truncated.txt"].endswith(b"\n"), "截断夹具须止于词中"
    for name, data in fixtures.items():
        with open(os.path.join(root, name), "wb") as f:
            f.write(data)
    # 清单：以 canonical 的钉扎哈希为准（模拟 runbook 钉扎 writer 产物）
    want = sha256_hex(canon)
    man = [
        "# manifest.txt — 钉扎 canonical.txt 的 sha256/size，其余文件用于分类演示",
        "canonical.txt %s %d" % (want, 1116),
        "drift_no_nl.txt %s %d" % (want, 1116),
        "drift_3nl.txt %s %d" % (want, 1116),
        "truncated.txt %s %d" % (want, 1116),
        "html404.txt %s %d" % (want, 1116),
        "same_size_diff.txt %s %d" % (want, 1116),
        "crlf.txt %s %d" % (want, 1116),
    ]
    with open(os.path.join(root, "manifest.txt"), "w", encoding="utf-8", newline="") as f:
        f.write("\n".join(man) + "\n")
    # runbook.md：6 步（含内嵌围栏的 heredoc、未终止 heredoc、钉扎行）
    inner_fence_step = (
        "STEP 3: write the shim wrapper\n"
        "cat > ~/.shim/claude << 'SHIM_EOF'\n"
        "#!/bin/sh\n"
        "echo 'usage: see runbook'\n"
        "```bash\n"
        "# inner fence line: an example inside the heredoc\n"
        "```\n"
        "exec /usr/local/bin/claude \"$@\"\n"
        "SHIM_EOF\n")
    runbook = "\n".join([
        "# Mini Rebuild Runbook (synthetic test)",
        "",
        "STEP 1: install toolchain",
        "```bash",
        "apt-get update && apt-get install -y cmake g++ make",
        "```",
        "",
        "STEP 2: write the pinned prompt",
        "```bash",
        "cat > ~/dynamic_system_prompt.txt << 'EOF'",
        "canonical prompt body",
        "EOF",
        "# sha256 must be: %s" % want,
        "```",
        "",
        "STEP 3 (heredoc embeds a code fence):",
        "```bash",
        *inner_fence_step.split("\n")[1:],
        "```",
        "",
        "STEP 4 (BROKEN on purpose: unterminated heredoc):",
        "```bash",
        "cat > /tmp/never_closed << 'OPEN_LABEL'",
        "payload line one",
        "```",
        "",
        "STEP 5: tilde-fence step",
        "~~~~sh",
        "ls -la ~/.shim",
        "~~~~",
        "",
        "STEP 6: verify",
        "```bash",
        "sha256sum ~/dynamic_system_prompt.txt",
        "# sha256: %s" % want,
        "```",
        "",
    ]) + "\n"
    with open(os.path.join(root, "runbook.md"), "w", encoding="utf-8", newline="") as f:
        f.write(runbook)
    out = {"command": "gen-fixtures", "tool": TOOL, "dir": root,
           "files": {k: len(v) for k, v in fixtures.items()} | {"manifest.txt": None, "runbook.md": None},
           "canonical_sha256": want,
           "deterministic": "是：相同参数输出字节相同（无时间戳/随机）"}
    emit(out)
    sys.exit(0)


def main():
    p = argparse.ArgumentParser(
        prog="rebuild_verify.py", description=TOOL + "（纯标准库、离线、确定性）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="flags:\n"
               "  verify        FILE --want HEX [--want-size N]   # 内容+尺寸双钉\n"
               "  manifest      MANIFEST [--root DIR]             # 每行: path sha256 [size]\n"
               "  extract-steps RUNBOOK [--lang bash|sh|shell|python|text|all] [--write-steps DIR]\n"
               "  wipe-audit    DIR | gen-fixtures DIR\n"
               "exit: 0 ok/全好 | 2 输入错误(stderr 单行 JSON) | 3 漂移/缺失/脚本缺失异常")
    sub = p.add_subparsers(dest="command", required=True)

    sp = sub.add_parser("verify", help="单文件漂移分类")
    sp.add_argument("file")
    sp.add_argument("--want", default=None, help="钉扎 sha256（64 hex）")
    sp.add_argument("--want-size", type=int, default=None, help="钉扎字节数")
    sp.set_defaults(fn=cmd_verify)

    sp = sub.add_parser("manifest", help="批量校验清单")
    sp.add_argument("manifest")
    sp.add_argument("--root", default=None)
    sp.set_defaults(fn=cmd_manifest)

    sp = sub.add_parser("pins", help="提取 runbook 钉扎")
    sp.add_argument("file")
    sp.set_defaults(fn=cmd_pins)

    sp = sub.add_parser("extract-steps", help="CommonMark 步骤提取")
    sp.add_argument("file")
    sp.add_argument("--lang", default=None, help="bash|sh|shell|python|text|all")
    sp.add_argument("--write-steps", default=None)
    sp.set_defaults(fn=cmd_extract)

    sp = sub.add_parser("wipe-audit", help="擦除后状态判定")
    sp.add_argument("dir")
    sp.set_defaults(fn=cmd_wipe)

    sp = sub.add_parser("gen-fixtures", help="生成确定性合成夹具")
    sp.add_argument("dir")
    sp.set_defaults(fn=cmd_genfixtures)

    args = p.parse_args()
    try:
        args.fn(args)
    except SystemExit:
        raise
    except Exception as e:
        err("未预期错误: %s: %s" % (type(e).__name__, e), 2)


if __name__ == "__main__":
    main()
