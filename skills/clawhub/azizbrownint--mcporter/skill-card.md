## Description:

List, configure, authenticate, call, and inspect MCP servers/tools with mcporter over HTTP or stdio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to guide agents in operating the mcporter CLI for MCP server discovery, configuration, authentication, tool calls, daemon management, and code generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents may use mcporter to contact untrusted MCP servers or remote endpoints.

Mitigation: Use trusted endpoints and review server URLs before allowing tool calls.

Risk: Authentication and configuration commands can affect credentials or persistent MCP access.

Mitigation: Review auth and config changes, avoid placing secrets in tool arguments unless necessary, and stop the daemon when persistent access is not needed.

## Reference(s):

- [mcporter homepage](http://mcporter.dev)
- [ClawHub skill page](https://clawhub.ai/azizbrownint/skills/mcporter)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can recommend JSON output for automation when using mcporter.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
