## Description:

Yingmi MCP (qieman.com) enables agents to read, create, and update data through the Yingmi MCP connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to discover Yingmi MCP tools and run Yingmi financial data, research, and advisory actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remotely downloaded installer commands that could be unsafe if run unattended or without verification.

Mitigation: Install or verify the oo CLI yourself before use, and do not allow an agent to run installer commands unattended.

Risk: The skill can invoke Yingmi MCP actions that may change account state when a live tool is writable or destructive.

Mitigation: Review each write or destructive payload and its intended effect before approving execution.

## Reference(s):

- [Yingmi MCP homepage](https://qieman.com/mcp/mcp-market)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-yingmi-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include connector execution data and execution IDs returned by the oo CLI.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
