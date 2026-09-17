#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
export_package.py —— 实现「导出」动词的底层机械步骤

用法（由 SKILL.md 的「导出」动词调用，推荐让 LLM 先确定节点与产物清单后传参）:
    python export_package.py --nodes R0-A2 --scope subtree \
        [--artifacts "E:/projA/src/app.py,E:/projA/output/report.md"] \
        [--workspace E:/projA] [--out D:/exports]

    # 便捷模式：只给一个节点 + 范围，脚本从 INDEX/handoff 自动收集
    python export_package.py --node R0-A2 --scope subtree [--workspace ...] [--out ...]

产物来源（合并去重）：
    1. INDEX 会话地图中选中节点的「产物清单」列（机器可解析的分号分隔路径）——主来源
    2. --artifacts 显式追加（临时补充）
    3. 从 handoff 文档文本启发式捞路径（兜底）

落位规则（artifact_relpath）：
    - 同盘且在 workspace 之内 → 相对路径（artifacts/<rel>）
    - 工作空间之外（跨盘或跨目录）→ artifacts/_external/<盘符>/<原路径>
      杜绝 os.path.relpath 的跨盘 ValueError 与 .. 逃逸。
    技能自身文件（.workbuddy/skills/ 或 .workbuddy/plugins/ 下）一律跳过并告警，不迁移。

包内容：
    1. INDEX.excerpt.md（选中节点所在地图表摘录）
    2. handoffs/（选中节点引用的交接文档副本）
    3. artifacts/（产物副本，含 _external/ 子目录）
    4. PROVENANCE.json（skill_id/skill_version/exported_by/source_workspace/source_node/
       exported_at/package_content_hash/scope）

原则：复制不移动；包自包含（产物副本随包走）；防污染靠「导入端命名空间落盘」。
"""

import argparse
import datetime
import hashlib
import json
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL_ROOT = os.path.dirname(HERE)
SKILL_ID = "edo-tensei-1fef9b18bc9c451395d4bf85c0814afd"

# 复用 config.py 的配置读取（个人配置在用户主目录，绝不进技能包）
import importlib.util as _ilu
_spec = _ilu.spec_from_file_location("edocfg", os.path.join(HERE, "config.py"))
edocfg = _ilu.module_from_spec(_spec)
_spec.loader.exec_module(edocfg)


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _read_manifest_version() -> str:
    p = os.path.join(SKILL_ROOT, "manifest.yaml")
    if os.path.isfile(p):
        for line in open(p, encoding="utf-8"):
            if line.strip().startswith("version:"):
                return line.split(":", 1)[1].strip().strip('"').strip("'")
    return "1.0.0"


def resolve_export_dir(explicit: str):
    if explicit:
        return os.path.abspath(os.path.expanduser(explicit))
    # 个人配置(~/.edo-tensei/config.yaml) > 出厂默认；绝不读技能包内的个人路径
    return edocfg.get_export_dir()


def _col_index(header, *names):
    """在表头列表中按子串匹配找到列下标；找不到返回 -1。"""
    if not header:
        return -1
    for name in names:
        for i, c in enumerate(header):
            if name in c:
                return i
    return -1


def _parse_session_map(index_text: str):
    """解析「会话地图」表（表头首单元格为「代号」）。
    返回 dict: code -> {'handoff': str, 'artifacts': str}
    跳过依赖表（§1.5）等其他表格，避免代号被重复选中。"""
    lines = index_text.splitlines()
    header = None
    rows = {}
    in_map = False
    for ln in lines:
        s = ln.strip()
        if not s.startswith("|"):
            if in_map:
                break  # 地图表结束（遇到空行/标题等）
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if not in_map:
            if cells and cells[0] == "代号":
                in_map = True
                header = cells
            continue
        if len(cells) < 2:
            continue
        code = cells[0]
        if code in ("", "代号"):
            continue
        hi_h = _col_index(header, "文件名")
        hi_a = _col_index(header, "产物清单", "产物")
        handoff = cells[hi_h] if hi_h >= 0 and hi_h < len(cells) else ""
        arts = cells[hi_a] if hi_a >= 0 and hi_a < len(cells) else ""
        rows[code] = {"handoff": handoff, "artifacts": arts}
    return rows


def find_nodes(index_text: str, node: str, scope: str):
    """返回 (selected_codes:list[去重], index_excerpt:str)。按会话地图表首列代号匹配。"""
    rows = _parse_session_map(index_text)
    codes = list(rows.keys())
    if scope == "single":
        selected = [c for c in codes if c == node]
    elif scope == "subtree":
        selected = [c for c in codes if c == node or c.startswith(node + "-")]
    else:  # whole：整塔全部节点
        selected = [c for c in codes if c]
    # 去重保序
    seen = set()
    selected = [c for c in selected if not (c in seen or seen.add(c))]
    if not selected and scope != "whole":
        # 兼容：若 node 不在地图表，退回全文件首列启发式（极少用）
        for ln in index_text.splitlines():
            s = ln.strip()
            if s.startswith("|"):
                c = s.strip("|").split("|")[0].strip()
                if c and c != "代号":
                    selected.append(c)
    return selected, index_text


def is_skill_own_file(p: str) -> bool:
    """技能自身文件（安装即得，不应随项目导出迁移）。"""
    p = os.path.abspath(p).replace("\\", "/").lower()
    return "/.workbuddy/skills/" in p or "/.workbuddy/plugins/" in p


def artifact_relpath(src: str, ws: str) -> str:
    """返回包内相对 artifacts/ 的落位路径。
    同盘且在 workspace 内 → 相对路径；否则 → _external/<盘符>/<原路径>
    （防跨盘 ValueError 与 .. 逃逸）。"""
    src = os.path.abspath(src)
    ws_a = os.path.abspath(ws)
    sd, srest = os.path.splitdrive(src)
    wd, _ = os.path.splitdrive(ws_a)
    if sd.lower() == wd.lower():
        try:
            rel = os.path.relpath(src, ws_a)
            if not rel.startswith(".."):
                return rel
        except ValueError:
            pass
    # 工作空间之外：_external/<盘符>/<路径>，完整保留来源、绝不产生 ..
    drive = sd.rstrip(":").upper() or "_root"
    rest = srest.lstrip(os.sep).lstrip("/")
    return os.path.join("_external", drive, rest)


def collect_artifacts_from_index(map_rows: dict, selected, ws: str):
    """解析选中节点的「产物清单」列（分号/中文逗号/换行分隔），返回 (found, warnings)。"""
    found = []
    warns = []
    for code in selected:
        raw = map_rows.get(code, {}).get("artifacts", "")
        if not raw:
            continue
        for tok in re.split(r"[;；\n]", raw):
            tok = tok.strip().strip('`"\'')
            if not tok:
                continue
            cand = tok if os.path.isabs(tok) else os.path.join(ws, tok)
            cand = os.path.abspath(cand)
            if is_skill_own_file(cand):
                warns.append(f"[跳过-技能文件] {code}: {tok} 属于技能自身文件，不迁移")
                continue
            if os.path.isfile(cand):
                found.append(cand)
            else:
                warns.append(f"[缺失-已忽略] {code}: {tok} 不存在")
    return found, warns


def collect_artifacts_heuristic(handoff_paths, workspace):
    """从 handoff 文档文本里捞看起来像文件路径、且在磁盘上存在的条目。
    技能自身文件会被过滤。"""
    found = []
    for hp in handoff_paths:
        if not os.path.isfile(hp):
            continue
        for line in open(hp, encoding="utf-8", errors="ignore"):
            for tok in line.replace("(", " ").replace(")", " ").split():
                tok = tok.strip('`"\'')
                if ("/" in tok or "\\" in tok) and tok.endswith((
                        ".py", ".md", ".json", ".png", ".jpg", ".jpeg",
                        ".txt", ".html", ".csv", ".xlsx", ".zip", ".png")):
                    cand = tok
                    if not os.path.isabs(cand):
                        cand = os.path.join(workspace, cand)
                    cand = os.path.abspath(cand)
                    if os.path.isfile(cand) and not is_skill_own_file(cand):
                        found.append(cand)
    return found


def _gen_context_digest(index_text: str, handoffs_src, selected) -> str:
    """full 深度时，从 INDEX 摘录 + 交接文档提炼关键上下文块（决策/依赖/风险/下一步等）。"""
    key_hdr = ("决策", "依赖", "风险", "坑", "下一步", "关键", "设计", "结论", "要点")
    blocks = []
    for hp in handoffs_src:
        if not os.path.isfile(hp):
            continue
        txt = open(hp, encoding="utf-8", errors="ignore").read()
        cur, in_block = [], False
        for line in txt.splitlines():
            if line.startswith("#"):
                if any(k in line for k in key_hdr):
                    if in_block and cur:
                        blocks.append("\n".join(cur))
                    in_block, cur = True, [line]
                else:
                    if in_block and cur:
                        blocks.append("\n".join(cur))
                    in_block = False
            elif in_block:
                cur.append(line)
        if in_block and cur:
            blocks.append("\n".join(cur))
    if not blocks:  # 兜底：取每个 handoff 前 50 行
        for hp in handoffs_src:
            if not os.path.isfile(hp):
                continue
            txt = open(hp, encoding="utf-8", errors="ignore").read()
            blocks.append("\n".join(txt.splitlines()[:50]))
    head = ("# 上下文浓缩摘要（CONTEXT_DIGEST，深度=full）\n\n"
            f"- 来源节点: {', '.join(selected)}\n"
            "- 生成自: INDEX 摘录 + 交接文档关键节（决策/依赖/风险/下一步等）\n\n---\n\n")
    return head + "\n\n".join(blocks)


def verify_export_zip(zip_path: str, expected: dict) -> bool:
    """打包后自校验：重算 zip 内文件哈希与 PROVENANCE.files 比对，打印 PASS/FAIL。"""
    import zipfile
    try:
        with zipfile.ZipFile(zip_path) as z:
            names = set(z.namelist())
        bad, miss = [], []
        for rel, exp in expected.items():
            if rel not in names:
                miss.append(rel); continue
            with zipfile.ZipFile(zip_path) as z:
                data = z.read(rel)
            if hashlib.sha256(data).hexdigest() != exp:
                bad.append(rel)
        if "PROVENANCE.json" not in names:
            miss.append("PROVENANCE.json")
        ok = not bad and not miss
        print(f"[校验] {'PASS ✓' if ok else 'FAIL ✗'} 文件数={len(expected)}"
              + (f" 异常={bad + miss}" if not ok else ""))
        return ok
    except Exception as e:
        print(f"[校验] 跳过（zip 读取失败: {e}）")
        return False


def main():
    ap = argparse.ArgumentParser(description="秽土转生 · 导出包")
    ap.add_argument("--nodes", help="逗号分隔的选中节点代号（推荐，LLM 已确定）")
    ap.add_argument("--node", help="便捷模式：单个节点代号，结合 --scope 启发式选后代")
    ap.add_argument("--scope", default="subtree", choices=["single", "subtree", "whole"])
    ap.add_argument("--artifacts", help="逗号分隔的额外产物文件路径（追加，不覆盖 INDEX 列）")
    ap.add_argument("--workspace", default=os.getcwd(), help="源工作空间根目录")
    ap.add_argument("--out", help="显式指定导出目录（最高优先级）")
    ap.add_argument("--verify", action="store_true", default=True,
                    help="打包后自校验（默认开）：重算 zip 内文件哈希与 PROVENANCE.files 比对，打印 PASS/FAIL，省去单独校验调用")
    ap.add_argument("--no-verify", dest="verify", action="store_false",
                    help="关闭打包后自校验")
    args = ap.parse_args()

    ws = os.path.abspath(args.workspace)
    ct = os.path.join(ws, ".workbuddy", "control-tower")
    index_path = os.path.join(ct, "INDEX.md")
    if not os.path.isfile(index_path):
        print(f"[错误] 未找到 INDEX.md: {index_path}（请先在该工作空间跑 转生/接管 建塔）")
        sys.exit(1)

    index_text = open(index_path, encoding="utf-8").read()
    if args.nodes:
        selected = [c.strip() for c in args.nodes.split(",") if c.strip()]
        excerpt = index_text
    else:
        if not args.node:
            print("[错误] 需提供 --nodes 或 --node")
            sys.exit(1)
        selected, excerpt = find_nodes(index_text, args.node, args.scope)

    if not selected:
        print("[错误] 未选中任何节点")
        sys.exit(1)

    # 解析会话地图（含 handoff 与产物清单列）
    map_rows = _parse_session_map(index_text)

    # 收集 handoff：按会话地图表「文件名」列定位真实交接文档；懒生成/占位行跳过
    handoffs_src = []
    for code in selected:
        field = map_rows.get(code, {}).get("handoff", "")
        fname = field.replace("handoffs/", "").strip()
        if not fname.endswith(".md"):
            continue  # （懒生成）/ 占位，无实际交接文档
        cand = os.path.join(ct, "handoffs", fname)
        if os.path.isfile(cand):
            handoffs_src.append(cand)
            continue
        alt = os.path.join(ct, "handoffs", f"{code}.md")  # 兜底命名
        if os.path.isfile(alt):
            handoffs_src.append(alt)
    handoffs_src = sorted(set(handoffs_src))

    # 收集产物（三源合并去重，均经 技能文件拦截 + 安全落位）
    idx_arts, warns = collect_artifacts_from_index(map_rows, selected, ws)
    extra = []
    if args.artifacts:
        for p in args.artifacts.split(","):
            p = p.strip()
            if not p:
                continue
            cand = os.path.abspath(p)
            if is_skill_own_file(cand):
                warns.append(f"[跳过-技能文件] --artifacts: {p} 属于技能自身文件，不迁移")
                continue
            if os.path.isfile(cand):
                extra.append(cand)
            else:
                warns.append(f"[缺失-已忽略] --artifacts: {p} 不存在")
    heur = collect_artifacts_heuristic(handoffs_src, ws)
    artifacts = sorted(set(idx_arts + extra + heur))

    # 建暂存
    ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    stage = os.path.join(ct, f"_export_stage_{ts}")
    os.makedirs(os.path.join(stage, "handoffs"), exist_ok=True)
    os.makedirs(os.path.join(stage, "artifacts"), exist_ok=True)

    excerpt_path = os.path.join(stage, "INDEX.excerpt.md")
    with open(excerpt_path, "w", encoding="utf-8") as f:
        f.write(excerpt)

    file_hashes = {}
    file_hashes["INDEX.excerpt.md"] = sha256_file(excerpt_path)
    for hp in handoffs_src:
        dest = os.path.join(stage, "handoffs", os.path.basename(hp))
        shutil.copy2(hp, dest)
        file_hashes["handoffs/" + os.path.basename(hp)] = sha256_file(dest)
    external_count = 0
    for apath in artifacts:
        rel = artifact_relpath(apath, ws)
        if rel.replace(os.sep, "/").startswith("_external/"):
            external_count += 1
        dest = os.path.join(stage, "artifacts", rel)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copy2(apath, dest)
        file_hashes["artifacts/" + rel.replace(os.sep, "/")] = sha256_file(dest)

    # 上下文深度：full 时额外生成 CONTEXT_DIGEST.md（关键决策/依赖/风险浓缩）
    depth = edocfg.get_context_depth()
    if depth == "full":
        digest = _gen_context_digest(index_text, handoffs_src, selected)
        digest_path = os.path.join(stage, "CONTEXT_DIGEST.md")
        with open(digest_path, "w", encoding="utf-8") as f:
            f.write(digest)
        file_hashes["CONTEXT_DIGEST.md"] = sha256_file(digest_path)

    # PROVENANCE
    # 复合哈希（防篡改速检）+ 逐文件清单（导入端无需猜算法即可逐文件校验）
    concat = "".join(file_hashes[k] for k in sorted(file_hashes))
    pkg_hash = hashlib.sha256(concat.encode("utf-8")).hexdigest()
    prov = {
        "skill_id": SKILL_ID,
        "skill_version": _read_manifest_version(),
        "exported_by": os.environ.get("EDO_EXPORTED_BY", "local-user"),
        "source_workspace": os.path.basename(ws),
        "source_node": ",".join(selected),
        "exported_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "package_content_hash": pkg_hash,
        "hash_algorithm": (
            "package_content_hash = SHA-256( ''.join(file_hashes[path] for path in sorted(file_hashes)) ); "
            "其中 file_hashes[path] = SHA-256(file bytes).hexdigest()（十六进制字符串）。"
            "即：先对包内每个内容文件算 SHA-256 取 hex 串，按 path 字典序排序后将这些 hex 串直接拼接，"
            "再对拼接串整体做一次 SHA-256（注意：是 hex 字符串拼接，不是摘要二进制字节拼接）。"
            "仅对包内内容文件计哈希，不含本 PROVENANCE.json；导入端应优先用下方 files 清单做逐文件校验。"
        ),
        "files": file_hashes,  # path(包内相对路径) -> sha256，导入端逐文件比对
        "scope": args.scope,
        "note": "本 PROVENANCE 仅记录本次导出事件溯源；导出包为复制不移动。",
    }
    with open(os.path.join(stage, "PROVENANCE.json"), "w", encoding="utf-8") as f:
        json.dump(prov, f, ensure_ascii=False, indent=2)

    # 打包
    out_dir = resolve_export_dir(args.out)
    os.makedirs(out_dir, exist_ok=True)
    zip_name = f"{os.path.basename(ws)}-{'-'.join(selected)[:40]}-{ts}.zip"
    zip_path = os.path.join(out_dir, zip_name)
    shutil.make_archive(zip_path[:-4], "zip", stage)
    if args.verify:
        verify_export_zip(zip_path, file_hashes)
    shutil.rmtree(stage, ignore_errors=True)

    for w in warns:
        print("[提示]", w)
    print(f"[OK] 已导出: {zip_path}")
    print(f"     节点: {', '.join(selected)}")
    print(f"     handoff: {len(handoffs_src)} 个, 产物副本: {len(artifacts)} 个"
          + (f"（其中工作空间外 _external: {external_count} 个）" if external_count else ""))
    print(f"     package_content_hash: {pkg_hash[:16]}...")
    used = ('显式 --out' if args.out
            else ('个人配置 ~/.edo-tensei/config.yaml' if os.path.isfile(edocfg.USER_CONFIG)
                  else '出厂默认 ~/.edo-tensei/exports'))
    print(f"     落地目录来源: {used}")
    print(f"     context_depth: {depth}（full 时包内含 CONTEXT_DIGEST.md）")


if __name__ == "__main__":
    main()
