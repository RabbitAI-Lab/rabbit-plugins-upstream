## Description:

Turn movies and TV shows into language-learning material by analyzing subtitle files to extract vocabulary, build frequency decks, and create contextual flashcards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

Language learners, teachers, and self-directed learners use this skill to turn subtitle files from TV shows and movies into vocabulary analysis, frequency-ranked study decks, and contextual flashcards for media-based language practice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Season-level deck building can process supported subtitle and text files in the selected directory, including files the user did not intend to include.

Mitigation: Use a scoped subtitle directory and an explicit output path, and avoid pointing the tool at sensitive or broad personal directories.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/language-immersion-tv)
- [Server-resolved GitHub source](https://github.com/voronindenis5/language-immersion-tv)
- [Learning Methodology - Comprehensible Input Through Media](references/methodology.md)
- [CEFR Levels and Media Recommendations](references/cefr-levels.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and file-format details; generated decks may be JSON, CSV, or Anki TSV.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Works with local .srt, .vtt, and .txt subtitle inputs; built-in stopword lists cover English, Spanish, French, German, Italian, and Portuguese.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
