---
name: text-summarizer
description: Summarize long text into structured, readable summaries with configurable length and language. Use when the user provides a long document, article, or paste and asks for a summary, digest, or key-points extraction.
metadata:
  openclaw:
    emoji: "📝"
---

# Text Summarizer

Provide concise, structured summaries of long-form text.

## When to use

- User provides a long article / document / paste and asks for a summary
- User asks for key points, TL;DR, or a digest of content
- User wants output in a specific language or format

## How it works

1. Read the full text the user provides (or fetch from a URL if given).
2. Identify the main topic and supporting arguments.
3. Produce a summary with:
   - **Title** (one line)
   - **Key points** (3–5 bullet points)
   - **Brief boilerplate** (1–2 sentence conclusion)
4. If the user specifies a language (zh/en/ja/etc.), respond in that language.
5. If the user specifies a desired length (short/medium/long), adjust accordingly.

## Output defaults

- **Length**: medium (~150–250 words)
- **Language**: same as the input text
- **Format**: Markdown with clear section headers

## Example

```
summarize this article for me in Chinese
```

Response:
```
# 文章标题

- 要点一……
- 要点二……
- 要点三……

总述：……
```

## Notes

- Do not fabricate information not present in the source.
- If the text is very short (< 200 words), note that it is already concise.
- For multi-document input, summarize each separately then provide a combined overview.
