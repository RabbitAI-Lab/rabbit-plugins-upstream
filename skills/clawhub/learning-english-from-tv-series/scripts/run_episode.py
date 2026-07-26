#!/usr/bin/env python3
"""DramaLex · run_episode.py — 一键编排 (one-click orchestrator)

把分散的 5 步收敛成 1–2 条命令：
  prepare  抓取并解析字幕 -> 写出「Agent 交接单」(dramalex_handoff.md)，告诉 agent 该产出哪些 JSON。
  build    给定 agent 产出的 JSON，跑 TTS + 一次性导出 4 种单文件交付物。
           JSON 不齐时，自动打印交接单并退出码 10（便于上层 wrapper 回到 agent 补生成）。

设计原则：agent 负责语言学生成，脚本负责机械流程。零幻觉、零静默失败。
纯标准库 + 可选 genanki/openpyxl/python-docx。
"""
import argparse, json, os, re, sys, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gen_audio as ga
import export_hub as eh
import estimate as est
import validate as val
import exam_map as exm

AUTHOR = eh.AUTHOR
CORE = ['words.json', 'listening.json', 'annotated.json', 'tasks.json']
OPT = ['watch.json']

def schema_hint(word_cap, cefr, cefr_suggest=None):
    cap = word_cap or '15–30'
    if cefr and cefr != 'auto':
        lvl = f'；学习者档位 CEFR={cefr}（校准任务难度，不筛词，需如实报告词表等级分布）'
    elif cefr_suggest:
        lvl = (f'；建议档位 CEFR≈{cefr_suggest}（{exm.exam_label(cefr_suggest)}；'
               f'由字幕词汇密度估算，可用 --cefr 覆盖；校准难度不筛词）')
    else:
        lvl = ''
    return {
        'words.json': f'schemas/vocab_card.schema.md — {cap} 个目标词/语块，含 ipa/cefr/gloss/collocation/line/example{lvl}',
        'listening.json': 'schemas/listening.schema.md — comprehension[] + dictation[]',
        'annotated.json': 'schemas/transcript_annotated.schema.md — annotations[] + cloze[]',
        'tasks.json': 'schemas/tasks.schema.md — speaking[] + writing[]',
        'watch.json': 'schemas/watch.schema.md — 观看协议 protocol[] + notice[]（缺省用内置三步字幕法）',
    }

REL = lambda p, base: os.path.relpath(p, base)


def next_episode(episode):
    """从 'Friends S01E01' 解析出下一集 'Friends S01E02'；无法解析则返回 None。"""
    m = re.search(r'S(\d+)E(\d+)', episode or '', re.IGNORECASE)
    if not m:
        return None
    s, e = m.group(1), int(m.group(2))
    base = episode[:m.start()] + f"S{s}E{e+1}" + episode[m.end():]
    return base


def discover(work_dir):
    found = {n: os.path.join(work_dir, n) for n in CORE + OPT}
    missing_core = [n for n in CORE if not os.path.exists(found[n])]
    return found, missing_core


def write_handoff(work_dir, found, missing_core, episode, word_cap='15–30', cefr='auto',
                  est_out=None, focus='balanced', chunks_only=False, ui_lang='zh',
                  cefr_suggest=None, vocab_bank_n=0, recall_n=0):
    path = os.path.join(work_dir, 'dramalex_handoff.md')
    hint = schema_hint(word_cap, cefr, cefr_suggest)
    cap_disp = word_cap if word_cap and word_cap != 'auto' else (f"≈{est_out['word_cap']}（由字幕估算）" if est_out else '15–30')
    lines = ["# 🎬 DramaLex · Agent 交接单 (Handoff)", "",
             f"剧集：`{episode}`",
             f"本集配置：词汇量 `word_cap={cap_disp}` · 学习者档位 `cefr={cefr or 'auto'}{((' ≈ '+exm.suggest_line(cefr_suggest)) if (cefr_suggest and cefr=='auto') else '')}` · 侧重 `{focus}` · 纯语块模式 `{chunks_only}` · 界面 `{ui_lang}`", "",
             "下列 JSON 尚未生成。请按对应 schema 产出后，再次运行：", "```bash",
             f"python {REL(__file__, work_dir)} build --work-dir \"{work_dir}\"", "```", ""]
    if est_out:
        lines += ["**📊 由字幕规模推导的建议数量（供参考，可覆盖）：**"]
        lines += est.render_bullets(est_out)
        lines += [""]
    for n in CORE + OPT:
        mark = "✅ 已存在" if os.path.exists(found[n]) else "❌ 缺失"
        extra = "（仅挖语块，不挖单词）" if (n == 'words.json' and chunks_only) else ""
        lines.append(f"- **{n}** {mark} — {hint[n]}{extra}")
    if vocab_bank_n:
        lines += ["", f"**📚 跨集词库**：已累计掌握/学过 `{vocab_bank_n}` 个词（见 `vocab_bank.json`）。"
                   f"建议本集优先挖掘**新词**，已掌握项可跳过，避免重复。"]
    if recall_n:
        lines += ["", f"**🔁 跨集复现**：`recall_hints.json` 里有 `{recall_n}` 个已学词在本集的**新语境**"
                   f"（旧语境→新台词对照）。精读/复习时把它们拎出来，复用记忆更牢。"]
    lines += ["", "---",
              f"👨‍💻 {AUTHOR} · yinjianheng@foxmail.com · WeChat: YJH-yinjianheng · GitHub: yinjianheng",
              "⚖️ 法律声明：本工具协助你从互联网公开渠道检索字幕，仅供个人非商业语言学习使用。",
              "生成物含第三方台词，请勿再分发或用于商业用途；如权利人主张权利，请联系作者下架。"]
    open(path, 'w', encoding='utf-8').write("\n".join(lines))
    return path


def _run(py, *a):
    return subprocess.run([sys.executable, os.path.join(HERE, py), *a])


def cmd_prepare(args):
    work_dir = args.work_dir
    os.makedirs(work_dir, exist_ok=True)
    # 学前诊断：若给了 diagnose.json，采用其 CEFR 档位（覆盖 --cefr）
    if args.diagnose and args.cefr == 'auto':
        try:
            d = json.load(open(args.diagnose, encoding='utf-8'))
            c = d.get('cefr')
            if c and c in ('A1', 'A2', 'B1', 'B2', 'C1', 'C2'):
                args.cefr = c
                print(f"已读取学前诊断：CEFR={c}（约 {exm.exam_label(c)}）")
        except Exception as e:
            print(f"⚠️ 读取 diagnose.json 失败（{e}），仍用 --cefr={args.cefr}")
    srt = None
    if args.subtitle and (args.subtitle.startswith('http://') or args.subtitle.startswith('https://')):
        print("检索字幕…")
        _run('fetch_subtitles.py', '--url', args.subtitle, '--output', os.path.join(work_dir, 'subtitle.auto.srt'))
        srt = os.path.join(work_dir, 'subtitle.auto.srt')
    elif args.subtitle and os.path.exists(args.subtitle):
        srt = args.subtitle
    out_json = os.path.join(work_dir, 'subtitle.json')
    if srt and os.path.exists(srt):
        ext = os.path.splitext(srt)[1].lower()
        if ext == '.json':
            # 已是解析后的 subtitle.json，直接复用（不重复解析，避免把 JSON 当纯文本拆行）
            if os.path.abspath(srt) != os.path.abspath(out_json):
                import shutil
                shutil.copyfile(srt, out_json)
            else:
                pass  # 同一文件，跳过
            print("字幕（已解析 JSON）就绪。")
        else:
            print("解析字幕…")
            _run('parse_subtitles.py', '--input', srt, '--output', out_json)
    elif args.text:
        print("解析粘贴文本…")
        _run('parse_subtitles.py', '--text', args.text, '--output', out_json)
    else:
        print("未提供字幕（--subtitle / --text）；可稍后补充。")
    # 空字幕防护：解析出 0 行必须显式报错，不能静默继续
    sj = os.path.join(work_dir, 'subtitle.json')
    if os.path.exists(sj):
        segs = est._load_subtitle(sj)
        if not segs:
            print("❌ 字幕解析结果为空（0 行）。请检查 --subtitle 链接/路径是否正确、"
                  "字幕是否为空文件或编码异常。已终止 prepare。")
            return 3
    # 由字幕规模推导建议数量（仅在未显式给 --word-cap 时展示估算）
    est_out = None
    if not args.word_cap or args.word_cap == 'auto':
        if os.path.exists(sj):
            est_out = est.estimate_counts(subtitle_json=sj, cefr=args.cefr)
            if est_out.get('error') == 'subtitle_empty':
                print("❌ 字幕为空，无法估算词量。请检查字幕源。")
                return 3
    # CEFR 档位自动建议（仅在用户未显式给 --cefr 时）
    cefr_suggest = None
    if args.cefr == 'auto' and os.path.exists(sj):
        cefr_suggest = est.suggest_cefr(subtitle_json=sj)
    # 跨集词库
    vocab_bank_n = 0
    recall_n = 0
    vb = os.path.join(work_dir, 'vocab_bank.json')
    if os.path.exists(vb):
        try:
            vocab_bank_n = len(json.load(open(vb, encoding='utf-8')) or [])
        except Exception:
            vocab_bank_n = 0
    # 跨集复现：若已有词库且本集字幕已解析，自动生成 recall_hints.json
    recall_n = 0
    if vocab_bank_n and os.path.exists(sj):
        try:
            import cross_episode as ce
            out = ce.build_recall_hints(json.load(open(vb, encoding='utf-8')),
                                        est._load_subtitle(sj), args.episode)
            json.dump(out, open(os.path.join(work_dir, 'recall_hints.json'), 'w', encoding='utf-8'),
                      ensure_ascii=False, indent=2)
            recall_n = out.get('recalled', 0)
            if recall_n:
                print(f"🔁 跨集复现：发现 {recall_n} 个已学词在本集出现新语境 → recall_hints.json")
        except Exception as e:
            print(f"⚠️ 跨集复现生成失败（不影响主流程）：{e}")
    found, missing = discover(work_dir)
    handoff = write_handoff(work_dir, found, missing, args.episode, args.word_cap, args.cefr,
                            est_out, args.focus, args.chunks_only, args.ui_lang, cefr_suggest, vocab_bank_n, recall_n)
    print("已写出交接单:", handoff)
    print("下一步：按交接单生成 agent JSON，然后 `run_episode.py build`。")
    return 0


def cmd_build(args):
    work_dir = args.work_dir
    found, missing = discover(work_dir)
    if missing:
        handoff = write_handoff(work_dir, found, missing, args.episode, args.word_cap, args.cefr)
        print("⚠️ 以下 JSON 缺失，无法 build：", ", ".join(missing))
        print("已写出交接单:", handoff)
        print("请先按 schema 生成它们，再运行 build。")
        return 10
    # 内容质量闸门（可 --no-validate 跳过）
    if not args.no_validate:
        sj = os.path.join(work_dir, 'subtitle.json')
        errs, warns = val.validate(work_dir, sj if os.path.exists(sj) else None)
        for w in warns:
            print("⚠️", w)
        if errs:
            print("❌ 内容校验未通过，终止导出（可用 --no-validate 跳过，但不推荐）：")
            for e in errs:
                print("   -", e)
            return 11
    words = json.load(open(found['words.json'], encoding='utf-8'))
    listening = json.load(open(found['listening.json'], encoding='utf-8'))
    annotated = json.load(open(found['annotated.json'], encoding='utf-8'))
    tasks = json.load(open(found['tasks.json'], encoding='utf-8'))
    watch = None
    if os.path.exists(found['watch.json']):
        watch = json.load(open(found['watch.json'], encoding='utf-8'))
    # 跨集复现提示（可选）
    recall = None
    rb = os.path.join(work_dir, 'recall_hints.json')
    if os.path.exists(rb):
        try:
            recall = json.load(open(rb, encoding='utf-8'))
        except Exception:
            recall = None
    media_dir = os.path.join(work_dir, args.media_dir)
    os.makedirs(media_dir, exist_ok=True)

    # 1) word audio (gen_audio writes paths back into words.json)
    backend = ga.pick_backend(args.backend)
    print("TTS 后端:", backend)
    word_missing = []
    for i, w in enumerate(words):
        base = f"{i+1:03d}_{re.sub(r'[^a-z0-9]+', '_', w['term'].lower())}"
        tw = os.path.join(media_dir, base + '.wav')
        p = ga.gen(w['term'], tw, backend, args.voice)
        if p:
            w['term_audio'] = p
        else:
            word_missing.append(w['term'])
        if w.get('line'):
            lw = os.path.join(media_dir, base + '_line.wav')
            p2 = ga.gen(w['line'], lw, backend, args.voice)
            if p2:
                w['line_audio'] = p2
            else:
                word_missing.append(f"{w['term']} 原句")
    json.dump(words, open(found['words.json'], 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

    # 2) line audio cache (listening / annotated / speaking lines)
    cache, line_missing = eh.collect_all_audio(words, listening, annotated, tasks, media_dir, backend, args.voice)

    # 3) export each format as a single file
    out_base = args.out_base
    results = []
    for fmt in [f.strip() for f in args.formats.split(',')]:
        od = os.path.join(out_base, 'out_' + fmt) if args.split_dirs else out_base
        os.makedirs(od, exist_ok=True)
        if fmt == 'html':
            doc = eh.build_html(words, listening, annotated, tasks, cache, args.mode, args.deck, watch=watch, media_dir=media_dir, ui_lang=args.ui_lang, recall=recall)
            p = os.path.join(od, 'practice.html')
            open(p, 'w', encoding='utf-8').write(doc)
            results.append(('html', p))
        elif fmt == 'anki':
            p = eh.build_anki(words, listening, annotated, tasks, cache, args.mode, args.deck, od, media_dir)
            if not p:
                print("Anki 生成失败（请 pip install genanki）", file=sys.stderr); return 1
            results.append(('anki', p))
        elif fmt == 'excel':
            p = eh.build_excel(words, listening, annotated, tasks, args.deck, od, watch=watch, ui_lang=args.ui_lang, recall=recall)
            if not p:
                print("Excel 生成失败（请 pip install openpyxl）", file=sys.stderr); return 1
            results.append(('excel', p))
        elif fmt == 'word':
            p = eh.build_word(words, listening, annotated, tasks, args.deck, od, watch=watch, ui_lang=args.ui_lang, recall=recall)
            if not p:
                print("Word 生成失败（请 pip install python-docx）", file=sys.stderr); return 1
            results.append(('word', p))
        elif fmt == 'md':
            p = eh.build_markdown(words, listening, annotated, tasks, args.deck, od, watch=watch, ui_lang=args.ui_lang, recall=recall)
            if not p:
                print("Markdown 生成失败", file=sys.stderr); return 1
            results.append(('md', p))
        else:
            print("未知 format:", fmt, file=sys.stderr); return 2

    print("\n✅ 一键导出完成 · 单文件交付物：")
    for fmt, p in results:
        print(f"   [{fmt}] {p}")

    # TTS 失败汇总（不致命，但必须让用户知道哪些缺音频）
    missing_all = list(dict.fromkeys(word_missing + line_missing))
    if missing_all:
        print(f"\n⚠️ TTS 合成失败 {len(missing_all)} 条（不影响导出，但以下卡片缺音频）：")
        for m in missing_all[:20]:
            print(f"   - {m}")
        if len(missing_all) > 20:
            print(f"   … 其余 {len(missing_all)-20} 条省略")

    # Anki 导入指引（最后一公里）
    anki_path = next((p for f, p in results if f == 'anki'), None)
    if anki_path:
        print(f"\n📚 Anki 导入：用 Anki 打开 {anki_path} 即可导入；牌组名「{args.deck} · DramaLex」。")

    # 写进度文件（供 --remind 复习提醒自动化读取）
    import datetime
    html_path = next((p for f, p in results if f == 'html'), None)
    prog = os.path.join(work_dir, 'progress.md')
    today = datetime.date.today().isoformat()
    nxt = next_episode(args.episode)
    fmts = ",".join(f for f, _ in results)
    head = ""
    if os.path.exists(prog):
        head = open(prog, encoding='utf-8').read()
    block = (f"\n## {today} · {args.deck}\n"
             f"- 剧集：`{args.episode}`" + (f" · 下一集：`{nxt}`" if nxt else "（电影/单集，无下一集）") + "\n"
             f"- word_cap={len(words)} · cefr={args.cefr} · mode={args.mode} · focus={args.focus}\n"
             f"- 导出格式：{fmts}\n"
             f"- 交付物：{('practice.html' if html_path else '—')} / {('Anki deck' if anki_path else '—')}\n"
             f"- 状态：已生成（打卡待用户点开复习）\n")
    # 只在当天首次生成时追加，避免重复
    if today not in head:
        open(prog, 'w', encoding='utf-8').write(head + block)
    else:
        open(prog, 'w', encoding='utf-8').write(head)

    # 维护跨集词库（供后续 prepare 提示跳过已学词）
    vb = os.path.join(work_dir, 'vocab_bank.json')
    try:
        bank = json.load(open(vb, encoding='utf-8')) if os.path.exists(vb) else []
    except Exception:
        bank = []
    seen = {b.get('term', '').lower() for b in bank}
    for w in words:
        t = (w.get('term') or '').strip()
        if t and t.lower() not in seen:
            bank.append({'term': t, 'cefr': w.get('cefr', ''), 'line': w.get('line', '')})
            seen.add(t.lower())
    json.dump(bank, open(vb, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

    if args.remind:
        print("\n📅 你选择了【每日复习提醒】。请在对话中让我（agent）执行：")
        print(f"   注册自动化（每日 21:00）：读 {prog}，若当日无打卡则提醒打开 "
              f"{html_path or 'practice.html'} / 复习 Anki；已打卡则鼓励"
              + (f"并预告「该看 {nxt} 了」" if nxt else "并预告下一部") + "。")
        print("   （提示：直接对我说「开启每日提醒」即可，我会用 automation_update 登记。）")

    print(f"\n👨‍💻 {AUTHOR} · yinjianheng@foxmail.com · WeChat: YJH-yinjianheng")
    return 0


def main():
    ap = argparse.ArgumentParser(prog='run_episode.py', description='DramaLex 一键编排')
    sub = ap.add_subparsers(dest='cmd')

    def common(p):
        p.add_argument('--episode', default='DramaLex', help='剧集代号，如 "Friends S01E01"')
        p.add_argument('--work-dir', default='.', help='工作目录（输入 JSON 与输出都在这里）')
        p.add_argument('--media-dir', default='media', help='音频输出子目录')
        p.add_argument('--out-base', default='out', help='输出基目录')
        p.add_argument('--split-dirs', action='store_true', default=True,
                       help='各 format 写入独立子目录 out_<fmt>（默认开；关闭则全部平铺到 out-base）')
        p.add_argument('--no-split-dirs', dest='split_dirs', action='store_false', help='关闭分目录')
        p.add_argument('--backend', default='auto', help='TTS 后端 auto/say/espeak/pyttsx3/gtts')
        p.add_argument('--voice', default='Samantha')
        p.add_argument('--mode', default='A', choices=['A', 'B', 'C'])
        p.add_argument('--word-cap', dest='word_cap', default=None,
                       help='目标词/语块数量，如 "20" 或 "15–30"；省略则按字幕规模自动估算')
        p.add_argument('--cefr', default='auto', choices=['auto', 'A1', 'A2', 'B1', 'B2', 'C1', 'C2'],
                       help='学习者档位；校准任务难度，不筛词（诚实档位）')
        p.add_argument('--diagnose', default=None,
                       help='读取 diagnose.py 产出的 diagnose.json，自动采用其 CEFR 档位（覆盖 --cefr）')
        p.add_argument('--focus', default='balanced',
                       choices=['balanced', 'listen', 'speak', 'read', 'write'],
                       help='技能侧重：按比例调高对应环节题量（balanced 为均衡）')
        p.add_argument('--chunks-only', dest='chunks_only', action='store_true',
                       help='词汇环节只挖语块（collocation/chunk），不挖孤立单词（进阶偏好）')
        p.add_argument('--ui-lang', dest='ui_lang', default='zh', choices=['zh', 'en'],
                       help='HTML 界面语言（中文/英文）')
        p.add_argument('--no-validate', dest='no_validate', action='store_true',
                       help='跳过内容质量校验（不推荐；默认 build 前做 JSON 质量闸门）')
        p.add_argument('--remind', dest='remind', action='store_true',
                       help='用户选择开启：登记每日复习提醒自动化（默认不开启，需显式指定）')
        p.add_argument('--deck', default=None, help='覆盖 deck 名（默认同 episode）')
        p.add_argument('--formats', default='html,anki,excel,word', help='逗号分隔的导出格式')

    pb = sub.add_parser('prepare', help='抓取+解析字幕，产出 Agent 交接单')
    common(pb)
    pb.add_argument('--subtitle', default=None, help='字幕 URL 或本地 .srt/.vtt 路径')
    pb.add_argument('--text', default=None, help='直接粘贴台词文本')
    bb = sub.add_parser('build', help='给定 agent JSON，跑 TTS + 导出 4 种单文件')
    common(bb)

    args = ap.parse_args()
    if not args.cmd:
        ap.print_help()
        return 2
    if args.deck is None:
        args.deck = args.episode
    if args.cmd == 'prepare':
        return cmd_prepare(args)
    if args.cmd == 'build':
        return cmd_build(args)
    return 2


if __name__ == '__main__':
    sys.exit(main())
