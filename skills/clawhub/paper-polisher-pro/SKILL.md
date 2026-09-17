# paper-polisher-pro — All-in-One Academic Paper Polishing Tool

> 🎯 **AI Detection · De-AI Rewriting · Paraphrase · Terminology Check · Quality Report**
> Bilingual (CN/EN) · Runs 100% Locally · Zero Data Upload · Zero Setup

## ✨ Why paper-polisher-pro?

| Feature | Description |
|---------|-------------|
| 🕵️ **14 AI Model Fingerprinting** | Detects DeepSeek V4, GLM-5, Qwen3.5, Kimi K2, ChatGPT, Claude, Gemini, MiniMax, Step, and more |
| 📊 **Quantitative Scoring** | 0-100 AI risk score — not vague guesses, actual numbers |
| 🛡️ **Terminology Protection** | 2,255 authoritative medical/academic terms auto-protected during paraphrasing |
| 🔒 **100% Local Privacy** | Your paper never leaves your machine. No upload. No accounts. |
| 🧪 **6-Layer Detection Engine** | Pattern matching + TTR + sentence length variance + info density + sentence-start patterns + paragraph features |
| 🌐 **Bilingual** | Full support for Chinese AND English academic papers, auto language detection |

**The only academic tool with Chinese LLM fingerprinting** — detects not just ChatGPT, but DeepSeek, GLM, Qwen, Kimi, MiniMax, Step, and other major Chinese models.

## Trigger Words

"polish paper", "deai", "reduce ai detection", "paraphrase", "check ai writing", "paper polish", "rewrite paper", "humanize paper", "AI paper detector", "academic writing assistant", "plagiarism reducer", "AI writing checker", "remove AI traces", "humanize AI text", "thesis polishing", "dissertation polish", "Turnitin helper", "AI content detector", "essay polisher", "research paper rewrite", "paper proofread", "grammar check academic", "journal submission polish", "SCI paper editing", "manuscript polishing", "detect AI writing", "AI writing score"

## 🚀 Quick Start

### Detect AI Traces in 30 Seconds

```bash
python3 {{SKILL_DIR}}/scripts/ai_detector.py your_paper.txt --lang auto
```

Sample output:
```
📄 your_paper.txt
AI Risk Score: 68.5 / 100 🔴 HIGH
Paragraphs analyzed: 12
Top patterns: "it is worth noting" (×3), "plays a crucial role" (×2)
Suggestion: Rewrite paragraphs 2, 5, 8
```

### Check Terminology Standardization

```bash
python3 {{SKILL_DIR}}/scripts/term_check.py your_paper.txt
```

### Generate Comprehensive Quality Report

```bash
python3 {{SKILL_DIR}}/scripts/quality_report.py your_paper.txt --format json
```

---

## 📋 Full Workflow (5 Steps)

### Step 1: AI Detection

```bash
python3 {{SKILL_DIR}}/scripts/ai_detector.py <input_file> --lang auto --format json --output <report.json>
```

Presents to user:
- **AI Risk Score** (0–100, higher = more AI-like)
- **Risk Level** (🟢 Low / 🟡 Medium / 🔴 High)
- **High-risk paragraph locations**
- **Top 10 matched AI patterns**

### Step 2: De-AI Rewriting

Triggered for paragraphs with AI score ≥ 35.

**For Chinese papers:**
- ❌ Delete filler: "值得注意的是", "综上所述", "具有重要的理论意义"
- ❌ Delete vague praise: "提供了新的视角" — replace with specifics or remove
- ❌ Break symmetry: "不仅…而且…" → natural progression or contrast
- ❌ Ban buzz verbs: "深入探讨" → "compared differences between X and Y"
- ✅ Use data: "取得了显著进展" → "3-year remission rate: 42% → 78%"
- ✅ Vary sentence length: long (20–40 chars) ↔ short (5–15 chars)
- ✅ Content-based transitions, not "此外", "与此同时" stacking
- ✅ Preserve all terms, data, citations exactly

**For English papers:**
- ❌ Ban: plays a crucial role, has gained significant attention, sheds light on, paves the way, a growing body of evidence, it is worth noting, delve into, myriad, plethora, multifaceted, of paramount importance
- ❌ Ban perfect parallelism: "Not only A but also B; moreover C; furthermore D"
- ✅ Use active voice: "We found" not "It was found that"
- ✅ Mix sentence length: 5–10 word sentences alongside 20–30 word ones

**Rewriting Prompt:**
```
Please rewrite the following academic paragraph to remove AI writing traces.

Rules:
1. Delete all AI filler phrases and vague evaluations
2. Replace fuzzy claims with specific data/facts or delete
3. Break symmetrical sentence structures; restore natural length variation
4. Use content-based transitions, not filler words
5. Preserve all technical terms, data, citations exactly as-is
6. Maintain original meaning and academic logic

Original paragraph:
{paragraph}

Output only the rewritten paragraph without explanation.
```

### Step 3: Smart Paraphrasing

**5-layer paraphrasing strategy:**
1. **Synonym replacement** — from `synonyms_general.json`, skip protected terms
2. **Voice transformation** — active ↔ passive, split long sentences, merge short ones
3. **Word order shift** — reorder info points (don't break logic)
4. **Abstraction ↔ expansion** — high-similarity → summarize / sparse → elaborate
5. **Perspective shift** — describe the same content from a different angle

⚠️ **Terminology protection**: 2,255 authoritative terms automatically skipped during paraphrasing.

### Step 4: Terminology Standardization

```bash
python3 {{SKILL_DIR}}/scripts/term_check.py <input_file>
```

Checks against a database of 2,255 authoritative terms (National Terms Commission + MeSH2026 + Drug Terminology), flags non-standard usage, and suggests corrections.

### Step 5: Quality Report

Re-run AI detection after rewriting and show before/after comparison:
- Pre-rewrite AI score → Post-rewrite AI score
- Per-paragraph improvement breakdown
- Terminology standardization rate
- Readability metrics

---

## 🎯 Supported AI Models

### Chinese LLMs (Exclusive)
| Model | Score | Risk |
|-------|-------|------|
| DeepSeek V4 | 84.3 | 🔴 High |
| GLM-5-Turbo | 98.6 | 🔴 High |
| GLM-5.1 | 74.9 | 🔴 High |
| Kimi K2 | 66.3 | 🔴 High |
| Step 3.5 Flash | 79.3 | 🔴 High |
| Qwen3.5-Plus | 39.5–58.6 | 🟡–🔴 |
| MiniMax M2.5 | 39.9 | 🟡 Medium |

### International Models
ChatGPT (77.3 🔴) · Claude (70+ 🔴) · Gemini (65+ 🔴)

### Human Text (Zero False Positives)
Clinical Records 24.8 🟢 · Academic Papers 31.6 🟢

---

## 📐 Discipline Adaptation

- **Medicine/Biology**: Preserves clinical terms, drug names, dosages, stats. Prioritizes connector and evaluative phrase replacement
- **Engineering/CS**: Protects algorithm names, formulas, performance metrics. Focuses on naturalizing methodology descriptions
- **Humanities/Social Sciences**: Allows more opinionated phrasing, avoids AI-style summarization
- **Business/Economics**: Preserves data and model names, replaces generic industry commentary

## ⚠️ Usage Constraints

1. **Never alter data**: Numbers, statistics, citation markers preserved exactly
2. **Terminology protection**: 2,255 professional terms auto-skipped during paraphrasing
3. **Semantic fidelity**: Before/after meanings are equivalent — no info added or removed
4. **Paragraph-by-paragraph**: Long papers processed incrementally to maintain logical flow
5. **User approval**: All changes presented for user confirmation before adoption

---

## 📦 File Structure

```
paper-polisher/
├── SKILL.md                    ← This file
├── scripts/
│   ├── ai_detector.py          ← AI detection engine (v3.3b, 6 layers, 300+ rules)
│   ├── term_check.py           ← Terminology standardization (2,255 terms)
│   ├── ngram_similarity.py     ← N-gram repetition analysis
│   └── quality_report.py       ← Comprehensive quality report
├── references/
│   ├── ai_patterns_zh.json     ← Chinese AI pattern library (300+ rules)
│   ├── ai_patterns_en.json     ← English AI pattern library (100+ rules)
│   └── synonyms_general.json   ← General synonym dictionary (291 groups)
├── data/
│   └── terminology.json        ← Standard terminology database (2,255 terms)
└── templates/                  ← Prompt templates
```

## Version

- **v1.0.0** — Initial release: AI detection (14 models) + De-AI rewriting + Paraphrasing + Terminology check + Quality report
- **v1.0.1** — English SKILL.md for ClawHub, streamlined descriptions, SEO keyword optimization
