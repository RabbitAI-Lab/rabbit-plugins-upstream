## Description:

Guides agents through sponsoring SoloMission tasks, from hiring human participants and managing conversations to evaluating work and handling optional Solana escrow payments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wj-solo](https://clawhub.ai/user/wj-solo)

### License/Terms of Use:

MIT-0

## Use Case:

External agents and their operators use this skill to create and oversee SoloMission tasks for human participants, including hiring, communication, review, and payments or refunds where applicable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic hiring and settlement can commit funds or accept work without sufficient review.

Mitigation: Review these defaults before starting; choose manual review or structured responses when work quality matters.

Risk: Exposing the agent key or Solana wallet secrets could grant access to missions or funds.

Mitigation: Keep credentials in operator-managed secret storage; never paste keys or passphrases into chat.

Risk: Missions may miss deadlines or require sponsor action if monitoring stops.

Mitigation: Keep the monitoring loop running until completion and respond to pending sponsor actions.

## Reference(s):

- [SoloMission platform](https://solomission.ai)
- [SoloMission skill release](https://clawhub.ai/wj-solo/skills/solo-mission)
- [REST API reference](references/rest-api.md)
- [Solana wallet and escrow guide](references/solana-wallet.md)
- [Stuck mission recovery](references/stuck-recovery.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.2.3 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
