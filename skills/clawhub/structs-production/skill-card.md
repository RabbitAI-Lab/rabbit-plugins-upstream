## Description:

Runs the Alpha Matter production pipeline in Structs: mine ore, refine it to Alpha Matter, and put the resulting Alpha Matter to work while managing scheduling and ore exposure risk.

This skill is ready for commercial/non-commercial use.

## Publisher:

[abstrct](https://clawhub.ai/user/abstrct)

### License/Terms of Use:

MIT-0

## Use Case:

External Structs players and operators use this skill to schedule ore mining and refining, protect stored ore during long-running jobs, and decide how to deploy refined Alpha Matter.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may guide an agent to launch long-running Structs CLI jobs that auto-submit game transactions with the configured signing key.

Mitigation: Before launch, confirm the target struct IDs, signing key, timing, and approval block; monitor job logs and verify chain state after completion.

## Reference(s):

- [Structs conventions](https://structs.ai/skills/conventions)
- [Structs combat](https://structs.ai/skills/structs-combat/SKILL)
- [Structs permissions](https://structs.ai/skills/structs-permissions/SKILL)
- [Under attack playbook](https://structs.ai/playbooks/situations/under-attack)
- [Resource-rich playbook](https://structs.ai/playbooks/situations/resource-rich)
- [Resource-scarce playbook](https://structs.ai/playbooks/situations/resource-scarce)
- [Hashing mechanics: raid pause](https://structs.ai/knowledge/mechanics/hashing#raid-pause-mine-and-refine)
- [Hashing mechanics: cycle lifecycle](https://structs.ai/knowledge/mechanics/hashing#minerefine-cycle-lifecycle)
- [Structs energy](https://structs.ai/skills/structs-energy/SKILL)
- [Structs commerce](https://structs.ai/skills/structs-commerce/SKILL)
- [Structsd install](https://structs.ai/skills/structsd-install/SKILL)
- [Structs resource mechanics](https://structs.ai/knowledge/mechanics/resources)
- [Structs planet mechanics](https://structs.ai/knowledge/mechanics/planet)
- [Async operations](https://structs.ai/awareness/async-operations)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes approval checks, command templates, verification steps, and troubleshooting guidance for Structs production jobs.]

## Skill Version(s):

1.25.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
