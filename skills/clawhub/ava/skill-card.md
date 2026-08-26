## Description:

Ava helps coding agents execute bounded DeFi actions, with live lending scoped to Base and Morpho after an Ava session and MCP connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kamalbuilds](https://clawhub.ai/user/kamalbuilds)

### License/Terms of Use:

MIT-0

## Use Case:

Developers using coding agents use Ava to connect to the Ava MCP server and carry out bounded Base/Morpho lending flows with preview, explicit approval, and receipt checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can assist with live DeFi actions that may affect user funds.

Mitigation: Confirm the MCP URL, review every preview, and approve live execution only when the asset, chain, amount, and venue match the user's intent.

Risk: Bearer tokens used for the Ava MCP connection could be exposed in logs or shared prompts.

Mitigation: Keep bearer tokens out of logs, transcripts, and shared prompts.

Risk: A testnet or simulation path could be mistaken for a live fill or holding.

Mitigation: Use the live lend flow for real DeFi, require the returned previewHash for execution, and report a fill only when the receipt shows chain-confirmed standing.

## Reference(s):

- [Ava homepage](https://getava.xyz)
- [Ava MCP endpoint](https://www.getava.xyz/mcp)
- [ClawHub ava listing](https://clawhub.ai/kamalbuilds/skills/ava)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls, markdown]

**Output Format:** [Markdown with inline commands and structured tool-call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user review of previews before live execution; bearer tokens must be kept out of logs and shared prompts.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
