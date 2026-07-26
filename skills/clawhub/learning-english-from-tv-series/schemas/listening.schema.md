# Schema · listening (Phase 2 · Listen)

Agent emits `listening.json`:

```json
{
  "episode": "Friends S01E01",
  "comprehension": [ { ... } ],
  "dictation": [ { ... } ],
  "minimal_pairs": [ { ... } ],
  "connected_speech": [ { ... } ]
}
```

## comprehension[ ] — gist / detail questions
Asked **audio-only first** (learner hears the line, not reads it).

| Field | Type | Notes |
|-------|------|-------|
| `id` | int | 1..N |
| `type` | enum | `gist` \| `detail` |
| `question` | string | the question |
| `options` | array<string> | 3–4 choices, one correct |
| `answer` | string | the correct option text (must match one in `options`) |
| `rationale` | string | why (references the line) |
| `audio_line` | string | the episode line to play as stimulus (matched to subtitle for audio) |

- 5–8 items total. Mix gist (main idea) + detail (specific fact).
- Difficulty scales with CEFR knob: fewer/cleaner options at A2, inference at C1.

## dictation[ ] — listen-and-type
| Field | Type | Notes |
|-------|------|-------|
| `id` | int | 1..N |
| `line` | string | full original line |
| `speaker` | string | `""` if unknown |
| `blanked` | string | line with target words replaced by `___` (1–3 blanks) |
| `answers` | array<string> | the exact missing words, in order |
| `target_words` | array<string> | must overlap the Phase-0 target lexicon (recycling spine) |

- 5–8 items. Blanks should include ≥1 Phase-0 target word.
- At lower CEFR, blank fewer words; at higher, blank function words too.

## minimal_pairs[ ] — 音素级 / 最小对立体（phoneme-level ear training）
专治「听得清但分不清」：两个只差一个音素的词（如 *ship/sheep*、*bad/bed*），
先看清 IPA 差别，再听原句判断本集实际说的是哪一个。这是听力从「能懂大意」到「能抓细节」的关键一跳。

| Field | Type | Notes |
|-------|------|-------|
| `id` | int | 1..N |
| `word_a` | string | 候选词 A |
| `ipa_a` | string | A 的 IPA |
| `word_b` | string | 候选词 B（与 A 仅一音素之差） |
| `ipa_b` | string | B 的 IPA |
| `in_episode` | enum | `a` \| `b` — 本集原句里**实际出现**的是哪一个（供对答案） |
| `line` | string | 含该词的真实原句（听音材料） |
| `hint` | string? | 辨音提示，如「长元音 /iː/ vs 短元音 /ɪ/：sheep 更长」 |

- 3–5 对。优先从本集真实台词里挑易混音素（长短元音、清浊辅音、/θ/–/s/、/v/–/w/ 等）。

## connected_speech[ ] — 连读拆解（connected speech breakdown）
把一条自然语速的原句**拆成口语真实读法**：弱读、连读、闪音、省音一一标注，
让 learner 看清楚「剧本写的」和「演员说的」之间的 gap（这正是没字幕时听不懂的根源）。

| Field | Type | Notes |
|-------|------|-------|
| `id` | int | 1..N |
| `line` | string | 原句（书面/字幕形式） |
| `gloss` | string? | 中文意思 |
| `breakdown` | array<{text, note}> | 逐块拆解；`text` 为该块的自然读法，`note` 标弱读/连读/闪音等，如 `{"text":"gonna","note":"going to 的弱读+连读"}` |

- 3–5 条。挑本集语速快、连读多的句子。

## Example
```json
{
  "comprehension": [
    {"id":1,"type":"gist","question":"Why did Rachel run away before the wedding?",
     "options":["She was afraid of flying","She realized she didn't love Barry","She lost her job"],
     "answer":"She realized she didn't love Barry",
     "rationale":"She says 'I just don't love him.'",
     "audio_line":"I just don't love him."}
  ],
  "dictation": [
    {"id":1,"line":"I was supposed to be headed for Aruba on my honeymoon.",
     "speaker":"Rachel","blanked":"I was ___ to be headed for Aruba on my ___.",
     "answers":["supposed","honeymoon"],"target_words":["be supposed to","honeymoon"]}
  ],
  "minimal_pairs": [
    {"id":1,"word_a":"ship","ipa_a":"/ʃɪp/","word_b":"sheep","ipa_b":"/ʃiːp/",
     "in_episode":"b","line":"Like a sheep, you know?","hint":"长元音 /iː/（sheep）比短元音 /ɪ/（ship）更长更紧"}
  ],
  "connected_speech": [
    {"id":1,"line":"I'm gonna go get it.","gloss":"我去拿。",
     "breakdown":[
       {"text":"I'm","note":"正常"},
       {"text":"gonna","note":"going to 的弱读+连读 /ˈɡənə/"},
       {"text":"go get","note":"go 尾元音与 get 首辅音连读 /ɡoʊɡɛt/"},
       {"text":"it","note":"正常"}]}
  ]
}
```
