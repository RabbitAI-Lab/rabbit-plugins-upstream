## Description:

DingTalk MCP lets agents discover DingTalk MCP tools, inspect live input schemas, and run schema-compliant connector actions through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to search and read DingTalk data, discover currently available DingTalk MCP tools, and invoke selected tools through an OOMOL-connected account. Write or destructive DingTalk operations require explicit confirmation before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands for the oo CLI.

Mitigation: Prefer a verified or package-managed oo CLI installation, or review the installer before running it.

Risk: The DingTalk MCP connection can expose actions that modify, overwrite, cancel, or delete DingTalk data.

Mitigation: List tools and inspect live schemas first, then require explicit user confirmation for write or destructive payloads.

Risk: Using this skill grants the connected OOMOL workflow access to DingTalk through server-side credentials.

Mitigation: Use an account and scopes appropriate for the task, and review the DingTalk connection before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-dingtalk-mcp)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [DingTalk MCP homepage](https://www.dingtalk.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May emit oo CLI commands and schema-compliant JSON arguments for DingTalk MCP connector actions.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
