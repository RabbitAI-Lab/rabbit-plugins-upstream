#!/usr/bin/env python3
"""Self-test: encode a synthetic .iwa, then verify the parser decodes it.

This proves the Snappy framing + raw Snappy + Protobuf container logic without
needing a real Apple document. Run: python3 test_iwa.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import iwa  # noqa: E402


def enc_varint(v: int) -> bytes:
    out = bytearray()
    while True:
        b = v & 0x7F
        v >>= 7
        if v:
            out.append(b | 0x80)
        else:
            out.append(b)
            break
    return bytes(out)


def ld(fnum: int, b: bytes) -> bytes:
    return bytes([(fnum << 3) | 2]) + enc_varint(len(b)) + b


def varint_field(fnum: int, v: int) -> bytes:
    return bytes([(fnum << 3) | 0]) + enc_varint(v)


def packed(fnum: int, vals) -> bytes:
    buf = b"".join(enc_varint(v) for v in vals)
    return ld(fnum, buf)


def snappy_compress_literals_only(data: bytes) -> bytes:
    out = bytearray(enc_varint(len(data)))
    pos = 0
    while pos < len(data):
        chunk = data[pos:pos + 60]
        l = len(chunk)
        tag = (l - 1) << 2  # type 00, len-1 in upper 6 bits
        out.append(tag)
        out += chunk
        pos += l
    return bytes(out)


def iwa_frame(raw: bytes) -> bytes:
    comp = snappy_compress_literals_only(raw)
    return bytes([0x00]) + comp.__len__().to_bytes(3, "little") + comp


# --- build a payload message with two string fields ---
payload = ld(1, "Hello from iWork".encode("utf-8")) + ld(
    2, "Multi\nline\nbody text".encode("utf-8"))

# --- build MessageInfo (type 1001) ---
mi = varint_field(1, 1001) + packed(2, [1, 0, 5]) + varint_field(3, len(payload))

# --- build ArchiveInfo (identifier 42) ---
ai = varint_field(1, 42) + ld(2, mi)

# --- assemble container object ---
obj = enc_varint(len(ai)) + ai + payload

# --- wrap in framing ---
iwa_bytes = iwa_frame(obj)

# --- parse ---
objects = iwa.parse_iwa(iwa_bytes)
assert len(objects) == 1, f"expected 1 object, got {len(objects)}"
assert objects[0]["identifier"] == 42, objects[0]
texts = iwa.collect_object_texts(objects[0])
assert "Hello from iWork" in texts, texts
assert "Multi\nline\nbody text" in texts, texts

# also verify framing round-trips literal-heavy data
rt = iwa.iwa_unframe(iwa_frame(b"x" * 1000 + b"y" * 5))
assert rt == b"x" * 1000 + b"y" * 5, "framing round-trip failed"

# verify snappy copy/back-reference path on a hand-built stream
def build_copy_stream():
    # "abc" then copy offset=3 len=6  -> reproduces "abcabcabc"
    out = bytearray(enc_varint(9))          # uncompressed length
    out.append((3 - 1) << 2)                # literal len 3, type 00
    out += b"abc"
    # copy with 1-byte offset: type 01, len-4 in bits2..4, offset upper3 in bits5..7
    cplen = 6
    offset = 3
    tag = (0b01) | ((cplen - 4) << 2) | ((offset >> 8) << 5)
    out.append(tag)
    out.append(offset & 0xFF)
    return bytes(out)

dec = iwa.snappy_decompress(build_copy_stream())
assert dec == b"abcabcabc", dec
print("OK: parser decodes synthetic .iwa correctly")
print("    extracted texts:", texts)
