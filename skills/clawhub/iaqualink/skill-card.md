## Description:

Helps users check and control their iAquaLink pool or spa equipment, temperatures, chemistry, schedules, and scenes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Pool and spa owners use this skill to check system status and request changes to equipment, heating, lights, chlorination, schedules, and scenes through their iAquaLink account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Changes to heaters, pumps, chlorinator output, and scenes affect physical pool or spa equipment.

Mitigation: Review the proposed change and obtain explicit user confirmation before each write.

Risk: Schedule deletion or timer changes can persist on the pool controller; deletion has no undo.

Mitigation: Review the current schedule and the proposed changes before confirming a write, especially deletion.

Risk: Some changes may not be visible immediately after the system accepts them.

Mitigation: Report unconfirmed changes accurately and check status later rather than blindly retrying.

## Reference(s):

- [iAqualink ClawHub skill listing](https://clawhub.ai/chrischall/skills/iaqualink)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports whether requested equipment changes are confirmed or still unconfirmed.]

## Skill Version(s):

0.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
