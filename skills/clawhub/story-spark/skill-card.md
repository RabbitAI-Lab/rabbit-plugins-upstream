## Description:

Generate creative writing prompts from your own life by scanning personal photo metadata, journal entries, and notes for emotionally resonant moments, then transforming them into fiction seeds across multiple genres.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External writers, creative writing students, teachers, journalers, and photographers use this skill to turn personal photos, journals, and notes into specific fiction prompts when they need story ideas or want to fictionalize real experiences.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated prompts may surface private photo GPS data, filenames, timestamps, or quoted journal text.

Mitigation: Use a small dedicated input folder, strip EXIF GPS data first when location privacy matters, and review console output or JSON exports before sharing.

## Reference(s):

- [Story Spark source repository](https://github.com/voronindenis5/story-spark)
- [Story Spark ClawHub listing](https://clawhub.ai/voronindenis5/skills/story-spark)
- [Creative Process](references/creative-process.md)
- [Genre Transformations](references/genre-transformations.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Console text with optional JSON export and Markdown or plain-text prompt content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompts include a source moment, genre, premise, character, conflict, and twist; CLI options control count, genre, source folders, and optional JSON output.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
