## Description:

Guides agents through Structs power capacity, load budgeting, offline recovery, substation allocations, and reactor or generator infusion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[abstrct](https://clawhub.ai/user/abstrct)

### License/Terms of Use:

MIT-0

## Use Case:

External Structs players and operators use this skill to plan power headroom, recover from offline states, and prepare capacity-related transactions such as reactor infusion, generator infusion, allocations, and substation connections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide signed game transactions that spend Alpha Matter or modify substation/player power state.

Mitigation: Confirm transaction amounts, targets, permissions, and power-state effects before signing.

Risk: Generator infusion is irreversible and can place infused matter at risk if the generator is raided.

Mitigation: Use generator infusion only after verifying ownership, generator type, online state, defenses, and the exact ualpha amount.

Risk: Incorrect substation allocations or player migrations can reduce available power and knock dependent players or structs offline.

Mitigation: Review allocation size, connection count, required permissions, and headroom before changing substation connections.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/abstrct/skills/structs-energy)
- [Structs energy mechanics](https://structs.ai/knowledge/mechanics/energy)
- [Structs power mechanics](https://structs.ai/knowledge/mechanics/power)
- [Structs resources mechanics](https://structs.ai/knowledge/mechanics/resources)
- [Structs conventions](https://structs.ai/skills/conventions)
- [structsd install skill](https://structs.ai/skills/structsd-install/SKILL)
- [structs-commerce skill](https://structs.ai/skills/structs-commerce/SKILL)
- [resource-rich playbook](https://structs.ai/playbooks/situations/resource-rich)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands]

**Output Format:** [Markdown guidance with inline shell commands and transaction checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent output may propose signed Structs transactions; users should confirm targets, amounts, denomination, and irreversible generator infusion warnings before approval.]

## Skill Version(s):

1.25.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
