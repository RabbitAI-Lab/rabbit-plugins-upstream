## Description:

Connects an agent to TikTok for Business MCP through OOMOL's oo CLI to discover available tools and run actions with account-connected credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent inspect TikTok for Business MCP schemas, list available tools, and run TikTok Business actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can call live TikTok Business MCP tools that may change account state.

Mitigation: Require explicit confirmation of the exact target, payload, and expected effect before budget, ad, access, or deletion operations.

Risk: A tool may appear read-oriented while its live schema permits account-changing behavior.

Mitigation: Fetch and review the live connector schema before each action and treat call_tool as account-changing unless the schema proves it is read-only.

## Reference(s):

- [TikTok for Business](https://business.tiktok.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-tiktok-business-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution; account-changing actions require explicit user confirmation.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
