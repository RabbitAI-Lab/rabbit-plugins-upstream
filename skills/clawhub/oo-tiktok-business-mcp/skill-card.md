## Description:

TikTok for Business MCP helps agents inspect live connector schemas and run TikTok for Business actions through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to discover available TikTok for Business MCP tools, inspect their live input schemas, and run account operations through the OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connector can expose tools that change or delete TikTok Business advertising assets, while parts of the skill describe read-oriented use.

Mitigation: Before any call_tool run, require the exact downstream tool, account, payload, budget or delivery effect, and whether the action writes or deletes data.

Risk: The skill depends on a generic connector whose available tools and schemas can change over time.

Mitigation: Inspect the live action schema before constructing each request and prefer read-only or narrower access when reporting is the only goal.

Risk: First-time setup includes pipe-to-shell installation commands for the oo CLI.

Mitigation: Avoid pipe-to-shell installation unless the installer source and contents have been verified.

## Reference(s):

- [TikTok for Business](https://business.tiktok.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-tiktok-business-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include live connector schemas, tool catalogs, execution responses, and setup guidance.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
