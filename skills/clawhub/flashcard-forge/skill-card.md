## Description:

Convert study text such as PDF excerpts, lecture notes, articles, and textbook chapters into spaced-repetition flashcards, including Anki-importable CSV with Q&A and cloze-deletion modes using regex-based extraction and sentence analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

Students, educators, and developers use this skill to turn raw study material into flashcards for active recall and spaced-repetition review. It is useful for generating Q&A cards, cloze cards, and Anki-ready CSV or JSON outputs from local text files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local study notes may contain sensitive private content that becomes part of generated flashcard output.

Mitigation: Use non-sensitive inputs or confirm that private notes are acceptable to transform before generating CSV or JSON files.

Risk: User-selected output paths can overwrite or place generated flashcard files where not intended.

Mitigation: Choose explicit output paths and check for existing files before writing output.

Risk: Regex-based extraction can produce inaccurate or low-quality cards from garbled OCR, noisy markup, or very large source texts.

Mitigation: Clean input text first, cap large runs with max-card settings, and review generated cards before importing them into a study deck.

## Reference(s):

- [Server-resolved source repository](https://github.com/voronindenis5/flashcard-forge)
- [Extraction Patterns](references/extraction-patterns.md)
- [Anki Import Guide](references/anki-import.md)
- [Study Strategies for Flashcard-Based Learning](references/study-strategies.md)
- [Anki](https://apps.ankiweb.net/)
- [Anki Manual](https://docs.ankiweb.net/)

## Skill Output:

**Output Type(s):** [Files, Text, Shell commands, Guidance]

**Output Format:** [Markdown guidance with command examples plus Anki-importable CSV or JSON flashcard files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CSV output uses semicolon-separated quoted fields; JSON output is an array of flashcard objects with front, back, type, and source fields.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
