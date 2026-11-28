"""从本机已登录的薇芯 4.x 进程内存中提取各数据库的 SQLCipher 密钥（仅限本人账号、本人设备）。"""
import ctypes
import json
import re
import sys
from ctypes import wintypes
from pathlib import Path

import psutil

from decrypt import PAGE_SIZE, read_salt, verify_key

# 薇芯 4.x 在内存里保留 WCDB 原始密钥串：x'<64位hex密钥><32位hex盐>'
KEY_RE = re.compile(rb"x'([0-9a-fA-F]{64})([0-9a-fA-F]{32})'")

PROCESS_QUERY_INFORMATION = 0x0400
PROCESS_VM_READ = 0x0010
MEM_COMMIT = 0x1000
READABLE = {0x02, 0x04, 0x08, 0x20, 0x40, 0x80}  # PAGE_READONLY / READWRITE / WRITECOPY / EXECUTE_*


class MBI(ctypes.Structure):
    _fields_ = [
        ("BaseAddress", ctypes.c_void_p), ("AllocationBase", ctypes.c_void_p),
        ("AllocationProtect", wintypes.DWORD), ("PartitionId", wintypes.WORD),
        ("RegionSize", ctypes.c_size_t), ("State", wintypes.DWORD),
        ("Protect", wintypes.DWORD), ("Type", wintypes.DWORD),
    ]


def _scan_process(pid: int):
    k32 = ctypes.windll.kernel32
    k32.OpenProcess.restype = wintypes.HANDLE
    k32.VirtualQueryEx.argtypes = [wintypes.HANDLE, ctypes.c_void_p, ctypes.POINTER(MBI), ctypes.c_size_t]
    k32.ReadProcessMemory.argtypes = [wintypes.HANDLE, ctypes.c_void_p, ctypes.c_void_p,
                                      ctypes.c_size_t, ctypes.POINTER(ctypes.c_size_t)]
    h = k32.OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, pid)
    if not h:
        return
    try:
        addr = 0
        mbi = MBI()
        while k32.VirtualQueryEx(h, addr, ctypes.byref(mbi), ctypes.sizeof(mbi)):
            base, size = mbi.BaseAddress or 0, mbi.RegionSize
            if mbi.State == MEM_COMMIT and (mbi.Protect & 0xFF) in READABLE and size < 512 * 1024 * 1024:
                buf = ctypes.create_string_buffer(size)
                n = ctypes.c_size_t()
                if k32.ReadProcessMemory(h, base, buf, size, ctypes.byref(n)) and n.value:
                    for m in KEY_RE.finditer(buf.raw[: n.value]):
                        yield bytes.fromhex(m.group(1).decode()), bytes.fromhex(m.group(2).decode())
            addr = base + size
    finally:
        k32.CloseHandle(h)


def extract_keys(db_dir: Path) -> dict[str, str]:
    """返回 {相对路径: 密钥hex}，只保留经 HMAC 校验通过的密钥。"""
    dbs = {}
    for p in db_dir.rglob("*.db"):
        try:
            with open(p, "rb") as f:
                head = f.read(PAGE_SIZE)
            if len(head) == PAGE_SIZE and not head.startswith(b"SQLite format 3"):
                dbs[p] = head
        except OSError:
            continue

    candidates = {}
    for proc in psutil.process_iter(["pid", "name"]):
        if (proc.info["name"] or "").lower() == "weixin.exe":
            for key, salt in _scan_process(proc.info["pid"]):
                candidates[(key, salt)] = True

    result = {}
    for p, head in dbs.items():
        salt = head[:16]
        for (key, s) in candidates:
            if s == salt and verify_key(key, head):
                result[str(p.relative_to(db_dir)).replace("\\", "/")] = key.hex()
                break
    return result


if __name__ == "__main__":
    db_dir = Path(sys.argv[1])
    keys = extract_keys(db_dir)
    print(f"verified keys: {len(keys)}")
    for rel in sorted(keys):
        print("  ", rel)
    out = Path(__file__).with_name("keys.json")
    out.write_text(json.dumps(keys, indent=2), encoding="utf-8")
    print("saved ->", out)
