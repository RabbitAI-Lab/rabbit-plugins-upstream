## Description:

Guides employees through read-only Workday HR data retrieval using an already signed-in browser session and the fpx CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized employees and developers can retrieve their accessible Workday app menu, worker profiles, org chart, pay, benefits, and other HR data without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HR, pay, benefits, and org-chart results may expose sensitive employee information.

Mitigation: Use only with authorized corporate access; avoid raw dumps, logs, screenshots, and shared terminal output, and redact personal and compensation details before sharing.

Risk: A persistent browser pairing and raw response fields may expose sensitive session information.

Mitigation: Project only needed data fields, never print raw response envelopes, and remove or re-pair access when a machine is shared or no longer trusted.

## Reference(s):

- [Workday FPX ClawHub release](https://clawhub.ai/chrischall/skills/workday-fpx)
- [Workday endpoint recipes](references/endpoints.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON]

**Output Format:** [Markdown with shell commands and projected JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only guidance; output should select only needed fields rather than expose raw response envelopes.]

## Skill Version(s):

1.1.10 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
