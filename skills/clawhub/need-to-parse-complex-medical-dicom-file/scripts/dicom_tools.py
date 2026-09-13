#!/usr/bin/env python3
"""dicom_tools.py — 纯标准库 DICOM 解析/检查/去标识化工具 v2.0.0

能力边界（诚实声明）：
  - 读取：Implicit VR Little Endian (1.2.840.10008.1.2) 与 Explicit VR
    Little Endian (1.2.840.10008.1.2.1)，含 File Meta、序列(SQ)、私有标签。
  - 像素导出：仅未压缩 (uncompressed) 8/16 位像素 → PNM (P5/P6)。
  - 不解码：JPEG/JPEG-LS/JPEG2000/RLE/MPEG 等封装(encapsulated)像素 ——
    会检测并如实报告，给出 pydicom+pylibjpeg 精确命令，绝不猜测像素值。
  - 仅技术检查用途，**不用于诊断**；去标识化输出不等同于合规认证。

命令：
  summary FILE                      紧凑摘要（默认推荐，省 token）
  parse FILE [--tags 0010,0020]     完整标签转储（可过滤）
  pixels FILE --out IMG.pnm         导出未压缩像素（P5/P6；封装像素诚实拒绝）
  check FILE                        一致性检查（findings；exit 3=有错误）
  deid FILE --out OUT.dcm           PS3.15 基础配置子集去标识化
  gen --out T.dcm [--vr explicit|implicit] [--rows N --cols N --seed N]
                                    [--encapsulated]  生成确定性合成测试文件（无真实 PHI）

退出码：0 成功 · 2 输入错误/诚实拒绝 · 3 check 发现一致性错误
输出：stdout JSON（ensure_ascii=False）；错误 JSON 在 stderr。
依据：DICOM PS3.5 2026c（NEMA）文件格式/值编码；PS3.15 2026c §6.9 属性保密配置。
"""
import argparse
import hashlib
import json
import os
import struct
import sys

TOOL = "dicom-tools v2.0.0"
PURPOSE = "技术检查用途；不用于诊断 (technical inspection only, not for diagnosis)"

# ── 值表示（PS3.5 2026c §6.2/§7.1.2）──────────────────────────────────────
# 使用 4 字节长度字段的 VR
LONG_VR = {"OB", "OW", "SQ", "UC", "UR", "UT"}
STR_VR = {"AE", "AS", "CS", "DA", "DS", "DT", "IS", "LO", "LT", "PN",
          "SH", "ST", "TM", "UI", "UR", "UT"}
NUM_VR = {"US", "SS", "UL", "SL", "FL", "FD"}

# Implicit VR 文件的 VR 推断表（标准字典中常见标签；未列出 → UN 十六进制预览）
IMPLICIT_VR = {
    (0x0008, 0x0005): "SH", (0x0008, 0x0008): "CS", (0x0008, 0x0016): "UI",
    (0x0008, 0x0018): "UI", (0x0008, 0x0020): "DA", (0x0008, 0x0030): "TM",
    (0x0008, 0x0050): "SH", (0x0008, 0x0060): "CS", (0x0008, 0x0070): "SH",
    (0x0008, 0x0080): "LO", (0x0008, 0x0081): "LO", (0x0008, 0x0090): "PN",
    (0x0008, 0x1030): "LO", (0x0008, 0x103E): "LO", (0x0008, 0x1040): "SH",
    (0x0008, 0x1048): "PN", (0x0008, 0x1050): "PN", (0x0008, 0x1070): "PN",
    (0x0010, 0x0010): "PN", (0x0010, 0x0020): "LO", (0x0010, 0x0030): "DA",
    (0x0010, 0x0032): "AS", (0x0010, 0x0040): "CS", (0x0010, 0x1000): "LO",
    (0x0010, 0x1001): "PN", (0x0010, 0x1010): "DS", (0x0010, 0x1020): "DS",
    (0x0010, 0x1040): "LO", (0x0010, 0x2154): "SH",
    (0x0012, 0x0062): "CS", (0x0012, 0x0063): "SQ",
    (0x0020, 0x000D): "UI", (0x0020, 0x000E): "UI", (0x0020, 0x0010): "SH",
    (0x0020, 0x0011): "IS", (0x0020, 0x0013): "IS", (0x0020, 0x0032): "DS",
    (0x0020, 0x0037): "DS", (0x0020, 0x0052): "UI",
    (0x0028, 0x0002): "US", (0x0028, 0x0004): "CS", (0x0028, 0x0006): "US",
    (0x0028, 0x0008): "IS", (0x0028, 0x0010): "US", (0x0028, 0x0011): "US",
    (0x0028, 0x0100): "US", (0x0028, 0x0101): "US", (0x0028, 0x0102): "US",
    (0x0028, 0x0103): "US", (0x0028, 0x0104): "DS",
    (0x7FE0, 0x0010): "OW",
}

SOP_CLASSES = {
    "1.2.840.10008.5.1.4.1.1.1": "X-Ray Radiograph",
    "1.2.840.10008.5.1.4.1.1.1.1": "Digital X-Ray Radiograph",
    "1.2.840.10008.5.1.4.1.1.1.2": "Enhanced X-Ray Radiograph",
    "1.2.840.10008.5.1.4.1.1.2": "CT Image Storage",
    "1.2.840.10008.5.1.4.1.1.2.1": "Enhanced CT Image Storage",
    "1.2.840.10008.5.1.4.1.1.4": "MR Image Storage",
    "1.2.840.10008.5.1.4.1.1.4.1": "Enhanced MR Image Storage",
    "1.2.840.10008.5.1.4.1.1.6.1": "Ultrasound Image Storage",
    "1.2.840.10008.5.1.4.1.1.6.1.1": "Enhanced US Image Storage",
    "1.2.840.10008.5.1.4.1.1.7": "Nuclear Medicine Image Storage",
    "1.2.840.10008.5.1.4.1.1.8.1": "Secondary Capture Image Storage",
    "1.2.840.10008.5.1.4.1.1.3.1.1": "Basic Structured Report Storage",
    "1.2.840.10008.5.1.4.1.1.481.3": "RT Structure Set Storage",
}

# PS3.5 2026c 附录 A 注册值（常见子集）
TRANSFER_SYNTAXES = {
    "1.2.840.10008.1.2": ("Implicit VR Little Endian", "uncompressed_le"),
    "1.2.840.10008.1.2.1": ("Explicit VR Little Endian", "uncompressed_le"),
    "1.2.840.10008.1.2.1.99": ("Deflated Explicit VR Little Endian", "deflated"),
    "1.2.840.10008.1.2.2": ("Explicit VR Big Endian (retired)", "big_endian"),
    "1.2.840.10008.1.2.4.50": ("JPEG Baseline (8-bit lossy)", "encapsulated"),
    "1.2.840.10008.1.2.4.51": ("JPEG Baseline (12-bit lossy)", "encapsulated"),
    "1.2.840.10008.1.2.4.57": ("JPEG Lossless", "encapsulated"),
    "1.2.840.10008.1.2.4.70": ("JPEG Lossless First-Order (default lossless)", "encapsulated"),
    "1.2.840.10008.1.2.4.80": ("JPEG-LS Lossless", "encapsulated"),
    "1.2.840.10008.1.2.4.81": ("JPEG-LS Near-Lossless", "encapsulated"),
    "1.2.840.10008.1.2.4.90": ("JPEG 2000 (lossless)", "encapsulated"),
    "1.2.840.10008.1.2.4.91": ("JPEG 2000", "encapsulated"),
    "1.2.840.10008.1.2.4.100": ("MPEG2 Main/Main", "encapsulated"),
    "1.2.840.10008.1.2.4.101": ("MPEG2 Main/High", "encapsulated"),
    "1.2.840.10008.1.2.4.102": ("MPEG-4 AVC/H.264 High/L4.1", "encapsulated"),
    "1.2.840.10008.1.2.5": ("RLE Lossless", "encapsulated"),
}

TAG_NAMES = {
    (0x0002, 0x0000): "FileMetaInformationGroupLength",
    (0x0002, 0x0001): "MediaStorageSOPClassUID",
    (0x0002, 0x0002): "MediaStorageSOPInstanceUID",
    (0x0002, 0x0003): "TransferSyntaxUID",
    (0x0002, 0x0010): "ImplementationClassUID",
    (0x0008, 0x0005): "SpecificCharacterSet",
    (0x0008, 0x0008): "ImageType",
    (0x0008, 0x0016): "SOPClassUID",
    (0x0008, 0x0018): "SOPInstanceUID",
    (0x0008, 0x0020): "StudyDate",
    (0x0008, 0x0030): "StudyTime",
    (0x0008, 0x0050): "AccessionNumber",
    (0x0008, 0x0060): "Modality",
    (0x0008, 0x0070): "StationName",
    (0x0008, 0x0080): "InstitutionName",
    (0x0008, 0x0081): "InstitutionAddress",
    (0x0008, 0x0090): "ReferringPhysicianName",
    (0x0008, 0x1030): "StudyDescription",
    (0x0008, 0x103E): "SeriesDescription",
    (0x0008, 0x1040): "InstitutionalDepartmentName",
    (0x0008, 0x1048): "PhysiciansOfRecord",
    (0x0008, 0x1050): "PerformingPhysicianName",
    (0x0008, 0x1070): "OperatorsName",
    (0x0008, 0x2111): "ContentDate",
    (0x0008, 0x2112): "ContentTime",
    (0x0010, 0x0010): "PatientName",
    (0x0010, 0x0020): "PatientID",
    (0x0010, 0x0030): "PatientBirthDate",
    (0x0010, 0x0032): "PatientAge",
    (0x0010, 0x0040): "PatientSex",
    (0x0010, 0x1000): "OtherPatientIDs",
    (0x0010, 0x1001): "OtherPatientNames",
    (0x0010, 0x1010): "PatientWeight",
    (0x0010, 0x1020): "PatientHeight",
    (0x0010, 0x1040): "PatientAddress",
    (0x0010, 0x2154): "PatientTelephoneNumbers",
    (0x0012, 0x0062): "PatientIdentityRemoved",
    (0x0012, 0x0063): "DeidentificationMethodCodeSequence",
    (0x0020, 0x000D): "StudyInstanceUID",
    (0x0020, 0x000E): "SeriesInstanceUID",
    (0x0020, 0x0010): "StudyID",
    (0x0020, 0x0011): "SeriesNumber",
    (0x0020, 0x0013): "InstanceNumber",
    (0x0020, 0x0032): "ImagePositionPatient",
    (0x0020, 0x0037): "ImageOrientationPatient",
    (0x0020, 0x0052): "FrameOfReferenceUID",
    (0x0028, 0x0002): "SamplesPerPixel",
    (0x0028, 0x0004): "PhotometricInterpretation",
    (0x0028, 0x0006): "PlanarConfiguration",
    (0x0028, 0x0008): "NumberOfFrames",
    (0x0028, 0x0010): "Rows",
    (0x0028, 0x0011): "Columns",
    (0x0028, 0x0100): "BitsAllocated",
    (0x0028, 0x0101): "BitsStored",
    (0x0028, 0x0102): "HighBit",
    (0x0028, 0x0103): "PixelRepresentation",
    (0x0028, 0x0104): "PixelSpacing",
    (0x7FE0, 0x0010): "PixelData",
}

UID_PREFIX = "1.2.826.0.1.3680043.8.498."  # 私有 OID 前缀（去标识化 UID 重映射）


def err(msg, code=2, **extra):
    out = {"status": "error", "tool": TOOL, "error": msg}
    out.update(extra)
    print(json.dumps(out, ensure_ascii=False, indent=2), file=sys.stderr)
    sys.exit(code)


def tag_str(g, e):
    return "[%04X,%04X]" % (g, e)


def remap_uid(uid):
    """确定性 UID 重映射：同一输入 UID 永远映射到同一输出 UID（批次内一致，不可逆）。"""
    h = hashlib.sha256(uid.encode("ascii")).hexdigest()[:16]
    return UID_PREFIX + h


# ── 元素与解析 ─────────────────────────────────────────────────────────────
class Element:
    __slots__ = ("group", "elem", "vr", "raw", "undefined", "items", "frags")

    def __init__(self, group, elem, vr, raw, undefined=False):
        self.group, self.elem, self.vr, self.raw, self.undefined = group, elem, vr, raw, undefined
        self.items = None  # SQ 解析结果（item 列表，每项 dict{tag: Element}）
        self.frags = None  # 封装像素 fragment 数

    @property
    def tag(self):
        return (self.group, self.elem)

    @property
    def name(self):
        return TAG_NAMES.get((self.group, self.elem),
                             "PrivateTag" if (self.group & 1) else "UnknownTag")

    def value(self, endian="<"):
        if self.vr == "SQ" or self.undefined:
            return None
        raw = self.raw
        if self.vr in STR_VR:
            s = raw.decode("latin-1", errors="replace")
            if self.vr == "UI":
                s = s.rstrip("\x00")
            return s.rstrip()
        if self.vr == "UN":
            return {"un": raw.hex() if len(raw) <= 64 else raw[:64].hex() + "…"}
        if self.vr == "OB":
            return raw
        if self.vr in NUM_VR:
            if not raw:
                return None
            fmt = {"US": "H", "SS": "h", "UL": "I", "SL": "i", "FL": "f", "FD": "d"}[self.vr]
            size = struct.calcsize(endian + fmt)
            n = len(raw) // size
            vals = struct.unpack(endian + fmt * n, raw[: n * size])
            vals = [round(v, 6) if isinstance(v, float) else v for v in vals]
            return vals[0] if n == 1 else list(vals)
        return raw.hex() if len(raw) <= 64 else raw[:64].hex() + "…"


def read_element(buf, pos, explicit, endian="<", warn=None):
    """读取一个数据元素头+值。返回 (Element|None, new_pos)。"""
    if pos + 4 > len(buf):
        return None, pos
    group, elem = struct.unpack_from(endian + "HH", buf, pos)
    pos += 4
    if group == 0xFFFE:
        if pos + 2 > len(buf):
            return None, pos
        length = struct.unpack_from(endian + "H", buf, pos)[0]
        pos += 2
        if elem == 0xE0DD:  # Sequence Delimitation
            return Element(0xFFFE, elem, "SeqDelim", b""), pos
        vr = {0xE000: "Item", 0xE00D: "ItemDelim"}.get(elem, "FFFE")
        return Element(0xFFFE, elem, vr, buf[pos:pos + length]), pos + length
    if explicit:
        if pos + 2 > len(buf):
            return None, pos
        vr = buf[pos:pos + 2].decode("latin-1", errors="replace")
        pos += 2
        if vr in LONG_VR:
            if pos + 8 > len(buf):
                return None, pos
            length = struct.unpack_from(endian + "I", buf, pos + 4)[0]
            pos += 8
        else:
            if pos + 4 > len(buf):
                return None, pos
            length = struct.unpack_from(endian + "H", buf, pos + 2)[0]
            pos += 4
    else:
        if pos + 2 > len(buf):
            return None, pos
        vr = IMPLICIT_VR.get((group, elem), "UN")
        if vr == "UN" and warn is not None and (group, elem) in TAG_NAMES:
            warn("标签 %s 在 implicit 文件中 VR 未推断出，按 UN 处理" % tag_str(group, elem))
        length = struct.unpack_from(endian + "H", buf, pos)[0]
        pos += 2
    undefined = length == 0xFFFFFFFF
    raw = b"" if undefined else buf[pos:pos + length]
    return Element(group, elem, vr, raw, undefined), (pos if undefined else pos + length)


def parse_items(buf, start, end, endian, depth, warnings):
    """解析 undefined-length 序列区域 buf[start:end]（到 SeqDelim 之前）为 item 列表。
    PS3.5 §7.5.3：序列内部总按 Explicit VR 解析。"""
    items = []
    pos = start
    while pos < end and depth < 8:
        el, pos = read_element(buf, pos, True, endian)
        if el is None or el.elem == 0xE0DD:
            break
        if el.elem == 0xE00D or el.vr != "Item":
            continue
        if el.undefined:
            warnings.append("未定义长度的 item：停止解析该序列（超出本工具边界）")
            break
        item = {}
        ipos = 0
        while ipos < len(el.raw):
            sub, ipos = read_element(el.raw, ipos, True, endian)
            if sub is None or sub.group == 0xFFFE:
                break
            if sub.vr == "SQ" and sub.undefined:
                d = el.raw.find(b"\xfe\xff\xdd\xe0", ipos)
                if d < 0:
                    warnings.append("序列内缺少 FFFE,E0DD 终止符")
                    break
                sub.items = parse_items(el.raw, ipos, d, endian, depth + 1, warnings)
            item[(sub.group, sub.elem)] = sub
        items.append(item)
    return items


def parse_file(buf, warnings):
    """返回 {file_meta, dataset, ts_uid, ts_name, ts_class, pixel, warnings}"""
    meta = {}
    pos = 132
    while pos + 4 <= len(buf):
        g0, _ = struct.unpack_from("<HH", buf, pos)
        if g0 != 0x0002:
            break  # 数据集开始（数据集的 VR 编码方式可能不同，先停）
        el, pos = read_element(buf, pos, True, "<")
        if el is None:
            break
        meta[(el.group, el.elem)] = el
        if el.vr == "SQ" and el.undefined:
            d = buf.find(b"\xfe\xff\xdd\xe0", pos)
            d = d if d >= 0 else len(buf)
            el.items = parse_items(buf, pos, d, "<", 0, warnings)
            pos = d + 4 if d < len(buf) else len(buf)
    ts_uid = ""
    if (0x0002, 0x0003) in meta:
        v = meta[(0x0002, 0x0003)].value()
        ts_uid = v if isinstance(v, str) else ""
    ts_name, ts_class = TRANSFER_SYNTAXES.get(ts_uid, ("UnknownTransferSyntax", "unknown"))
    if ts_class == "deflated":
        warnings.append("deflated 传输语法：本工具不解 zlib 数据集，仅报告 file meta")
        return {"file_meta": meta, "dataset": {}, "ts_uid": ts_uid, "ts_name": ts_name,
                "ts_class": ts_class, "pixel": None, "warnings": warnings}

    if ts_class == "big_endian":
        warnings.append("big-endian 传输语法（已退役）：按大端解析，建议用 pydicom 复核")
        explicit, endian = True, ">"
    elif ts_class == "uncompressed_le":
        explicit, endian = (ts_uid != "1.2.840.10008.1.2"), "<"
    else:
        explicit, endian = True, "<"  # 未知/封装：file meta 后尽力按显式小端读元数据

    dataset = {}
    pixel = None
    while pos < len(buf):
        el, new_pos = read_element(buf, pos, explicit, endian, warn=warnings.append)
        if el is None:
            break
        if el.tag == (0x7FE0, 0x0010):
            pixel = el
            if el.undefined:
                frag_start = new_pos
                nfrag, new_pos = count_fragments(buf, frag_start)
                el.raw = buf[frag_start:new_pos]  # 片段+终止符的原始结构（不解码）
                el.frags = nfrag
            pos = new_pos
            continue
        dataset[(el.group, el.elem)] = el
        if el.vr == "SQ":
            if el.undefined:
                d = buf.find(b"\xfe\xff\xdd\xe0", new_pos)
                d = d if d >= 0 else len(buf)
                el.items = parse_items(buf, new_pos, d, endian, 0, warnings)
                pos = d + 4 if d < len(buf) else len(buf)
            else:
                el.items = parse_items(el.raw, 0, len(el.raw), endian, 0, warnings)
                pos = new_pos
            continue
        pos = new_pos
    return {"file_meta": meta, "dataset": dataset, "ts_uid": ts_uid, "ts_name": ts_name,
            "ts_class": ts_class, "pixel": pixel, "warnings": warnings}


def count_fragments(buf, pos):
    """封装像素内的 FFFE,E000 项：长度字段为 4 字节（区别于 SQ item 的 2 字节）。"""
    n = 0
    while pos + 6 <= len(buf):
        g, e = struct.unpack_from("<HH", buf, pos)
        if g != 0xFFFE:
            break
        if e == 0xE0DD:
            return n, pos + 6
        if e == 0xE000:
            ln = struct.unpack_from("<I", buf, pos + 4)[0]
            pos += 8 + ln
            n += 1
        else:
            break
    return n, pos


def sniff(buf):
    if len(buf) < 132:
        return False, "文件小于 132 字节"
    if buf[128:132] != b"DICM":
        return False, "缺少 128 字节前导 + 'DICM' 魔数"
    return True, "ok"


def read_file(path):
    try:
        with open(path, "rb") as f:
            return f.read()
    except OSError as e:
        err("无法读取文件: %s" % e, 2, file=path)


# ── 输出辅助 ───────────────────────────────────────────────────────────────
def get_str(parsed, tag, default=""):
    el = parsed["dataset"].get(tag) or parsed["file_meta"].get(tag)
    if el is None:
        return default
    v = el.value()
    return v if isinstance(v, str) else default


def get_num(parsed, tag, default=None):
    el = parsed["dataset"].get(tag) or parsed["file_meta"].get(tag)
    if el is None:
        return default
    v = el.value()
    if isinstance(v, list):
        return v[0] if v else default
    return v


def pixel_info(parsed):
    p = parsed["pixel"]
    d = {
        "present": p is not None,
        "rows": get_num(parsed, (0x0028, 0x0010)),
        "columns": get_num(parsed, (0x0028, 0x0011)),
        "bits_allocated": get_num(parsed, (0x0028, 0x0100)),
        "bits_stored": get_num(parsed, (0x0028, 0x0101)),
        "high_bit": get_num(parsed, (0x0028, 0x0102)),
        "pixel_representation": get_num(parsed, (0x0028, 0x0103)),
        "samples_per_pixel": get_num(parsed, (0x0028, 0x0002)),
        "photometric": get_str(parsed, (0x0028, 0x0004), ""),
        "frames": get_num(parsed, (0x0028, 0x0008), 1),
    }
    if p is not None:
        if p.undefined:
            d["encapsulated"] = True
            d["fragments"] = p.frags
            d["decodable_by_this_tool"] = False
            d["decoder_hint"] = ("pip install 'pydicom pylibjpeg[all]' 后运行："
                                 "python3 -c \"from pydicom import dcmread; "
                                 "ds=dcmread('FILE'); print(ds.pixel_array.shape)\"")
        else:
            d["encapsulated"] = False
            d["pixel_bytes"] = len(p.raw)
            d["decodable_by_this_tool"] = parsed["ts_class"] == "uncompressed_le"
    return d


def ts_view(parsed):
    return {"uid": parsed["ts_uid"], "name": parsed["ts_name"], "class": parsed["ts_class"]}


# ── 命令：summary / parse ──────────────────────────────────────────────────
def cmd_summary(args):
    buf = read_file(args.file)
    ok, why = sniff(buf)
    if not ok:
        err("不是 DICOM 文件: " + why, 2, file=args.file)
    parsed = parse_file(buf, [])
    sop_cls = get_str(parsed, (0x0002, 0x0001)) or get_str(parsed, (0x0008, 0x0016))
    out = {
        "command": "summary", "status": "ok", "tool": TOOL, "purpose": PURPOSE,
        "file": os.path.basename(args.file), "bytes": len(buf),
        "transfer_syntax": ts_view(parsed),
        "sop": {"class_uid": sop_cls,
                "class_name": SOP_CLASSES.get(sop_cls, "unknown"),
                "instance_uid": get_str(parsed, (0x0002, 0x0002)) or get_str(parsed, (0x0008, 0x0018))},
        "modality": get_str(parsed, (0x0008, 0x0060)),
        "patient": {"name": get_str(parsed, (0x0010, 0x0010)), "id": get_str(parsed, (0x0010, 0x0020)),
                    "sex": get_str(parsed, (0x0010, 0x0040)),
                    "birth_date": get_str(parsed, (0x0010, 0x0030))},
        "study": {"instance_uid": get_str(parsed, (0x0020, 0x000D)),
                  "date": get_str(parsed, (0x0008, 0x0020)),
                  "accession": get_str(parsed, (0x0008, 0x0050)),
                  "description": get_str(parsed, (0x0008, 0x1030))},
        "series": {"instance_uid": get_str(parsed, (0x0020, 0x000E)),
                   "number": get_num(parsed, (0x0020, 0x0011)),
                   "description": get_str(parsed, (0x0008, 0x103E))},
        "instance": {"number": get_num(parsed, (0x0020, 0x0013))},
        "image": pixel_info(parsed),
        "n_tags": len(parsed["dataset"]),
        "warnings": parsed["warnings"],
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))
    sys.exit(0)


def element_view(el, endian="<"):
    v = {"tag": tag_str(el.group, el.elem), "name": el.name, "vr": el.vr}
    if el.vr == "SQ":
        v["items"] = len(el.items) if el.items is not None else None
        if el.items:
            v["first_item_tags"] = [tag_str(g, e) for (g, e) in list(el.items[0].keys())[:10]]
        return v
    val = el.value(endian)
    if isinstance(val, bytes):
        v["value"] = {"bytes": len(val), "hex_preview": val[:32].hex() + ("…" if len(val) > 32 else "")}
    else:
        v["value"] = val
    return v


def cmd_parse(args):
    buf = read_file(args.file)
    ok, why = sniff(buf)
    if not ok:
        err("不是 DICOM 文件: " + why, 2, file=args.file)
    parsed = parse_file(buf, [])
    keep = None
    if args.tags:
        keep = set()
        for t in args.tags:
            t = t.strip().replace("[", "").replace("]", "").replace(" ", "")
            g, e = t.split(",")
            keep.add((int(g, 16), int(e, 16)))
    endian = ">" if parsed["ts_class"] == "big_endian" else "<"
    fm = [element_view(el, endian) for el in parsed["file_meta"].values()
          if keep is None or el.tag in keep]
    ds = [element_view(parsed["dataset"][k], endian) for k in sorted(parsed["dataset"])
          if keep is None or k in keep]
    out = {"command": "parse", "status": "ok", "tool": TOOL, "purpose": PURPOSE,
           "transfer_syntax": ts_view(parsed), "file_meta": fm, "dataset": ds,
           "n_tags": len(ds), "warnings": parsed["warnings"]}
    print(json.dumps(out, ensure_ascii=False, indent=2))
    sys.exit(0)


# ── 命令：pixels ───────────────────────────────────────────────────────────
def cmd_pixels(args):
    buf = read_file(args.file)
    ok, why = sniff(buf)
    if not ok:
        err("不是 DICOM 文件: " + why, 2, file=args.file)
    parsed = parse_file(buf, [])
    p = parsed["pixel"]
    if p is None:
        err("文件中没有 PixelData", 2)
    if p.undefined:
        hint = pixel_info(parsed)["decoder_hint"]
        err("像素为封装(压缩)格式 %s：本工具（纯标准库）不解码压缩像素，不会猜测像素值。" % parsed["ts_name"],
            2, decoder_hint=hint, fragments=p.frags)
    if parsed["ts_class"] != "uncompressed_le":
        err("仅支持未压缩小端像素导出（当前: %s）" % parsed["ts_name"], 2)
    rows = get_num(parsed, (0x0028, 0x0010))
    cols = get_num(parsed, (0x0028, 0x0011))
    bits = get_num(parsed, (0x0028, 0x0100))
    spp = get_num(parsed, (0x0028, 0x0002), 1)
    rep = get_num(parsed, (0x0028, 0x0103), 0)
    frames = get_num(parsed, (0x0028, 0x0008), 1)
    if not all(isinstance(x, int) for x in (rows, cols, bits, spp)):
        err("缺少必需的像素标签 (0028,0010)/(0028,0011)/(0028,0100)/(0028,0002)", 2)
    if bits not in (8, 16):
        err("仅支持 8/16 位像素导出（BitsAllocated=%s）" % bits, 2)
    if rep not in (0, 1):
        err("仅支持 PixelRepresentation 0/1（当前 %s）" % rep, 2)
    frame_bytes = rows * cols * spp * (bits // 8)
    if len(p.raw) < frame_bytes:
        err("PixelData 长度 %d 小于单帧所需 %d" % (len(p.raw), frame_bytes), 2)
    raw = p.raw[:frame_bytes]
    if bits == 16:
        vals = struct.unpack("<" + "H" * (len(raw) // 2), raw)
        if rep == 1:
            vals = tuple(v & 0xFFFF for v in vals)  # 有符号→无符号偏移（仅检视用）
        data = struct.pack(">" + "H" * len(vals), *vals)  # PNM 16 位为大端
        maxval = 65535
    else:
        data, maxval = raw, 255
    if spp == 1:
        header = "P5\n%d %d\n%d\n" % (cols, rows, maxval)
    elif spp == 3:
        header = "P6\n%d %d\n%d\n" % (cols, rows, maxval)
    else:
        err("仅支持 SamplesPerPixel 1 或 3 的 PNM 导出（当前 %s）" % spp, 2)
    with open(args.out, "wb") as f:
        f.write(header.encode("ascii") + data)
    print(json.dumps({"command": "pixels", "status": "ok", "tool": TOOL, "purpose": PURPOSE,
                      "out": args.out, "format": "PNM (P5 灰度 / P6 RGB)",
                      "rows": rows, "columns": cols, "maxval": maxval,
                      "frame": 1, "total_frames": frames,
                      "note": "多帧文件仅导出第 1 帧；直接位平面导出，非窗宽窗位渲染"},
                     ensure_ascii=False, indent=2))
    sys.exit(0)


# ── 命令：check ────────────────────────────────────────────────────────────
REQUIRED_META = ((0x0002, 0x0001), (0x0002, 0x0002), (0x0002, 0x0003))
REQUIRED_PIXEL = ((0x0028, 0x0010), (0x0028, 0x0011), (0x0028, 0x0100))


def cmd_check(args):
    buf = read_file(args.file)
    ok, why = sniff(buf)
    if not ok:
        err("不是 DICOM 文件: " + why, 2, file=args.file)
    findings = []
    parsed = parse_file(buf, [])
    for t in REQUIRED_META:
        if t not in parsed["file_meta"]:
            findings.append({"level": "error", "code": "missing_file_meta",
                             "tag": tag_str(*t), "name": TAG_NAMES.get(t, ""),
                             "message": "缺少 File Meta 必需标签"})
    if parsed["ts_class"] == "unknown":
        findings.append({"level": "error", "code": "unknown_transfer_syntax",
                         "tag": "[0002,0003]",
                         "message": "未识别的传输语法 UID %s（本工具仅识别常见子集；用 pydicom 处理）" % parsed["ts_uid"]})
    for w in parsed["warnings"]:
        findings.append({"level": "warn", "code": "parse_warning", "message": w})
    p = parsed["pixel"]
    if p is not None and not p.undefined and parsed["ts_class"] == "uncompressed_le":
        for t in REQUIRED_PIXEL:
            if t not in parsed["dataset"]:
                findings.append({"level": "error", "code": "missing_pixel_tag",
                                 "tag": tag_str(*t), "name": TAG_NAMES.get(t, ""),
                                 "message": "未压缩像素缺少必需标签"})
        rows = get_num(parsed, (0x0028, 0x0010))
        cols = get_num(parsed, (0x0028, 0x0011))
        bits = get_num(parsed, (0x0028, 0x0100))
        spp = get_num(parsed, (0x0028, 0x0002), 1)
        rep = get_num(parsed, (0x0028, 0x0103), 0)
        if all(isinstance(x, int) for x in (rows, cols, bits, spp)):
            expect = rows * cols * spp * (bits // 8)
            if len(p.raw) < expect:
                findings.append({"level": "error", "code": "pixel_too_short",
                                 "message": "PixelData %d 字节 < 单帧所需 %d 字节" % (len(p.raw), expect)})
            elif len(p.raw) > expect and (len(p.raw) % expect) != 0:
                findings.append({"level": "warn", "code": "pixel_length_odd",
                                 "message": "PixelData 长度不是单帧字节数的整数倍（%d vs %d）" % (len(p.raw), expect)})
        if rep not in (0, 1):
            findings.append({"level": "error", "code": "bad_pixel_representation",
                             "tag": "[0028,0103]", "message": "PixelRepresentation=%s（应为 0 或 1）" % rep})
    if p is not None and p.undefined and parsed["ts_uid"] == "1.2.840.10008.1.2.4.50" \
            and get_num(parsed, (0x0028, 0x0100)) == 16:
        findings.append({"level": "warn", "code": "jpeg8_with_16bit",
                         "tag": "[0002,0003]",
                         "message": "JPEG Baseline 8-bit (.4.50) 声明 16 位像素：该语法仅支持 8 位，常见于误配/损坏"})
    if p is not None and p.undefined:
        findings.append({"level": "info", "code": "encapsulated_pixel_data",
                         "tag": "[7FE0,0010]",
                         "message": "封装像素数据（%s，%s 个 fragment）：本工具不解码，属正常结构" % (
                             parsed["ts_name"], p.frags if p.frags is not None else "?")} )
    nerr = sum(1 for f in findings if f["level"] == "error")
    out = {"command": "check", "status": "ok" if nerr == 0 else "errors", "tool": TOOL,
           "purpose": PURPOSE, "transfer_syntax": ts_view(parsed),
           "findings": findings, "n_errors": nerr, "n_warnings": sum(1 for f in findings if f["level"] == "warn")}
    print(json.dumps(out, ensure_ascii=False, indent=2))
    sys.exit(3 if nerr else 0)


# ── 命令：deid（PS3.15 基础配置 子集）─────────────────────────────────────
# 动作：Z=置零/空 · X=移除 · D=哑值 · K=保留 · U=UID 重映射
# 依据 PS3.15 2026c §6.9/Annex E（权威 300+ 标签表）；此处为实现其直接标识符子集。
DEID_ACTIONS = {
    (0x0010, 0x0010): "Z",   # PatientName（Type 2：置零；不用移除以兼容严格读取器）
    (0x0010, 0x0020): "Z",   # PatientID
    (0x0010, 0x0030): "Z",   # PatientBirthDate
    (0x0010, 0x0032): "Z",   # PatientAge
    (0x0010, 0x1000): "X",   # OtherPatientIDs
    (0x0010, 0x1001): "X",   # OtherPatientNames
    (0x0010, 0x1040): "X",   # PatientAddress
    (0x0010, 0x2154): "X",   # PatientTelephoneNumbers
    (0x0008, 0x0050): "Z",   # AccessionNumber
    (0x0008, 0x0070): "Z",   # StationName
    (0x0008, 0x0080): "Z",   # InstitutionName
    (0x0008, 0x0081): "X",   # InstitutionAddress
    (0x0008, 0x0090): "Z",   # ReferringPhysicianName
    (0x0008, 0x0092): "Z",   # ReferringPhysicianAddress
    (0x0008, 0x1040): "Z",   # InstitutionalDepartmentName
    (0x0008, 0x1048): "Z",   # PhysiciansOfRecord
    (0x0008, 0x1050): "Z",   # PerformingPhysicianName
    (0x0008, 0x1070): "Z",   # OperatorsName
    (0x0008, 0x1110): "Z",   # ReferringPhysicianIdentificationSequence
    (0x0020, 0x0010): "Z",   # StudyID
}
UID_TAGS = ((0x0002, 0x0002), (0x0008, 0x0018), (0x0020, 0x000D), (0x0020, 0x000E),
            (0x0020, 0x0052), (0x0020, 0x0070), (0x0040, 0x0551))

DEID_LIMITATIONS = [
    "本工具实现 PS3.15 基础配置的直接标识符子集（约 20 标签）；权威完整表为 PS3.15 2026c Annex E（300+ 标签），生产使用前必须对照完整配置核实",
    "像素内烧录的注释/水印（burned-in annotations）不检测、不移除",
    "本工具输出不等同于合规认证（如 HIPAA Safe Harbor / GDPR 匿名化）",
    "UID 重映射为确定性哈希（同一 UID→同一新 UID，批次内一致），不保存/不输出重映射表",
]


def _enc_explicit(tag, vr, value_bytes):
    g, e = tag
    if vr in LONG_VR:
        return (struct.pack("<HH", g, e) + vr.encode("ascii") + b"\x00\x00\x00\x00" +
                struct.pack("<I", len(value_bytes)) + value_bytes)
    return (struct.pack("<HH", g, e) + vr.encode("ascii") + b"\x00\x00" +
            struct.pack("<H", len(value_bytes)) + value_bytes)


def _pad(b):
    return b + (b" " if len(b) % 2 else b"")


def _str_bytes(s):
    return _pad(s.encode("ascii", errors="replace"))


def _uid_bytes(s):
    b = s.encode("ascii")
    return b + (b"\x00" if len(b) % 2 else b"")


def _num_bytes(vr, val):
    if vr == "US":
        return struct.pack("<H", val & 0xFFFF)
    if vr == "SS":
        return struct.pack("<h", val)
    if vr == "UL":
        return struct.pack("<I", val & 0xFFFFFFFF)
    if vr == "SL":
        return struct.pack("<i", val)
    if vr == "DS":
        return _pad(str(val).encode("ascii"))
    if vr == "IS":
        return _pad(str(val).encode("ascii"))
    return _pad(str(val).encode("ascii"))


def deid_element(el, stats, in_meta=False):
    """返回 (new_tag_or_None, vr, value_bytes)。None = 移除。"""
    tag = el.tag
    if in_meta:
        if tag == (0x0002, 0x0002):  # MediaStorageSOPInstanceUID → U
            v = el.value()
            if isinstance(v, str):
                stats["uids"] += 1
                return tag, "UI", _uid_bytes(remap_uid(v))
        return tag, el.vr, el.raw if el.raw is not None else b""
    # 私有标签 → 移除（最常见泄漏源）
    if tag[0] & 1:
        stats["private_removed"] += 1
        return None, None, None
    if tag in DEID_ACTIONS:
        act = DEID_ACTIONS[tag]
        if act == "X":
            stats["removed"] += 1
            return None, None, None
        stats["zeroed"] += 1
        return tag, el.vr, b""
    if tag in UID_TAGS:
        v = el.value()
        if isinstance(v, str) and v.startswith("1."):
            stats["uids"] += 1
            return tag, "UI", _uid_bytes(remap_uid(v))
        return tag, el.vr, el.raw
    if el.vr in ("DA", "DT", "TM"):
        stats["dates"] += 1
        dummy = {"DA": b"19000101", "DT": b"19000101000000.000000", "TM": b"000000.000000"}[el.vr]
        return tag, el.vr, _pad(dummy)
    # 其余：按原 VR 保留（UI 类型但不在 UID_TAGS 的也原样保留）
    return tag, el.vr, el.raw


def reserialize_item(item):
    """item dict{tag:Element} → 字节（显式 VR，defined length）。"""
    out = b""
    for (g, e), el in sorted(item.items()):
        enc = deid_element(el, {"uids": 0, "private_removed": 0, "zeroed": 0, "removed": 0, "dates": 0})
        if enc is None or enc[0] is None:
            continue
        tag, vr, vb = enc
        if vr in LONG_VR and vb == b"" and vr == "SQ":
            out += struct.pack("<HH", tag[0], tag[1]) + b"SQ\x00\x00\x00\x00" + struct.pack("<I", 0)
        else:
            out += _enc_explicit(tag, vr if vr not in (None,) else "LO", vb)
    return out


def cmd_deid(args):
    buf = read_file(args.file)
    ok, why = sniff(buf)
    if not ok:
        err("不是 DICOM 文件: " + why, 2, file=args.file)
    warnings = []
    parsed = parse_file(buf, warnings)
    if parsed["ts_class"] == "deflated":
        err("deflated 传输语法：本工具不去标识化该格式，请先用 pydicom 转码为未压缩", 2)
    stats = {"uids": 0, "private_removed": 0, "zeroed": 0, "removed": 0, "dates": 0}
    # File meta（总是显式小端）
    meta_body = b""
    for el in parsed["file_meta"].values():
        if el.tag == (0x0002, 0x0000):
            continue  # group length 稍后重建
        enc = deid_element(el, stats, in_meta=True)
        if enc is not None and enc[0] is not None:
            meta_body += _enc_explicit(enc[0], enc[1], enc[2])
    meta_out = _enc_explicit((0x0002, 0x0000), "UL", struct.pack("<I", len(meta_body))) + meta_body
    # 数据集（保持原文件 VR 编码：仅 1.2.840.10008.1.2 为隐式，其余含封装均为显式）
    explicit = parsed["ts_uid"] != "1.2.840.10008.1.2"
    ds_out = b""
    for (g, e), el in parsed["dataset"].items():
        if (g, e) == (0x7FE0, 0x0010):
            continue  # 像素在循环后统一重写
        if (g, e) in ((0x0012, 0x0062), (0x0012, 0x0063)):
            continue  # 旧声明移除，循环后统一写入新声明
        enc = deid_element(el, stats)
        if enc is None or enc[0] is None:
            continue
        tag, vr, vb = enc
        if vr == "SQ" and el.items is not None:
            item_bytes = b""
            for item in el.items:
                ib = reserialize_item(item)
                item_bytes += struct.pack("<HHH", 0xFFFE, 0xE000, len(ib)) + ib
            ds_out += _enc_explicit(tag, "SQ", item_bytes)
            continue
        if explicit:
            ds_out += _enc_explicit(tag, vr, vb)
        else:
            ds_out += struct.pack("<HHH", tag[0], tag[1], len(vb)) + vb
    # 去标识化声明（PS3.15）：0012,0062 = YES；0012,0063 = SQ[{113040, DCM}]
    decl_item = (_enc_explicit((0x0008, 0x0070), "SH", _str_bytes("113040")) +
                 _enc_explicit((0x0008, 0x0080), "SH", _str_bytes("DCM")) +
                 _enc_explicit((0x0008, 0x0102), "LO", _str_bytes(
                     "De-identification using Basic Application Level Confidentiality Profile")))
    decl_sq = struct.pack("<HHH", 0xFFFE, 0xE000, len(decl_item)) + decl_item
    if explicit:
        ds_out += _enc_explicit((0x0012, 0x0062), "CS", _str_bytes("YES"))
        ds_out += _enc_explicit((0x0012, 0x0063), "SQ", decl_sq)
    else:
        ds_out += struct.pack("<HHH", 0x0012, 0x0062, len(_str_bytes("YES"))) + _str_bytes("YES")
        ds_out += struct.pack("<HHH", 0x0012, 0x0063, len(decl_sq)) + decl_sq
    # 像素
    if parsed["pixel"] is not None:
        p = parsed["pixel"]
        if p.undefined:
            # 封装结构原样复制（p.raw = 片段+终止符，parse 时已截取）
            ds_out += (struct.pack("<HH", 0x7FE0, 0x0010) + b"OW\x00\x00\x00\x00" +
                       struct.pack("<I", 0xFFFFFFFF) + p.raw)
        else:
            pv = p.raw + (b"\x00" if len(p.raw) % 2 else b"")
            ds_out += (_enc_explicit((0x7FE0, 0x0010), "OW", pv) if explicit else
                       struct.pack("<HHH", 0x7FE0, 0x0010, len(pv)) + pv)
    out = b"\x00" * 128 + b"DICM" + meta_out + ds_out
    with open(args.out, "wb") as f:
        f.write(out)
    print(json.dumps({"command": "deid", "status": "ok", "tool": TOOL, "purpose": PURPOSE,
                      "out": args.out, "bytes": len(out),
                      "stats": {"uids_remapped": stats["uids"],
                                "private_tags_removed": stats["private_removed"],
                                "tags_zeroed": stats["zeroed"], "tags_removed": stats["removed"],
                                "dates_scrubbed": stats["dates"]},
                      "declaration": {"PatientIdentityRemoved": "YES",
                                      "DeidentificationMethodCodeSequence": "113040 / DCM"},
                      "limitations": DEID_LIMITATIONS},
                     ensure_ascii=False, indent=2))
    sys.exit(0)


# ── 命令：gen（确定性合成测试文件，无真实 PHI）────────────────────────────
def _uid(seed, kind):
    h = hashlib.sha256(("dicwork-test-%d-%s" % (seed, kind)).encode("ascii")).hexdigest()
    return "1.2.826.0.1.3680043.8.498.test." + h[:16]


def make_pixels(rows, cols, bits=16):
    """确定性图案：对角渐变 + 白方块（位于 8,8，32x32，越界则整行）。"""
    px = bytearray()
    for r in range(rows):
        for c in range(cols):
            if bits == 8:
                v = ((r + c) * 250) % 256
                full = 255
            else:
                v = ((r + c) * 1000) % 4096
                full = 4095
            if 8 <= r < min(rows, 40) and 8 <= c < min(cols, 40):
                v = full
            px += struct.pack("<B" if bits == 8 else "<H", v)
    return bytes(px)


def cmd_gen(args):
    rows, cols, seed, bits = args.rows, args.cols, args.seed, args.bits
    explicit = args.vr == "explicit"
    ts = "1.2.840.10008.1.2.1" if explicit else "1.2.840.10008.1.2"
    px = make_pixels(rows, cols, bits)
    pnum = b"1"
    if args.encapsulated:
        ts = "1.2.840.10008.1.2.4.50"
        frag = b"\xff\xd8\xff\xe0\x00\x10STUB" + b"\x00" * 16
        pd = (struct.pack("<HH", 0xFFFE, 0xE000) + struct.pack("<I", len(frag)) + frag +
              struct.pack("<HH", 0xFFFE, 0xE0DD) + b"\x00\x00")
        pd_inline = False
    else:
        pd = px + (b"\x00" if len(px) % 2 else b"")
        pd_inline = True

    def E(tag, vr, b):  # 显式
        return _enc_explicit(tag, vr, b)

    def I(tag, b):      # 隐式
        g, e = tag
        return struct.pack("<HHH", g, e, len(b)) + b

    study_uid, series_uid, inst_uid = _uid(seed, "study"), _uid(seed, "series"), _uid(seed, "instance")
    pname = ("TESTPATIENT^SYNTH^%04d" % seed).encode("ascii")
    pid = ("SYN-PAT-%06d" % (100000 + seed * 7)).encode("ascii")
    ds = b""
    if explicit:
        ds += E((0x0008, 0x0016), "UI", _uid_bytes("1.2.840.10008.5.1.4.1.1.2"))
        ds += E((0x0008, 0x0018), "UI", _uid_bytes(inst_uid))
        ds += E((0x0008, 0x0060), "CS", b"CT ")
        ds += E((0x0008, 0x0008), "CS", b"ORIGINAL^PRIMARY^AXIAL")
        ds += E((0x0008, 0x0050), "SH", _pad(("ACC-%04d" % (seed % 10000)).encode()))
        ds += E((0x0008, 0x0020), "DA", b"20260101")
        ds += E((0x0020, 0x000D), "UI", _uid_bytes(study_uid))
        ds += E((0x0020, 0x000E), "UI", _uid_bytes(series_uid))
        ds += E((0x0020, 0x0011), "IS", pnum)
        ds += E((0x0020, 0x0013), "IS", pnum)
        ds += E((0x0010, 0x0010), "PN", _pad(pname))
        ds += E((0x0010, 0x0020), "LO", _pad(pid))
        ds += E((0x0010, 0x0030), "DA", b"19850715")
        ds += E((0x0010, 0x0040), "CS", b"O ")
        ds += E((0x0008, 0x0080), "LO", b"Synthetic Hospital  ")
        ds += E((0x0008, 0x0090), "PN", _pad(b"REF^PHYSICIAN"))
        ds += E((0x0008, 0x0070), "SH", _pad(b"STATION-01"))
        ds += E((0x0020, 0x0010), "SH", _pad(("STUDY-%03d" % (seed % 100)).encode()))
        ds += E((0x0009, 0x0010), "LO", b"PRIVATE-SECRET")
        ds += E((0x0028, 0x0002), "US", struct.pack("<H", 1))
        ds += E((0x0028, 0x0004), "CS", b"MONOCHROME2")
        ds += E((0x0028, 0x0008), "IS", pnum)
        ds += E((0x0028, 0x0010), "US", struct.pack("<H", rows))
        ds += E((0x0028, 0x0011), "US", struct.pack("<H", cols))
        ds += E((0x0028, 0x0100), "US", struct.pack("<H", bits))
        ds += E((0x0028, 0x0101), "US", struct.pack("<H", bits - 4))
        ds += E((0x0028, 0x0102), "US", struct.pack("<H", bits - 5))
        ds += E((0x0028, 0x0103), "US", struct.pack("<H", 0))
        if args.encapsulated:
            ds += struct.pack("<HH", 0x7FE0, 0x0010) + b"OW\x00\x00\x00\x00" + struct.pack("<I", 0xFFFFFFFF) + pd
        else:
            ds += E((0x7FE0, 0x0010), "OW", px)
    else:
        ds += I((0x0008, 0x0016), _uid_bytes("1.2.840.10008.5.1.4.1.1.2"))
        ds += I((0x0008, 0x0018), _uid_bytes(inst_uid))
        ds += I((0x0008, 0x0060), b"CT ")
        ds += I((0x0008, 0x0008), b"ORIGINAL^PRIMARY^AXIAL")
        ds += I((0x0008, 0x0050), _pad(("ACC-%04d" % (seed % 10000)).encode()))
        ds += I((0x0008, 0x0020), b"20260101")
        ds += I((0x0020, 0x000D), _uid_bytes(study_uid))
        ds += I((0x0020, 0x000E), _uid_bytes(series_uid))
        ds += I((0x0020, 0x0011), pnum)
        ds += I((0x0020, 0x0013), pnum)
        ds += I((0x0010, 0x0010), _pad(pname))
        ds += I((0x0010, 0x0020), _pad(pid))
        ds += I((0x0010, 0x0030), b"19850715")
        ds += I((0x0010, 0x0040), b"O ")
        ds += I((0x0008, 0x0080), b"Synthetic Hospital  ")
        ds += I((0x0008, 0x0090), _pad(b"REF^PHYSICIAN"))
        ds += I((0x0008, 0x0070), _pad(b"STATION-01"))
        ds += I((0x0020, 0x0010), _pad(("STUDY-%03d" % (seed % 100)).encode()))
        ds += I((0x0009, 0x0010), b"PRIVATE-SECRET")
        ds += I((0x0028, 0x0002), struct.pack("<H", 1))
        ds += I((0x0028, 0x0004), b"MONOCHROME2")
        ds += I((0x0028, 0x0008), pnum)
        ds += I((0x0028, 0x0010), struct.pack("<H", rows))
        ds += I((0x0028, 0x0011), struct.pack("<H", cols))
        ds += I((0x0028, 0x0100), struct.pack("<H", bits))
        ds += I((0x0028, 0x0101), struct.pack("<H", bits - 4))
        ds += I((0x0028, 0x0102), struct.pack("<H", bits - 5))
        ds += I((0x0028, 0x0103), struct.pack("<H", 0))
        if args.encapsulated:
            ds += struct.pack("<HH", 0x7FE0, 0x0010) + b"OW\x00\x00\x00\x00" + struct.pack("<I", 0xFFFFFFFF) + pd
        else:
            ds += I((0x7FE0, 0x0010), px)
    body = E((0x0002, 0x0001), "UI", _uid_bytes("1.2.840.10008.5.1.4.1.1.2")) + \
        E((0x0002, 0x0002), "UI", _uid_bytes(inst_uid)) + \
        E((0x0002, 0x0003), "UI", _uid_bytes(ts))
    meta = E((0x0002, 0x0000), "UL", struct.pack("<I", len(body))) + body
    out = b"\x00" * 128 + b"DICM" + meta + ds
    with open(args.out, "wb") as f:
        f.write(out)
    print(json.dumps({"command": "gen", "status": "ok", "tool": TOOL, "out": args.out,
                      "bytes": len(out), "rows": rows, "columns": cols, "seed": seed, "bits": bits,
                      "transfer_syntax": ts, "encapsulated": bool(args.encapsulated),
                      "synthetic": "合成测试数据，非真实 PHI；相同参数输出字节相同（无时间戳）"},
                     ensure_ascii=False, indent=2))
    sys.exit(0)


def main():
    p = argparse.ArgumentParser(prog="dicom_tools.py", description=TOOL + "（纯标准库、离线、确定性）")
    sub = p.add_subparsers(dest="command", required=True)

    sp = sub.add_parser("summary", help="紧凑摘要（默认推荐，省 token）")
    sp.add_argument("file")
    sp.set_defaults(fn=cmd_summary)

    sp = sub.add_parser("parse", help="完整标签转储")
    sp.add_argument("file")
    sp.add_argument("--tags", nargs="+", default=None,
                    help="仅显示指定标签，每个参数一个 GGGG,EEEE，如 --tags 0010,0020 0028,0010")
    sp.set_defaults(fn=cmd_parse)

    sp = sub.add_parser("pixels", help="导出未压缩像素为 PNM")
    sp.add_argument("file")
    sp.add_argument("--out", required=True)
    sp.set_defaults(fn=cmd_pixels)

    sp = sub.add_parser("check", help="一致性检查（exit 3=有错误）")
    sp.add_argument("file")
    sp.set_defaults(fn=cmd_check)

    sp = sub.add_parser("deid", help="PS3.15 基础配置子集去标识化")
    sp.add_argument("file")
    sp.add_argument("--out", required=True)
    sp.set_defaults(fn=cmd_deid)

    sp = sub.add_parser("gen", help="生成确定性合成测试 DICOM（无真实 PHI）")
    sp.add_argument("--out", required=True)
    sp.add_argument("--rows", type=int, default=64)
    sp.add_argument("--cols", type=int, default=64)
    sp.add_argument("--seed", type=int, default=7)
    sp.add_argument("--bits", type=int, choices=[8, 16], default=16)
    sp.add_argument("--vr", choices=["explicit", "implicit"], default="explicit")
    sp.add_argument("--encapsulated", action="store_true")
    sp.set_defaults(fn=cmd_gen)

    args = p.parse_args()
    try:
        args.fn(args)
    except SystemExit:
        raise
    except Exception as e:
        err("未预期错误: %s: %s" % (type(e).__name__, e), 2)


if __name__ == "__main__":
    main()
