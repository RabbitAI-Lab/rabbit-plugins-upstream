## Description:

Turn movies and TV shows into language-learning material by analyzing subtitle files to extract vocabulary, build frequency decks, and create contextual flashcards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External language learners, teachers, and self-directed media learners use this skill to analyze subtitle files, identify useful vocabulary and phrases, and build study decks before watching TV shows or movies in a target language.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads subtitle files and writes deck outputs at paths selected by the user.

Mitigation: Run it only on intended subtitle files and choose output paths that do not expose private media-library information.

Risk: Subtitle files may be copyrighted, unauthorized, or unsuitable for reuse in study decks.

Mitigation: Use authorized subtitle files and review generated decks before sharing or importing them.

## Reference(s):

- [Server-resolved GitHub source](https://github.com/voronindenis5/language-immersion-tv)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/language-immersion-tv)
- [Learning Methodology](references/methodology.md)
- [CEFR Levels and Media Recommendations](references/cefr-levels.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Analysis, Files]

**Output Format:** [Markdown guidance with inline shell commands; generated study-deck files may be JSON, CSV, or Anki-compatible TSV.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces frequency-ranked vocabulary, phrase summaries, CEFR estimates, context sentences, and deck outputs from user-selected subtitle files.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
