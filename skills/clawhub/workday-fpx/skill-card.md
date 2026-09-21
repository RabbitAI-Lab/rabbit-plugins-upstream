## Description:

Read Workday HR data (org chart, worker profiles, tasks, pay, benefits, compensation, your app menu) from a shell with the fpx CLI (@fetchproxy/cli) instead of running the workday-mcp server — fetch any *.htmld data endpoint through your own signed-in *.myworkday.com tab (SSO/Ping/Okta/Entra already cleared). Use when you want Workday data without the MCP, in a script, or on a machine where the MCP isn't installed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, developers, and internal automation operators use this skill to query Workday HR data from an already authenticated browser session with fpx and jq, especially when the Workday MCP server is unavailable or unnecessary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables access to sensitive Workday HR data through an authenticated browser session.

Mitigation: Install and use it only when authorized for the tenant and specific HR data involved, and keep outputs out of shared logs.

Risk: Raw Workday response envelopes can include session tokens or internal fields.

Mitigation: Use field-selecting jq projections and avoid dumping raw responses or session tokens.

Risk: Long-lived fpx and Transporter pairing can preserve access beyond the immediate task.

Mitigation: Revoke the fpx/Transporter pairing when access is no longer needed.

## Reference(s):

- [Workday fpx endpoint reference](artifact/references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/workday-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell and jq command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only Workday endpoint guidance and field-selecting jq projections; users must provide their own authorized tenant, session, and fpx profile.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
