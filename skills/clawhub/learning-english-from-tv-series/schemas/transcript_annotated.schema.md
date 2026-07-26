# Schema · transcript_annotated (Phase 3 · Read · Transcript Literacy)

Agent emits `annotated.json`. This phase trains **pragmatic / discourse reading** of spoken text — NOT academic reading.

```json
{
  "episode": "Friends S01E01",
  "annotations": [ { ... } ],
  "cloze": [ { ... } ]
}
```

## annotations[ ] — pragmatic / discourse notes
| Field | Type | Notes |
|-------|------|-------|
| `id` | int | 1..N |
| `line` | string | the real transcript line |
| `speaker` | string | `""` if unknown |
| `focus` | enum | `idiom` \| `register` \| `implicature` \| `pragmatics` \| `culture` \| `humor` \| `grammar` \| `pattern` \| `collocation` \| `discourse` \| `pronunciation` |
| `note` | string | what's going on beneath the words (meaning, why funny, social meaning) |
| `tip` | string | a learner takeaway |
| `rule` | string? | **规则/模式**：当 focus 为 grammar/pattern/collocation/pronunciation 时，写明可迁移的语法规则或语音规律（如 "if + 过去时 → 第二条件句，表虚拟"） |
| `more` | string? | **更多例句**：1–2 个脱离本片的同类例句，帮助泛化 |

- 8–10 items. Prefer lines that reveal **how meaning is built beyond words**: sarcasm, politeness, indirectness, turn-taking, cultural reference.
- **语言知识点维度（核心增强）**：除词汇外，必须挖掘字幕里的「非单词」知识点——语法结构(grammar/pattern)、固定搭配(collocation)、语篇衔接(discourse)、语音规律(pronunciation)、文化(culture)。每条 grammar/pattern 必须给 `rule` + `more`，让 learner 能把单句规律迁移到新语境。
- `focus: humor` is encouraged for sitcoms (mechanism of the joke = high affective engagement).

## cloze[ ] — reading comprehension blanks
| Field | Type | Notes |
|-------|------|-------|
| `id` | int | 1..N |
| `line` | string | full line |
| `blanked` | string | line with `___` (1–2 blanks) |
| `answers` | array<string> | missing words in order |

- 3–4 items. Reading-level (not listening-level): learner sees the text.

## Example
```json
{
  "annotations": [
    {"id":1,"line":"Joey, stop hitting on her! It's her wedding day.",
     "speaker":"Monica","focus":"pragmatics",
     "note":"'hitting on' = slang for flirting/approaching romantically. Monica uses it to police Joey's behavior — indirect social correction.",
     "tip":"Slang verbs like 'hit on' are common in casual US dialogue; note the register."}
  ],
  "cloze": [
    {"id":1,"line":"Welcome back to the world. Grab a spoon!",
     "blanked":"Welcome back to the ___. Grab a ___!","answers":["world","spoon"]}
  ]
}
```
