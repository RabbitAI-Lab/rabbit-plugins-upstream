## Description:

Guides an authorized operator through low-balance Verdikta wallet onboarding, approved bounty transactions on Base, and withdrawals to the recorded owner address.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nigelon11](https://clawhub.ai/user/nigelon11)

### License/Terms of Use:

MIT-0

## Use Case:

External operators use this skill to set up a low-balance Verdikta wallet and API identity, commission owner-approved bounties, manage authorized transactions, and return funds to the recorded owner address on Base or Base Sepolia.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hot-wallet signing can cause irreversible loss of funds.

Mitigation: Use a fresh low-balance wallet, enforce tight owner-reviewed spend caps, and inspect dry-runs before authorizing exact transactions.

Risk: Exposed wallet credentials or recovery state can compromise funds.

Mitigation: Keep the wallet password in a secret store or mode-600 file outside the skill, and protect recovery state containing signed transaction bytes.

Risk: Unreviewed sibling skill code can run in the wallet-signing process during draft handoff.

Mitigation: Review the verdikta-discover package and its locked dependencies before using draft handoff.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/nigelon11/skills/verdikta-bounties-onboarding)
- [Verdikta Bounties](https://bounties.verdikta.org)
- [Operator onboarding](artifact/references/onboarding.md)
- [Commission and recovery](artifact/references/commission.md)
- [Custody and security](artifact/references/security.md)
- [API endpoints](artifact/references/api_endpoints.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with command examples and transaction summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report bounty IDs and transaction hashes after authorized execution.]

## Skill Version(s):

1.8.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
