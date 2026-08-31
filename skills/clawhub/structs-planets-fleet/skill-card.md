## Description:

Manages planets and fleets in Structs by guiding planet exploration, claiming and relocation decisions, fleet movement, fleet composition, evacuation, and onStation versus away state.

This skill is ready for commercial/non-commercial use.

## Publisher:

[abstrct](https://clawhub.ai/user/abstrct)

### License/Terms of Use:

MIT-0

## Use Case:

External Structs players and agents use this skill to decide when to explore or relocate planets, how to move or recall fleets, and how to avoid losing planet or fleet assets during normal game operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes Structs CLI transactions that can change in-game state.

Mitigation: Install and use it only when the operator intends to run Structs commands, and review transaction prompts before signing.

Risk: Subsequent planet exploration destroys the current planet and remaining planet structs.

Mitigation: Use the skill's depletion, onStation, evacuation, and approval-block checks before running planet-explore for an existing player.

Risk: Sending the fleet away prevents local planet actions and can expose home shields or strand the fleet in hostile space.

Mitigation: Confirm fleet status and destination, keep raids short, and recall the fleet home before building, mining, refining, or exploring.

## Reference(s):

- [Structs planet mechanics](https://structs.ai/knowledge/mechanics/planet)
- [Structs fleet mechanics](https://structs.ai/knowledge/mechanics/fleet)
- [Structs production skill](https://structs.ai/skills/structs-production/SKILL)
- [Structs combat skill](https://structs.ai/skills/structs-combat/SKILL)
- [Structs conventions](https://structs.ai/skills/conventions)
- [Structs install skill](https://structs.ai/skills/structsd-install/SKILL)
- [Mid-game expansion playbook](https://structs.ai/playbooks/phases/mid-game)
- [Under-attack evacuation playbook](https://structs.ai/playbooks/situations/under-attack)

## Skill Output:

**Output Type(s):** [guidance, shell commands]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires structsd on PATH and a configured signing key for executable command examples.]

## Skill Version(s):

1.25.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
