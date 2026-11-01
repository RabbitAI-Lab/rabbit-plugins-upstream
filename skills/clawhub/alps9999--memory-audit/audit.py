#!/usr/bin/env python3
"""
memory-audit —— 记忆机制体检
只读实现：不修改任何记忆文件。

用法:
  python3 audit.py --memory ~/.claude/projects/X/memory \
                   --sessions ~/.claude/projects/X \
                   --spec ~/CLAUDE.md \
                   --json out.json --html report.html
"""
import os, re, sys, json, glob, time, argparse, subprocess
from collections import Counter, defaultdict

DAY = 86400.0


def read(p):
    try:
        return open(p, encoding="utf-8").read()
    except Exception:
        return ""


def build_list(memory_dir, index_name, exclude_dirs):
    files = []
    for entry in sorted(os.listdir(memory_dir)):
        full = os.path.join(memory_dir, entry)
        if not os.path.isfile(full) or not entry.endswith(".md"):
            continue
        if entry == index_name:
            continue
        files.append(entry)
    return files


def git_log(memory_dir):
    try:
        out = subprocess.run(
            ["git", "-C", memory_dir, "log", "--name-only", "--format=@@@%cI"],
            capture_output=True, text=True, timeout=30).stdout
    except Exception:
        return {}
    commits = defaultdict(list)
    cur = None
    for line in out.splitlines():
        if line.startswith("@@@"):
            cur = line[3:].strip()
        elif line.strip() and cur:
            commits[line.strip()].append(cur)
    return commits


def scan_reads(sessions_dir, names, limit=None):
    """统计真实的 Read 工具调用"""
    read_cnt = defaultdict(int)
    sess_seen = defaultdict(set)
    if not sessions_dir or not os.path.isdir(sessions_dir):
        return read_cnt, sess_seen, 0
    paths = sorted(glob.glob(os.path.join(sessions_dir, "*.jsonl")),
                   key=os.path.getmtime)
    if limit:
        paths = paths[-limit:]
    for sp in paths:
        sid = os.path.basename(sp)[:8]
        try:
            fh = open(sp, encoding="utf-8", errors="ignore")
        except Exception:
            continue
        with fh:
            for line in fh:
                if '"tool_use"' not in line:
                    continue
                try:
                    obj = json.loads(line)
                except Exception:
                    continue
                cont = (obj.get("message") or {}).get("content")
                if not isinstance(cont, list):
                    continue
                for it in cont:
                    if not isinstance(it, dict) or it.get("type") != "tool_use":
                        continue
                    if it.get("name") != "Read":
                        continue
                    fp = str((it.get("input") or {}).get("file_path") or "")
                    if not fp.endswith(".md"):
                        continue
                    base = os.path.basename(fp)
                    if base in names:
                        read_cnt[base] += 1
                        sess_seen[base].add(sid)
    return read_cnt, sess_seen, len(paths)


def main():
    ap = argparse.ArgumentParser(description="记忆机制体检（只读）")
    ap.add_argument("--memory", default=".")
    ap.add_argument("--index", default="MEMORY.md")
    ap.add_argument("--spec", default=None, help="常驻层文件，如 CLAUDE.md")
    ap.add_argument("--sessions", default=None, help="会话 jsonl 目录")
    ap.add_argument("--json", dest="json_out", default=None)
    ap.add_argument("--html", default=None)
    ap.add_argument("--session-limit", type=int, default=None)
    a = ap.parse_args()

    mem = os.path.abspath(os.path.expanduser(a.memory))
    files = build_list(mem, a.index, None)
    names = set(files)
    now = time.time()

    index_text = read(os.path.join(mem, a.index))
    spec_text = read(os.path.expanduser(a.spec)) if a.spec else ""

    # ---- R 引用度 ----
    all_md = {f: read(os.path.join(mem, f)) for f in files}
    R = {}
    for f in files:
        slug = f[:-3]
        in_idx = 1 if f in index_text else 0
        wl = sum(len(re.findall(r"\[\[" + re.escape(slug) + r"\]\]", t))
                 for g, t in all_md.items() if g != f)
        in_spec = len(re.findall(re.escape(slug), spec_text)) if spec_text else 0
        R[f] = {"index": in_idx, "wikilink": wl, "spec": in_spec,
                "raw": in_idx * 2 + wl + min(in_spec, 3)}

    # ---- C / T ----
    commits = git_log(mem)
    C, T = {}, {}
    for f in files:
        ds = commits.get(f, [])
        C[f] = len(ds)
        if ds:
            try:
                t = time.mktime(time.strptime(max(ds)[:19], "%Y-%m-%dT%H:%M:%S"))
                T[f] = (now - t) / DAY
            except Exception:
                T[f] = 9999
        else:
            try:
                T[f] = (now - os.stat(os.path.join(mem, f)).st_mtime) / DAY
            except Exception:
                T[f] = 9999

    # ---- H 命中度 ----
    read_cnt, sess_seen, n_sess = scan_reads(a.sessions, names, a.session_limit)

    # ---- 打分 ----
    def nz(v, hi):
        return 0.0 if hi <= 0 else max(0.0, min(1.0, v / hi))

    rmax = max([x["raw"] for x in R.values()] + [1])
    cmax = max(list(C.values()) + [1])
    hmax = max(list(read_cnt.values()) + [1])
    smax = max([len(v) for v in sess_seen.values()] + [1])

    rows = []
    for f in files:
        h = 0.6 * nz(read_cnt.get(f, 0), hmax) + 0.4 * nz(len(sess_seen.get(f, ())), smax)
        score = (0.4 * h + 0.3 * nz(R[f]["raw"], rmax)
                 + 0.2 * nz(C[f], cmax) + 0.1 * (1 - min(T[f], 365) / 365))
        d = T[f]
        if score >= 0.55 and d < 90:      bucket = "核心"
        elif score >= 0.35 and d >= 90:   bucket = "沉淀"
        elif score < 0.18 and d > 300:    bucket = "冷舱"
        else:                             bucket = "待查"
        rows.append({"file": f, "score": round(score, 3),
                     "reads": read_cnt.get(f, 0), "sessions": len(sess_seen.get(f, ())),
                     "refs": R[f]["raw"], "indexed": R[f]["index"],
                     "commits": C[f], "days": round(d), "bucket": bucket})
    rows.sort(key=lambda x: -x["score"])

    # ---- 完整性 ----
    idx_targets = re.findall(r"\]\(([^)]+?\.md)\)", index_text)
    dangling = [t for t in idx_targets if not os.path.exists(os.path.join(mem, t))]
    unindexed = [f for f in files if f not in index_text]
    idx_bytes = len(index_text.encode())

    report = {
        "generatedAt": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "memoryDir": mem,
        "totalFiles": len(files),
        "sessionsScanned": n_sess,
        "indexLines": len(index_text.splitlines()),
        "indexBytes": idx_bytes,
        "estTokens": round(idx_bytes / 2.2),
        "neverRead": sum(1 for r in rows if r["reads"] == 0),
        "buckets": dict(Counter(r["bucket"] for r in rows)),
        "dangling": dangling,
        "unindexedCount": len(unindexed),
        "rows": rows,
    }

    # ---- 输出 ----
    print(f"\n记忆机制体检 · {mem}")
    print("=" * 58)
    print(f"  记忆条目          {len(files)}")
    print(f"  索引             {report['indexLines']} 行 / {idx_bytes} 字节 "
          f"(≈{report['estTokens']} tokens/轮)")
    print(f"  会话扫描          {n_sess} 个")
    print(f"  从未被读取        {report['neverRead']} 条 "
          f"({report['neverRead']*100//max(len(files),1)}%)")
    print(f"  索引未覆盖        {len(unindexed)} 条")
    if dangling:
        print(f"  悬空引用          {len(dangling)} 条  {dangling}")
    print(f"\n  分档: " + "  ".join(f"{k} {v}" for k, v in report["buckets"].items()))
    print("\n  最常用 5 条:")
    for r in rows[:5]:
        print(f"    {r['score']:.2f}  读{r['reads']:2d}次  {r['file']}")
    if report["neverRead"]:
        print(f"\n  从未被读取（前 10）:")
        for r in [x for x in rows if x["reads"] == 0][:10]:
            print(f"    {r['file']}")
    print()

    if a.json_out:
        json.dump(report, open(a.json_out, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        print(f"  JSON -> {a.json_out}")

    if a.html:
        write_html(report, a.html)
        print(f"  HTML -> {a.html}")


def write_html(rep, path):
    rows = "".join(
        f"<tr><td>{r['file']}</td><td class='n'>{r['reads']}</td>"
        f"<td class='n'>{r['refs']}</td><td class='n'>{r['days']}</td>"
        f"<td><span class='b b{r['bucket']}'>{r['bucket']}</span></td></tr>"
        for r in rep["rows"])
    html = f"""<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">
<title>记忆体检报告</title><style>
body{{font-family:"Hiragino Sans GB","PingFang SC",sans-serif;max-width:820px;
margin:40px auto;padding:0 20px;background:#f8f8f5;color:#141414;font-size:14px}}
h1{{font-size:24px;border-bottom:2px solid #141414;padding-bottom:12px}}
table{{width:100%;border-collapse:collapse;margin-top:16px;font-size:13px}}
th{{text-align:left;font-size:11px;text-transform:uppercase;color:#6e6e6e;
padding:6px 8px;border-bottom:1.5px solid #141414}}
td{{padding:6px 8px;border-bottom:1px solid #efefea}}
.n{{text-align:right;font-variant-numeric:tabular-nums}}
.b{{font-size:11px;padding:1px 7px;border-radius:9px;border:1px solid #ddd}}
.b核心{{color:#1a4d7a;border-color:#cfdde9;background:#eef3f8}}
.b沉淀{{color:#2f6b4f;border-color:#cfe3d8;background:#f2f8f5}}
.b冷舱{{color:#5b6b7a;border-color:#dde2e6;background:#f4f6f8}}
.b待查{{color:#8a6a12;border-color:#ecdfc0;background:#fcf8ee}}
</style></head><body>
<h1>记忆体检报告</h1>
<p>生成于 {rep['generatedAt']} · 共 {rep['totalFiles']} 条 ·
索引 {rep['indexLines']} 行（≈{rep['estTokens']} tokens/轮）·
从未读取 {rep['neverRead']} 条</p>
<table><thead><tr><th>记忆</th><th class="n">读取</th><th class="n">引用</th>
<th class="n">天数</th><th>分档</th></tr></thead><tbody>{rows}</tbody></table>
</body></html>"""
    open(path, "w", encoding="utf-8").write(html)


if __name__ == "__main__":
    main()
