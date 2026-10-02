## Description:

Connects Tang and Song poetry to everyday moments through daily poem cards, plain-language readings, recitation practice, and reading summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-language readers use the skill to find poetry suited to a real moment, understand Tang and Song poems in everyday language, practice recall, and review or export their learning history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Preference and study-progress files can remain on the user's device.

Mitigation: Explain the files and obtain consent before first write; offer a no-persistence mode and allow inspection or deletion.

Risk: Optional online lookups disclose poem terms or a city name to external services.

Mitigation: Limit lookups to poem title, author, verse, or city; never send personal descriptions or study records, and honor online: false or a request not to use the network.

Risk: Saving notes to a chosen destination or generating an image may invoke other tools or create additional files.

Mitigation: Perform these actions only when the user explicitly requests them.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/bonniegeng-max/skills/poetry-resonance)
- [Poem library](artifact/references/poems.md)
- [Theme index](artifact/references/themes.md)
- [Poet profiles](artifact/references/poets_profile.md)
- [Weather mapping](artifact/references/weather_map.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Chinese text and Markdown; optional Markdown and Anki-compatible CSV exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-only; optional user-requested illustrations and local study exports.]

## Skill Version(s):

1.5.2 (source: frontmatter, CHANGELOG, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
