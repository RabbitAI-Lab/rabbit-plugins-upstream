## Description:

Reads and controls a user's iAquaLink pool or spa, including temperatures, pumps, heaters, lighting, chlorination, schedules, and scenes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Pool and spa owners use this skill to check their own system's status and request confirmed changes to equipment, temperature, lighting, chlorination, schedules, and scenes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Equipment, heater, chlorinator, scene, or schedule changes can affect a physical pool or spa.

Mitigation: Review the proposed change and obtain the owner's explicit confirmation before applying it.

Risk: Deleting a panel schedule has no undo.

Mitigation: List and identify the exact schedule first, then review the deletion preview before confirming.

Risk: A write may be unconfirmed, and retrying toggle commands can reverse the intended state.

Mitigation: Report unconfirmed results plainly, check status again later, and avoid blind retries.

## Reference(s):

- [iAqualink on ClawHub](https://clawhub.ai/chrischall/skills/iaqualink)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports status and confirmation previews; distinguishes confirmed changes from changes awaiting verification.]

## Skill Version(s):

0.2.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
