#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""selfcheck.py — 发布前回归自检（v2.5.3）。

每次改动（规则包 / 引擎 / 文档）后运行，作为「自扫描零误报 + 恶意样例命中 + 版本一致性」
三道回归的门禁，输出 PASS/FAIL 并以退出码反映结果（供 CI / 发布流程消费）。

用法：
  python selfcheck.py [--skill-dir <path>] [--rules-dir <path>]

不依赖第三方库；恶意样例在临时目录动态构造，不写入本包。
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import sys
import tempfile
from pathlib import Path

SCRIPT_DIR = Path(os.path.abspath(__file__)).parent
sys.path.insert(0, str(SCRIPT_DIR))

# v3.0.1 沙箱模式：优先 import 明文（常规部署），否则 zipimport 从 engine.zip 内存加载
from _load_engine import load as _load_engine
a = _load_engine()

SEV_ORDER = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}


def _self_scan(skill_dir: Path):
    """断言：自扫描必须 🟢 准入 PASS，且无 P0/P1 信号。"""
    r = a.analyze(skill_dir)
    if "error" in r:
        return False, f"自扫描出错：{r['error']}"
    bad = [s for s in r.get("signals", []) if s.startswith(("P0:", "P1:"))]
    if bad:
        return False, f"自扫描检出高危信号：{bad[:5]}"
    gate = r.get("admission_gate", "")
    if not gate.startswith("PASS"):
        return False, f"自扫描准入非 PASS：{gate}"
    return True, f"自扫描 {gate}，score {r.get('risk_score', {}).get('score')}"


def _malicious_corpus_gate(corpus: Path):
    """v3.0.5 起：恶意样例检测**不构造任何恶意夹具**，改为从独立基准库（--corpus）
    取一个恶意样本验证 BLOCK + P0 命中。基准库仅在维护者隔离环境使用，主包不含恶意夹具。"""
    mal_dir = corpus / "malicious"
    if not mal_dir.is_dir():
        return False, "基准库无 malicious 目录"
    for d in sorted(mal_dir.iterdir()):
        if d.is_dir() and (d / "SKILL.md").exists():
            r = a.analyze(d)
            gate = r.get("admission_gate", "")
            has_p0 = any(s.startswith("P0:") for s in r.get("signals", []))
            if gate.startswith("BLOCK") and has_p0:
                return True, f"恶意样例 BLOCK+P0（{d.name}）"
            return False, f"恶意样例未 BLOCK/P0：{gate}（{d.name}）"
    return False, "基准库无恶意样例"


def _version_consistency(skill_dir: Path, rules_dir: Path):
    """断言：SKILL.md frontmatter / 规则包 manifest / 引擎 docstring 版本一致。

    三重一致：SKILL.md 与 manifest 的版本号必须相同；引擎 docstring 的版本历史块
    必须包含该版本标记（形如 vX.Y.Z），否则视为未同步——避免「只改两处漏改引擎文档」。
    """
    ver = {}
    fm = skill_dir.joinpath("SKILL.md").read_text(encoding="utf-8")
    m = re.search(r"^version:\s*([0-9.]+)", fm, re.MULTILINE)
    ver["SKILL.md"] = m.group(1) if m else "?"
    try:
        manifest = json.loads(rules_dir.joinpath("manifest.json").read_text(encoding="utf-8"))
        ver["rules/manifest"] = manifest.get("pack_version", "?")
    except Exception:
        ver["rules/manifest"] = "?"
    sk_ver = ver["SKILL.md"]
    # 引擎源码：常规模式读 __file__（v3.3.3 起为明文 analyze_skill.txt）；兜底直读同路径
    doc = ""
    afile = getattr(a, "__file__", "") or ""
    if afile and os.path.isfile(afile):
        doc = Path(afile).read_text(encoding="utf-8")
    else:
        root = Path(os.environ.get("SKAUDIT_ROOT") or SCRIPT_DIR.parent)
        txtp = root / "scripts" / "analyze_skill.txt"
        if txtp.exists():
            try:
                doc = txtp.read_text(encoding="utf-8", errors="replace")
            except Exception:
                doc = ""
    engine_ok = (sk_ver != "?" and f"v{sk_ver}" in doc)
    ver["analyze_skill.py"] = "✓ 含版本标记" if engine_ok else "✗ 引擎文档未同步"
    if ver["SKILL.md"] != ver["rules/manifest"]:
        return False, f"版本不一致：{ver}"
    if not engine_ok:
        return False, f"版本不一致：{ver}"
    return True, f"版本一致 v{sk_ver}"


def _corpus_metrics(corpus: Path):
    """对抗基准库量化（v2.5.3）：benign/ 下良性与 malicious/ 下恶意样本。

    检出率 = 恶意样本中被 BLOCK 的比例；误报率 = 良性样本中误报 P0/P1 的比例。
    语料库不随包分发（避免自扫误报与泄露），由维护者置于包外目录。
    """
    benign_dir, malicious_dir = corpus / "benign", corpus / "malicious"
    benign = [d for d in benign_dir.iterdir() if d.is_dir() and (d / "SKILL.md").exists()] if benign_dir.is_dir() else []
    malicious = [d for d in malicious_dir.iterdir() if d.is_dir() and (d / "SKILL.md").exists()] if malicious_dir.is_dir() else []
    if not benign and not malicious:
        return False, "基准库为空（需含 benign/ 与 malicious/ 子目录，每个子目录放 Skill 目录）"

    def _flagged(d: Path):
        r = a.analyze(d)
        if "error" in r:
            return True, "error"
        bad = [s for s in r.get("signals", []) if s.startswith(("P0:", "P1:"))]
        return bool(bad), (len(bad))

    detected = sum(1 for d in malicious if _flagged(d)[0])
    fp_names = [f"{d.name}({_flagged(d)[1]} 条)" for d in benign if _flagged(d)[0]]

    total_mal = len(malicious)
    dr = (detected / total_mal * 100) if total_mal else 100.0
    fr = (len(fp_names) / len(benign) * 100) if benign else 0.0
    ok = (not fp_names) and (not malicious or detected == total_mal)
    msg = (f"检出率 {dr:.0f}%（{detected}/{total_mal}），误报率 {fr:.0f}%（{len(fp_names)}/{len(benign)}）"
           + (f"；误报样本：{', '.join(fp_names)}" if fp_names else ""))
    return ok, msg


def _rule_pack_integrity(skill_dir: Path):
    """v3.0.3 规则包完整性门禁：manifest.json 逐文件 SHA-256 比对，
    并检查 rules/ 顶层规则文件是否全部入清单（防止改规则文件/新增规则后清单失配被静默回退）。"""
    rules_dir = skill_dir / "rules"
    man_p = rules_dir / "manifest.json"
    if not man_p.exists():
        return False, "manifest.json 缺失"
    try:
        man = json.loads(man_p.read_text(encoding="utf-8"))
    except Exception as e:
        return False, f"manifest.json 解析失败 {e}"
    files_map = man.get("files", {})
    if not files_map:
        return False, "manifest.json files 为空"
    bad, missing = [], []
    for name, expected in files_map.items():
        fp = rules_dir / name
        if not fp.exists():
            missing.append(name)
            continue
        actual = hashlib.sha256(fp.read_bytes()).hexdigest()
        if actual != expected:
            bad.append(f"{name}({actual[:8]}≠{expected[:8]})")
    top = {p.name for p in rules_dir.glob("*.json")} - {"manifest.json", "engine_hashes.json"}
    not_listed = sorted(top - set(files_map))
    # v3.3.4 门禁加固：哈希相符 ≠ 应用成功——规则缺字段/编译失败会让 load_rule_pack 跳过该文件
    # 并静默回退内置默认（实测 obf-017 缺 why 导致整个 obfuscation.json 被跳过仍报 PASS）。
    # 此处直接调引擎 _apply_rule_file 逐文件验证「能成功应用」，杜绝该类假阴性。
    apply_fail = []
    try:
        a  # noqa: F821  引擎模块（selfcheck 全局）
        for name in sorted(files_map):
            fp_rule = rules_dir / name
            try:
                obj = json.loads(fp_rule.read_text(encoding="utf-8"))
                if not a._apply_rule_file(name, obj):
                    apply_fail.append(f"{name}(装载器不受理)")
            except Exception as exc:
                apply_fail.append(f"{name}({type(exc).__name__})")
    except NameError:
        pass  # 引擎模块不可用时交由其他门禁兜底
    ok = not bad and not missing and not not_listed and not apply_fail
    msg = (f"manifest 校验 {len(files_map)} 个规则文件"
           + (f"；哈希不符：{', '.join(bad)}" if bad else "")
           + (f"；缺失：{', '.join(missing)}" if missing else "")
           + (f"；未入清单：{', '.join(not_listed)}" if not_listed else "")
           + (f"；应用失败：{', '.join(apply_fail)}" if apply_fail else ""))
    return ok, msg


def _signature_chain(skill_dir: Path):
    """v3.3.1 发布者签名链门禁：核验 engine_sha256 锚 + 文件锚 + signature_digest。

    复用随包 scripts/verify_signature.py 的核验逻辑，检出关键文件被篡改或未同步改动。
    """
    try:
        import verify_signature
    except Exception as exc:  # noqa: BLE001
        return False, f"无法导入 verify_signature：{exc}"
    import contextlib
    import io as _io
    buf = _io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = verify_signature.verify(skill_dir)
    lines = [ln for ln in buf.getvalue().strip().splitlines() if ln.strip()]
    msg = lines[0].lstrip("✓✗ ").strip() if lines else ""
    return (rc == 0), (msg or ("签名链核验通过" if rc == 0 else "签名链核验失败"))


def _dynamic_gate(corpus: Path):
    """v3.0.2 动态沙箱门禁：恶意样本（m7/m8/m9）动态实证须有 P1 命中；
    良性样本动态执行须零 P0/P1（P2/P3 不计）。"""
    mal_dir = corpus / "malicious"
    dyn_targets = ["m7-context-tamper", "m8-self-replication", "m9-command-assembly", "m13-taint-exfil", "m18-ws-envsteal", "m19-ghostsplice"]
    notes, ok = [], True
    for name in dyn_targets:
        d = mal_dir / name
        if not d.is_dir():
            ok = False
            notes.append(f"{name}: 目录缺失")
            continue
        try:
            ev = a.dynamic_probe(d)
            hits = a.scan_dynamic_behavior(ev)
        except Exception as exc:
            ok = False
            notes.append(f"{name}: 动态执行异常 {exc}")
            continue
        p1 = [h for h in hits if h["sev"] == "P1"]
        notes.append(f"{name}: 动态 P1×{len(p1)}")
        if p1:
            continue
        # 无 P1：若因外部依赖缺失（-I 隔离无站点包，requests 等网络型样本无法复现），
        # 判 not_applicable 而非 FAIL；其余视为未通过。
        all_ev = [e for v in ev.values() for e in v if isinstance(e, (list, tuple))]
        import_fail = any(
            e and e[0] == "error" and e[1] in ("ModuleNotFoundError", "ImportError")
            for e in all_ev)
        if import_fail:
            notes.append(f"{name}: 依赖缺失 not_applicable")
            continue
        ok = False
    ben_dir = corpus / "benign"
    if ben_dir.is_dir():
        for d in sorted(ben_dir.iterdir()):
            if not d.is_dir() or not (d / "SKILL.md").exists():
                continue
            try:
                ev = a.dynamic_probe(d)
                hits = a.scan_dynamic_behavior(ev)
            except Exception as exc:
                ok = False
                notes.append(f"benign/{d.name}: 动态异常 {exc}")
                continue
            bad = [h for h in hits if h["sev"] in ("P0", "P1")]
            notes.append(f"benign/{d.name}: 动态 P0/P1×{len(bad)}")
            if bad:
                ok = False
    return ok, "；".join(notes)


def main():
    ap = argparse.ArgumentParser(description="skill-analysis 发布前回归自检")
    ap.add_argument("--skill-dir", default=str(SCRIPT_DIR.parent), help="Skill 根目录（默认本包）")
    ap.add_argument("--rules-dir", default="", help="规则包目录（默认 Skill 根下 rules/）")
    ap.add_argument("--corpus", default="", help="对抗基准库目录（含 benign/ 与 malicious/ 子目录；可选）")
    args = ap.parse_args()

    skill_dir = Path(a._norm_msys_path(args.skill_dir)).resolve()
    rules_dir = Path(a._norm_msys_path(args.rules_dir)).resolve() if args.rules_dir else skill_dir / "rules"

    checks = []
    checks.append(("自扫描零误报", _self_scan(skill_dir)))
    checks.append(("版本一致性", _version_consistency(skill_dir, rules_dir)))
    checks.append(("规则包完整性", _rule_pack_integrity(skill_dir)))
    checks.append(("发布者签名链", _signature_chain(skill_dir)))
    if args.corpus:
        corpus_dir = Path(a._norm_msys_path(args.corpus)).resolve()
        checks.append(("恶意样例命中（基准库）", _malicious_corpus_gate(corpus_dir)))
        checks.append(("对抗基准库", _corpus_metrics(corpus_dir)))
        checks.append(("动态沙箱门禁", _dynamic_gate(corpus_dir)))
    else:
        print("ℹ️ 未提供 --corpus：恶意样例检测与动态沙箱门禁需独立基准库，"
              "仅在维护者隔离环境运行（主包不含恶意样本夹具）。")

    print("Skill Analysis 回归自检")
    print("=" * 52)
    ok = True
    for name, (passed, msg) in checks:
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}：{msg}")
        ok = ok and passed
    print("=" * 52)
    print("结论：" + ("✅ 全部通过，可发布" if ok else "❌ 存在失败项，禁止发布"))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
