## Description:

Guides agents in retrieving Blave market data and using exchange APIs for research, analysis, and trading workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[blave-wei](https://clawhub.ai/user/blave-wei)

### License/Terms of Use:

MIT-0

## Use Case:

Traders, analysts, and developers use this skill to query crypto, Taiwan equity, and futures market data and to prepare or perform exchange trading and funding actions with explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live exchange actions can cause financial loss or move funds.

Mitigation: Require explicit confirmation for each action; start in testnet or paper mode and use least-privilege API keys with withdrawals disabled and IP allowlists enabled.

Risk: Marketplace strategy code may be downloaded and run without sufficient containment.

Mitigation: Review strategy code before running it, and execute it in a sandbox isolated from API secrets and valuable accounts.

## Reference(s):

- [ClawHub release](https://clawhub.ai/blave-wei/skills/blave-quant-skill)
- [Blave documentation](https://blave.org/docs/en)
- [Blave API reference](references/blave-api.md)
- [Exchange trading references](SKILL.md)
- [Marketplace strategy reference](references/marketplace.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, API calls]

**Output Format:** [Markdown with code and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Trading, cancellations, transfers, and funding actions require a separate explicit confirmation for each action.]

## Skill Version(s):

1.23.17 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
