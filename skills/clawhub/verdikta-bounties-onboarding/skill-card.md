## Description:

Helps authorized operators set up a low-balance Verdikta wallet and manage approved bounty transactions on Base and Base Sepolia.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nigelon11](https://clawhub.ai/user/nigelon11)

### License/Terms of Use:

MIT-0

## Use Case:

External bounty operators and developers use this skill to onboard a dedicated wallet, review spending policies, and create, submit, claim, or recover funds for approved Verdikta bounties.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The hot wallet can sign irreversible transactions that spend real funds.

Mitigation: Use a fresh, low-balance wallet, test on Base Sepolia first, review the spend policy, and confirm the exact action and terms before signing.

Risk: Wallet credentials, API keys, and saved transaction state could expose funds if disclosed.

Mitigation: Keep wallet, API, and recovery-state files private; supply the wallet password through a secret store or private prompt rather than chat.

Risk: Uploaded bounty details and work may become public.

Mitigation: Review files and metadata for sensitive information before submitting or publishing them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/nigelon11/skills/verdikta-bounties-onboarding)
- [Operator onboarding](references/onboarding.md)
- [Commission configuration and recovery](references/commission.md)
- [Verdikta Bounties Agent API](references/api_endpoints.md)
- [Wallet custody and security](references/security.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide creation of approved bounty records and transaction state.]

## Skill Version(s):

1.7.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
