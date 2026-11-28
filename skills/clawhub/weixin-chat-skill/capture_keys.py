"""抓取薇芯 4.x 各数据库的 SQLCipher 密钥（每库一把）。仅限本人设备 / 本人账号。

原理：薇芯 4.x 把 key 混淆存放，内存里找不到明文。但 SQLCipher 打开每个数据库连接时都会调用
Weixin.dll 里（静态链接的 OpenSSL）`aesni_set_encrypt_key` 展开 AES 密钥，入口 RCX 指向 32 字节
原始 key。用 Frida hook 该函数抓取；再用「AES 解 contact.db 首块看 SQLite 头」的方案无关校验把
每把 key 对应到具体库文件。函数入口按特征字节自动定位（跨小版本更稳）：
    48 83 EC 08            sub rsp, 8
    48 C7 C0 FF FF FF FF   mov rax, -1
    48 85 C9               test rcx, rcx

可作为模块被小程序调用 `capture(...)`，也可独立运行：
    python capture_keys.py [秒数]
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import frida
import psutil
from Crypto.Cipher import AES

MODULE = "Weixin.dll"
PROC_NAME = "weixin.exe"
SIG = "48 83 EC 08 48 C7 C0 FF FF FF FF 48 85 C9"   # aesni_set_encrypt_key 入口

_JS = r"""
var m = Process.getModuleByName(%r);
var hits = Memory.scanSync(m.base, m.size, %r);
if (!hits.length) { send("no-sig"); } else {
  Interceptor.attach(hits[0].address, { onEnter: function (a) {
    var ctx = this.context;
    if (((ctx.rdx.toInt32()) & 0xffffffff) !== 256) return;   // 只要 AES-256
    try { send({k: 1}, ctx.rcx.readByteArray(32)); } catch (e) {}
  }});
  send("hooked");
}
""" % (MODULE, SIG)


def load_encrypted_dbs(db_dir: Path) -> dict[str, bytes]:
    """返回 {相对路径: 首页4096字节}，只含加密库（非明文 SQLite）。"""
    dbs = {}
    for p in sorted(Path(db_dir).rglob("*.db")):
        try:
            head = p.read_bytes()[:4096]
        except OSError:
            continue
        if len(head) == 4096 and head[:16] != b"SQLite format 3\x00":
            dbs[p.relative_to(db_dir).as_posix()] = head
    return dbs


def verify(key: bytes, head: bytes) -> bool:
    """方案无关校验：用 key AES-CBC 解第 1 页首块，检查 SQLite 头特征字节。"""
    if len(key) != 32:
        return False
    iv = head[4096 - 80:4096 - 80 + 16]
    try:
        pb = AES.new(key, AES.MODE_CBC, iv).decrypt(head[16:32])
    except Exception:
        return False
    return pb[0:2] == b"\x10\x00" and pb[5] == 0x40 and pb[6] == 0x20 and pb[7] == 0x20


def db_pid() -> int | None:
    """持有 .db 句柄的 weixin.exe 进程（账号主进程）。"""
    best = None
    for p in psutil.process_iter(["pid", "name"]):
        if (p.info["name"] or "").lower() == PROC_NAME:
            try:
                if any(f.path.lower().endswith(".db") for f in p.open_files()):
                    return p.info["pid"]
            except Exception:
                pass
            best = best or p.info["pid"]
    return best


def capture(db_dir: Path, keys_file: Path, run_secs: int = 120, on_progress=None,
            should_stop=None) -> dict[str, str]:
    """hook 薇芯抓取 db_dir 下各库密钥，合并进 keys_file 并返回最新映射。

    on_progress(done, total, rel): 每破解一把回调。should_stop(): 返回 True 可提前停止。
    需薇芯正在运行并登录；运行期间请在薇芯里多点开会话/搜索/打开收藏等以触发各库连接。
    """
    db_dir = Path(db_dir)
    dbs = load_encrypted_dbs(db_dir)
    prev = {}
    if Path(keys_file).exists():
        try:
            prev = json.loads(Path(keys_file).read_text(encoding="utf-8"))
        except Exception:
            prev = {}
    # 合并：保留已有密钥（本轮不一定会重新打开这些库的连接），新抓到的覆盖之。
    # 不再因“当前首页校验不过”而丢弃旧密钥，避免误删仍在用的库。
    cracked: dict[str, str] = dict(prev)

    pid = db_pid()
    if not pid:
        raise RuntimeError("找不到正在运行的薇芯进程，请先启动并登录薇芯。")

    seen: set[bytes] = set()

    def save():
        Path(keys_file).parent.mkdir(parents=True, exist_ok=True)
        Path(keys_file).write_text(json.dumps(cracked, indent=2), encoding="utf-8")

    sig_ok = {"v": None}

    def on_message(msg, data):
        if msg.get("type") != "send":
            return
        p = msg["payload"]
        if isinstance(p, str):
            sig_ok["v"] = (p == "hooked")
            return
        if not data:
            return
        k = bytes(data)
        if k in seen:
            return
        seen.add(k)
        for rel, head in dbs.items():
            if rel in cracked:
                continue
            if verify(k, head):
                cracked[rel] = k.hex()
                save()
                if on_progress:
                    on_progress(len(cracked), len(dbs), rel)

    session = frida.attach(pid)
    script = session.create_script(_JS)
    script.on("message", on_message)
    script.load()
    if sig_ok["v"] is False:
        script.unload(); session.detach()
        raise RuntimeError("未能在 Weixin.dll 中定位密钥函数（特征字节不匹配，可能薇芯版本变化）。")
    try:
        t0 = time.time()
        while time.time() - t0 < run_secs and len(cracked) < len(dbs):
            if should_stop and should_stop():
                break
            time.sleep(0.3)
    finally:
        script.unload()
        session.detach()
    save()
    return cracked


# ------------------------------------------------------------------ CLI ----
def _main() -> None:
    import wxread
    run_secs = int(sys.argv[1]) if len(sys.argv) > 1 else 120
    accts = wxread.find_accounts()
    if not accts:
        print("找不到薇芯账号，请先启动并登录薇芯。")
        return
    acct = accts[0]
    keys_file = Path(__file__).resolve().parent / "keys" / f"{acct['wxid']}.json"
    print(f"账号 {acct['wxid']}  数据目录 {acct['db_dir']}")
    print(f">>> 请在薇芯里多点开会话、搜索聊天内容、打开收藏/朋友圈/公众号等，约 {run_secs}s <<<")

    def prog(done, total, rel):
        print(f"  CRACKED {rel}  ({done}/{total})")

    cracked = capture(acct["db_dir"], keys_file, run_secs, on_progress=prog)
    print(f"完成：{len(cracked)} 把密钥 -> {keys_file}")


if __name__ == "__main__":
    _main()
