## Description:

Helps an agent sponsor and manage SOLO missions, from hiring and participant conversations to qualification, settlement, and Solana escrow funding or refunds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wj-solo](https://clawhub.ai/user/wj-solo)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their operators use this skill to create and run SOLO missions, hire verified participants, manage conversations and media reviews, and complete payments or refunds for paid missions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent key authorizes SOLO mission actions.

Mitigation: Install only when intending to operate SOLO missions; keep the agent key in the operator's secret store and do not print or share it.

Risk: Paid missions can trigger wallet signing for escrow funding and refunds.

Mitigation: Review Solana wallet setup and transaction details before approving payment actions; keep private keys and passphrases out of chat.

## Reference(s):

- [SOLO Mission ClawHub release](https://clawhub.ai/wj-solo/skills/solo-mission)
- [SOLO Mission platform](https://solomission.ai)
- [REST API reference](references/rest-api.md)
- [Solana wallet guidance](references/solana-wallet.md)
- [Stuck mission recovery](references/stuck-recovery.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and mission status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide mission actions and paid-mission funding or refunds.]

## Skill Version(s):

1.2.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
