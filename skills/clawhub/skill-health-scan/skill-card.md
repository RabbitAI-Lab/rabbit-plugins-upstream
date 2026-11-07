## Description:

Use when two skills fire for the same request, or a skill never fires at all — scans every installed skill, maps trigger overlaps and blind spots, delivers one health report with fixes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thomaszhou22](https://clawhub.ai/user/thomaszhou22)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to inspect installed skill descriptions for trigger conflicts, coverage gaps, weak triggers, duplicates, and unnecessary loading weight, then review suggested description edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Proposed description edits can change when other skills activate.

Mitigation: Choose the intended skills directory and review each proposed diff before applying it.

## Reference(s):

- [ClawHub release](https://clawhub.ai/thomaszhou22/skills/skill-health-scan)
- [Health report template](references/report-template.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown health report with comparison tables and proposed description edits]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A single report with findings and prioritized fixes]

## Skill Version(s):

1.1.0 (source: server release metadata, SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
