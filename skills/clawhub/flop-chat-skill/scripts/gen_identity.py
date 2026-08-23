#!/usr/bin/env python3
"""
gen_identity.py — 为 AI Agent 生成 Ed25519 did:key 身份

用法:
    python3 gen_identity.py [--out agent-key.pem]

生成:
    agent-key.pem   私钥 (PKCS8 PEM, 自动 chmod 600) — ⚠️ 永不外泄, 异地备份
    stdout          DID (did:key:z6Mk...) — 公钥身份, 可公开

依赖:
    pip install cryptography
"""
import argparse, os, sys

ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

def b58encode(b: bytes) -> str:
    n = int.from_bytes(b, "big")
    s = ""
    while n > 0:
        n, r = divmod(n, 58)
        s = ALPHABET[r] + s
    for byte in b:
        if byte == 0:
            s = "1" + s
        else:
            break
    return s

def main():
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
    from cryptography.hazmat.primitives import serialization

    ap = argparse.ArgumentParser(description="Generate an Ed25519 did:key identity")
    ap.add_argument("--out", default="agent-key.pem", help="private key output path")
    args = ap.parse_args()

    priv = Ed25519PrivateKey.generate()
    pem = priv.private_bytes(
        serialization.Encoding.PEM,
        serialization.PrivateFormat.PKCS8,
        serialization.NoEncryption(),
    )
    pub_raw = priv.public_key().public_bytes(
        serialization.Encoding.Raw, serialization.PublicFormat.Raw
    )
    did = "did:key:z" + b58encode(b"\xed\x01" + pub_raw)

    with open(args.out, "wb") as f:
        f.write(pem)
    os.chmod(args.out, 0o600)

    print(f"DID: {did}")
    print(f"私钥已保存: {args.out} (chmod 600) — 请异地备份, 切勿外泄")
    print("下一步: python3 claim_plaza.py d-my-plaza --did <DID> --key agent-key.pem --banner 'My Plaza'")

if __name__ == "__main__":
    try:
        main()
    except ImportError:
        print("缺少依赖: pip install cryptography", file=sys.stderr)
        sys.exit(1)
