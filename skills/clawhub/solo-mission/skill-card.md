## Description:

Helps an agent create and manage SoloMission tasks for human participants, including hiring, conversations, media reviews, settlement, and optional Solana escrow funding or refunds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wj-solo](https://clawhub.ai/user/wj-solo)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their operators use this skill to commission and manage tasks with human participants on SoloMission, communicate with participants, and handle mission payments and refunds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Solo agent key grants access to mission actions.

Mitigation: Keep the key in the operator's secret store; do not share it in chat or write it to mission files.

Risk: Solana escrow funding or refunds can move funds.

Mitigation: Review mission budgets, protect wallet credentials, and use dry-run and verification paths before signing.

Risk: Uploaded tracks or conversation images may be accessible to participants.

Mitigation: Upload only files intended for the mission participants or conversation recipient.

## Reference(s):

- [SoloMission skill release](https://clawhub.ai/wj-solo/skills/solo-mission)
- [SoloMission platform](https://solomission.ai)
- [REST API reference](artifact/references/rest-api.md)
- [Solana wallet and escrow guide](artifact/references/solana-wallet.md)
- [Stuck mission recovery](artifact/references/stuck-recovery.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Configuration]

**Output Format:** [Markdown with shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update a local mission state file; paid missions require an operator-configured Solana wallet.]

## Skill Version(s):

1.2.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
