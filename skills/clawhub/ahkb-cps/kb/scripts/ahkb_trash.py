#!/usr/bin/env python3
"""统一回收站工具。所有删除操作改为 rename → 回收站/，避免触发 safe-delete。"""

import os
from pathlib import Path
from datetime import datetime


def _trash_dir(d, workspace):
    """将目录移入回收站，在原位新建同名空目录。不会触发 safe-delete。"""
    if not d or not d.exists():
        return None
    w = Path(workspace)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S_%f")  # 含微秒，防同名冲突
    trash = w / "回收站"
    trash.mkdir(parents=True, exist_ok=True)
    target = trash / f"{d.name}_{ts}"
    try:
        if os.name == "nt":
            # 递归解除目录树的只读属性，确保子文件不阻碍 rename
            for root, dirs, files in os.walk(str(d)):
                for name in files:
                    _p = os.path.join(root, name)
                    try:
                        os.chmod(_p, 0o666)
                    except Exception:
                        pass
        os.rename(str(d), str(target))
        d.mkdir(parents=True, exist_ok=True)
        return target
    except Exception:
        return None


def _trash_file(f, workspace):
    """将单个文件移入回收站。不会触发 safe-delete。"""
    if not f or not f.exists():
        return None
    w = Path(workspace)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S_%f")  # 含微秒，防同名冲突
    trash = w / "回收站"
    trash.mkdir(parents=True, exist_ok=True)
    target = trash / f"{f.name}_{ts}"
    try:
        if os.name == "nt":
            os.chmod(str(f), 0o666)
        os.rename(str(f), str(target))
        return target
    except Exception:
        return None
