## Description:

Sorftime MCP (sorftime.com) helps agents search and read marketplace, keyword, category, product, market, and trend data through an OOMOL-connected Sorftime MCP account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Sorftime MCP through the OOMOL `oo` CLI for marketplace research across Amazon, Walmart, TikTok, Shopee, Temu, and 1688. It supports product inspection, keyword discovery, category research, trend analysis, and account-specific Sorftime tool calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary reports that the skill under-discloses account-changing actions.

Mitigation: Require explicit user confirmation before using `call_tool` for actions that change favorites, delete data, or spend credits.

Risk: The security summary reports unsafe remote installer execution guidance.

Mitigation: Review before installing and do not let an agent run the installer pipeline automatically.

Risk: The security guidance limits appropriate use to Sorftime MCP tasks.

Mitigation: Use the skill only for Sorftime MCP research, inspection, and account-specific tool calls.

## Reference(s):

- [Sorftime MCP homepage](https://www.sorftime.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sorftime-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the OOMOL `oo` CLI and return connector responses with `data` and `meta.executionId` fields.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
