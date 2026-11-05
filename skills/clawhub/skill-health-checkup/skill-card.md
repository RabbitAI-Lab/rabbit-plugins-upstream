## Description:

Use when two skills fire for the same request, or a skill never fires at all — scans every installed skill, maps trigger overlaps and blind spots, delivers one health report with fixes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thomaszhou22](https://clawhub.ai/user/thomaszhou22)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to assess an installed skills collection for trigger overlaps, uncovered tasks, weak descriptions, duplicates, and skills that may be unnecessary. It produces a health report with concrete description-fix suggestions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Suggested description edits could change when installed skills activate or introduce misleading guidance.

Mitigation: Confirm the intended skills directory, review proposed description diffs, and scan the edited skills before applying them.

## Reference(s):

- [Health report template](references/report-template.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown health report with tables and proposed description edits]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.1 (source: SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
