# Extraction Patterns

This document catalogs the regex patterns Flashcard Forge uses to extract
flashcard-worthy content from text. Each pattern targets a specific sentence
structure common in educational material.

## Definition Patterns

These extract "term → definition" pairs, producing cards with the term as the
front and the definition as the back.

### "X is Y"

```regex
\b([A-Z][a-z]+(?:\s+\w+){0,4})\s+is\s+(?:a|an|the)\s+(.+?)[.]
```

Matches:
- "Photosynthesis is a process by which plants make food."
- "Mitosis is a type of cell division."

### "X is defined as Y"

```regex
\b(.+?)\s+is\s+defined\s+as\s+(.+?)[.]
```

### "X refers to Y" / "X means Y"

```regex
\b(.+?)\s+(?:refers\s+to|means)\s+(.+?)[.]
```

### "X: Y" (colon definitions)

```regex
^([A-Z][^:]{2,40}):\s+(.+?)[.]?$
```

Matches:
- "Photosynthesis: The process by which plants convert light to energy."

## Q&A Patterns

### Explicit question markers

```regex
\b(What|Why|How|When|Where|Who|Which)\s+.+?\?\s*(.+?)[.]?
```

Matches embedded questions and their answers:
- "What is DNA? It is the genetic material in cells."

### "The question is..." / "The answer is..."

```regex
\bThe\s+(?:question|answer)\s+is\s+(.+?)[.]
```

## List Patterns

### "There are N types of X: A, B, C"

```regex
\bThere\s+are\s+(\w+)\s+(types|kinds|categories|forms)\s+of\s+(.+?):\s*(.+?)[.]
```

Produces one card per list item with the category as context.

### Numbered/enumerated items

```regex
^(?:\d+[.)]\s+|[-*]\s+)(.+)$
```

## Cause/Effect Patterns

```regex
\b(.+?)\s+(?:causes|leads\s+to|results\s+in|produces|triggers)\s+(.+?)[.]
```

Matches:
- "Smoking causes lung cancer."
- "Insulin deficiency results in diabetes."

## Comparison Patterns

```regex
\b(?:Unlike|Whereas|While|In\s+contrast\s+to)\s+(.+?),\s+(.+?)\s+(.+?)[.]
```

Matches:
- "Unlike prokaryotes, eukaryotes have a nucleus."

## Cloze Targets

For cloze mode, the following are high-priority candidates for masking:

| Category         | Pattern                                    |
| ---------------- | ------------------------------------------ |
| Proper nouns     | `\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b`       |
| Numbers/Dates    | `\b\d{1,4}(?:\s?(?:BCE|CE|AD|BC))?\b`      |
| Years            | `\b(?:1[5-9]\d{2}|20\d{2})\b`             |
| Percentages      | `\b\d+(?:\.\d+)?\s?%\b`                    |
| Chemical formulas| `\b[A-Z][a-z]?\d*(?:[A-Z][a-z]?\d*)+\b`    |
| Key terms (all-caps acronyms) | `\b[A-Z]{2,}\b`              |

## Scoring Heuristics

Each extracted candidate is scored for information density:

| Signal                   | Points |
| ------------------------ | ------ |
| Contains a number        | +2     |
| Contains a definition    | +3     |
| Contains a comparison    | +2     |
| Sentence length 15-40    | +1     |
| Sentence length > 50     | -1     |
| Contains a list          | +2     |
| Contains cause/effect    | +2     |

Candidates scoring below a threshold (default: 2) are discarded.

## Tuning

All patterns are defined as constants at the top of `flashcard_forge.py`.
Adjust them to match the style of your input material:

- **Textbook style** (formal definitions): strengthen definition patterns.
- **Lecture transcript** (conversational): add patterns for "so basically" and
  "in other words."
- **Scientific paper** (dense): lower `--min-length` and increase
  `--max-cards`.
