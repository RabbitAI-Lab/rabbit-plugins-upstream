## Description:

Draft, review, publish, fund and follow an Elgora bounty challenge (bounty_challenge.md) as its Poster, on the Elgora website, with the Elgora CLI or through its API. Use when someone wants to post a bounty on Elgora, write or fix a bounty_challenge.md, act on Elgora review issues, publish and fund a bounty in USDC on Base, or check a bounty's result or claim its refund.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elgora](https://clawhub.ai/user/elgora)

### License/Terms of Use:

MIT-0

## Use Case:

External users acting as Posters use this skill to turn a task into a clear Elgora bounty challenge, resolve review feedback, and publish, fund, or follow the bounty using the website, CLI, or API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marked the release suspicious over a medium-confidence concern about accessing other installed skills, and the scan is incomplete.

Mitigation: Review the flagged behavior and the install mechanism concern before installing; account for the incomplete scan when deciding whether to proceed.

Risk: Publishing can require wallet signatures and funding a bounty with real USDC on Base.

Mitigation: Keep wallet secrets private, inspect signing requests, and limit any server-wallet policy and funding amount to the Poster-approved bounty.

## Reference(s):

- [Elgora Poster Skill on ClawHub](https://clawhub.ai/elgora/skills/elgora-poster-skill)
- [Elgora Poster examples](https://docs.elgora.ai/docs/poster/examples)
- [Elgora deployment details](https://elgora.ai/deployments.json)
- [Published skill source](https://elgora.ai/skills/elgora-poster-skill/)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands, API calls]

**Output Format:** [Markdown challenge drafts and review guidance, with route-specific shell commands or HTTP API requests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Publishing and funding steps depend on the selected route and require the Poster's wallet and authorization.]

## Skill Version(s):

6.3.0 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
