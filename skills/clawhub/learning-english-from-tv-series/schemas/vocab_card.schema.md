# Schema · vocab_card (Phase 0 · Prime)

Every agent MUST emit `words.json` as a JSON **array** of objects matching this schema. This guarantees consistent card quality across agents.

## Fields (all required unless noted)

| Field | Type | Notes |
|-------|------|-------|
| `term` | string | the word OR chunk (e.g. `freak out`, `be supposed to`) |
| `type` | enum | `word` \| `chunk` |
| `cefr` | enum | `A2`\|`B1`\|`B2`\|`C1`\|`C2` — honest level of THIS item |
| `exam` | string? | 考试对照标注（可选但推荐），由 `cefr` 经考试分数量表自动得出，如 `雅思4.0–5.0 · 托福42–71 · 四六级CET-4（四级）`；可留空，导出时会按 `cefr` 自动补注 |
| `pos` | string | part of speech / kind, e.g. `phrasal verb`, `noun`, `chunk` |
| `ipa` | string | GenAm or RP IPA, e.g. `/friːk aʊt/` |
| `gloss` | string | concise Chinese meaning |
| `collocation` | string | typical partner, e.g. `totally freaked out` |
| `line` | string | a REAL line from the episode containing the term |
| `line_speaker` | string | speaker name if known, else `""` |
| `example` | string | a model sentence (not from episode) reusing the term |
| `why` | string? | **为什么学**：这个词/语块在该语境下的高价值点（如「口语高频」「考试写作加分」「含易混搭配」），帮 learner 判断优先级 |
| `l1_note` | string? | **中文易错点**：针对中文母语者的典型干扰（false friend / 搭配误用 / 词性混淆），如 "pursue 不接 to do" |
| `tags` | array<string> | topic tags, e.g. `["phrasal","emotion"]` |
| `term_audio` | string? | filled by `gen_audio.py` (path) |
| `line_audio` | string? | filled by `gen_audio.py` (path) |

## Selection rules
- **Chunks prioritized**: phrasal verbs / collocations first; single words only to fill gaps.
- **Count**: auto-estimated from subtitle length (≈22–34 per 15 min; long films can reach 100+), conveyed via `word_cap` in the handoff. Treat it as a soft ceiling — pick high-value items, don't pad to the number. Override with `--word-cap` if desired.
- **CEFR target**: default B1–C1; if the show is easier (e.g. Friends), most cards are B1 consolidation — grade honestly, do NOT inflate.
- **Real lines only**: `line` must be an actual utterance from the parsed subtitle, not invented.

## Example
```json
{
  "term": "freak out",
  "type": "chunk",
  "cefr": "B2",
  "pos": "phrasal verb",
  "ipa": "/friːk aʊt/",
  "gloss": "（突然）极度慌乱、崩溃",
  "collocation": "totally freaked out; freak sb out",
  "line": "And then I really freaked out, when it hit me:",
  "line_speaker": "Rachel",
  "example": "Don't freak out — I'm only five minutes late.",
  "tags": ["phrasal","emotion"]
}
```
