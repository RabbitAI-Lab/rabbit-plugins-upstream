## Description:

Builds and manages Structs game buildings, including construction decisions, activation and deactivation, Command Ship movement, defense assignment, stealth, generator infusion, and build-time planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[abstrct](https://clawhub.ai/user/abstrct)

### License/Terms of Use:

MIT-0

## Use Case:

External players and developers use this skill to plan Structs building operations and prepare safe structsd commands for construction, movement, defense, stealth, activation, and generator infusion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Irreversible actions such as trash and generator infusion can permanently destroy a struct or convert Alpha Matter.

Mitigation: Require explicit approval after checking the signer, struct ID, amount, power budget, and defense posture before proposing these transactions.

Risk: Background build-compute jobs may complete and auto-activate later after game state has changed.

Mitigation: Confirm the struct ID and power headroom before starting the job, then query chain state after completion instead of treating broadcast as success.

Risk: Power or charge shortfalls can cause transactions to fail or leave a built struct offline.

Mitigation: Run the documented power-budget and state queries before proposing build, activation, movement, defense, stealth, or infusion commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/abstrct/skills/structs-building)
- [Structs conventions](https://structs.ai/skills/conventions)
- [Struct types catalog](https://structs.ai/knowledge/entities/struct-types)
- [Building mechanics](https://structs.ai/knowledge/mechanics/building)
- [Hashing mechanics](https://structs.ai/knowledge/mechanics/hashing#worked-example-fresh-vs-aged-anchor)
- [Structs energy](https://structs.ai/skills/structs-energy/SKILL)
- [Structs combat](https://structs.ai/skills/structs-combat/SKILL)
- [structsd install](https://structs.ai/skills/structsd-install/SKILL)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and command tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires structsd on PATH and a signing key; includes transaction approval checks and background compute instructions.]

## Skill Version(s):

1.25.0 (source: server release evidence and target metadata; artifact/_meta.json reports 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
