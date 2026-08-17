## Description:

Convert any text, including PDF excerpts, lecture notes, articles, and textbook chapters, into spaced-repetition flashcards with Anki-importable CSV, Q&A, and cloze-deletion modes using regex-based extraction and sentence analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

Students, educators, and agents assisting study workflows use this skill to turn source notes or reading material into reviewable flashcards for Anki or downstream curation. It supports Q&A, cloze, and auto modes for extracting definitions, facts, lists, cause/effect statements, and comparisons.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private or sensitive study notes may be processed into files at a user-selected output path.

Mitigation: Choose input and output paths deliberately, keep generated decks in an appropriate local location, and avoid sharing outputs that contain private notes.

Risk: The output path can overwrite an existing file when the user supplies -o.

Mitigation: Use a new output filename or confirm that replacing the existing file is intended before running the script.

Risk: Regex-based extraction can produce incomplete, low-quality, or misleading flashcards when source text is noisy or complex.

Mitigation: Review generated cards before import or study, use max-card and sentence-length filters for large inputs, and test-import a small sample into Anki first.

## Reference(s):

- [Source repository](https://github.com/voronindenis5/flashcard-forge)
- [ClawHub release page](https://clawhub.ai/voronindenis5/skills/flashcard-forge)
- [Extraction Patterns](references/extraction-patterns.md)
- [Anki Import Guide](references/anki-import.md)
- [Study Strategies for Flashcard-Based Learning](references/study-strategies.md)
- [Anki Manual](https://docs.ankiweb.net/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; generated flashcard files are CSV or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled Python utility reads a user-selected UTF-8 text file and writes to stdout or to a user-selected output path.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata; artifact SKILL.md frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
