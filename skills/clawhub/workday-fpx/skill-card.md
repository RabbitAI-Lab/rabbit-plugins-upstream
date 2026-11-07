## Description:

Read Workday HR data (org chart, worker profiles, tasks, pay, benefits, compensation, your app menu) from a shell with the fpx CLI (@fetchproxy/cli) instead of running the workday-mcp server — fetch any *.htmld data endpoint through your own signed-in *.myworkday.com tab (SSO/Ping/Okta/Entra already cleared). Use when you want Workday data without the MCP, in a script, or on a machine where the MCP isn't installed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Workday employees and developers can use the skill to read HR information from a shell through their own signed-in Workday browser session, without running the Workday MCP server. Its examples cover organization charts, worker profiles, tasks, pay, benefits, compensation, and app menus.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI and browser extension can use a signed-in Workday session to access sensitive HR information, including information about other employees.

Mitigation: Install them only if trusted, verify the extension checksum, limit requests to the intended tenant, people, and fields, and revoke pairing when finished.

Risk: Dumping a raw Workday response can expose session tokens and other envelope data.

Mitigation: Use the documented field-selecting jq projections and never print the raw response envelope.

## Reference(s):

- [Workday *.htmld Endpoints for fpx](artifact/references/endpoints.md)
- [ContextMint Bridge Releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ContextMint Bridge Source](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.4.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
