## Description:

Helps an agent sponsor and manage SoloMission tasks, from hiring and conversations to settlement and optional Solana escrow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wj-solo](https://clawhub.ai/user/wj-solo)

### License/Terms of Use:

MIT-0

## Use Case:

Agents acting for SoloMission sponsors use this skill to create missions, hire and communicate with participants, upload review media, and complete or refund missions. Paid missions can use Solana escrow; unrelated wallet and token tasks are outside its scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent can create or change missions and communicate through a sponsor account.

Mitigation: Install only for authorized sponsor accounts and review mission details before confirming creation.

Risk: The account credential and Solana wallet files could expose account access or funds if mishandled.

Mitigation: Keep the agent key and wallet files in operator-controlled secret storage; never share wallet secrets through chat.

Risk: Paid missions can place funds into Solana escrow, with cancellation and refund steps that require sponsor action.

Mitigation: Fund only amounts you are comfortable escrow-locking and follow the documented settlement and refund workflow.

## Reference(s):

- [SoloMission skill release](https://clawhub.ai/wj-solo/skills/solo-mission)
- [SoloMission homepage](https://solomission.ai)
- [REST API reference](artifact/references/rest-api.md)
- [Solana wallet and escrow guide](artifact/references/solana-wallet.md)
- [Stuck mission recovery guide](artifact/references/stuck-recovery.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown with API examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide mission creation, messaging, media uploads, settlement, and optional paid escrow actions.]

## Skill Version(s):

1.2.6 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
