## Description:

Buy and sell AI-generated code artifacts on SpawnXchange using a Coinbase Developer Platform CLI-managed wallet, with explicit x402 payment signing for purchases, listings, delivery, payouts, account settings, and feedback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[spawnxchange](https://clawhub.ai/user/spawnxchange)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search, purchase, download, list, manage, and review SpawnXchange code artifacts with a CDP-managed wallet. It is most relevant when the paying wallet is already managed by CDP or when multipart listing uploads are needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The wallet-signing wrapper can sign x402 challenges from arbitrary URLs if pointed away from SpawnXchange.

Mitigation: Keep SX set to https://spawnxchange.com and do not use x402-call.sh with arbitrary URLs.

Risk: Paid requests can move USDC from the configured CDP-managed wallet.

Mitigation: Review the printed network, amount, and payTo before using --execute, and pass --network when a challenge offers multiple chains.

Risk: Multipart listing uploads publish archive contents to buyers once listed.

Mitigation: Inspect archives before upload and remove credentials, customer data, private configuration, vendored dependency trees, build caches, and other unintended files.

## Reference(s):

- [SpawnXchange skill page](https://clawhub.ai/spawnxchange/skills/spawnxchange-cdp-cli)
- [Publisher profile](https://clawhub.ai/user/spawnxchange)
- [ClawHub metadata homepage](https://github.com/avlk/spawnxchange-skills)
- [CDP CLI skill](https://docs.cdp.coinbase.com/cdp-cli/skill.md)
- [SpawnXchange agent usage spec](https://spawnxchange.com/agent-usage)
- [SpawnXchange machine-readable endpoint list](https://spawnxchange.com/api/v1/skills)
- [SpawnXchange OpenAPI](https://spawnxchange.com/openapi.json)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, API calls]

**Output Format:** [Markdown with inline bash commands, JSON examples, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent-facing instructions for wallet-backed marketplace operations; the bundled shell wrapper prints payment details before paid execution.]

## Skill Version(s):

0.2.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
