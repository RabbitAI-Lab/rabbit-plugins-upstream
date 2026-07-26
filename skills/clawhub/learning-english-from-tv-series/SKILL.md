---
name: learning-english-from-tv-series
title: 🎬 Learning English from TV Series (DramaLex)
description: "看剧/看电影学英语的完整闭环学习引擎（别名 DramaLex），面向中文母语者。当用户说「看美剧学英语」「用<剧名/电影名>学英语」「Friends S01E01 学英语」「把这一集做成英语学习材料」「电影台词精读」「字幕学英语」「刷剧背单词/练听力/练口语」，或给出任意剧集代码（如 S01E01）/电影名（如 The Pursuit of Happyness、Forrest Gump）希望据此学英语时，都应触发本 skill。核心能力：agent 用自身联网能力自主检索并解析公开字幕（两层递进检索 Tier1 已知字幕源 + Tier2 通用互联网广搜，均失败才用精选台词兜底，全程不主张版权、不存储外传，仅供个人非商业学习），再围绕这一集/这部电影产出完整学习闭环——学前 CEFR 水平诊断、目标词汇预热、听力理解、字幕精读与语言点标注（语法/搭配/篇章/发音）、口语跟读与角色扮演、写作改写续写并给反馈、跨集/跨技能间隔复现。产物覆盖 4 份结构化 CORE JSON（words/listening/annotated/tasks）与 5 种可交付格式（HTML 学习页 / Anki 卡片 / Excel 词表 / Word 文档 / Markdown），并可用 macOS say 生成 TTS 跟读音频。覆盖电视剧与电影两类；本 skill 每次可见回复末尾都会附作者落款与法律声明。"
---

# 🎬 Learning English from TV Series (DramaLex) — 看剧/看电影学英语完整闭环

> **别名 / Alias：`DramaLex`** · 一句话定位：*Learning English from the TV series & films you love.*
> 名字虽写 **TV Series**，但**同样覆盖电影（Film/Movie）**——输入一部电影名（如 *The Pursuit of Happyness*）与一集剧集（如 *Friends S01E01*）走的是同一套流程，仅时长/词量估算不同。
> 中文用户专用：本 skill 服务于「中文母语者学英语」，释义/易错点默认中文视角。

> **One episode as the single anchor → four skills (听/说/读/写) in a guided loop. Vocabulary priming + listening comprehension + transcript literacy + speaking drills + writing with feedback + cross-skill spaced review.**
>
> Input a drama name + episode code (e.g. *Friends S01E01*). DramaLex mines the target lexicon **and the non-word language knowledge hidden in the subtitle** (grammar patterns, collocations, discourse, pronunciation), then walks you through a six-phase journey that recycles those same items across listening, speaking, reading and writing.

---

## 🔎 Phase -1 · 字幕检索与使用（agent 检索定位，你授权使用）

> **设计原则（用户明确诉求）**：字幕由 **agent 自己**用联网能力去互联网各大公开字幕渠道**检索、核对准确性、并把字幕解析到位供你使用**——全程不把"找直链 / 传文件"这种脏活推给你。你只需说一句「纸牌屋 S01E01」就够了。
>
> **风险规避（法律视角 · 内置、不阻塞你）**：agent 只做"**检索 + 定位 + 解析**"，**不主张对任何第三方字幕的版权**，也**不存储、不托管、不外传**任何字幕；字幕来源于互联网公开渠道，仅供**个人非商业**语言学习使用。agent 在检索字幕前会**自动打印一份法律免责声明**（说明式，不拦截、不阻塞）。详细边界见 `references/SUBTITLE_LEGAL.md`。

**精确 agent SOP（你只给模糊剧名/集数即可，无需任何链接）：**
1. **接收模糊输入**：你说「当幸福来敲门」「Friends S01E01」「纸牌屋 S01E01」等——无需精确链接、无需权利自证。
2. **agent 自主检索（两层递进，逐层扩大范围）**：
   - **Tier 1 · 已知高命中源（优先）**：用自身联网能力，先在 **OpenSubtitles / Subscene / TVsubtitles / archive.org / 字幕组** 等已知公开渠道检索。关键词组合：片名（中/英）+ 年份 + 语言（英文名优先 `English`）+ 集数（如 `S01E01` / `Season 3`）。**多找几个候选**，比较哪个最匹配、最可能是直链可下。
   - **Tier 2 · 更大范围互联网自主检索（Tier 1 拿不到时才启用）**：若 Tier 1 的所有候选都拿不到可用直链（站点需登录、需验证码、被反爬、或本环境网络受限），**不要立刻兜底**——进行「通用联网广搜」：
     - 用 agent 自身的通用联网检索能力（WebSearch / WebFetch 等），做**多组差异化查询**撒网，例如：`<英文名> english subtitles srt`、`<片名> 字幕 下载 英语`、`<imdb_id> subtitle`、`<英文名> "<集数>" opensubtitles`、`<英文名> subs archive.org` 等；也可加年份 / 发布组 / 分辨率缩小范围。
     - 主动发现 **更多字幕托管站、论坛 / Reddit / 博客帖子、直接 `.srt/.zip/.vtt` 直链、archive.org 条目、GitHub Gist / Pastebin 片段** 等——把搜索面从"几个已知源"扩展到"整个公开互联网"。
     - 对每个有希望的候选：先 `WebFetch` 打开页面、定位**真实下载直链**（绕过下载按钮 / 中转页 / Cloudflare 中转），再调用 `retrieve_subtitles.py --url "<直链>"` 尝试取回并解析。**广撒网 + 多试候选**，直到拿到一个可解析的字幕或候选耗尽。
     - **实测可用的 Tier 2 线索（供起手参考，非穷举）**：通用搜索常能发现 `subtitlecat.com`（其英文条目提供**直接 `.srt` 直链**，如 `…/subs/<id>/<file>-en.srt`，`WebFetch` 该页即可拿到）、`moviesubtitles.org`、`kickasssubtitles.com`、`zimuku.org`、`lwltv.com` 等；优先挑页面里带 `Download` 的**英文条目**，再用 `WebFetch` 定位真实直链后取回。
3. **核对准确性（不可跳过，但 agent 自己完成）**：在把任何字幕解析到位前，agent 内部必须核对——
   - 片名/年份是否与你的意图一致（如 *House of Cards* 2013 美版，不是 1990 英版/mini-series）；
   - 集数/季数是否对（S01E01 ≠ S02E05）；
   - 语言是否为目标语言（English 听力练习要英文字幕，不是中文字幕）；
   - 若手头有一两句**已知台词**，打开候选页预览，确认台词出现在字幕里（版本正确）。
4. **agent 自主检索 + 解析（把字幕检索到位，不交给用户找直链）**：agent 选定最可靠的候选直链后，**直接调用 `retrieve_subtitles.py` 把字幕检索到位并解析**，内置免责声明——
   ```bash
   python scripts/retrieve_subtitles.py --url "<agent 自己核对过的直链>" \
       --title "House of Cards" --year 2013 --episode "S01E01" --known-lines known.txt \
       --output subtitle.srt --parse-out subtitle.json
   ```
   脚本会：①打印法律免责声明；②把字幕检索到位；③解析；④**校验**（行数 + 已知台词命中率），确认没找错版本。全程你无需粘贴任何链接。
5. **检索成功 → 继续闭环**：校验通过后，照常 `run_episode.py prepare/build` 出学习包。
6. **兜底（Tier 1 + Tier 2 两层检索都实在失败时）**：仅当 **Tier 1 与 Tier 2 两层检索都拿不到任何可用直链**（站点需登录、需验证码、全面被反爬、或本环境网络受限且无任何可发现来源）时，才**降级兜底**——改用「精选经典台词」方案（agent 手工建 20 句左右高质量台词卡，明确标注非完整字幕，仅供学习），并在结果里**如实标注**"本集为精选台词兜底，非完整检索字幕"。绝不偷偷爬版权字幕、绝不谎称已检索到完整字幕。

**铁律**：skill 不内建字幕爬虫；字幕来源于互联网公开渠道，仅供个人非商业学习使用；工具不存储、不托管、不外传任何字幕，亦不主张第三方内容版权。

---

## 🎓 Phase 0 · 学前诊断（Pre-learning Diagnostic · 学任何一集之前先做）

> 痛点：很多人不知道自己到底 A2 还是 B1，结果材料过难劝退、或过易无聊。DramaLex 让你**先定位档位**，再开工。档位只校准任务难度，**不自动筛词**（诚实档位），但它是整条闭环的起点。

**两种定位方式（任选）：**

1. **凭考试分数直接定位**（最常用）——
   ```bash
   python scripts/diagnose.py --ielts 6.5        # 雅思 → 反推 CEFR
   python scripts/diagnose.py --toefl 90         # 托福 iBT
   python scripts/diagnose.py --cet "CET-6"      # 四六级/专四专八
   python scripts/diagnose.py --ielts 5.5 --toefl 80   # 多条证据取最保守档位
   ```
   分数→档位对照（约，保守低侧）：
   | 档位 | 雅思 | 托福 iBT | 四六级/专四专八 |
   |------|------|----------|----------------|
   | **A1** | ＜4.0 | 0–31 | 低于四级 |
   | **A2** | 3.0–3.5 | 32–41 | 接近四级 |
   | **B1** | 4.0–5.0 | 42–71 | CET-4（四级） |
   | **B2** | 5.5–6.5 | 72–94 | CET-6（六级） |
   | **C1** | 7.0–8.0 | 95–120 | 专四/专八 |
   | **C2** | 8.5–9.0 | 110–120 | 专八优秀 |

2. **自适应自测小测**（无分数时）——
   ```bash
   python scripts/diagnose.py --quiz            # 交互问答（12 题，A1→C2 递进）
   ```
   脚本逐级判定，输出你**连续通过的最高档位**（保守，避免高估）。

**输出 `diagnose.json`**，随后 `prepare --diagnose diagnose.json` 自动采用该档位：
```bash
python scripts/run_episode.py prepare --episode "Friends S01E01" \
    --subtitle "<字幕 .srt/.json 路径或直链>" --diagnose diagnose.json --work-dir .
```
> 也可 `--by-cefr B1` 手动指定；`auto` 时则改由字幕词汇密度反推建议档位。

---

## 🆕 全量能力（全球顶尖闭环的硬指标）

除上面的检索与诊断外，本 skill 还把「听说读写」每个环节的反馈做成**闭环**，而不是单向练习：

- **🎧 听力 · 音素级 + 连读拆解**：`listening.json` 新增 `minimal_pairs`（最小对立体，专治听得清分不清）与 `connected_speech`（把自然语速原句拆成弱读/连读/闪音读法）。导出在听标签页、Excel/Word「最小对立体·连读拆解」表、Markdown 均有呈现。
- **🗣️ 口语 · Whisper 实际评分闭环**：每条口语可带 `asr_target`（目标句）。录完音运行 `score_speaking.py --audio 录音 --target "..."`（或 `--tasks tasks.json` 批量），用 Whisper 转写并逐词比对，标出丢失/错误/多余词与词序问题。**诚实边界**：只做转写比对，不评口音；真实发音回看正片跟读。
- **✍️ 写作 · rubric 自动化校验**：每条写作可带 `checks`（机器可校验量规：`has_word` / `min_words` / `max_words` / `tense`）。把作文存 `essay.txt`，运行 `score_writing.py --task <id> --text essay.txt --tasks tasks.json`，自动给出逐项通过与改进建议；agent 再在此基础上做深度批改。
- **🔁 跨集 · 同词多语境复现**：`build` 自动维护 `vocab_bank.json`（已学词+旧语境）。学下一集时 `prepare` 自动跑 `cross_episode.py`，把已学词在新字幕里的新语境捞出来写成 `recall_hints.json`（旧语境→新台词对照），纳入复习页，复用记忆更牢。

---

## 🎯 Why DramaLex? (Pain → Solution)

| Pain Point | DramaLex Solution |
|------------|-------------------|
| 📺 Watch but learn nothing — words vanish after the credits | **Target-lexicon priming**: mine a batch of B1–C1 words/chunks *before* you watch (count auto-estimated from subtitle length, ≈22–34 per 15 min; override with `--word-cap`), so input is comprehensible (Krashen i+1) |
| 🦻 Can understand with subs, lost without them | **Listening phase**: gist/detail Qs + dictation with the *same* target lines — ear-training, not just reading |
| 🗣️ Know words but can't produce them | **Speaking phase**: shadowing + role-play + output prompts that *force-reuse* the target lexicon (Swain output hypothesis) |
| 📝 Subtitles aren't "real reading", and writing gets no feedback | **Transcript literacy** (pragmatics/register/implicature) + **writing with rubric + agent correction** |
| 🔁 Review is a separate chore | **Cross-skill SRS**: vocab + dictation + listening + cloze flow back into one review stream |

---

## 🧠 Methodology Foundation (evidence-based, not vibes)

| Framework | How DramaLex uses it |
|-----------|----------------------|
| **Nation's Four Strands** | Meaningful input (Watch/Read) + meaningful output (Speak/Write) + language focus (vocab cards) + fluency (shadowing) — all four covered per episode |
| **Krashen i+1 / Comprehensible Input** | Visual context of drama + pre-primed vocab makes input understandable |
| **VanPatten Input Processing** | Priming directs attention to form *before* viewing |
| **Schmidt's Noticing** | Transcript annotation + dictation make form *noticeable* |
| **Swain Output Hypothesis** | Speaking/writing tasks *push* production; agent feedback closes the loop |
| **Laufer & Hulst Involvement Load** | Production tasks (reuse target words) carry higher involvement than passive review |
| **Webb & Rodgers (vocabulary through viewing)** | Words met repeatedly across skills = deeper retention |
| **Ebbinghaus / SM-2** | Spaced repetition via Anki / HTML-local storage |
| **Zimmerman Self-Regulated Learning** | Pre-goal + post-reflection + exit check metacognition layer |

---

## 🧬 The Integrative Spine (what makes it "complete", not a grab-bag)

> **One target lexicon → four-skill recycling.**
> The words/chunks mined in Phase 0 are *required* again in Phase 2 (dictation lines), Phase 3 (annotation examples), Phase 4 (speaking prompts), Phase 5 (writing tasks). The same items resurface in review. This is the difference between a playlist of exercises and a real learning loop.

---

## 🔄 Six-Phase Workflow

Each phase: **Agent does the linguistic generation following the schema in `schemas/`; scripts do the mechanical work (parse / audio / export).** This keeps output consistent across *every* agent (Claude / WorkBuddy / OpenClaw / Code X / Cursor / Doubao…).

### Phase 0 · Prime (预习)
- **Goal**: activate schemas, pre-teach the target lexicon.
- **Agent**: from `subtitle.json` candidates, select a high-value batch of items (count per `word_cap` in the handoff — auto-estimated from subtitle length, or set via `--word-cap`; chunks prioritized), enrich each with IPA / CEFR / gloss / collocation / real line / model example.
- **Script**: `parse_subtitles.py` → `gen_audio.py` → `export_cards.py`.
- **Output**: `words.json` + vocab cards (Anki/HTML).
- **Schema**: `schemas/vocab_card.schema.md`.

### Phase 1 · Watch (看)
- **Goal**: first comprehensible pass.
- **Agent**: generates `watch.json` (viewing protocol: no-subs gist → subs detail → no-subs again; a "catch expression" note slot) — follows `schemas/watch.schema.md`. *No cards produced*, this is consumption.
- **Deliverable**: exported into HTML (`🎬 看` tab), Excel (`观看` sheet), Word (`1 · 看` heading). Anki mode has no Watch card by design (consumption, no memory item).
- **Honest note**: real native-speed listening is built here by *watching the actual episode*; DramaLex prepares and quizzes you, it does not replace the show.

### Phase 2 · Listen (听)
- **Agent**: generates `listening.json`:
  - **Comprehension Qs** (5–8): gist + detail, multiple-choice, with rationale. Asked *audio-only* first.
  - **Dictation** (5–8): key lines with target words blanked; learner types what they hear.
- **Script**: `generate_listening.py` (validate + `listening.md`; audio for referenced lines is collected centrally by `export_hub.py`).
- **Schema**: `schemas/listening.schema.md`.

### Phase 3 · Read (读 · Transcript Literacy)
- **Goal**: pragmatic/discourse reading of the transcript — *not* academic reading (subtitles are spoken text). Train turn-taking, implicature, register, humor **and the grammar/collocation/pronunciation knowledge hiding in the lines**.
- **Agent**: generates `annotated.json`:
  - **Annotations** (8–10): 维度必须覆盖 **idiom / register / implicature / pragmatics / culture / humor / grammar / pattern / collocation / discourse / pronunciation**。其中 `grammar`/`pattern`/`collocation`/`pronunciation` 必须填 `rule`（可迁移规则）+ `more`（脱离本片的同类例句），让单句规律能泛化。这正是「字幕里除了单词的英语知识点」。
  - **Cloze** (3–4): key lines with blanks for reading comprehension.
- **Script**: `annotate_transcript.py` → `transcript_annotated.md`.
- **Schema**: `schemas/transcript_annotated.schema.md`.

### Phase 4 · Speak (说)
- **Agent**: generates `tasks.json → speaking`:
  - **Shadowing**: model line + TTS reference audio + pronunciation micro-checklist (stress / vowels / -ed / linking).
  - **Role-play**: assign a character's lines.
  - **Output prompt**: "retell using ≥3 target words" / "make a sentence with X".
  - **Optional Whisper**: record → transcribe → diff vs target → flag dropped/wrong words (transcript-match, *not* a pronunciation score).
- **Script**: `generate_tasks.py` + audio in `export_hub.py`.
- **Schema**: `schemas/tasks.schema.md`.

### Phase 5 · Write (写)
- **Agent**: generates `tasks.json → writing`:
  - **Rewrite** (register shift: diary ↔ text message ↔ email).
  - **Continue** (write next 5 lines of dialogue).
  - **Summary** (≤50 words using ≥3 target words).
  - Each with a **self-review rubric** + **agent correction pass** (learner pastes writing → agent corrects and shows where target chunks should appear). *Feedback is the learning.*
- **Script**: `generate_tasks.py`.

### Phase 6 · Review + Exit (复习 + 出口)
- **Cross-skill SRS (HTML mode now included)**: vocab **and** dictation **and** cloze cards each carry a local 间隔复习 (Leitner-style interval doubling) in `practice.html` — grading "记住了/没记住" hides the card and reschedules it. The habit bar at the top shows 🔥 连续打卡天数、📚 今日待复习、📅 明日待复习, so the "跨技能复习" actually lives in the zero-install HTML, not just Anki.
- **Cross-skill SRS (Anki mode)**: vocab + dictation + listening + cloze → Anki recall items (full spaced repetition via SM-2). For true cross-device scheduling, import the `.apkg` or use `--mode B` (all→Anki).
- **Metacognition**: pre-episode 1-line goal + post-episode reflection ("noticed / still fuzzy") + **exit mini-check** (randomly drawn 2–3 Qs spanning the four skills; saved locally).

---

## 🎛️ CEFR Level Knob

Set learner level (**A1–C2**) to calibrate: `# of dictation blanks`, question difficulty, whether subtitles are allowed in Listen phase, and how many target words the writing task must reuse. Friends S01E01 ≈ A2–B1, so most cards are B1 consolidation with a B2–C1 core — graded honestly.

**档位从哪来**：先用「Phase 0 · 学前诊断」（`diagnose.py` 凭雅思/托福/四六级分数或自适应自测定位），再 `prepare --diagnose diagnose.json`；或 `--cefr` 手动指定；`auto` 时由字幕词汇密度反推。

**Honesty rule for the CEFR knob**: the knob calibrates *task difficulty*, it does **not** auto-filter the vocab by the learner's level. At low learner levels (A2/B1) the agent must either exclude C1 abstract words (e.g. *revelation / vulnerability / metaphor*) or mark them `挑战★` and skip them in production tasks; and **always report the level distribution** of the mined cards (e.g. "10×B1 / 7×B2 / 2×C1") so the learner sees the truth instead of a flat "B1".

### 🎓 考试对照标注（雅思 / 托福 / 四六级）
为让难度更直观，CEFR 档位会自动映射主流英语考试分数区间（见 `scripts/exam_map.py`，约值）：
`B1 → 雅思4.0–5.0 · 托福42–71 · 四六级CET-4`；`B2 → 雅思5.5–6.5 · 托福72–94 · CET-6`；`C1 → 雅思7.0–8.0 · 托福95–120 · 专四/专八`。
- 难度建议行会直接写成 `B1（约 雅思4.0–5.0 · 托福42–71 · 四六级CET-4）`。
- 每个单词卡（HTML 复习/预习、Anki 卡背、Excel「考试对照」列）都会标注其 `cefr` 对应的考试区间；`words.json` 也可显式写 `exam` 字段覆盖。
- 分数区间非官方精确边界，已在展示处标注"约"，仅供用户定位自身水平参考。

---

## 📅 每日复习提醒（agent 自动化 · 用户选择开启）

> 设计动机：HTML 里的 habit loop 是**被动**的——用户不打开网页就看不到。要"主动"提醒，用支持调度自动化的 agent（Claude / WorkBuddy / OpenClaw / Code X / Cursor / Doubao 等）的**调度自动化**能力，而非 HTML。

**默认不开启。** 仅当用户显式要求（如 `build --remind` 或直接说"开启每日提醒"）时，agent 才用 `automation_update` 登记一条：

```
name:    DramaLex 每日复习提醒
scheduleType: recurring
rrule:   FREQ=DAILY;BYHOUR=21;BYMINUTE=0
prompt:  读 <work_dir>/progress.md。若今天日期无「已打卡」记录，提醒用户打开
         practice.html 做跨技能复习 / 打开 Anki 复习牌组；若已打卡则鼓励并预告下一集。
         语气简短、不啰嗦。
cwds:    <work_dir>
```

- `progress.md` 由 `build` 自动写出（记录每天生成的剧集与状态），提醒逻辑读它判断"今天学了没"。
- 用户随时可让我"关闭每日提醒"，agent 用 `automation_update` 将其暂停/删除。
- 注意：这是"agent 会话内的主动提醒"（Claude / WorkBuddy / OpenClaw / Code X / Cursor / Doubao 等会话内均同），不是操作系统推送；要做到微信/系统通知需额外连接器。

---

## ✅ 内容质量闸门（validate）

`build` 在跑 TTS 与导出**之前**自动调用 `scripts/validate.py`，校验：
- `word.line` 确实来自真实字幕（防 agent 编台词）、`cefr` 合法、目标词不重复；
- 听写/精读/任务字段非空、`id` 连续；
- **诚实档位**：若 `C1` 词占比 > 30% 且未标 `挑战★`，给 warning（提示低档位用户易被劝退）；
- **词句一致性**：单词目标词未出现在其 `line` 中时给 warning（语块例外）。

有 error 级问题会**终止导出**并退出码 11（可用 `--no-validate` 跳过，但不推荐）。也可单独跑：
`python scripts/validate.py --work-dir . --subtitle subtitle.json`

---

## 🔧 本轮增强能力（最高标准质检）

- **`--formats` 新增 `md`**：导出 Obsidian / 双链笔记友好的单文件 Markdown（纯文本、可检索、可互相链接）。完整格式现为 `html,anki,excel,word,md`。
- **口语/写作产出卡进 HTML 复习**：Review 页现在包含口语/写作卡（纳入本地 SRS 与 habit 计数），纯 HTML 用户（Mode C）也有说/写复习入口，与 Anki 模式互补。
- **复习进度可导出/导入**：HTML 复习页提供「⤓ 导出 / ⤒ 导入」按钮，把 `localStorage` 里的复习状态存成 JSON 文件——换设备、清缓存都不丢（单文件离线可用，无需后端）。
- **本周打卡日历**：HTML 顶部新增 7 天打卡格（一…日），已打卡日显示绿色 ✓，动力更直观（状态同样存 localStorage）。
- **空字幕防护**：`prepare` 解析出 0 行字幕会**显式报错并退出码 3**，不会静默给最小词量、把下游建立在空数据上。
- **TTS 失败汇总**：某条词/句 TTS 合成失败时不再静默跳过，`build` 末尾汇总缺音频清单（不阻断导出）。
- **Anki 导入指引**：生成 `.apkg` 后自动打印导入方式与牌组名（`Friends S01E01 · DramaLex`）。
- **下一集追踪**：`progress.md` 记录剧集序号并自动推导下一集（如 `S01E01 → S01E02`）；每日提醒据此预告"该看下一集了"。
- **跨集词库**：`build` 维护 `vocab_bank.json`（累计已学词），`prepare` 据此在交接单提示"优先挖新词、跳过已掌握项"。
- **Excel / Word 双语**：`--ui-lang zh/en` 现在同时作用于 Excel 表头、Word 章节标题与法律声明（HTML 早已完整双语）。



---

## 🗂️ Three Review Modes (all supported — pick per user)

| Mode | Recall items (vocab/dictation/listening/cloze) | Production (speaking/writing) |
|------|-----------------------------------------------|-------------------------------|
| **A · Layered (default)** | → Anki | → HTML practice hub |
| **B · All-to-Anki** | → Anki | also → Anki as production cards |
| **C · All-HTML** | → HTML hub | → HTML hub (weaker SRS) |

Set via `export_hub.py --mode A|B|C`. Combine with `--format {html,anki,excel,word}` to pick the delivery platform; each format emits exactly one file.

---

## 🤖 Cross-Agent & Mobile

- **Scripts** use only Python stdlib + optional `genanki` / `whisper` — no agent-specific APIs. Any agent that can run Python can use DramaLex.
- **Generation ≠ Review** decoupled: the agent generates; Anki / browser handle review, scheduling and mobile sync.
- **Zero-install option**: `practice.html` opens in any browser (phone included), audio embedded, no app needed.
- See `references/CROSS_AGENT.md` for per-agent usage.

---

## ⚠️ Honest Boundaries (read before trusting the hype)

1. **TTS ≠ original audio.** Line audio is synthesized (macOS `say` / espeak / gTTS). It is a *pronunciation reference / ear primer*, not the actor's voice. Real connected-speech listening (weak forms, linking, intonation) comes from **watching the actual episode**.
2. **Whisper = transcript-match, not pronunciation scoring.** It flags missing/wrong *words*, not accent or phoneme accuracy.
3. **Drama is not a full curriculum.** DramaLex is a *fluency + spoken-register + listening* engine. It does not replace systematic grammar teaching, academic writing, or extensive reading.
4. **合法检索字幕（检索与使用）。** 默认不抓取版权字幕。Agent 用 `find_subtitles.py` / WebSearch **检索并定位**公开来源链接，把字幕解析到位供你使用；字幕来源于互联网公开渠道，仅供个人非商业学习使用。详见 `references/SUBTITLE_LEGAL.md`。
5. **Privacy.** If Whisper is used, audio is processed locally; nothing is uploaded.

---

## 📁 File Layout

```
drama-lex/
├── SKILL.md                 # this file
├── schemas/                 # cross-agent output templates (vocab/listening/annotation/tasks/watch)
├── scripts/
│   ├── find_subtitles.py    # 合法字幕检索入口（生成来源链接，不爬不下载）
│   ├── retrieve_subtitles.py# 检索字幕来源 + 解析 + 版本校验（agent 检索流程最后一公里）
│   ├── fetch_subtitles.py   # 检索/获取用户提供的字幕直链（法律闸门在用户侧；兼容旧用法）
│   ├── parse_subtitles.py   # .srt/.vtt → cleaned lines + word freq + candidates
│   ├── diagnose.py          # 学前诊断：雅思/托福/四六级分数→CEFR，或自适应自测小测
│   ├── gen_audio.py         # TTS → wav (say/espeak/pyttsx3/gTTS)
│   ├── generate_listening.py
│   ├── annotate_transcript.py
│   ├── generate_tasks.py
│   ├── score_speaking.py    # 口语 Whisper 实际评分闭环（录音→转写比对→标记丢失/错误词）
│   ├── score_writing.py     # 写作 rubric 自动化校验（has_word/min_words/max_words/tense）
│   ├── cross_episode.py     # 跨集同词多语境复现（vocab_bank + 新字幕 → recall_hints.json）
│   ├── export_hub.py        # 单文件导出：--format {html,anki,excel,word,md} + --mode A|B|C + --watch + --ui-lang
│   ├── estimate.py          # 由字幕时长+词汇密度推导各材料数量（连续公式）；suggest_cefr 反推档位；空字幕防护
│   ├── validate.py          # 内容质量闸门（line 真实/cefr/去重/诚实档位/词句一致性）
│   ├── exam_map.py          # CEFR ↔ 雅思/托福/四六级 分数量表（A1–C2 全分段 + 反向映射）
│   └── run_episode.py       # 一键编排：prepare（抓字幕+解析+诊断+跨集复现+交接单）/ build（TTS+导出）
└── references/
    ├── stopwords.txt
    ├── ANKI_GUIDE.md
    ├── CROSS_AGENT.md
    ├── TTS_NOTE.md
    └── SUBTITLE_LEGAL.md   # 字幕获取与法律边界（Safe Harbor 指南）
```

---

## 🚀 Quick Start

### 一键编排（推荐 · 1–2 条命令）

```bash
# A) 准备：抓字幕 + 解析 → 写出 Agent 交接单（告诉 agent 该产出哪些 JSON）
python scripts/run_episode.py prepare --episode "Friends S01E01" \
    --subtitle "<字幕 .srt/.json 路径或直链>" --work-dir . \
    --cefr B1 --focus balanced --chunks-only --ui-lang zh
#   或直接粘贴台词：--text "paste dialogue here"
#   --word-cap  每集目标词/语块数量（如 20 或 15–30）；省略则按字幕时长+词汇密度自动估算
#              （约每 15 分钟 22–34 个，长片可达 100+；结果只作建议上限，agent 按价值取舍）
#   --cefr      学习者档位 auto/A2/B1/B2/C1/C2，只校准任务难度、不筛词（诚实档位）；缺省 auto
#   --focus     balanced/listen/speak/read/write，按比例调高对应环节题量
#   --chunks-only  词汇环节只挖语块，不挖孤立单词（进阶偏好）
#   --ui-lang   zh/en，HTML 界面语言

# B) Agent 按 schemas/ 生成 words.json / listening.json / annotated.json / tasks.json / watch.json
#    （JSON 不齐时 build 会自动打印交接单并退出码 10，便于回到 agent 补生成）

# C) 构建：跑 TTS + 一次性导出单文件（html/anki/excel/word/md 任选，逗号分隔）
python scripts/run_episode.py build --work-dir . --episode "Friends S01E01" \
    --deck "Friends S01E01" --mode A --formats html,anki,excel,word,md
#    → out/out_html/practice.html · out/out_anki/<deck>.apkg
#    → out/out_excel/<deck>.xlsx · out/out_word/<deck>.docx · out/out_md/<deck>.md
#   其他实用开关：--remind（开启每日复习提醒，默认关）/ --no-validate（跳过质量闸门）
```

### 分步（等价，便于调试单个平台）

```bash
# 1) Get the subtitle (you provide a link you have the right to use)
python scripts/fetch_subtitles.py --url "<your-subtitle-url>" --output subtitle.srt
#   or just paste/Upload the .srt

# 2) Parse
python scripts/parse_subtitles.py --input subtitle.srt --output subtitle.json

# 3) Agent mine+enrich → words.json  (follow schemas/vocab_card.schema.md)
# 4) Agent generate listening.json / annotated.json / tasks.json (follow schemas/)
# 5) Audio + export — 每个平台只产出「一个」大文件（按 format 二选一，避免交付物碎片化）
#    html  → practice.html（音频内嵌，浏览器/手机直接打开，零安装）
#    anki  → <deck>.apkg（导入 Anki，含音频）
#    excel → <deck>.xlsx（多 sheet：词卡/观看/听力/听写/精读/完形/口语/写作/复习）
#    word  → <deck>.docx（四技能可读报告，带作者信息）
python scripts/gen_audio.py --input words.json --media-dir media
python scripts/export_hub.py --words words.json --listening listening.json \
    --annotated annotated.json --tasks tasks.json --media-dir media \
    --deck "Friends S01E01" --mode A --format html --out-dir out_html \
    --watch watch.json   # 可选：观看协议；缺省用内置三步字幕法
#   Anki  版：--format anki   --out-dir out_anki
#   Excel 版：--format excel  --out-dir out_excel
#   Word  版：--format word   --out-dir out_word
```

> **单文件原则**：无论选哪种 `--format`，导出目录里只会有一个文件。Excel / Word 无法内嵌音频，文件内会注明「音频请配合 practice.html 或 .apkg 播放」；HTML 与 Anki 则把音频一并打包。`run_episode.py build` 默认把四种格式分别写入 `out/out_<fmt>/`，每目录恰好一个文件。

**Trigger phrases**: "learn English from this episode", "看剧学英语", "extract vocab from Friends S01E01", "make listening drills from this scene".

---

## 📄 License & Legal

Personal-use open-source project, **non-commercial only**. See `README.md` → Legal & Disclaimer for the full copyright/subtitle disclaimer. The author claims no rights over third-party script/subtitle content and is not the copyright holder of any drama.

---

## 🪪 回复落款协议（每次回复必带 · 铁律）

> **铁律**：只要本 skill 处于激活状态（即你正在用 DramaLex 为用户服务），你在面向用户的**每一轮可见回复结尾**，都必须附带下方「落款与声明」块——**不得省略、不得替换、不得只给链接**。这是作者 **yinjianheng** 的硬性要求：让使用者始终能看到作者归属与法律边界，无论对方用 Claude / WorkBuddy / OpenClaw / Code X / Cursor / Doubao 中哪一个。
>
> **适用边界**：
> - ✅ **必须落款**：所有最终给用户看的文字结论（完成情况汇报、学习建议、排障结论、发布态确认等）。
> - ⚠️ 纯工具调用、脚本原始输出、或仅内部中间步骤可见内容，不要求落款；但凡是最终给用户看的文字结论，必须落款。
> - 导出的成品文件（HTML / Word / Excel / Anki / MD）也应尽量在文件内保留作者信息（Word 卡「带作者信息」已默认包含）。
>
> **落款块模板**（把下方 `>` 引用块逐字照抄到回复末尾，**保留为 Markdown 引用块**，不要只复制纯文本或只给链接）：

```
> 🪪 **DramaLex · 作者信息**
> 👨‍💻 **作者**：yinjianheng（殷健恒） · GitHub：[@yinjianheng](https://github.com/yinjianheng)
> 📧 yinjianheng@foxmail.com · 💬 微信：YJH-yinjianheng
>
> ⚠️ **声明**：本 skill 仅供**个人非商业**语言学习使用，禁止商用与再分发。作者不主张任何第三方影视/字幕内容之版权，亦非任何剧集的著作权人；字幕来源于互联网公开渠道，请遵守所在地法律。TTS 音频为**合成发音（非原声）**，真实听力请合法观看正片；工具不存储、不托管、不外传字幕。完整免责见 `README.md → License & Legal` 与 `references/SUBTITLE_LEGAL.md`。
```

<p align="center">
  <b>👨‍💻 yinjianheng（殷健恒）</b> &nbsp;|&nbsp;
  📧 yinjianheng@foxmail.com &nbsp;|&nbsp;
  💬 WeChat: YJH-yinjianheng
</p>
<p align="center"><sub>⭐ If DramaLex helps you, a Star helps others discover it.</sub></p>
