## Description:

Meeting Load Balancer helps agents audit exported ICS calendars, measure meeting load and focus-time fragmentation, rank recurring meeting costs, and propose simulated meeting changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

Knowledge workers, managers, team leads, consultants, and facilitators use this skill to turn local calendar exports into a meeting-load audit with stats, focus analysis, series ranking, prescriptions, and before/after simulations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Malformed recurrence data in ICS files can cause the local parser to hang.

Mitigation: Use trusted calendar exports where possible and avoid malformed or untrusted ICS files until recurrence interval validation is fixed.

Risk: Calendar exports can contain sensitive meeting titles, names, and email addresses.

Mitigation: Process exports locally, collect team calendars only with consent, share aggregate findings when possible, and delete or access-control ICS files after analysis.

## Reference(s):

- [ICS Export How-To + Meeting Audit Methodology](references/ics-export.md)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/meeting-load-balancer)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [Markdown guidance with shell commands and plain-text command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally against user-provided ICS calendar files; no upload behavior is described.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
