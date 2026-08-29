## Description:

Combat and raiding in Structs: raids for stealing ore, direct struct attacks, and defense decisions for raiding targets, attacking enemy structs, defending a planet, or preparing for incoming attacks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[abstrct](https://clawhub.ai/user/abstrct)

### License/Terms of Use:

MIT-0

## Use Case:

External Structs players and agent operators use this skill to evaluate raid opportunities, plan direct attacks, set defensive posture, and choose safer command sequences for combat actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help propose irreversible in-game combat or raid transactions.

Mitigation: Review target IDs, guild implications, costs, and expected outcomes before authorizing any transaction with a signing key.

Risk: The raid-compute flow may auto-submit a completion step after operator approval.

Mitigation: Confirm the approval block, target vulnerability, home-defense exposure, and auto-submit behavior before running the command.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/abstrct/skills/structs-combat)
- [Structs conventions](https://structs.ai/skills/conventions)
- [Interface routing](https://structs.ai/skills/conventions#choosing-your-interface-capability-aware)
- [Combat mechanics](https://structs.ai/knowledge/mechanics/combat)
- [Fleet mechanics](https://structs.ai/knowledge/mechanics/fleet)
- [Under attack playbook](https://structs.ai/playbooks/situations/under-attack)
- [Guild war playbook](https://structs.ai/playbooks/situations/guild-war)
- [Counter-strategies playbook](https://structs.ai/playbooks/meta/counter-strategies)
- [Team operations playbook](https://structs.ai/playbooks/meta/team-operations)
- [structsd install skill](https://structs.ai/skills/structsd-install/SKILL)
- [Structs database schema](https://structs.ai/knowledge/infrastructure/database-schema)
- [structs-intel skill](https://structs.ai/skills/structs-intel/SKILL)
- [structs-production skill](https://structs.ai/skills/structs-production/SKILL)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and command references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or prepare irreversible in-game transaction commands that require operator review and signing-key authorization.]

## Skill Version(s):

1.25.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
