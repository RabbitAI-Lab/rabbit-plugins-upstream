# Schema · tasks (Phase 4 Speak · Phase 5 Write)

Agent emits `tasks.json`:

```json
{
  "episode": "Friends S01E01",
  "speaking": [ { ... } ],
  "writing": [ { ... } ]
}
```

## speaking[ ] — production drills (reuse target lexicon!)
| Field | Type | Notes |
|-------|------|-------|
| `id` | int | 1..N |
| `type` | enum | `shadow` \| `roleplay` \| `prompt` |
| `instruction` | string | what to do |
| `model_line` | string? | the line to shadow / the character line (audio generated) |
| `use_words` | array<string> | target words/chunks that MUST be reused (recycling spine) |
| `checklist` | array<string> | pronunciation micro-checklist, e.g. `["stress","vowels","-ed","linking"]` |
| `focus_sounds` | array<string>? | **逐句重点发音**：针对该 model_line 的具体音（而非通用清单），如 `["gotta 的 /t/ 闪音化","protect 的元音 /e/","连读 got a → /ɡɒdə/"]`，让 learner 知道这句中到底练什么 |
| `asr_target` | string? | **口语评分目标句**：用于 Whisper 实际评分闭环（`score_speaking.py`）的对照文本。shadow/roleplay 取 `model_line`；prompt 取「应当产出」的范例句。留空则该条不参与自动评分 |
| `character` | string? | for roleplay, who you play |

- 3–4 items. At least one `prompt` item forces reuse of ≥3 Phase-0 target words.
- Shadowing audio is **TTS reference**, not the actor — state this.

## writing[ ] — with feedback loop
| Field | Type | Notes |
|-------|------|-------|
| `id` | int | 1..N |
| `type` | enum | `rewrite` \| `continue` \| `summary` |
| `instruction` | string | the task |
| `register` | enum | `casual` \| `formal` \| `mixed` |
| `require_words` | array<string> | target words that MUST appear (recycling spine) |
| `rubric` | array<string> | self-review checklist (3–4 items, 人工自评用) |
| `checks` | array<object>? | **自动化评分量规**（`score_writing.py` 用）：每项 `{type, value}`，支持 `has_word`（必须含某词/语块，大小写不敏感）、`min_words`/`max_words`（字数上下限）、`tense`（soft，仅提示，如 `past`）。留空则只做人工 rubric 自评 |
| `model` | string? | a model answer for comparison (agent also does a correction pass on learner text) |

- 3 items, one of each type. `summary` ≤50 words.
- Feedback is mandatory: agent corrects learner writing and shows where target chunks should appear.

## Example
```json
{
  "speaking": [
    {"id":1,"type":"prompt","instruction":"Imagine you're Rachel telling a friend you left your fiancé. Use 'drift apart' and 'freak out'.",
     "use_words":["drift apart","freak out"],"checklist":["stress","vowels"]}
  ],
  "writing": [
    {"id":1,"type":"summary","instruction":"Summarize Rachel's runaway in ≤50 words using ≥3 target words.",
     "register":"casual","require_words":["freak out","drift apart","be supposed to"],
     "rubric":["Used ≥3 target words?","Past tense correct?","Under 50 words?"],
     "model":"Rachel freaked out before the wedding — she and Barry had drifted apart, and she wasn't supposed to marry him."}
  ]
}
```
