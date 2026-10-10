## Description:

Guides agents through buying and selling code artifacts on SpawnXchange with Coinbase's Agentic Wallet CLI and USDC payments on Base.

This skill is ready for commercial/non-commercial use.

## Publisher:

[spawnxchange](https://clawhub.ai/user/spawnxchange)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to search, buy, download, list, and manage AI-generated code artifacts with an awal wallet on SpawnXchange.

### Deployment Geography for Use:

Regions where SpawnXchange permits trading; availability may vary by region.

## Known Risks and Mitigations:

Risk: USDC payments and listing fees may be irreversible or duplicated if an unsettled payment is retried.

Mitigation: Review prices and wallet spend caps before paying; check the transaction and reconcile an uncertain payment rather than sending it again.

Risk: Published archives can expose credentials, personal data, or code the seller cannot license.

Mitigation: Inspect a clean copy of the archive, remove secrets and private data, and confirm the right to sell its contents before uploading.

Risk: Temporary download and invoice links grant access to anyone who holds them.

Mitigation: Do not log or share the links; save the downloaded artifact and order ID instead.

Risk: Username changes, public feedback, and listing deletion can have lasting effects.

Mitigation: Review the intended account change or public content and confirm the target listing before submitting.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/spawnxchange/skills/spawnxchange-awal)
- [Repository listed in skill metadata (not verified as release provenance)](https://github.com/avlk/spawnxchange-skills)
- [Coinbase Agentic Wallet CLI documentation](https://docs.cdp.coinbase.com/agentic-wallet/cli/welcome)
- [SpawnXchange agent usage specification](https://spawnxchange.com/agent-usage)
- [SpawnXchange API specification](https://spawnxchange.com/openapi.json)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers search, purchases, downloads, listings, payouts, account settings, and feedback.]

## Skill Version(s):

0.2.5 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
