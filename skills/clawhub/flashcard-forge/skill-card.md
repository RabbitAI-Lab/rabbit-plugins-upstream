## Description:

Convert any text, including PDF excerpts, lecture notes, articles, and textbook chapters, into spaced-repetition flashcards with Anki-importable CSV, Q&A, and cloze-deletion modes using regex-based extraction and sentence analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External learners, educators, and developers use this skill to convert study material into active-recall flashcards for Anki. It is suited for extracting definitions, key facts, Q&A pairs, and cloze-deletion cards from reasonably clean text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The script reads study files supplied by the user and generated decks can contain source text from private notes.

Mitigation: Review input and output locations before running, and treat generated CSV or JSON decks as sensitive when the source material is private.

Risk: Automatically extracted cards may be low quality, over-generated, duplicated across runs, or affected by poor OCR and messy input formatting.

Mitigation: Use caps and filters such as max cards and minimum sentence length, pre-clean noisy text, and review a sample of generated cards before importing or studying.

Risk: Anki import can fail or create unusable cards if the output mode, delimiter, encoding, or note type is mismatched.

Mitigation: Import Q&A output as Basic cards and cloze output as Cloze cards, confirm semicolon-separated UTF-8 CSV formatting, and test import a small batch first.

## Reference(s):

- [Source repository](https://github.com/voronindenis5/flashcard-forge)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/flashcard-forge)
- [Extraction Patterns](references/extraction-patterns.md)
- [Anki Import Guide](references/anki-import.md)
- [Study Strategies for Flashcard-Based Learning](references/study-strategies.md)
- [Anki](https://apps.ankiweb.net/)
- [Anki Manual](https://docs.ankiweb.net/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell commands; generated flashcard files are CSV or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated CSV uses semicolon-separated quoted fields for Anki Basic or Cloze note types; JSON output is an array of flashcard objects.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
