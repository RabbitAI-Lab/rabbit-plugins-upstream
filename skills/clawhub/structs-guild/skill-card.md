## Description:

Guilds in Structs - choosing and joining one, ranks and rank-permissions, membership flows, settings, UGC moderation, charter vs entitlement founding, and the Central Bank (mint/redeem/convert).

This skill is ready for commercial/non-commercial use.

## Publisher:

[abstrct](https://clawhub.ai/user/abstrct)

### License/Terms of Use:

MIT-0

## Use Case:

Structs players and operators use this skill to choose or create guilds, manage members and ranks, moderate member identity, and run guild Central Bank token operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes commands for consequential signed transactions such as ownership transfer, UGC moderation, token minting, redemption, conversion, and confiscate-and-burn actions.

Mitigation: Before approving any transaction, verify target IDs, token amounts, rank or permission requirements, and slippage limits against the intended Structs state.

Risk: Guild moderation commands can change member names or profile images and may affect user-facing identity.

Mitigation: Use moderation commands only under the guild's policy and review emitted audit events for actor, target, field, old value, and new value.

## Reference(s):

- [Structs conventions](https://structs.ai/skills/conventions)
- [Structs guild charter hashing](https://structs.ai/knowledge/mechanics/hashing#guild-charter)
- [Structs permissions skill](https://structs.ai/skills/structs-permissions/SKILL)
- [Structs UGC moderation](https://structs.ai/knowledge/mechanics/ugc-moderation)
- [Structs guild banking](https://structs.ai/knowledge/economy/guild-banking)
- [Structs permissions mechanics](https://structs.ai/knowledge/mechanics/permissions)
- [Structs guild war playbook](https://structs.ai/playbooks/situations/guild-war)
- [Structs CLI install](https://structs.ai/skills/structsd-install/SKILL)
- [ClawHub skill page](https://clawhub.ai/abstrct/skills/structs-guild)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline bash code blocks and command tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes user-reviewed transaction commands for guild membership, rank administration, UGC moderation, and guild token operations.]

## Skill Version(s):

1.25.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
