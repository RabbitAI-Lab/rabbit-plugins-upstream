"""SQLCipher 4 页解密（薇芯 4.x：4096 页、保留 80 字节 = 16 IV + 64 HMAC-SHA512）。"""
import hashlib
import hmac
from pathlib import Path

from Crypto.Cipher import AES

PAGE_SIZE = 4096
SALT_SIZE = 16
IV_SIZE = 16
HMAC_SIZE = 64
RESERVE = IV_SIZE + HMAC_SIZE
SQLITE_HEADER = b"SQLite format 3\x00"


def read_salt(db_path: Path) -> bytes:
    with open(db_path, "rb") as f:
        return f.read(SALT_SIZE)


def verify_key(enc_key: bytes, first_page: bytes) -> bool:
    """用第 1 页的 HMAC 校验密钥是否正确。"""
    salt = first_page[:SALT_SIZE]
    mac_salt = bytes(b ^ 0x3A for b in salt)
    mac_key = hashlib.pbkdf2_hmac("sha512", enc_key, mac_salt, 2, 32)
    body = first_page[SALT_SIZE:PAGE_SIZE - HMAC_SIZE]
    stored = first_page[PAGE_SIZE - HMAC_SIZE:PAGE_SIZE]
    calc = hmac.new(mac_key, body + (1).to_bytes(4, "little"), hashlib.sha512).digest()
    return hmac.compare_digest(calc, stored)


def decrypt_db(src: Path, dst: Path, enc_key: bytes) -> None:
    """把整个加密库解密成普通 SQLite 文件。"""
    data = src.read_bytes()
    if len(data) < PAGE_SIZE or len(data) % PAGE_SIZE:
        data = data[: len(data) // PAGE_SIZE * PAGE_SIZE]
    out = bytearray()
    for i in range(len(data) // PAGE_SIZE):
        page = data[i * PAGE_SIZE:(i + 1) * PAGE_SIZE]
        iv = page[PAGE_SIZE - RESERVE:PAGE_SIZE - RESERVE + IV_SIZE]
        start = SALT_SIZE if i == 0 else 0
        enc = page[start:PAGE_SIZE - RESERVE]
        plain = AES.new(enc_key, AES.MODE_CBC, iv).decrypt(enc)
        if i == 0:
            out += SQLITE_HEADER + plain
        else:
            out += plain
        out += b"\x00" * RESERVE
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_bytes(bytes(out))
