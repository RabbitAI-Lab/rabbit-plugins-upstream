## Description:

Guides developers integrating the unofficial Go client for Klavis AI API and MCP server operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add the Go client to an application and work with Klavis AI APIs, including MCP server discovery, tool calls, instances, and integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys or downstream authentication data may be exposed or sent to the wrong host.

Mitigation: Keep credentials out of code and logs, and use the account's correct US or EU host.

Risk: Tool calls or management operations may change external services and remote resources.

Mitigation: Verify MCP server URLs and tool arguments; obtain explicit user approval before destructive operations, auth changes, sandbox execution, or downstream tool calls.

## Reference(s):

- [go-klavis setup and reference](references/setup.md)
- [go-klavis Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-klavis)
- [go-klavis project](https://github.com/psyb0t/go-klavis)
- [go-klavis ClawHub release](https://clawhub.ai/psyb0t/skills/go-klavis)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for integrating an API client; remote operations require an API key.]

## Skill Version(s):

0.2.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
