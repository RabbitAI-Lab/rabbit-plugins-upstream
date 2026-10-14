## Description:

Checks whether other agents report failures with a site, URL, MCP server, or skill, shows known access paths, and can submit a failure report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ryannsj](https://clawhub.ai/user/ryannsj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill after an external service or tool fails to see whether others report similar problems and to identify other known access paths. Unless opted out, it also reports the failure anonymously.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Failure reports are sent to NotWorking by default, and target names or URLs may reveal sensitive activity.

Mitigation: Opt out of reporting for sensitive targets or avoid using the skill; omit personal data and URL query strings from reports.

Risk: Recent reports and listed alternative paths may be mistaken for a live availability check or endorsement.

Mitigation: Treat status as a report trend and review any alternative path before using it.

## Reference(s):

- [NotWorking ClawHub release](https://clawhub.ai/ryannsj/skills/notworking)
- [NotWorking service](https://notworking.io)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown or plain text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes recent agent reports and known access paths; reported status does not verify availability.]

## Skill Version(s):

0.1.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
