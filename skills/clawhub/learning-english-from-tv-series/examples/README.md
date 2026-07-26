# DramaLex 示例包（Examples）

本目录提供可直接 `build` 的示例学习包，用来验证整条「检索 → 诊断 → 解析 → 听说读写闭环 → 单文件导出」流水线。

## 目录

| 示例 | 内容 | 新闭环字段 | 说明 |
|------|------|------------|------|
| `Friends-S01E01/` | 《老友记》S01E01 基础包 | 无（基线） | 早期样板，演示六阶段最小闭环；不含音素/连读/Whisper/自动量规。 |
| `Happyness-2006/` | 《当幸福来敲门》(2006) 完整包 | ✅ 全量 | **推荐**：覆盖本轮全量改造的全部能力，是检验 skill 是否「全球顶尖」的金标准。 |

> 想看全部新能力（最小对立体、连读拆解、Whisper 口语评分、写作 rubric 自动校验、跨集复现），请用 `Happyness-2006/`。

## 一键构建（5 种单文件交付物）

以 `Happyness-2006/` 为例（无需字幕，包内已含 `subtitle.json` 精选台词）：

```bash
cd examples/Happyness-2006
python ../../scripts/run_episode.py build \
  --work-dir . \
  --episode "The Pursuit of Happyness (2006)" \
  --deck "The Pursuit of Happyness" \
  --mode A \
  --formats html,anki,excel,word,md
```

构建会：
1. 跑 TTS（macOS `say` / Linux `espeak-ng` / 在线 `gTTS`），为每个词原句与听力/口语目标句生成音频；
2. 自动维护 `vocab_bank.json`（已学词库）；
3. 产出 5 种单文件：

| 格式 | 产物 | 含新字段 |
|------|------|----------|
| `html` | `out/out_html/practice.html` | 四技能看板 + 音素级 + 连读 + 口语可评分提示 + 写作自动量规 + 跨集复现 |
| `anki` | `out/out_anki/<deck>.apkg` | 词汇 + 听写 + 听力 + 完形（模式 A）；模式 B 加口语/写作产出卡 |
| `excel` | `out/out_excel/<deck>.xlsx` | 含「最小对立体」「连读拆解」表 + 口语「可评分目标句」列 + 写作「自动量规」列 |
| `word` | `out/out_word/<deck>.docx` | 同上结构的 Word 版 |
| `md` | `out/out_md/<deck>.md` | 纯文本/微信转发友好版 |

## 评分闭环（验证用）

```bash
# 写作 rubric 自动校验：把作文存 essay.txt
python ../../scripts/score_writing.py --task 3 --text-file essay.txt --tasks tasks.json
#   checks 支持 has_word / min_words / max_words / tense
#   输出逐项通过率 + 改进建议（缺目标词/字数不足/时态提示）

# 口语 Whisper 评分（需 pip install openai-whisper 或 faster-whisper）
python ../../scripts/score_speaking.py --tasks tasks.json --audio-dir ./recordings
#   对每条带 asr_target 的口语做转写比对，标出丢失/错误/多余词与词序问题
#   未安装 Whisper 时优雅退出并给出安装指引，不静默失败
```

## 跨集复现

学完一集后 `vocab_bank.json` 已累计已学词。学下一集时 `prepare` 阶段会自动跑 `cross_episode.py`，
把已学词在新字幕里的新语境捞成 `recall_hints.json`（旧语境 → 新台词对照），纳入复习页。

```bash
python ../../scripts/cross_episode.py --bank vocab_bank.json --subtitle ../下一集/subtitle.json --episode "下一集代号"
```

## 学前诊断（可选）

```bash
python ../../scripts/diagnose.py --ielts 6.5     # 雅思/托福/四六级分数 → CEFR
python ../../scripts/diagnose.py --quiz           # 自适应自测（12 题 A1→C2）
# 输出 diagnose.json，再 --diagnose diagnose.json 交给 prepare 自动采用档位
```

## 字幕检索（合法优先）

DramaLex 不内建爬虫。user 给模糊剧名/集数 → agent 用 WebSearch 上网核对正确字幕 →
agent 自主 `retrieve_subtitles.py` 检索解析（字幕来源于公开渠道，仅供个人非商业学习）。法律边界见 `references/SUBTITLE_LEGAL.md`。
