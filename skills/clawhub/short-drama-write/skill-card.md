## Description:

Writes and revises shootable Chinese short-drama and motion-comic episode screenplays in Markdown, including faithful formatting of existing drafts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

Writers and production teams use this skill to turn episode plans or drafts into performable Chinese screenplays, refine scenes and dialogue, and prepare existing scripts for downstream production without rewriting unrelated material.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional timing and validation helpers read local screenplay files and can create derived index data.

Mitigation: Point helpers only at the intended project and keep generated indexes in a temporary directory.

Risk: Timing estimates are approximate and may not capture actual spoken or performed duration.

Mitigation: Check target duration through a real read-through and action pass before production.

## Reference(s):

- [Chinese screenplay format](references/screenplay-format.md)
- [Script craft](references/script-craft.md)
- [Dialogue craft](references/dialogue-craft.md)
- [Production screenplay format](references/production-format-dialect.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Chinese Markdown screenplay with scene headings, dialogue, action, and production tags]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional local timing estimates and screenplay checks; no media generation.]

## Skill Version(s):

1.0.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
