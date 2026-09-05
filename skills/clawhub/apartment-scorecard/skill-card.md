## Description:

Compares apartment and rental-home listings by applying hard constraints, scoring surviving listings on weighted criteria, computing true all-in monthly cost, checking affordability, comparing finalists, and drafting negotiation guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and agents use this skill to screen, rank, budget, compare, and negotiate apartment or rental-home options using structured listing data, user-defined constraints, and weighted tour criteria.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Apartment preferences and listing files may contain sensitive housing, budget, commute, pet, and move-date details.

Mitigation: Keep JSON/CSV listing and weights files local, apply appropriate file permissions, and avoid committing or sharing them unless intentionally redacted.

Risk: The skill may create or use a default home-directory weights file at ~/.apartment-scorecard.json.

Mitigation: Review the default weights-file behavior before use, or pass an explicit weights path when you do not want preferences stored in the default location.

## Reference(s):

- [Listing Format & Tour Protocol](references/listing-format.md)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/apartment-scorecard)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or terminal text with shell commands and JSON/CSV configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local analysis from user-provided listing and weights files; no network calls are described by the release evidence.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
