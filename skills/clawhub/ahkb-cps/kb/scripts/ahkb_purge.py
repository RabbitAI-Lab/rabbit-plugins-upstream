#!/usr/bin/env python3
"""ahkb_purge.py - Purge all knowledge units and resource files (fast, rename-to-trash)."""
import argparse, json, sys, os, subprocess
from pathlib import Path

# 终端 UTF-8 支持（跨平台安全）
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding='utf-8')
    except Exception:
        pass
if sys.platform == "win32":
    try:
        subprocess.run(["chcp", "65001"], capture_output=True, timeout=2)
    except Exception:
        pass

from ahkb_trash import _trash_dir, _trash_file

def find_workspace():
    cwd = Path.cwd().resolve()
    for p in [cwd] + list(cwd.parents):
        if (p / "知识元").exists() or (p / "原始文件").exists():
            return p
    return cwd


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--workspace")
    a = p.parse_args()
    ws = Path(a.workspace).resolve() if a.workspace else find_workspace()
    if not ws.exists():
        print(json.dumps({"error": f"workspace not found: {ws}"})); sys.exit(1)
    sd = Path(__file__).resolve().parent.parent
    if ws == sd or sd in ws.parents:
        print(json.dumps({"error": "skill directory is not allowed as workspace"})); sys.exit(1)

    dl = {"knowledge_units": 0, "resources": 0, "chunks": 0, "root_node": None, "html_map": 0, "manifest": False}
    err = []

    # 1. 知识元/ — rename 到回收站
    kd = ws / "知识元"
    if kd.exists():
        if _trash_dir(kd, ws) is None:
            err.append(f"知识元: 移入回收站失败（可能被占用）")
    dl["knowledge_units"] = "all"

    # 2. 图片及其他资源/ — rename 到回收站
    rb = ws / "图片及其他资源"
    if rb.exists():
        if _trash_dir(rb, ws) is None:
            err.append(f"图片及其他资源: 移入回收站失败（可能被占用）")
    dl["resources"] = "all"

    # 3. chunks/ — rename 到回收站
    chunks_dir = ws / "chunks"
    if chunks_dir.exists():
        if _trash_dir(chunks_dir, ws) is None:
            err.append(f"chunks: 移入回收站失败（可能被占用）")
    dl["chunks"] = "all"

    # 4. 根节点 .md（文件名含"(根)"的全部移入回收站）
    for f in ws.iterdir():
        if f.suffix.lower() == ".md" and "(根)" in f.name:
            result = _trash_file(f, ws)
            if result:
                dl["root_node"] = f.name
            else:
                err.append(f"根节点: {f.name} 被占用，无法移入回收站")

    # 5. 知识地图 HTML（*-知识地图.html）— rename 到回收站
    html_cleared = 0
    for f in ws.glob("*知识地图.html"):
        _trash_file(f, ws)
        html_cleared += 1
    dl["html_map"] = html_cleared

    # 6. _processed_docs.json — rename 到回收站
    for mf in [ws / "原始文件" / "_processed_docs.json", ws / "_processed_docs.json"]:
        if mf.exists():
            _trash_file(mf, ws)
            dl["manifest"] = True
            break

    # 7. 临时工作文件 — rename 到回收站
    for d in [ws / "临时工作文件"]:
        _trash_dir(d, ws)

    rs = {"ok": len(err) == 0, "deleted": dl}
    if err:
        rs["errors"] = err
    print(json.dumps(rs, ensure_ascii=False))

if __name__ == "__main__":
    main()
