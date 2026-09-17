## Description:

SellerSprite MCP (open.sellersprite.com). Use this skill for ANY SellerSprite MCP request: reading, creating, and updating data through the SellerSprite MCP connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate SellerSprite MCP through an OOMOL-connected account for Amazon product, keyword, competitor, market, review, traffic, trend, and trademark research. It guides agents to inspect live action schemas, build valid JSON payloads, run read actions, and request explicit confirmation before state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands for the oo CLI.

Mitigation: Install the oo CLI through a trusted, verifiable method and review installer contents before use.

Risk: Tagged write actions can change SellerSprite MCP state.

Mitigation: Require explicit user confirmation of the exact payload and expected effect before running any write-tagged action.

## Reference(s):

- [SellerSprite MCP homepage](https://open.sellersprite.com/mcp)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sellersprite-mcp)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI connector schema and run commands; write-tagged actions require explicit user confirmation.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
