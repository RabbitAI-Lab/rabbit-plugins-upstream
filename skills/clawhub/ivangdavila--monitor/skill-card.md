## Description:

Create monitors for anything. User defines what to check, skill handles scheduling and alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:


## Use Case:

Developers and operators use this skill to define recurring checks for endpoints, certificates, processes, disks, ports, or user-provided commands, then receive status-change alerts and monitor summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recurring user-defined command checks can execute unsafe or overly broad commands when monitor definitions are not trusted.

Mitigation: Use this skill only with trusted monitor definitions, require explicit approval for custom command checks, and keep command scope narrow.

Risk: Alert payloads and webhook destinations can expose service names, outages, timestamps, and failure details to third-party services.

Mitigation: Validate alert URLs and webhook destinations before use, and avoid sending sensitive operational details unless the recipient is approved.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ivangdavila/skills/monitor)
- [Monitor Templates](artifact/templates.md)
- [Alert Configuration](artifact/alerts.md)
- [Monitor Analysis Patterns](artifact/insights.md)
- [Pushover Messages API](https://api.pushover.net/1/messages.json)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON configuration examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates monitor definitions, alert configuration, log summaries, and recurring check instructions based on user-provided targets.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
