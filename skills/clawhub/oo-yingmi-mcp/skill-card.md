## Description:

Yingmi MCP helps agents discover and invoke Yingmi MCP financial data, research, and advisory tools through an OOMOL-connected oo CLI account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent inspect Yingmi MCP tool schemas, list available financial tools, and call selected tools through an authenticated OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill presents a read-oriented workflow while exposing a broad generic tool-calling path through an authenticated financial service connector.

Mitigation: Inspect the live tool schema and behavior annotations before each call, and require explicit user confirmation before any write, destructive, transaction, or account-changing action.

Risk: Connected Yingmi or OOMOL accounts may expose sensitive financial, advisory, or account-level capabilities.

Mitigation: Install and use the skill only with accounts whose available connector tools are appropriate for agent access, and review the account permissions before deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-yingmi-mcp)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Yingmi MCP Homepage](https://qieman.com/mcp/mcp-market)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces guidance for schema inspection, connector calls, setup recovery, and user confirmation before write or destructive actions.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
