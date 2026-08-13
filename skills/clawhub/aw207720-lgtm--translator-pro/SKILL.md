---
name: "translator-pro"
description: "Professional translation between Mandarin, English, and Spanish with cultural context, tone matching, and domain-specific formatting (business, legal, casual)."
---

# Translator Pro

High-quality translation engine for Mandarin↔English↔Spanish. Handles
documents, snippets, UI strings, and correspondence with cultural nuance.

## Capabilities

- Translate full documents or short text between any pair of: Mandarin (zh-CN), English (en), Spanish (es)
- Preserve formatting (Markdown, HTML, plain text, structured JSON)
- Adapt tone for context: business formal, legal, casual/conversational
- Provide cultural context notes explaining nuance, register, and potential pitfalls
- Glossary override support for domain-specific terminology

## Workflow

1. Detect or confirm source language. If ambiguous, detect via script:
   - CJK characters → Mandarin (zh-CN)
   - Latin script with Spanish markers (ñ, ¿, áéíóú) → Spanish (es)
   - Otherwise default to English (en)
2. Confirm target language and context mode:
   - `business` — formal register, precise terminology, conservative phrasing
   - `legal` — exact legal equivalents, Latin terms preserved where standard, jurisdiction-aware
   - `casual` — natural conversational tone, idiomatic expressions, slang adaptation
3. Load domain glossary if provided (see `references/glossary-format.md`).
4. Translate preserving structure:
   - Markdown headers, lists, code blocks, links intact
   - HTML tags preserved (translate text content only)
   - JSON: translate string values, preserve keys
   - Line breaks and paragraph boundaries preserved
5. Generate cultural context notes for:
   - Idioms/colloquialisms that lack direct equivalents
   - Register/formality shifts between source and target
   - Potentially sensitive or culturally loaded terms
   - Date/number/currency format differences
6. Return structured result:
   - `translation` — the translated text
   - `source_language` — detected/confirmed source
   - `target_language` — requested target
   - `context_mode` — business | legal | casual
   - `cultural_notes` — array of note objects with `type`, `source_phrase`, `explanation`
   - `glossary_terms` — any matched glossary overrides applied
   - `warnings` — ambiguity or confidence flags

## Translation Guidelines by Language Pair

### Mandarin ↔ English
- See `references/mandarin-english-notes.md` for detailed rules
- Key points: measure words, honorifics, business titles, chengyu idioms, formal vs informal 你/您
- Legal: translate 章程 as "Articles of Association", 合同 as "Contract", 协议 as "Agreement"
- Avoid literal translation of four-character idioms; provide meaning + note

### Spanish ↔ English
- See `references/spanish-english-notes.md` for detailed rules
- Key points: usted/tú register, regional variants (Castilian vs Latin American), subjunctive nuance
- Legal: translate poder as "Power of Attorney", contrato as "Contract", escritura as "deed"
- Handle false friends (e.g., actualmente = currently, not actually)

### Mandarin ↔ Spanish
- Route through English as pivot when direct confidence is low
- Flag pivot-translated content with reduced confidence
- Note any terms that lose nuance through pivot

## Quality Checks

- Back-translation spot check for critical/legal documents
- Terminology consistency across a single document
- Flag untranslated segments (code, URLs, proper nouns left in original)
- Verify number/date/currency localization

## Usage Examples

### Translate a business email
```
Input: "Dear Mr. Zhang, I hope this email finds you well. Regarding the Q3 contract..."
Target: Mandarin, business mode
Output: "张先生您好，希望您一切顺利。关于第三季度的合同..."
```

### Translate legal clause with notes
```
Input: "The Parties agree to indemnify and hold harmless..."
Target: Mandarin, legal mode
Output: "双方同意赔偿并使对方免受损害..."
Notes: "indemnify and hold harmless" is a standard legal doublet; translated as a single concept per Chinese legal convention.
```

### Casual conversation
```
Input: "¡Qué chévere! Nos vemos mañana."
Target: English, casual mode
Output: "How cool! See you tomorrow."
Notes: "chévere" is Latin American casual for "cool/great" — regional usage, primarily Andean/Caribbean Spanish.
```
