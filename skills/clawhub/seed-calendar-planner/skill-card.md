## Description:

Builds a personalized vegetable seed-starting and planting calendar from last and first frost dates, including crop windows, tray sizing, row-footage estimates, succession schedules, and optional moon-phase annotations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External gardeners and agents assisting gardeners use this skill to turn local frost dates, crop selections, and household size into dated sowing, transplanting, harvest, seed-tray, and row-footage guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill expects an agent or user to run a local Python helper.

Mitigation: Review proposed shell commands before execution and run the script in an appropriate local workspace.

Risk: Zone-based frost estimates can be inaccurate for local conditions.

Mitigation: Verify frost dates against local extension or NOAA data before relying on generated planting dates.

Risk: Moon-phase annotations are folklore and could be mistaken for agronomic recommendations.

Mitigation: Treat moon-phase output as optional annotation only; do not use it to override frost-date and crop-window guidance.

## Reference(s):

- [Seed Crop Library](references/seed-crop-library.md)
- [Server-resolved source repository](https://github.com/voronindenis5/seed-calendar-planner)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell command examples and optional JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The local Python helper can emit human-readable tables or machine-readable JSON for plan and garden commands.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata; SKILL.md frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
