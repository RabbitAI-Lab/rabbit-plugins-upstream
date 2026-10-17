## Description:

Checks and controls a user's iAquaLink pool or spa equipment, including temperatures, pumps, heaters, lights, chlorination, schedules, and scenes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Pool and spa owners use this skill to check equipment status and, with explicit confirmation, adjust their own iAquaLink systems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Equipment or schedule changes can affect pool and spa operation; deleted schedules cannot be undone.

Mitigation: Review the proposed change and obtain explicit owner confirmation before acting, especially for heaters, pumps, chlorinators, schedules, and scenes.

Risk: A change reported as sent-unconfirmed may not have taken effect, and repeating toggle commands can reverse equipment state.

Mitigation: Disclose the uncertainty, recheck status later, and do not blindly retry a toggle.

Risk: Some iAqua write operations and eXO support have not been exercised on live hardware.

Mitigation: Treat unverified write results cautiously and confirm the equipment state before reporting success.

## Reference(s):

- [iaqualink on ClawHub](https://clawhub.ai/chrischall/skills/iaqualink)
- [Publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports equipment readings, change previews, confirmation outcomes, and unconfirmed changes.]

## Skill Version(s):

0.2.1 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
