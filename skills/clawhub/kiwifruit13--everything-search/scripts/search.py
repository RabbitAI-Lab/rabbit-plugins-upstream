#!/usr/bin/env python3
"""Everything 本地文件搜索引擎 - 极简脚本。

职责：仅负责调用 Everything 引擎（IPC 或 CLI），返回结构化 JSON。
搜索策略、查询构造、结果解读由智能体根据 SKILL.md 指导完成。
"""

from __future__ import annotations

import argparse
import ctypes
import csv
import json
import subprocess
import sys
import time
from ctypes import CDLL, POINTER, byref, c_bool, c_int64, c_uint, c_wchar_p
from datetime import datetime, timedelta, timezone
from io import StringIO
from pathlib import Path
from typing import List, Optional, Tuple

# 路径配置
_BASE = Path(__file__).resolve().parent.parent
_DLL_PATH = _BASE / "assets" / "Everything64.dll"
_ES_EXE = _BASE / "assets" / "es.exe"
_BUNDLED_EXE = _BASE / "assets" / "everything" / "Everything.exe"

# Everything IPC 请求标志
_REQ_FULL_PATH = 0x00000004
_REQ_SIZE = 0x00000010
_REQ_DATE_MODIFIED = 0x00000040

# Windows FILETIME 纪元
_EPOCH_1601 = datetime(1601, 1, 1, tzinfo=timezone.utc)


class _FILETIME(ctypes.Structure):
    _fields_ = [("dwLowDateTime", c_uint), ("dwHighDateTime", c_uint)]


def filetime_to_dt(ft: _FILETIME) -> Optional[str]:
    """将 Windows FILETIME 转换为 ISO 格式字符串。"""
    val = (ft.dwHighDateTime << 32) | ft.dwLowDateTime
    if val == 0:
        return None
    dt = _EPOCH_1601 + timedelta(microseconds=val // 10)
    return dt.strftime("%Y-%m-%d %H:%M:%S")


# ==================== IPC 引擎 ====================

_dll: Optional[CDLL] = None


def load_dll() -> CDLL:
    """加载 Everything64.dll（单例）。"""
    global _dll
    if _dll is not None:
        return _dll
    if not _DLL_PATH.exists():
        raise RuntimeError(f"未找到 Everything64.dll：{_DLL_PATH}")
    try:
        d = CDLL(str(_DLL_PATH))
    except OSError as e:
        raise RuntimeError(f"加载 DLL 失败：{e}")

    # 设置函数签名（宽字符版本，中文安全）
    d.Everything_Reset.argtypes = []
    d.Everything_Reset.restype = None
    d.Everything_SetSearchW.argtypes = [c_wchar_p]
    d.Everything_SetSearchW.restype = None
    d.Everything_SetMax.argtypes = [c_uint]
    d.Everything_SetMax.restype = None
    d.Everything_SetOffset.argtypes = [c_uint]
    d.Everything_SetOffset.restype = None
    d.Everything_SetRequestFlags.argtypes = [c_uint]
    d.Everything_SetRequestFlags.restype = None
    d.Everything_QueryW.argtypes = [c_bool]
    d.Everything_QueryW.restype = c_bool
    d.Everything_GetLastError.argtypes = []
    d.Everything_GetLastError.restype = c_uint
    d.Everything_GetNumResults.argtypes = []
    d.Everything_GetNumResults.restype = c_uint
    d.Everything_GetTotResults.argtypes = []
    d.Everything_GetTotResults.restype = c_uint
    d.Everything_IsFolderResult.argtypes = [c_uint]
    d.Everything_IsFolderResult.restype = c_bool
    d.Everything_GetResultFullPathNameW.argtypes = [c_uint, c_wchar_p, c_uint]
    d.Everything_GetResultFullPathNameW.restype = c_uint
    d.Everything_GetResultSize.argtypes = [c_uint, POINTER(c_int64)]
    d.Everything_GetResultSize.restype = c_bool
    d.Everything_GetResultDateModified.argtypes = [c_uint, POINTER(_FILETIME)]
    d.Everything_GetResultDateModified.restype = c_bool

    _dll = d
    return d


def ipc_available() -> bool:
    """检测 IPC 是否可用。"""
    try:
        d = load_dll()
        d.Everything_Reset()
        d.Everything_SetSearchW("")
        d.Everything_SetMax(1)
        d.Everything_SetRequestFlags(_REQ_FULL_PATH)
        return bool(d.Everything_QueryW(True))
    except Exception:
        return False


def ipc_query(query: str, limit: int, offset: int) -> Tuple[List[dict], int]:
    """通过 IPC 执行查询。"""
    d = load_dll()
    d.Everything_Reset()
    d.Everything_SetSearchW(query)
    d.Everything_SetMax(limit)
    d.Everything_SetOffset(offset)
    d.Everything_SetRequestFlags(_REQ_FULL_PATH | _REQ_SIZE | _REQ_DATE_MODIFIED)

    ok = d.Everything_QueryW(True)
    if not ok:
        err = d.Everything_GetLastError()
        if err == 2:
            raise RuntimeError("Everything 未运行或 IPC 不可达")
        raise RuntimeError(f"查询失败，错误码 {err}")

    total = d.Everything_GetTotResults()
    n = d.Everything_GetNumResults()
    results = []
    buf = ctypes.create_unicode_buffer(4096)
    size_buf = c_int64()
    ft_mod = _FILETIME()

    for i in range(n):
        d.Everything_GetResultFullPathNameW(i, buf, 4096)
        path = buf.value or ""
        is_folder = bool(d.Everything_IsFolderResult(i))
        name = path.rsplit("\\", 1)[-1] if path else ""

        size = None
        if d.Everything_GetResultSize(i, byref(size_buf)):
            size = size_buf.value

        date_modified = None
        if d.Everything_GetResultDateModified(i, byref(ft_mod)):
            date_modified = filetime_to_dt(ft_mod)

        results.append({
            "path": path,
            "name": name,
            "is_folder": is_folder,
            "size": size,
            "date_modified": date_modified,
        })

    return results, total


# ==================== CLI 引擎 ====================

def cli_available() -> bool:
    """检测 es.exe 是否可用。"""
    if not _ES_EXE.exists():
        return False
    try:
        r = subprocess.run(
            [str(_ES_EXE), "", "-n", "1"],
            capture_output=True,
            encoding="gbk",
            errors="replace",
            timeout=15,
        )
        return r.returncode == 0
    except Exception:
        return False


def cli_query(query: str, limit: int, offset: int) -> Tuple[List[dict], int]:
    """通过 es.exe 执行查询。"""
    if not _ES_EXE.exists():
        raise RuntimeError(f"未找到 es.exe：{_ES_EXE}")

    cmd = [str(_ES_EXE), query, "-n", str(limit), "-csv", "-size", "-date-modified"]
    if offset:
        cmd += ["-offset", str(offset)]

    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            encoding="gbk",
            errors="replace",
            timeout=30,
        )
    except subprocess.TimeoutExpired:
        raise RuntimeError("es.exe 查询超时")
    except OSError as e:
        raise RuntimeError(f"启动 es.exe 失败：{e}")

    if proc.returncode != 0:
        raise RuntimeError(f"es.exe 退出码 {proc.returncode}")

    # 解析 CSV 输出
    reader = csv.reader(StringIO(proc.stdout))
    results = []
    header_skipped = False
    for row in reader:
        if not row:
            continue
        if not header_skipped:
            if row[0].strip().lower() == "filename":
                header_skipped = True
                continue
            header_skipped = True

        path = row[0].strip().strip('"').rstrip("\\") if row else ""
        if not path:
            continue

        size = None
        if len(row) > 1 and row[1].strip():
            try:
                size = int(row[1].strip())
            except ValueError:
                pass

        date_modified = None
        if len(row) > 2 and row[2].strip():
            try:
                dt = datetime.strptime(row[2].strip(), "%Y/%m/%d %H:%M:%S")
                date_modified = dt.strftime("%Y-%m-%d %H:%M:%S")
            except ValueError:
                pass

        name = path.rsplit("\\", 1)[-1] if path else ""
        is_folder = path.endswith("\\") or (len(row) > 3 and row[3].strip() and int(row[3]) & 0x10)

        results.append({
            "path": path,
            "name": name,
            "is_folder": is_folder,
            "size": size,
            "date_modified": date_modified,
        })

        if len(results) >= limit:
            break

    return results, len(results)


# ==================== 启动 Everything ====================

def ensure_server(max_wait: int = 20) -> bool:
    """确保 Everything 服务端可达，必要时启动自带 exe。"""
    if ipc_available() or cli_available():
        return True
    if _BUNDLED_EXE.exists():
        try:
            subprocess.Popen(
                [str(_BUNDLED_EXE)],
                creationflags=0x00000008,  # DETACHED_PROCESS
            )
        except Exception:
            return False
        deadline = time.time() + max_wait
        while time.time() < deadline:
            if ipc_available() or cli_available():
                return True
            time.sleep(1)
    return ipc_available() or cli_available()


# ==================== 主入口 ====================

def search(query: str, limit: int = 50, offset: int = 0, engine: str = "auto") -> dict:
    """统一搜索入口。"""
    warning = None

    # 确保服务端可用
    if not ensure_server():
        raise RuntimeError("Everything 服务端不可用，请先启动 Everything")

    # 自动选择引擎
    if engine == "auto":
        if ipc_available():
            results, total = ipc_query(query, limit, offset)
            engine_used = "ipc"
        elif cli_available():
            results, total = cli_query(query, limit, offset)
            engine_used = "cli"
            warning = "已降级到 CLI 引擎"
        else:
            raise RuntimeError("无可用引擎")
    elif engine == "ipc":
        results, total = ipc_query(query, limit, offset)
        engine_used = "ipc"
    elif engine == "cli":
        results, total = cli_query(query, limit, offset)
        engine_used = "cli"
        warning = "CLI 引擎（total 为近似值）"
    else:
        raise ValueError(f"未知引擎：{engine}")

    return {
        "query": query,
        "engine": engine_used,
        "total": total,
        "returned": len(results),
        "results": results,
        "warning": warning,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Everything 本地文件搜索（IPC/CLI 自适应）"
    )
    parser.add_argument("query", help="Everything 查询语法")
    parser.add_argument("-n", "--limit", type=int, default=50, help="返回条数上限")
    parser.add_argument("--offset", type=int, default=0, help="分页偏移")
    parser.add_argument(
        "-e", "--engine",
        choices=["auto", "ipc", "cli"],
        default="auto",
        help="强制引擎"
    )
    args = parser.parse_args()

    try:
        result = search(args.query, args.limit, args.offset, args.engine)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except Exception as e:
        print(json.dumps({"error": str(e)}, ensure_ascii=False), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
