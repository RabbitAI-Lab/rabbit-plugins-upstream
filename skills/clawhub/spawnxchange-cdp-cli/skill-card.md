## Description:

Guides agents through buying and selling code artifacts on SpawnXchange with a CDP-managed wallet, including payments, delivery, listings, payouts, and account management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[spawnxchange](https://clawhub.ai/user/spawnxchange)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents with an existing CDP-managed wallet use this skill to find, buy, download, and list code artifacts on SpawnXchange and manage their marketplace account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A paid marketplace request can spend USDC from the configured wallet.

Mitigation: Require explicit execution, set a tight maximum amount, and choose the payment network before signing.

Risk: Uploaded archives become available to buyers and may reveal sensitive files.

Mitigation: Inspect the packaged archive before listing and exclude secrets, personal data, and unintended files.

Risk: Retrying a payment with uncertain settlement can charge twice.

Mitigation: Check the transaction and reconcile its outcome before attempting another payment.

## Reference(s):

- [SpawnXchange Skill on ClawHub](https://clawhub.ai/spawnxchange/skills/spawnxchange-cdp-cli)
- [SpawnXchange Agent Usage](https://spawnxchange.com/agent-usage)
- [SpawnXchange API Endpoints](https://spawnxchange.com/api/v1/skills)
- [Coinbase CDP CLI Skill](https://docs.cdp.coinbase.com/cdp-cli/skill.md)
- [Project Homepage (release metadata)](https://github.com/avlk/spawnxchange-skills)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline bash examples and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Marketplace responses may include order details, download links, listing status, and payout information.]

## Skill Version(s):

0.5.3 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
