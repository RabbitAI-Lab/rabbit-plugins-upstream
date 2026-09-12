#!/usr/bin/env python3
"""selftest.py — dicom-tools v2.0.0 离线自检（确定性，无网络，合成数据）

运行：python3 scripts/selftest.py
全部 PASS 才可交付。检查组：
  G1 生成器确定性  G2 显式解析  G3 隐式解析  G4 封装检测
  G5 像素导出  G6 诚实拒绝  G7 check 语义  G8 deid PHI 清零
  G9 deid UID/声明  G10 deid 隐式/封装  G11 CLI 契约与文档
"""
import importlib.util
import json
import os
import struct
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
TOOL = os.path.join(HERE, "dicom_tools.py")
T = tempfile.mkdtemp(prefix="dicselftest_")

RESULTS = []


def check(group, name, ok, dbg=""):
    RESULTS.append((group, name, bool(ok), dbg))


def run(*args):
    return subprocess.run([sys.executable, TOOL, *args],
                          capture_output=True, text=True, timeout=120)


def jout(r):
    return json.loads(r.stdout) if r.stdout.strip() else None


def jerr(r):
    return json.loads(r.stderr) if r.stderr.strip() else None


def gen(path, *extra):
    run("gen", "--out", path, *extra)


def load():
    spec = importlib.util.spec_from_file_location("dt", TOOL)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main():
    dt = load()
    f_exp = T + "/e.dcm"
    f_imp = T + "/i.dcm"
    f_jpg = T + "/j.dcm"
    f_8 = T + "/e8.dcm"
    gen(f_exp, "--rows", "32", "--cols", "32", "--seed", "7")
    gen(f_imp, "--vr", "implicit", "--rows", "32", "--cols", "32", "--seed", "7")
    gen(f_jpg, "--encapsulated", "--rows", "32", "--cols", "32", "--seed", "7")
    gen(f_8, "--bits", "8", "--rows", "32", "--cols", "32", "--seed", "7")

    # ── G1 生成器确定性 ─────────────────────────────────────────────────
    g1 = "G1-gen-determinism"
    gen(T + "/e2.dcm", "--rows", "32", "--cols", "32", "--seed", "7")
    check(g1, "explicit 字节一致", open(f_exp, "rb").read() == open(T + "/e2.dcm", "rb").read())
    gen(T + "/i2.dcm", "--vr", "implicit", "--rows", "32", "--cols", "32", "--seed", "7")
    check(g1, "implicit 字节一致", open(f_imp, "rb").read() == open(T + "/i2.dcm", "rb").read())
    gen(T + "/j2.dcm", "--encapsulated", "--rows", "32", "--cols", "32", "--seed", "7")
    check(g1, "encapsulated 字节一致", open(f_jpg, "rb").read() == open(T + "/j2.dcm", "rb").read())
    gen(T + "/s8.dcm", "--rows", "32", "--cols", "32", "--seed", "8")
    check(g1, "不同 seed 不同文件", open(f_exp, "rb").read() != open(T + "/s8.dcm", "rb").read())
    gen(T + "/b64.dcm", "--rows", "64", "--cols", "64", "--seed", "7")
    check(g1, "64x64 大于 32x32", os.path.getsize(T + "/b64.dcm") > os.path.getsize(f_exp))
    b = open(f_exp, "rb").read()
    check(g1, "前导 128 零 + DICM 魔数", b[:128] == b"\x00" * 128 and b[128:132] == b"DICM")
    check(g1, "meta 含正确 TS UID", b"1.2.840.10008.1.2.1" in b)
    check(g1, "8-bit 文件不同", os.path.getsize(f_8) < os.path.getsize(f_exp))

    # ── G2 显式解析 ─────────────────────────────────────────────────────
    g2 = "G2-parse-explicit"
    d = jout(run("summary", f_exp))
    check(g2, "summary 有效 JSON", d is not None)
    check(g2, "modality=CT", d["modality"] == "CT")
    check(g2, "patient 名", d["patient"]["name"] == "TESTPATIENT^SYNTH^0007")
    check(g2, "patient id", d["patient"]["id"] == "SYN-PAT-100049")
    check(g2, "ts=Explicit VR LE", d["transfer_syntax"]["class"] == "uncompressed_le")
    check(g2, "sop class 名 CT", d["sop"]["class_name"] == "CT Image Storage")
    img = d["image"]
    check(g2, "rows/cols/bits", img["rows"] == 32 and img["columns"] == 32 and img["bits_allocated"] == 16)
    check(g2, "pixel_bytes=2048", img["pixel_bytes"] == 2048 and img["encapsulated"] is False)
    check(g2, "n_tags>=20", d["n_tags"] >= 20)
    check(g2, "series/instance 号", d["series"]["number"] == "1" and d["instance"]["number"] == "1")
    p = jout(run("parse", f_exp, "--tags", "0010,0020", "0028,0010"))
    check(g2, "--tags 过滤只留指定标签", len(p["dataset"]) == 2
          and p["dataset"][0]["tag"] == "[0010,0020]" and p["dataset"][1]["tag"] == "[0028,0010]")
    check(g2, "parse 值类型", p["dataset"][0]["value"] == "SYN-PAT-100049" and p["dataset"][1]["value"] == 32)

    # ── G3 隐式解析 ─────────────────────────────────────────────────────
    g3 = "G3-parse-implicit"
    d = jout(run("summary", f_imp))
    check(g3, "summary 有效 JSON", d is not None)
    check(g3, "ts=Implicit VR LE", d["transfer_syntax"]["class"] == "uncompressed_le"
          and d["transfer_syntax"]["uid"] == "1.2.840.10008.1.2")
    check(g3, "patient 名一致", d["patient"]["name"] == "TESTPATIENT^SYNTH^0007")
    check(g3, "rows/cols 一致", d["image"]["rows"] == 32 and d["image"]["columns"] == 32)
    check(g3, "无警告", d["warnings"] == [])
    check(g3, "modality CT", d["modality"] == "CT")

    # ── G4 封装检测 ─────────────────────────────────────────────────────
    g4 = "G4-encapsulated-detect"
    d = jout(run("summary", f_jpg))
    check(g4, "ts=JPEG Baseline", d["transfer_syntax"]["name"].startswith("JPEG Baseline"))
    check(g4, "encapsulated=True", d["image"]["encapsulated"] is True)
    check(g4, "fragments=1", d["image"]["fragments"] == 1)
    check(g4, "decodable_by_this_tool=False", d["image"]["decodable_by_this_tool"] is False)
    check(g4, "decoder_hint 含 pylibjpeg", "pylibjpeg" in d["image"]["decoder_hint"])
    c = run("check", f_jpg)
    dc = jout(c)
    check(g4, "check 报 info encapsulated", any(f["code"] == "encapsulated_pixel_data" for f in dc["findings"])
          and c.returncode == 0)

    # ── G5 像素导出 ─────────────────────────────────────────────────────
    g5 = "G5-pixels-export"
    r = run("pixels", f_exp, "--out", T + "/e.pnm")
    check(g5, "pixels exit 0", r.returncode == 0)
    data = open(T + "/e.pnm", "rb").read()
    check(g5, "P5 头 16 位", data.startswith(b"P5\n32 32\n65535\n"))
    check(g5, "PNM 大小", len(data) == 15 + 2048)
    vals = struct.unpack(">" + "H" * 1024, data[15:])
    okpat = all(vals[rr * 32 + cc] == (4095 if 8 <= rr < 40 and 8 <= cc < 40 else ((rr + cc) * 1000) % 4096)
                for rr in range(32) for cc in range(32))
    check(g5, "16 位图案 1024/1024", okpat)
    check(g5, "白方块 4095", vals[9 * 32 + 9] == 4095)
    check(g5, "对角渐变值", vals[0] == 0 and vals[31] == 31000 % 4096)
    r = run("pixels", f_imp, "--out", T + "/i.pnm")
    check(g5, "implicit 像素导出", r.returncode == 0 and open(T + "/i.pnm", "rb").read() == data)
    r = run("pixels", f_8, "--out", T + "/e8.pnm")
    d8 = open(T + "/e8.pnm", "rb").read()
    h8 = b"P5\n32 32\n255\n"
    check(g5, "8-bit P5 头 255", r.returncode == 0 and d8.startswith(h8))
    check(g5, "8-bit 图案", d8[len(h8)] == 0 and d8[len(h8) + 9 * 32 + 9] == 255)

    # ── G6 诚实拒绝 ─────────────────────────────────────────────────────
    g6 = "G6-honest-refusal"
    r = run("pixels", f_jpg, "--out", T + "/x.pnm")
    check(g6, "封装 pixels exit 2", r.returncode == 2)
    e = jerr(r)
    check(g6, "错误 JSON 到 stderr", e is not None and e["status"] == "error")
    check(g6, "拒绝原因说明不解码", "不解码" in e["error"] and "pylibjpeg" in e["decoder_hint"])
    check(g6, "未生成输出文件", not os.path.exists(T + "/x.pnm"))
    open(T + "/notd.bin", "wb").write(b"hello world this is not a dicom file, definitely not dicom" * 4)
    r = run("summary", T + "/notd.bin")
    check(g6, "非 DICOM exit 2", r.returncode == 2 and "不是 DICOM" in jerr(r)["error"])
    r = run("summary", T + "/missing.dcm")
    check(g6, "缺文件 exit 2", r.returncode == 2)

    # ── G7 check 语义 ───────────────────────────────────────────────────
    g7 = "G7-check-semantics"
    r = run("check", f_exp)
    c = jout(r)
    check(g7, "干净文件 exit 0", r.returncode == 0 and c["n_errors"] == 0)
    open(T + "/trunc.dcm", "wb").write(open(f_exp, "rb").read()[:2500])
    r = run("check", T + "/trunc.dcm")
    c = jout(r)
    check(g7, "截断像素 exit 3", r.returncode == 3 and c["n_errors"] >= 1)
    check(g7, "截断原因 pixel_too_short", any(f["code"] == "pixel_too_short" for f in c["findings"]))
    gen(T + "/j16.dcm", "--encapsulated", "--bits", "16", "--rows", "32", "--cols", "32", "--seed", "7")
    c = jout(run("check", T + "/j16.dcm"))
    check(g7, "4.50+16bit 告警", any(f["code"] == "jpeg8_with_16bit" for f in c["findings"]))
    r = run("check", T + "/notd.bin")
    check(g7, "非 DICOM check exit 2", r.returncode == 2)
    ri = run("check", f_imp)
    ci = jout(ri)
    check(g7, "implicit 干净 exit 0", ri.returncode == 0 and ci["n_errors"] == 0)

    # ── G8 deid PHI 清零 ────────────────────────────────────────────────
    g8 = "G8-deid-phi-removal"
    r = run("deid", f_exp, "--out", T + "/e_deid.dcm")
    check(g8, "deid exit 0", r.returncode == 0)
    deidb = open(T + "/e_deid.dcm", "rb").read()
    orig = open(f_exp, "rb").read()
    for phi in [b"TESTPATIENT", b"SYN-PAT-", b"19850715", b"Synthetic Hospital",
                b"REF^PHYSICIAN", b"STATION-01", b"ACC-", b"PRIVATE-SECRET", b"20260101"]:
        check(g8, "PHI 消失: " + phi.decode(), phi in orig and phi not in deidb)
    w = []
    pd_ = dt.parse_file(deidb, w)
    check(g8, "deid 回读无警告", w == [])
    check(g8, "PatientName 置空但保留", (0x0010, 0x0010) in pd_["dataset"]
          and pd_["dataset"][(0x0010, 0x0010)].value() == "")
    check(g8, "PatientID 置空但保留", (0x0010, 0x0020) in pd_["dataset"]
          and pd_["dataset"][(0x0010, 0x0020)].value() == "")
    check(g8, "PatientSex 保留", dt.get_str(pd_, (0x0010, 0x0040)) == "O")
    check(g8, "StudyDate 清洗", dt.get_str(pd_, (0x0008, 0x0020)) == "19000101")
    check(g8, "像素逐字节不变", dt.parse_file(orig, [])["pixel"].raw == pd_["pixel"].raw)
    stats = jout(r)["stats"]
    check(g8, "stats 数值", stats["uids_remapped"] == 4 and stats["private_tags_removed"] == 1
          and stats["tags_zeroed"] == 8 and stats["dates_scrubbed"] == 1)

    # ── G9 deid UID/声明 ────────────────────────────────────────────────
    g9 = "G9-deid-uid-declaration"
    wo = []
    po = dt.parse_file(orig, wo)
    study_old = dt.get_str(po, (0x0020, 0x000D))
    study_new = dt.get_str(pd_, (0x0020, 0x000D))
    check(g9, "Study UID 重映射前缀", study_new.startswith(dt.UID_PREFIX) and study_new != study_old)
    check(g9, "remap 可复现", dt.remap_uid(study_old) == study_new)
    check(g9, "Series UID 一致映射", dt.get_str(pd_, (0x0020, 0x000E))
          == dt.remap_uid(dt.get_str(po, (0x0020, 0x000E))))
    check(g9, "SOP Instance 一致映射", dt.get_str(pd_, (0x0008, 0x0018))
          == dt.remap_uid(dt.get_str(po, (0x0008, 0x0018))))
    check(g9, "Meta SOP Instance 一致映射",
          dt.get_str(pd_, (0x0002, 0x0002)) == dt.remap_uid(dt.get_str(po, (0x0002, 0x0002))))
    check(g9, "PatientIdentityRemoved=YES", dt.get_str(pd_, (0x0012, 0x0062)) == "YES")
    dseq = pd_["dataset"].get((0x0012, 0x0063))
    it = dseq.items[0] if dseq and dseq.items else {}
    check(g9, "声明 SQ 存在", bool(it))
    check(g9, "CodeValue=113040", it.get((0x0008, 0x0070), dt.Element(0, 0, "SH", b"")).value() == "113040")
    check(g9, "Scheme=DCM", it.get((0x0008, 0x0080), dt.Element(0, 0, "SH", b"")).value() == "DCM")
    check(g9, "私有标签归零", all((k[0] & 1) == 0 for k in pd_["dataset"]))
    r2 = run("deid", T + "/e_deid.dcm", "--out", T + "/e_deid2.dcm")
    w2 = []
    p2 = dt.parse_file(open(T + "/e_deid2.dcm", "rb").read(), w2)
    k2 = list(p2["dataset"].keys())
    check(g9, "二次 deid 无重复声明", k2.count((0x0012, 0x0062)) == 1 and k2.count((0x0012, 0x0063)) == 1)
    check(g9, "二次 deid 仍无 PHI", b"TESTPATIENT" not in open(T + "/e_deid2.dcm", "rb").read())

    # ── G10 deid 隐式/封装 ──────────────────────────────────────────────
    g10 = "G10-deid-implicit-encaps"
    run("deid", f_imp, "--out", T + "/i_deid.dcm")
    w = []
    pi = dt.parse_file(open(T + "/i_deid.dcm", "rb").read(), w)
    check(g10, "implicit deid 回读无警告", w == [])
    check(g10, "implicit deid 声明 YES", dt.get_str(pi, (0x0012, 0x0062)) == "YES")
    check(g10, "implicit deid 无 PHI", b"TESTPATIENT" not in open(T + "/i_deid.dcm", "rb").read())
    check(g10, "implicit deid 像素不变", dt.parse_file(open(f_imp, "rb").read(), [])["pixel"].raw
          == pi["pixel"].raw)
    r = run("deid", f_jpg, "--out", T + "/j_deid.dcm")
    check(g10, "encapsulated deid exit 0", r.returncode == 0)
    pj = dt.parse_file(open(T + "/j_deid.dcm", "rb").read(), [])
    check(g10, "封装结构原样保留", dt.parse_file(open(f_jpg, "rb").read(), [])["pixel"].raw
          == pj["pixel"].raw and pj["pixel"].frags == 1)
    check(g10, "encapsulated deid 无 PHI", b"TESTPATIENT" not in open(T + "/j_deid.dcm", "rb").read())

    # ── G11 CLI 契约与文档 ──────────────────────────────────────────────
    g11 = "G11-cli-contract"
    for cmd in (["summary", f_exp], ["parse", f_exp], ["check", f_exp]):
        r = run(*cmd)
        ok = r.stdout.strip().startswith("{") and json.loads(r.stdout)["tool"].endswith("v2.0.0")
        check(g11, "JSON 输出带 tool: " + cmd[0], ok)
    r = run("summary", T + "/notd.bin")
    e = jerr(r)
    check(g11, "错误 JSON 含 tool+error", e is not None and "tool" in e and "error" in e)
    help_r = run("--help")
    check(g11, "help 含全部命令", all(c in help_r.stdout for c in
          ("summary", "parse", "pixels", "check", "deid", "gen")))
    sk = open(os.path.join(ROOT, "SKILL.md")).read()
    check(g11, "SKILL 前置 name/version", "name: need-to-parse-complex-medical-dicom-file" in sk
          and "version: 2.0.0" in sk)
    check(g11, "SKILL 命令表齐全", all(c in sk for c in ("summary", "parse", "pixels", "check", "deid", "gen")))
    for ref in ("dicom_basics.md", "transfer_syntaxes.md", "ps315_deid.md"):
        p = os.path.join(ROOT, "references", ref)
        check(g11, "参考文档存在: " + ref, os.path.exists(p) and "供参考" in open(p).read())
    src = open(TOOL).read()
    bad_imports = [l for l in src.splitlines()
                   if (l.startswith("import ") or l.startswith("from "))
                   and not any(l.startswith(p) for p in
                               ("import argparse", "import hashlib", "import json", "import os",
                                "import struct", "import sys", "from "))]
    check(g11, "仅标准库导入", not bad_imports, str(bad_imports))
    check(g11, "诚实声明在 docstring", "绝不猜测像素值" in src and "不用于诊断" in src)
    st = run("summary", f_exp)
    check(g11, "purpose 字段恒在", json.loads(st.stdout).get("purpose", "").startswith("技术检查"))

    # ── 汇总 ────────────────────────────────────────────────────────────
    total = len(RESULTS)
    fails = [x for x in RESULTS if not x[2]]
    for g, n, ok, dbg in RESULTS:
        if not ok:
            print("FAIL %s :: %s %s" % (g, n, dbg))
    print("selftest: %d/%d PASS" % (total - len(fails), total))
    sys.exit(0 if not fails else 1)


if __name__ == "__main__":
    main()
