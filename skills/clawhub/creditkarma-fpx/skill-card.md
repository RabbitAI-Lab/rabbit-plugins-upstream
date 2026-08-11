## Description:

Query Credit Karma transactions from a shell with the fpx CLI, capture a signed-in browser session cookie once, and use curl against Credit Karma transaction and refresh endpoints without running the creditkarma-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation-focused users use this skill to retrieve Credit Karma transaction data from a shell or script when they do not want to run the MCP server. It provides setup guidance, request bodies, pagination handling, and token refresh commands for working with a live signed-in Credit Karma session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow extracts and reuses live Credit Karma session credentials.

Mitigation: Install only if this credential access is acceptable, avoid logs and shell history, keep any saved secrets under restrictive permissions, and re-authenticate or revoke the session if credentials are exposed.

Risk: Temporary response files may contain sensitive financial transaction data.

Mitigation: Avoid storing response files unless necessary, protect files with restrictive permissions, and delete temporary files after use.

## Reference(s):

- [Credit Karma requests for fpx + curl](artifact/references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/creditkarma-fpx)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown with shell command, JSON, and jq snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes commands that operate on a live Credit Karma session and may produce sensitive financial data.]

## Skill Version(s):

2.5.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
