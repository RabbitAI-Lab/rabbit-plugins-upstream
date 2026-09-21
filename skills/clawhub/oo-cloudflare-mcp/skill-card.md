## Description:

Cloudflare MCP helps agents read, create, and update Cloudflare data through OOMOL's Cloudflare MCP connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Cloudflare MCP action schemas, search Cloudflare documentation and API specifications, and run Cloudflare API workflows through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands for the oo CLI.

Mitigation: Install the oo CLI only from a trusted source and prefer documented installers with verification where available.

Risk: The execute action can perform high-impact Cloudflare writes through a connected account.

Mitigation: Confirm every write payload and intended Cloudflare effect before allowing the execute action to run.

Risk: Production or administrative Cloudflare access increases the impact of mistakes.

Mitigation: Review the skill before installation and use least-privilege Cloudflare credentials where possible.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-cloudflare-mcp)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Cloudflare MCP](https://github.com/cloudflare/mcp)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Cloudflare action schemas, API guidance, command output summaries, and confirmation prompts for write or destructive actions.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
