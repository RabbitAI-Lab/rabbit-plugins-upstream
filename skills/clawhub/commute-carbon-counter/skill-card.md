## Description:

Commute Carbon Counter helps an agent log commute trips, compare transport modes, calculate CO2 by trip and period, and report trends against a personal emissions budget.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users, sustainability teams, and developers can use this skill to compare commuting choices, track personal or group mobility emissions, and export commute records for lightweight reporting. It is suitable for planning-grade comparisons, not certified carbon accounting or offset purchases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trip dates, transport modes, distances, passenger counts, and notes are stored in a local JSON file and may reveal commute habits.

Mitigation: Use the file override option to choose an appropriate storage location, protect exported files, and avoid entering sensitive notes.

Risk: Emission factors are planning-grade averages and are not appropriate for certified carbon accounting, regulatory reporting, or offset purchases.

Mitigation: Use measured or certified data for formal reporting and review the included emission-factor reference before relying on comparisons.

## Reference(s):

- [Emission Factors - Sources, Ranges, and Honesty](references/emission-factors.md)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/commute-carbon-counter)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with CLI commands, text reports, local JSON logs, and optional CSV exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Trip data is stored locally in a JSON file by default and can be exported to CSV.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
