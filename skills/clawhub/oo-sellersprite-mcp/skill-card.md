## Description:

SellerSprite MCP lets an agent operate SellerSprite Amazon product, keyword, competitor, market, traffic, review, trend, and trademark research actions through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect SellerSprite MCP action schemas and run SellerSprite research actions for Amazon product, keyword, competitor, market, traffic, review, trend, and trademark workflows through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes unverified remote installer commands that can execute arbitrary code on a user's machine.

Mitigation: Review the setup path before installing; prefer a trusted existing oo CLI installation, a pinned package, checksum or signature verification, or inspecting the installer before execution.

Risk: SellerSprite MCP actions tagged as write can change service state.

Mitigation: Confirm the exact payload and intended effect with the user before running write actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sellersprite-mcp)
- [SellerSprite MCP homepage](https://open.sellersprite.com/mcp)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload conventions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects with data and meta.executionId; actions tagged as write require user confirmation before execution.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
