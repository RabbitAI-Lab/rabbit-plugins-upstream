"""
iwa.py - Low-level parser for Apple iWork '13+ file format (.pages/.numbers/.key)

The format is a bundle (ZIP) containing an Index.zip. Inside Index.zip are
.iwa files. Each .iwa is a Protobuf stream wrapped in a *non-standard* Snappy
framing:

  - Snappy framing (iWork variant, does NOT follow the official spec):
      chunk = [1 byte type][3-byte LE length][length bytes data]
      iWork only ever emits type 0x00 (compressed). It omits the mandatory
      stream-identifier chunk (0xff "sNaPpY") and omits the CRC-32C checksum
      that the official framing puts before compressed data.
      The chunk body for type 0x00 is a *raw* Snappy stream (it starts with an
      uncompressed-length varint), NOT an official framed stream.

  - Raw Snappy block:
      varint uncompressed_length
      then LZ77 elements (literals / back-references) until done.

  - Protobuf container stream (after Snappy decompression):
      repeated objects, each:
        varint archive_info_len
        ArchiveInfo message:
            field 1: identifier (uint64)
            field 2: repeated MessageInfo
        then, for each MessageInfo, its payload:
            field 1: type (uint32)      -> selects the protobuf schema
            field 2: version (packed uint32)
            field 3: length (uint32)     -> payload byte length
            field 5: object_references (packed uint64)
            field 6: data_references  (packed uint64)
        payload bytes (a protobuf message of the given `type`)

Protobuf is not self-describing, so the `type` -> schema mapping (the
"TSPRegistry") is recovered from the iWork binaries at runtime and varies per
app/version. Without it we cannot perfectly decode payloads, BUT human-readable
text is stored in UTF-8 string fields, so a generic walk recovers nearly all
visible content. That is what this module does.

Pure stdlib (zipfile, struct, io, dataclasses, plistlib). No third-party deps.
"""

import io
import os
import re
import zipfile
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple


# --------------------------------------------------------------------------
# Varint
# --------------------------------------------------------------------------
def read_varint(buf: bytes, pos: int) -> Tuple[int, int]:
    """Read a protobuf-style unsigned LEB128 varint. Returns (value, new_pos)."""
    result = 0
    shift = 0
    while True:
        if pos >= len(buf):
            raise ValueError("varint truncated")
        b = buf[pos]
        pos += 1
        result |= (b & 0x7F) << shift
        if not (b & 0x80):
            break
        shift += 7
        if shift > 63:
            raise ValueError("varint too long")
    return result, pos


# --------------------------------------------------------------------------
# Raw Snappy decompression (block format, NOT framing)
# --------------------------------------------------------------------------
def snappy_decompress(raw: bytes) -> bytes:
    """Decompress a *raw* Snappy stream (uncompressed-length varint prefix)."""
    if not raw:
        return b""
    pos = 0
    length, pos = read_varint(raw, pos)
    out = bytearray()
    n = len(raw)
    while pos < n:
        tag = raw[pos]
        pos += 1
        typ = tag & 0x03
        if typ == 0:  # literal
            lenfield = tag >> 2
            if lenfield < 60:
                l = lenfield + 1
            else:
                num = lenfield - 59  # 1..4 bytes for the length
                l = 0
                for i in range(num):
                    l |= raw[pos] << (8 * i)
                    pos += 1
                l += 1
            out += raw[pos:pos + l]
            pos += l
        else:  # copy (back-reference)
            if typ == 1:  # 1-byte offset
                cplen = ((tag >> 2) & 0x07) + 4
                offset = ((tag >> 5) << 8) | raw[pos]
                pos += 1
            elif typ == 2:  # 2-byte offset
                cplen = (tag >> 2) + 1
                offset = raw[pos] | (raw[pos + 1] << 8)
                pos += 2
            else:  # typ == 3: 4-byte offset
                cplen = (tag >> 2) + 1
                offset = (raw[pos] | (raw[pos + 1] << 8)
                          | (raw[pos + 2] << 16) | (raw[pos + 3] << 24))
                pos += 4
            if offset == 0 or offset > len(out):
                raise ValueError("invalid Snappy copy offset")
            start = len(out) - offset
            for i in range(cplen):
                out.append(out[start + i])
    if len(out) != length:
        raise ValueError(
            f"Snappy length mismatch: got {len(out)}, expected {length}")
    return bytes(out)


# --------------------------------------------------------------------------
# Snappy framing (iWork variant)
# --------------------------------------------------------------------------
def iwa_unframe(data: bytes) -> bytes:
    """Unwrap iWork's Snappy framing, returning the concatenated raw streams."""
    out = bytearray()
    pos = 0
    n = len(data)
    while pos < n:
        if pos + 4 > n:
            break
        ctype = data[pos]
        clen = data[pos + 1] | (data[pos + 2] << 8) | (data[pos + 3] << 16)
        pos += 4
        if pos + clen > n:
            raise ValueError("Snappy chunk overruns buffer")
        chunk = data[pos:pos + clen]
        pos += clen
        if ctype == 0x00:  # compressed data (raw snappy inside)
            out += snappy_decompress(chunk)
        elif ctype == 0x01:  # uncompressed data (4-byte masked CRC then raw)
            out += chunk[4:]
        elif ctype == 0xFF:  # stream identifier (iWork omits it) -> ignore
            continue
        elif 0x80 <= ctype <= 0xFD:  # skippable / padding -> ignore
            continue
        else:  # 0x02..0x7F reserved unskippable
            raise ValueError(f"unskippable Snappy chunk type {ctype:#x}")
    return bytes(out)


# --------------------------------------------------------------------------
# Generic Protobuf message parser
# --------------------------------------------------------------------------
@dataclass
class Field:
    wire_type: int
    value: int = 0           # for varint (0) / 64-bit (1) / 32-bit (5)
    raw: bytes = b""         # for length-delimited (2)
    text: Optional[str] = None       # utf-8 decode if printable
    sub: Optional[dict] = None       # parsed sub-message if applicable


Message = Dict[int, List[Field]]


def _looks_like_message(b: bytes) -> bool:
    if len(b) == 0:
        return False
    first = b[0]
    wt = first & 0x07
    fnum = first >> 3
    return wt in (0, 1, 2, 5) and fnum >= 1


def _is_printable(s: str) -> bool:
    if not s:
        return False
    for ch in s:
        o = ord(ch)
        if ch in "\t\n\r" or (32 <= o < 127) or o >= 0xA0:
            continue
        return False
    return True


def parse_message(data: bytes) -> Message:
    """Parse a protobuf message into {field_number: [Field, ...]}."""
    msg: Message = {}
    pos = 0
    n = len(data)
    while pos < n:
        key, pos = read_varint(data, pos)
        fnum = key >> 3
        wt = key & 0x07
        if wt == 0:
            v, pos = read_varint(data, pos)
            msg.setdefault(fnum, []).append(Field(wire_type=0, value=v))
        elif wt == 1:
            v = int.from_bytes(data[pos:pos + 8], "little")
            pos += 8
            msg.setdefault(fnum, []).append(Field(wire_type=1, value=v))
        elif wt == 5:
            v = int.from_bytes(data[pos:pos + 4], "little")
            pos += 4
            msg.setdefault(fnum, []).append(Field(wire_type=5, value=v))
        elif wt == 2:
            ln, pos = read_varint(data, pos)
            if pos + ln > n:
                raise ValueError("length-delimited field overruns buffer")
            b = data[pos:pos + ln]
            pos += ln
            f = Field(wire_type=2, raw=b)
            try:
                s = b.decode("utf-8")
                if _is_printable(s):
                    f.text = s
            except UnicodeDecodeError:
                pass
            if f.text is None and _looks_like_message(b):
                try:
                    f.sub = parse_message(b)
                except Exception:
                    f.sub = None
            msg.setdefault(fnum, []).append(f)
        else:
            raise ValueError(f"unknown wire type {wt}")
    return msg


# --------------------------------------------------------------------------
# Container parsing: .iwa -> list of objects with payloads
# --------------------------------------------------------------------------
def parse_iwa(data: bytes) -> List[dict]:
    """Parse an unframed .iwa container into a list of objects.

    Each object: {'identifier': int|None, 'parts': [(type_id, Message), ...]}
    """
    stream = iwa_unframe(data)
    objects = []
    pos = 0
    n = len(stream)
    while pos < n:
        ln, pos = read_varint(stream, pos)
        if pos + ln > n:
            break
        ai = parse_message(stream[pos:pos + ln])
        pos += ln

        identifier = None
        if 1 in ai:
            identifier = ai[1][0].value

        message_infos = []
        object_refs = []
        data_refs = []
        if 2 in ai:
            for f in ai[2]:
                if f.sub is not None:
                    message_infos.append(f.sub)
                if f.wire_type == 2 and f.raw is not None and f.sub is None:
                    # packed varints (object_references / data_references)
                    refs = []
                    pp = 0
                    while pp < len(f.raw):
                        v, pp = read_varint(f.raw, pp)
                        refs.append(v)
                    object_refs.extend(refs)
        # data_references are typically in message_info field 6 (packed uint64)
        for mi in ai.get(2, []) if isinstance(ai.get(2), list) else []:
            if mi.sub is not None:
                for fld in mi.sub.get(6, []):
                    if fld.wire_type == 2 and fld.raw is not None:
                        pp = 0
                        while pp < len(fld.raw):
                            v, pp = read_varint(fld.raw, pp)
                            data_refs.append(v)

        parts = []
        for mi in message_infos:
            mtype_f = mi.get(1)
            mlen_f = mi.get(3)
            if not mtype_f or not mlen_f:
                continue
            mtype = mtype_f[0].value
            mlen = mlen_f[0].value
            if pos + mlen > n:
                break
            payload = parse_message(stream[pos:pos + mlen])
            pos += mlen
            parts.append((mtype, payload))

        objects.append({"identifier": identifier, "parts": parts,
                         "object_refs": object_refs, "data_refs": data_refs})
    return objects


# --------------------------------------------------------------------------
# Text extraction helpers
# --------------------------------------------------------------------------
def extract_texts(msg: Message, out: List[str]) -> None:
    """Recursively collect all printable UTF-8 strings from a parsed message."""
    if not isinstance(msg, dict):
        return
    for items in msg.values():
        for f in items:
            if f.text is not None and len(f.text.strip()) > 0:
                out.append(f.text)
            if f.sub is not None:
                extract_texts(f.sub, out)


def collect_object_texts(obj: dict) -> List[str]:
    texts: List[str] = []
    for _type_id, payload in obj["parts"]:
        extract_texts(payload, texts)
    return texts


def best_body(texts: List[str]) -> Optional[str]:
    """Pick the most document-like string: longest with a newline, else longest."""
    candidates = [t for t in texts if "\n" in t or len(t) > 40]
    if not candidates:
        return None
    candidates.sort(key=len, reverse=True)
    return candidates[0]


# --------------------------------------------------------------------------
# Numbers spreadsheet tables (TST.Table = type 6001, DataList = type 6005)
# --------------------------------------------------------------------------
def _cell_text(cell: dict) -> str:
    """Extract display text from a TST.Cell (type 6006) parsed message.

    Cell kinds in modern Numbers:
      - field 3: string value
      - field 5: number value (nested sub -> f42 carries the double bits)
      - field 4: formula/reference cell (sub -> f1 is a referenced object id)
      - field 2: cell type/flags (int)
    We render strings and numbers as-is; formulas as '=...'.
    """
    # String value (field 3)
    for f in cell.get(3, []):
        if f.text:
            return f.text.strip()
    # Number value (field 5 -> sub with f42 double bits)
    for f in cell.get(5, []):
        if f.sub is not None:
            for sf in f.sub.get(42, []):
                if sf.wire_type == 1:  # 64-bit, double bits
                    val = sf.value
                    # interpret as little-endian double
                    import struct as _struct
                    d = _struct.unpack("<d", val.to_bytes(8, "little"))[0]
                    if d == int(d):
                        return str(int(d))
                    return repr(d)
    # Formula / reference cell (field 4)
    for f in cell.get(4, []):
        if f.sub is not None:
            return "=formula"
    return ""


def extract_numbers_tables(objects: List[dict]) -> List[List[List[str]]]:
    """Reconstruct Numbers tables from Table (6001) + DataList (6005) objects.

    Returns a list of tables; each table is a list of rows; each row a list of
    cell strings. Handles the modern flat-DataList layout where a Table
    references its DataLists by id (embedded as nested ints in the Table).
    """
    # Gather all DataLists by id, with their ordered cell texts.
    datalists = {}
    for obj in objects:
        oid = obj.get("identifier")
        for tid, payload in obj["parts"]:
            if tid == 6005:  # DataList
                cells = []
                for fld in payload.get(3, []):
                    if fld.sub is not None:
                        cells.append(_cell_text(fld.sub))
                datalists[oid] = cells
    dl_ids = set(datalists.keys())

    def _collect_ints(o, out):
        if isinstance(o, dict):
            for items in o.values():
                if not isinstance(items, list):
                    continue
                for f in items:
                    if hasattr(f, "wire_type") and f.wire_type in (0, 1, 5):
                        out.append(f.value)
                    if getattr(f, "sub", None) is not None:
                        _collect_ints(f.sub, out)

    tables = []
    for obj in objects:
        for tid, payload in obj["parts"]:
            if tid != 6001:  # TST.Table
                continue
            nrows = 0
            for f in payload.get(6, []):
                nrows = f.value
            ncols = 0
            for f in payload.get(7, []):
                ncols = f.value
            if nrows <= 0 or ncols <= 0:
                continue
            # Find DataList ids referenced inside the Table (nested ints)
            ints = []
            _collect_ints(payload, ints)
            refs = [v for v in ints if v in dl_ids]
            # de-dupe preserving order
            seen = set()
            ordered_refs = []
            for r in refs:
                if r not in seen:
                    seen.add(r)
                    ordered_refs.append(r)
            cells = []
            for r in ordered_refs:
                cells.extend(datalists[r])
            if not cells:
                continue
            if len(cells) < nrows * ncols:
                cells = cells + [""] * (nrows * ncols - len(cells))
            grid = []
            for r in range(nrows):
                grid.append(cells[r * ncols:(r + 1) * ncols])
            tables.append(grid)
    return tables


# --------------------------------------------------------------------------
# Bundle handling
# --------------------------------------------------------------------------
_TIMEZONE_RE = re.compile(r"^[A-Za-z]+/[A-Za-z_]+$")  # e.g. Asia/Shanghai
_LOCALE_RE = re.compile(r"^[a-z]{2}[_-][A-Za-z]{2}$")    # e.g. en_HK, zh_CN


def _is_locale_like(s: str) -> bool:
    return bool(_LOCALE_RE.match(s)) or bool(_TIMEZONE_RE.match(s))


def open_iwa_sources(path: str):
    """Return (reader, [iwa member names]) for a .pages/.numbers/.key file.

    `reader` is either a zipfile.ZipFile or a _DirBundle (directory package).
    Two physical layouts are supported:
      - A single ZIP file whose outer layer is the bundle (classic iWork '13),
        containing either .iwa members directly or an Index.zip.
      - A *directory bundle* on disk (macOS package) containing Index.zip or
        an Index/ folder of .iwa files.
    """
    if os.path.isdir(path):
        # Directory bundle (package)
        idx = os.path.join(path, "Index.zip")
        if os.path.isfile(idx):
            zf = zipfile.ZipFile(idx)
            return zf, [n for n in zf.namelist() if n.endswith(".iwa")]
        idx_dir = os.path.join(path, "Index")
        if os.path.isdir(idx_dir):
            iwas = []
            for root, _dirs, files in os.walk(idx_dir):
                for fn in files:
                    if fn.endswith(".iwa"):
                        iwas.append(os.path.join(root, fn))
            if iwas:
                return _DirBundle(iwas), iwas
        raise ValueError("no Index.zip or Index/ found in directory bundle")

    # ZIP-file bundle
    zf = zipfile.ZipFile(path)
    names = zf.namelist()
    if any(n.endswith(".iwa") for n in names):
        return zf, [n for n in names if n.endswith(".iwa")]
    idx_name = next((n for n in names if n.lower().endswith("index.zip")), None)
    if idx_name is None:
        raise ValueError("no Index.zip or .iwa members found in bundle")
    inner = zipfile.ZipFile(io.BytesIO(zf.read(idx_name)))
    return inner, [n for n in inner.namelist() if n.endswith(".iwa")]


class _DirBundle:
    """Minimal read interface over a directory of .iwa files."""
    def __init__(self, paths):
        self.paths = paths
    def read(self, p):
        with open(p, "rb") as f:
            return f.read()
    def close(self):
        pass


def list_media(path: str) -> List[str]:
    """List filenames under the Data/ directory (images, video, etc.)."""
    media = []
    if os.path.isdir(path):
        data_dir = os.path.join(path, "Data")
        if os.path.isdir(data_dir):
            for root, _dirs, files in os.walk(data_dir):
                for fn in files:
                    rel = os.path.relpath(os.path.join(root, fn), path)
                    media.append(rel)
        return sorted(media)
    zf = zipfile.ZipFile(path)
    return [n for n in zf.namelist() if "/Data/" in n or n.startswith("Data/")]


def read_title(path: str) -> Optional[str]:
    """Best-effort read of document title from Metadata/Properties.plist."""
    try:
        import plistlib
        raw = None
        if os.path.isdir(path):
            cand = os.path.join(path, "Metadata", "Properties.plist")
            if os.path.isfile(cand):
                with open(cand, "rb") as f:
                    raw = f.read()
        else:
            zf = zipfile.ZipFile(path)
            cand = next((n for n in zf.namelist()
                         if n.endswith("Properties.plist")), None)
            if cand:
                raw = zf.read(cand)
        if not raw:
            return None
        plist = plistlib.loads(raw)
        for key in ("Title", "title", "name", "documentTitle"):
            v = plist.get(key)
            if isinstance(v, str) and v.strip() and not _is_locale_like(v):
                return v
    except Exception:
        pass
    return None
