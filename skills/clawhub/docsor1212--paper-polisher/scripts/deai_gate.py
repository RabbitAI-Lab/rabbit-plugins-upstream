#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""deai_gate.py — 4层去AI化加权融合门禁 (deai-medical-writing skill 核心)

实现 ImmunoLens DeAI 记录中的优化方向#3: 加权融合综合评分, 替代各层独立判定。

层权重依据 EVAL 判别力(2026-06-25 定稿数据):
  层4 style_distance 文体特征工程 — 正负差距49.2(最强) → 0.45
  层2 ai_detector   词级9层+段落均匀度 → 0.35
  层3 translation_smell 翻译腔+盲区新词 → 0.20
  层1 term_check    术语质量 → 建议性输出, 不计入AI风险分

综合AI风险 = 0.35*ai_score + 0.45*(100-style_score) + 0.20*smell_score
判定: <35 通过 / 35-55 需复核 / ≥55 疑似AI

用法:
  python3 deai_gate.py <file> [--json]
"""
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPTS = Path(__file__).parent
W_L2, W_L4, W_L3 = 0.35, 0.45, 0.20


def run_py(script, args):
    """运行同目录脚本, 返回 (returncode, stdout, stderr)。"""
    p = subprocess.run([sys.executable, str(SCRIPTS / script)] + args,
                       capture_output=True, text=True, encoding="utf-8", timeout=120)
    return p.returncode, p.stdout or "", p.stderr or ""


def layer2_ai(text_file):
    """层2: ai_detector 词级检测 → (0-100 AI分, 说明)"""
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False, mode="w") as f:
        out = f.name
    rc, so, se = run_py("ai_detector.py", [text_file, "--lang", "auto",
                                           "--format", "json", "--output", out])
    try:
        r = json.load(open(out, encoding="utf-8"))
        return float(r.get("overall_ai_score", 50)), \
            f"词级{r.get('overall_ai_score')}({r.get('overall_risk')})"
    except Exception:
        return 50.0, f"层2解析失败(rc={rc})"
    finally:
        Path(out).unlink(missing_ok=True)


def layer4_style(text_file):
    """层4: style_distance 文体特征 → (0-100 人类相似分, 说明)"""
    rc, so, se = run_py("style_distance.py", [text_file, "--json"])
    try:
        r = json.loads(so)
        if r.get("style_score") is None:
            return 50.0, "层4:文本过短"
        return float(r["style_score"]), f"文体{r['style_score']}({r['verdict']})"
    except Exception:
        return 50.0, f"层4解析失败(rc={rc})"


def layer3_smell(text_file):
    """层3: translation_smell 翻译腔 → (0-100 可疑度, 说明)。启发式计分。"""
    rc, so, se = run_py("translation_smell_check.py", [text_file, "--json"])
    hits = blind = 0
    try:
        r = json.loads(so)
        for key in ("hits", "result", "results"):
            v = r.get(key) if isinstance(r, dict) else None
            if isinstance(v, list):
                hits = len(v)
                blind = sum(1 for h in v if isinstance(h, dict)
                            and "盲区" in str(h.get("suggestion", "")))
                break
        else:
            m = re.search(r'命中\s*(\d+)', so + se)
            if m:
                hits = int(m.group(1))
    except Exception:
        m = re.search(r'命中\s*(\d+)', so + se)
        hits = int(m.group(1)) if m else 0
    score = min(100, hits * 8 + blind * 25)
    return float(score), f"翻译腔命中{hits}(盲区{blind})"


def layer1_term(text_file):
    """层1: term_check 术语质量 → (通过?, 说明)。建议性。"""
    rc, so, se = run_py("term_check.py", [text_file])
    out = so + se
    m = re.search(r'标准率\s*(\d+(?:\.\d+)?)\s*%', out)
    if m:
        rate = float(m.group(1))
        return rate >= 97, f"标准率{rate}%"
    if "✅" in out or "术语检查通过" in out:
        return True, "术语检查通过"
    m2 = re.search(r'发现\s*(\d+)\s*处非标准', out)
    if m2:
        return False, f"{m2.group(1)}处非标准术语"
    return None, out.strip()[:50] or "层1无输出"


def gate(text_file, json_out=False):
    ai, ai_note = layer2_ai(text_file)
    style, style_note = layer4_style(text_file)
    smell, smell_note = layer3_smell(text_file)
    term_ok, term_note = layer1_term(text_file)

    composite = W_L2 * ai + W_L4 * (100 - style) + W_L3 * smell
    if composite < 35:
        verdict = "pass"
    elif composite < 55:
        verdict = "review"
    else:
        verdict = "ai_suspect"

    result = {
        "composite_ai_risk": round(composite, 1),
        "verdict": verdict,
        "layers": {
            "L2_word_patterns": {"ai_score": ai, "weight": W_L2, "note": ai_note},
            "L4_style_features": {"style_score": style, "weight": W_L4, "note": style_note},
            "L3_translation_smell": {"smell_score": smell, "weight": W_L3, "note": smell_note},
            "L1_terminology": {"advisory": term_ok, "note": term_note},
        },
        "bands": "composite<35 通过 | 35-55 需复核 | >=55 疑似AI",
        "honesty": "文体与词级检测是概率性判断, 不构成定罪; 阈值依据2026-06 EVAL, 建议结合人工审阅",
    }
    if json_out:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        mark = {"pass": "✅", "review": "🟡", "ai_suspect": "🔴"}[verdict]
        print(f"综合AI风险: {composite:.1f}/100 {mark} {verdict}")
        print(f"  层2 词级:   {ai_note}  (权重{W_L2})")
        print(f"  层4 文体:   {style_note}  (权重{W_L4})")
        print(f"  层3 翻译腔: {smell_note}  (权重{W_L3})")
        t = "✅" if term_ok else ("❌" if term_ok is False else "⚠️")
        print(f"  层1 术语:   {t} {term_note}  (建议性)")
        print(f"  判定带: {result['bands']}")
        if verdict != "pass":
            print("  ⚠️ 概率性判断非定罪; 建议参照顶刊范文改写长短句节奏与标点多样性后复测")
    return result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python3 deai_gate.py <file> [--json]")
        sys.exit(2)
    gate(sys.argv[1], json_out="--json" in sys.argv)
