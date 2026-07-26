#!/usr/bin/env python3
"""DramaLex · score_speaking.py — 口语 Whisper 实际评分闭环

把「说」从「凭感觉」变成「有反馈」：
  1) 用 Whisper（可选依赖）把 learner 的录音转写成文本；
  2) 与目标句（tasks.json 中 speaking[].asr_target）逐词比对；
  3) 标出【丢失 / 错误 / 多余】的词（transcript-match，不是发音评分）；
  4) 给出可操作的改进建议（哪些词没说出来、顺序是否对）。

⚠️ 诚实边界：Whisper 只做「转写比对」，不评口音/音素。真实发音请回看正片跟读。
录音在本地处理，绝不上传。

依赖（可选）：pip install openai-whisper  或  faster-whisper
若未安装，脚本会打印安装指引并退出码 3，不静默失败。

用法：
  # 单条评分
  python score_speaking.py --audio my_recording.m4a --target "I'm gonna go get it."
  # 批量：直接吃整份 tasks.json（对每条带 asr_target 的做评分）
  python score_speaking.py --tasks tasks.json --audio-dir ./recordings
"""
import argparse, json, os, re, sys, subprocess

def norm(t):
    return re.findall(r"[a-z0-9']+", (t or '').lower())

def transcribe(audio_path):
    """用 whisper 转写。返回文本或 None（未安装）。"""
    try:
        import whisper  # openai-whisper
    except Exception:
        try:
            from faster_whisper import WhisperModel
        except Exception:
            return None, "whisper 未安装"
        # faster-whisper 路径
        model = WhisperModel("base", device="cpu")
        segs, _ = model.transcribe(audio_path)
        text = " ".join(s.text for s in segs)
        return text, None
    model = whisper.load_model("base")
    res = model.transcribe(audio_path)
    return res.get("text", ""), None

def diff(target, actual):
    """对齐目标句与实际转写，标出差异。简单 LCS 风格对齐（够用）。"""
    t = norm(target)
    a = norm(actual)
    # 用集合找缺失/多余
    from collections import Counter
    tc, ac = Counter(t), Counter(a)
    missing = []
    for w, n in tc.items():
        if ac.get(w, 0) < n:
            missing += [w] * (n - ac.get(w, 0))
    extra = []
    for w, n in ac.items():
        if tc.get(w, 0) < n:
            extra += [w] * (n - tc.get(w, 0))
    # 顺序检查（连续子序列）
    order_ok = True
    i = 0
    for w in t:
        if i < len(a) and a[i] == w:
            i += 1
        elif w in a[i:]:
            order_ok = False
            i = a.index(w, i) + 1
        else:
            i = len(a)
    return missing, extra, order_ok

def score_one(target, actual):
    missing, extra, order_ok = diff(target, actual)
    exact = (norm(target) == norm(actual))
    score = 1.0 if exact else max(0.0, 1.0 - 0.12 * len(missing) - 0.06 * len(extra))
    feedback = []
    if exact:
        feedback.append("✅ 完全一致，所有目标词都正确说出。")
    else:
        if missing:
            feedback.append(f"❌ 没说出来的词：{', '.join(missing)}")
        if extra:
            feedback.append(f"➕ 多说的词（不在目标句）：{', '.join(extra)}")
        if not order_ok:
            feedback.append("🔄 词序与目标句不一致，注意自然语序。")
        feedback.append("💡 重听目标句 → 跟读 → 再录一次，直到丢失词清零。")
    return {"target": target, "actual": actual, "score": round(score, 2),
            "missing": missing, "extra": extra, "order_ok": order_ok,
            "feedback": feedback}

def main():
    ap = argparse.ArgumentParser(description="DramaLex 口语 Whisper 评分闭环")
    ap.add_argument('--audio', help='单条录音文件路径')
    ap.add_argument('--target', help='对照目标句（单条评分时）')
    ap.add_argument('--tasks', help='整份 tasks.json（批量评分带 asr_target 的条）')
    ap.add_argument('--audio-dir', default='.', help='批量模式：录音文件所在目录（按 id 命名 target-<id>.ext）')
    ap.add_argument('--json', action='store_true', help='输出 JSON')
    args = ap.parse_args()

    if args.tasks:
        tasks = json.load(open(args.tasks, encoding='utf-8'))
        results = []
        for s in tasks.get('speaking', []):
            tgt = s.get('asr_target')
            if not tgt:
                continue
            sid = s.get('id')
            # 找同名录音：target-<id>.ext
            rec = None
            for ext in ('m4a', 'mp3', 'wav', 'webm', 'ogg'):
                cand = os.path.join(args.audio_dir, f"target-{sid}.{ext}")
                if os.path.exists(cand):
                    rec = cand; break
            if not rec:
                results.append({"id": sid, "target": tgt, "status": "no_recording",
                                "feedback": [f"未找到录音 {os.path.join(args.audio_dir, f'target-{sid}.*')}，录完再评。"]})
                continue
            text, err = transcribe(rec)
            if text is None:
                print("⚠️", err, "→ pip install openai-whisper 后重试。", file=sys.stderr)
                return 3
            results.append({"id": sid, **score_one(tgt, text)})
        if args.json:
            print(json.dumps(results, ensure_ascii=False, indent=2))
        else:
            for r in results:
                print(f"\n🗣️ 口语 #{r.get('id')}")
                if r.get('status') == 'no_recording':
                    print("  ", r['feedback'][0]); continue
                print(f"  目标：{r['target']}")
                print(f"  你说：{r['actual']}")
                print(f"  匹配度：{r['score']}")
                for f in r['feedback']:
                    print("  ", f)
        return 0

    if not (args.audio and args.target):
        print("请给 --audio + --target（单条），或 --tasks（批量）。", file=sys.stderr)
        return 2
    if not os.path.exists(args.audio):
        print("录音不存在:", args.audio, file=sys.stderr); return 2
    text, err = transcribe(args.audio)
    if text is None:
        print("⚠️", err, "→ pip install openai-whisper 后重试。", file=sys.stderr)
        return 3
    r = score_one(args.target, text)
    if args.json:
        print(json.dumps(r, ensure_ascii=False, indent=2))
    else:
        print(f"目标句：{r['target']}")
        print(f"你说出：{r['actual']}")
        print(f"匹配度：{r['score']}")
        for f in r['feedback']:
            print(" ", f)
    return 0

if __name__ == '__main__':
    sys.exit(main())
