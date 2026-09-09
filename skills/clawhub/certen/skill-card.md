## Description:

Give this agent a CERTEN identity and let it execute proof-gated actions on any chain it is linked to. It never spends without the owner's explicit consent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jason-gregoire](https://clawhub.ai/user/jason-gregoire)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to give an agent a CERTEN identity, inspect account state, and run consent-gated on-chain actions. It is intended for money-at-stake workflows such as escrow, settlement, arbitration, insurance, and regulated approval flows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to create and persist signing and API credentials that could authorize financial actions if leaked.

Mitigation: Use a dedicated low-value or testnet identity first, avoid storing raw key and API config files in shared workspaces, and protect any persisted CERTEN credential files.

Risk: A persistent CERTEN identity can submit identity, transaction, governance, and funding commands that may move funds or alter control policy.

Mitigation: Require explicit owner approval for each specific action before running any spending, identity, transaction, governance, or funding command.

## Reference(s):

- [CERTEN ClawHub Skill Page](https://clawhub.ai/jason-gregoire/skills/certen)
- [CERTEN CLI Package](https://www.npmjs.com/package/@certen.io/cli)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with bash command examples and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Bundled status script prints one JSON object summarizing organization, identities, spendable balance, enforcement mode, and credential errors.]

## Skill Version(s):

0.1.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
