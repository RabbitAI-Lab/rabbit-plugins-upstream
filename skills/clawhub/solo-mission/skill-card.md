## Description:

Operate SoloMission missions from recruiting and conversations through qualification, settlement, and Solana escrow management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wj-solo](https://clawhub.ai/user/wj-solo)

### License/Terms of Use:

MIT-0

## Use Case:

SoloMission sponsors use the skill to create and run human-participant missions, manage conversations and media reviews, and handle qualification, settlement, ratings, and escrow actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recovery and refund actions can affect other missions or use stale mission state.

Mitigation: Require operator approval before recovery affects other missions and refresh mission details before refunds.

Risk: Wallet lookups or paid missions may involve access to sensitive wallet files.

Mitigation: Use a dedicated SoloMission account and wallet; use a public wallet address for lookups instead of granting additional key-file access.

Risk: Uploaded media is shared with mission participants.

Mitigation: Upload only media approved for sharing with those participants.

## Reference(s):

- [SoloMission](https://solomission.ai)
- [SoloMission API](https://api.mission.projectsolo.ai)
- [ClawHub skill release](https://clawhub.ai/wj-solo/skills/solo-mission)

## Skill Output:

**Output Type(s):** [Guidance, API calls, Shell commands, Text, JSON]

**Output Format:** [Natural-language guidance, shell commands, and structured API data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Mission actions and outputs depend on the selected mission and sponsor approval.]

## Skill Version(s):

1.2.7 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
