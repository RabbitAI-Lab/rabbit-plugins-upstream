#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""yiigle_tracker.py — 中华医学期刊网（yiigle）指南/共识/标准定时追踪下载工具。

复用 cn_med_oa.py 的 yiigle 检索/详情/下载能力（同目录 import），独立轻量：
  1. 关键词追踪：--keywords "指南,共识,标准" 逐词扫描最新文献
  2. 期刊追踪：--journals "中华内科杂志,中华儿科杂志" 按刊名过滤关键词结果
  3. 快照 diff：状态文件记录已见文献 ID，只报告新增（首次运行建立基线不报告）
  4. 儿科优先：标题含儿科关键词（儿童/小儿/新生儿/婴幼儿等）排前并标 🧒
  5. best-effort 下载：复用 yiigle_try_download（验证码门槛 → artUrl 浏览器下载）
  6. 报告 + 飞书推送：markdown 变更报告，有新增时推送到 hermes 飞书频道

用法示例:
  # 首次建立基线（只扫描不报告新增）
  python yiigle_tracker.py --keywords "指南,共识,标准" --out-dir ./tracker_out
  # 定时追踪（cron 每天跑）：新增即报告+推送
  python yiigle_tracker.py --keywords "指南,共识,标准" --journals "中华内科杂志" \
      --out-dir ./tracker_out --notify
  # 只看儿科优先，最多每词 20 条
  python yiigle_tracker.py --keywords "指南" --max 20 --out-dir ./tracker_out

cron 示例（每天 08:00）:
  0 8 * * * cd /path/to/cn-med-oa && python3 scripts/yiigle_tracker.py \
      --keywords "指南,共识,标准" --journals "中华内科杂志,中华儿科杂志" \
      --out-dir ./tracker_out --notify >> tracker_cron.log 2>&1

合规铁律（继承 cn_med_oa）:
  - 不碰付费/登录墙：PDF 有验证码门槛时不硬闯，给 artUrl 浏览器下载
  - 控频：检索/下载间隔 ≥3s（复用 _throttle）
  - 相关性透明：只标记不隐藏，报告如实展示状态
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
import cn_med_oa as m  # 复用 yiigle_search / yiigle_try_download / _throttle / _decode_ssr_escapes

VERSION = "1.0.0"

# 默认追踪关键词与文献类型
DEFAULT_KEYWORDS = ["指南", "共识", "标准"]
DEFAULT_DOC_TYPES = ("指南", "共识", "标准", "规范", "建议")
# 儿科优先关键词（标题命中即置顶 + 🧒 标记）
PEDIATRIC_PATTERNS = [
    "儿童", "小儿", "儿科", "新生儿", "婴幼儿", "婴儿", "患儿", "学龄", "青少年",
    "早产儿", "围产", "胎儿", "母乳", "疫苗接种", "预防接种", "生长发育", "青春期",
]
_PED_RE = re.compile("|".join(PEDIATRIC_PATTERNS))


def ped_score(title, journal=""):
    """儿科相关度：标题或期刊名命中儿科关键词个数（0=无关）。

    期刊名命中同样计入（如 中华小儿外科杂志/中国实用儿科杂志 是儿科期刊，
    即使标题未含儿科词也应优先）。
    """
    hits = 0
    for s in (title, journal):
        if not s:
            continue
        hits += len([p for p in PEDIATRIC_PATTERNS if p in s])
    return hits


def doc_type_ok(row):
    """文献类型过滤：docType 或标题含 指南/共识/标准 等。"""
    dt = (row.get("docType") or "").strip()
    title = row.get("title") or ""
    if any(k in dt for k in DEFAULT_DOC_TYPES):
        return True
    return any(k in title for k in DEFAULT_DOC_TYPES)


def load_state(path):
    """读取追踪状态（已见文献 ID 集合）。"""
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"seen": {}, "last_run": ""}


def save_state(path, state):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)
    os.replace(tmp, path)


def scan_keyword(keyword, max_results, journals=None):
    """扫描单个关键词：多翻页收集最新文献（复用 yiigle_search + 节流）。

    流程：收集（最多 5 页 100 条）→ docType 过滤 → 期刊过滤 → 儿科优先排序 → 截断。
    返回过滤后 rows（含儿科标记 _ped）。
    """
    rows = []
    for page in range(1, 6):
        got, err = m.yiigle_search(keyword, page=page, size=20)
        if err or not got:
            break
        m._throttle()  # 控频 ≥3s
        for r in got:
            r["_ped"] = ped_score(r.get("title") or "", r.get("journal") or "")
            rows.append(r)
        if len(got) < 20:
            break
    rows = [r for r in rows if doc_type_ok(r)]
    if journals:
        rows = journal_filter(rows, journals)
    rows.sort(key=lambda r: r["_ped"], reverse=True)  # 儿科优先
    return rows[:max_results]


def journal_filter(rows, journals):
    """按期刊名过滤（含模糊匹配：目标刊名出现在结果刊名中即可）。"""
    if not journals:
        return rows
    out = []
    for r in rows:
        jn = r.get("journal") or ""
        if any(j in jn or jn in j for j in journals):
            out.append(r)
    return out


def report_new(new_rows, keyword, journals):
    """把新增文献追加到报告 lines。返回 (lines, n)。"""
    lines = []
    n = 0
    for r in new_rows:
        n += 1
        ped = "🧒 " if r.get("_ped") else ""
        dt = (r.get("docType") or "文献")
        vol = r.get("vol") or ""
        iss = r.get("issue") or ""
        vi = f"{vol}({iss})" if vol else ""
        jn = r.get("journal") or ""
        lines.append(f"{n}. {ped}**{r.get('title') or '无标题'}**")
        seg = f"   - {jn} {r.get('year') or ''}{(';' + vi) if vi else ''} [{dt}]"
        if r.get("artDoi"):
            seg += f" DOI: {r['artDoi']}"
        lines.append(seg)
        if r.get("artUrl"):
            lines.append(f"   - 阅读: {r['artUrl']}")
        if r.get("download"):
            lines.append(f"   - 下载: ✅ {r['download']}")
        elif r.get("download_url"):
            lines.append(f"   - 下载: 🔗 {r['download_url']}")
        elif r.get("download_error"):
            lines.append(f"   - 下载: ❌ {r['download_error']}")
        lines.append("")
    return lines, n


def try_download(row, out_dir):
    """best-effort 下载新增文献 PDF（复用 yiigle_try_download，失败给 artUrl）。"""
    art_id = row.get("id")
    title = row.get("title") or ""
    if not art_id or not title:
        return
    path, sha = m.yiigle_try_download(art_id, out_dir, title)
    if path:
        row["download"] = os.path.basename(path) + (f" ({sha[:8]})" if sha else "")
    else:
        # 登录墙/验证码 → artUrl 供浏览器下载（不硬闯）
        row["download_url"] = row.get("artUrl") or ""
        row["download_error"] = "登录墙/验证码，请浏览器打开阅读链接"


def send_feishu(text_path):
    """推送文件内容到 hermes 飞书频道（复用 feishu-send 通道：192.168.3.82）。

    通道固定：ubsea@192.168.3.82 的 hermes 飞书企业应用，凭证在 ~/.hermes/.env。
    返回 (ok, msg)。
    """
    try:
        # 1) 传 payload 到 .82
        scp = subprocess.run(
            ["scp", "-o", "StrictHostKeyChecking=no", "-o", "ConnectTimeout=8",
             text_path, "ubsea@192.168.3.82:/tmp/yiigle_tracker_report.txt"],
            capture_output=True, timeout=30)
        if scp.returncode != 0:
            return False, "scp 失败: " + scp.stderr.decode(errors="ignore")[:120]
        # 2) 在 .82 上发送（脚本经 stdin 传入，避免引号嵌套坑）
        send_sh = r'''#!/usr/bin/env bash
set -e
export PATH="$HOME/.local/bin:/usr/bin:/bin:$PATH"
set -a; source ~/.hermes/.env; set +a
TOKEN=$(curl -s -X POST "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal" \
  -H "Content-Type: application/json" \
  -d "{\"app_id\":\"$FEISHU_APP_ID\",\"app_secret\":\"$FEISHU_APP_SECRET\"}" \
  | grep -o '"tenant_access_token":"[^"]*"' | cut -d'"' -f4)
[ -z "$TOKEN" ] && echo "token 获取失败" && exit 1
python3 - "$TOKEN" "$FEISHU_HOME_CHANNEL" << 'PYEOF'
import json, sys, urllib.request
token, chat_id = sys.argv[1], sys.argv[2]
text = open("/tmp/yiigle_tracker_report.txt", encoding="utf-8").read()
body = json.dumps({"receive_id": chat_id, "msg_type": "text",
                   "content": json.dumps({"text": text}, ensure_ascii=False)}).encode()
req = urllib.request.Request(
    "https://open.feishu.cn/open-apis/im/v1/messages?receive_id_type=chat_id",
    data=body, method="POST",
    headers={"Authorization": "Bearer " + token, "Content-Type": "application/json"})
with urllib.request.urlopen(req, timeout=20) as r:
    ok = json.load(r).get("code") == 0
sys.exit(0 if ok else 1)
PYEOF
'''
        ssh = subprocess.run(
            ["ssh", "-o", "StrictHostKeyChecking=no", "-o", "ConnectTimeout=8",
             "ubsea@192.168.3.82", "bash -s"],
            input=send_sh.encode(), capture_output=True, timeout=60)
        if ssh.returncode != 0:
            return False, "发送失败: " + ssh.stderr.decode(errors="ignore")[:120]
        return True, "已推送飞书"
    except Exception as e:
        return False, "飞书推送异常: " + str(e)[:120]


def main():
    ap = argparse.ArgumentParser(description="yiigle 指南/共识/标准 定时追踪下载（儿科优先）")
    ap.add_argument("--keywords", default=",".join(DEFAULT_KEYWORDS),
                    help="追踪关键词，逗号分隔（默认: 指南,共识,标准）")
    ap.add_argument("--journals", default="", help="期刊过滤（逗号分隔），如 中华内科杂志,中华儿科杂志")
    ap.add_argument("--max", type=int, default=15, help="每关键词最多收集条数（默认 15）")
    ap.add_argument("--out-dir", default="./tracker_out", help="PDF/报告输出目录")
    ap.add_argument("--state", default="", help="状态文件路径（默认 <out-dir>/tracker_state.json）")
    ap.add_argument("--no-download", action="store_true", help="只追踪不下载 PDF")
    ap.add_argument("--notify", action="store_true", help="有新增时推送飞书")
    ap.add_argument("--version", action="version", version=f"yiigle_tracker {VERSION}")
    args = ap.parse_args()

    out_dir = os.path.abspath(args.out_dir)
    os.makedirs(out_dir, exist_ok=True)
    state_path = args.state or os.path.join(out_dir, "tracker_state.json")
    state = load_state(state_path)
    seen = state.setdefault("seen", {})
    keywords = [k.strip() for k in args.keywords.split(",") if k.strip()]
    journals = [j.strip() for j in args.journals.split(",") if j.strip()]

    report_lines = [f"# yiigle 指南/共识/标准 追踪报告",
                    f"- 时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                    f"- 关键词: {', '.join(keywords)}" + (f" | 期刊过滤: {', '.join(journals)}" if journals else ""),
                    ""]
    total_new = 0
    all_new_rows = []
    first_run = not state.get("last_run")

    for kw in keywords:
        rows = scan_keyword(kw, args.max, journals)
        if not rows:
            report_lines.append(f"## 「{kw}」 无匹配文献")
            report_lines.append("")
            continue
        key = f"kw:{kw}|jn:{','.join(journals)}"
        seen_ids = set(seen.get(key, []))
        new_rows = []
        for r in rows:
            rid = r.get("id") or (r.get("artDoi") or r.get("title"))
            if rid not in seen_ids:
                seen_ids.add(rid)
                new_rows.append(r)
        seen[key] = sorted(seen_ids)
        if new_rows and not first_run:
            m._throttle()
            if not args.no_download:
                for r in new_rows:
                    try_download(r, out_dir)
            sec, n = report_new(new_rows, kw, journals)
            report_lines.append(f"## 「{kw}」 新增 {n} 条" + ("（儿科优先置顶 🧒）" if any(r.get("_ped") for r in new_rows) else ""))
            report_lines.append("")
            report_lines += sec
            total_new += n
            all_new_rows += new_rows
        elif first_run:
            report_lines.append(f"## 「{kw}」 基线已建立（{len(seen_ids)} 条已见，下次起报告新增）")
            report_lines.append("")

    state["last_run"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_state(state_path, state)

    if first_run and total_new == 0:
        report_lines.append("> 首次运行：仅建立基线，不报告新增（下次运行起 diff 新增）。")
        report_lines.append("")

    report_path = os.path.join(out_dir, "tracker_report.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))
    print("\n".join(report_lines))
    print(f"\n报告: {report_path} | 状态: {state_path}")

    if args.notify and total_new > 0:
        ok, msg = send_feishu(report_path)
        print(msg)


if __name__ == "__main__":
    main()