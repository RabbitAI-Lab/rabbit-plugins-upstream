## Description:

Inventories installed agent skills, estimates their context cost, and suggests conservative categories for reviewing which skills to keep or disable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elisabeth15501](https://clawhub.ai/user/elisabeth15501)

### License/Terms of Use:

MIT-0

## Use Case:

Agent users and administrators review installed skills, estimated context use, duplicate candidates, and dependencies before deciding whether to disable a skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Applying a proposed disable list can persistently turn off skills needed by the agent.

Mitigation: Review the impact preview and backup path before explicitly confirming --overrides --apply --yes.

Risk: An overly broad skills directory can expose unrelated local files to the inventory scan.

Mitigation: Point --root or --probe only at the intended skills directory.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/elisabeth15501/skills/skill-inventory)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Terminal report or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only by default; JSON keys remain in English, and report language can be selected.]

## Skill Version(s):

1.5.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
