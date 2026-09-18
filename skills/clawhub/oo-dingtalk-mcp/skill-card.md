## Description:

DingTalk MCP helps an agent search, read, and operate DingTalk MCP data through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to discover live DingTalk MCP tools, inspect schemas, and run schema-compliant actions through an OOMOL-connected account. It supports DingTalk search and reading workflows, with confirmation steps for operations that may change or delete DingTalk data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can invoke broad live DingTalk account actions, including operations that may change or delete data.

Mitigation: Inspect the live action schema before building a payload and get explicit user confirmation before running any mutating or destructive action.

Risk: The setup guidance includes remote installer commands that pipe downloaded scripts into a shell.

Mitigation: Use the installer only after independently trusting and verifying the OOMOL CLI source, or follow a reviewed installation path.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-dingtalk-mcp)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [DingTalk homepage](https://www.dingtalk.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector command responses are JSON when --json is used.]

## Skill Version(s):

1.0.2 (source: evidence release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
