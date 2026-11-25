## Description:

Draft, review, publish, fund and follow an Elgora bounty challenge (bounty_challenge.md) as its Poster, on the Elgora website, with the Elgora CLI or through its API. Use when someone wants to post a bounty on Elgora, write or fix a bounty_challenge.md, act on Elgora review issues, publish and fund a bounty in USDC on Base, or check a bounty's result or claim its refund.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elgora](https://clawhub.ai/user/elgora)

### License/Terms of Use:

MIT-0

## Use Case:

External posters use this skill to draft and review a bounty challenge, publish and fund it on Elgora, and follow its result or claim a refund. It supports the website, CLI, and API routes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some references were unresolved by the partial scan, so not all referenced material was assessed.

Mitigation: Review the referenced Elgora documentation and files before relying on publishing or funding guidance.

Risk: Publishing and funding use the Poster's wallet; a private-key signer can spend the funds held by that key.

Mitigation: Keep wallet secrets in the host's secret manager and use a dedicated wallet funded only for the agreed bounty and gas. Never disclose the wallet secret, and fund only at the Poster's request.

## Reference(s):

- [Elgora Poster examples](https://docs.elgora.ai/docs/poster/examples)
- [Elgora deployment details](https://elgora.ai/deployments.json)
- [Elgora API reference](https://docs.elgora.ai/docs/reference/api)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands, API calls]

**Output Format:** [Markdown challenge drafts and review guidance, with CLI command or API request examples as needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Publishing and funding require the Poster's direction and wallet authorization.]

## Skill Version(s):

6.4.0 (source: frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
