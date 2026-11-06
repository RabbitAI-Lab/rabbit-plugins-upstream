## Description:

Read Workday HR data (org chart, worker profiles, tasks, pay, benefits, compensation, your app menu) from a shell with the fpx CLI (@fetchproxy/cli) instead of running the workday-mcp server — fetch any *.htmld data endpoint through your own signed-in *.myworkday.com tab (SSO/Ping/Okta/Entra already cleared). Use when you want Workday data without the MCP, in a script, or on a machine where the MCP isn't installed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Workday employees and developers use this skill to retrieve authorized HR data through their existing signed-in Workday browser session, including when they want shell-based access without running the Workday MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workday responses may contain employee information and session-related fields.

Mitigation: Use only with authorization to access the relevant Workday information, project only needed fields, and keep session tokens and sensitive HR output out of shared logs.

Risk: Browser pairing persists and the external CLI and extension binaries were not audited in this review.

Mitigation: Review requested domains and capabilities, verify the extension release checksum, and revoke pairing when it is no longer needed.

## Reference(s):

- [Workday endpoint examples](artifact/references/endpoints.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ContextMint Bridge source repository](https://github.com/nullnet-app/contextmint-bridge)
- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/workday-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and jq filters; retrieved Workday data is JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only endpoint requests; examples project selected fields from responses.]

## Skill Version(s):

1.3.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
