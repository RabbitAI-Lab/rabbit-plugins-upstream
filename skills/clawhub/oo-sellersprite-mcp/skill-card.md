## Description:

SellerSprite MCP (open.sellersprite.com) helps agents operate SellerSprite MCP through OOMOL-connected accounts for Amazon product, keyword, market, traffic, trademark, and analytics workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run SellerSprite MCP actions through the oo CLI after inspecting live schemas, covering Amazon ASIN research, keyword research, market analysis, traffic analysis, trademark lookup, and tool discovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include unverified remote script execution for installing the oo CLI.

Mitigation: Prefer an official package-managed or checksum-verified installation path before running the CLI installer.

Risk: The SellerSprite MCP connector exposes a write-capable call_tool action.

Mitigation: Inspect the live tool schema and behavior annotations, then confirm any write-capable payload and expected effect with the user before execution.

## Reference(s):

- [SellerSprite MCP homepage](https://open.sellersprite.com/mcp)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub release page](https://clawhub.ai/oomol/skills/oo-sellersprite-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands call SellerSprite MCP through the oo CLI and return JSON responses that include data and execution metadata.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
