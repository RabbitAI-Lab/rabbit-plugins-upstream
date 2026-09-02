---
name: text-summarizer
description: Summarize long text or documents into concise structured summaries. Use when the user provides a long article, report, transcript, or multi-page text and wants the key points, action items, or a brief overview without reading the full content.
metadata: { "openclaw": { "emoji": "📝" } }
---

# Text Summarizer

Produce structured, concise summaries from long text inputs.

## When to use

- User provides a long document and asks for a summary
- User wants action items extracted from a meeting transcript
- User needs a brief overview of a report or article
- User asks "give me the key points" or "TL;DR" on lengthy content

## Input

- A single block of text (article, report, transcript, etc.)
- Optional: desired summary style (brief, detailed, bullet points, action items only)

## Steps

1. **Read the full text** carefully before summarizing.
2. **Identify the core message** — what is the main point or argument?
3. **Extract key facts** — dates, names, numbers, decisions.
4. **Structure the output**:
   - **One-line TL;DR** if the user wants brevity.
   - **Key points** (3-7 bullets) for a structured summary.
   - **Action items** if the text is a meeting or task-oriented transcript.
   - **Open questions** if anything is unresolved.
5. **Match the user's requested style** — default to concise bullets unless asked for prose.

## Output format

```
**TL;DR:** <one sentence>

**Key Points:**
- <point 1>
- <point 2>
- ...

**Action Items:** (if applicable)
- [ ] <action> — owner/deadline if available

**Open Questions:** (if applicable)
- <question>
```

## Guidelines

- Do not fabricate facts not present in the source text.
- Preserve specific numbers, names, and dates verbatim.
- When summarizing transcripts, attribute statements to speakers when possible.
- If the text is short enough (<200 words), state that and give a light edit instead of a full summary.
