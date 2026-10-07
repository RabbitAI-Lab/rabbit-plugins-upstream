## Description:

Guides authorized operators through Verdikta Bounties wallet onboarding and reviewed bounty transactions on Base and Base Sepolia.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nigelon11](https://clawhub.ai/user/nigelon11)

### License/Terms of Use:

MIT-0

## Use Case:

Operators and developers use this skill to set up a low-balance Verdikta wallet and API identity, then create, submit to, and manage bounties with explicit owner approval and spending limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hot-wallet signing can spend real funds through irreversible transactions.

Mitigation: Use a fresh low-balance wallet, test on Base Sepolia, set tight owner spending limits, and review each transaction before confirmation.

Risk: Wallet passwords and API credentials could be exposed during setup or operation.

Mitigation: Keep passwords out of chat and .env; supply them through a secret store or private terminal prompt and protect the local API key.

Risk: Bounty details, submitted work, wallet addresses, and transactions may become public.

Mitigation: Review all content and files before upload or signing; avoid including private information.

Risk: An unreviewed sibling skill could run alongside wallet-signing code during draft handoff.

Mitigation: Review and protect the optional verdikta-discover installation and its dependencies as part of the signing trust boundary.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/nigelon11/skills/verdikta-bounties-onboarding)
- [Operator onboarding](artifact/references/onboarding.md)
- [Commission configuration and recovery](artifact/references/commission.md)
- [API endpoints](artifact/references/api_endpoints.md)
- [Security and custody](artifact/references/security.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide wallet setup and transaction review; financial actions require separate owner authorization.]

## Skill Version(s):

1.6.0 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
