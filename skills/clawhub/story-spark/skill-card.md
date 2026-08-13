## Description:

Generate creative writing prompts from your own life. Scans personal photos metadata, journal entries, and notes to find emotionally resonant moments, then transforms them into fiction seeds across multiple genres. Use when experiencing writer's block or wanting to fictionalize real experiences.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External writers, creative writing students, teachers, journalers, and photographers use Story Spark to turn selected photos, journal entries, and notes into fiction prompts with genre, premise, character, conflict, and twist suggestions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads user-selected photos, journals, and notes that may contain private text, timestamps, or location metadata.

Mitigation: Use small curated input folders and avoid files with highly sensitive third-party or location data.

Risk: Exported prompts or JSON may preserve private details from the selected source material.

Mitigation: Review exported JSON or prompt files before sharing, syncing, or committing them.

## Reference(s):

- [Creative Process Reference](references/creative-process.md)
- [Genre Transformations Reference](references/genre-transformations.md)
- [Source Repository](https://github.com/voronindenis5/story-spark)
- [ClawHub Skill Page](https://clawhub.ai/voronindenis5/skills/story-spark)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands; generated prompts can be printed as text or exported as JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompts include a source moment, genre lens, story seed, character suggestion, conflict hook, and twist idea.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter: 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
