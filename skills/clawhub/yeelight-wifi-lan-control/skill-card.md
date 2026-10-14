## Description:

Helps an agent discover, control, and organize Yeelight WiFi lights over the local network, including scenes and host-managed schedules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yeelight](https://clawhub.ai/user/yeelight)

### License/Terms of Use:

MIT-0

## Use Case:

People with Yeelight WiFi lights use this skill to find and control lights on their LAN, organize rooms and groups, apply scenes, and prepare schedules for a host scheduler.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A mistaken command can change the physical state of selected lights.

Mitigation: Confirm the intended targets and action before requesting execution; review reported device outcomes.

Risk: Scene changes across multiple lights may complete only partially or have an uncertain outcome.

Mitigation: Check each reported result and fresh device state; request recovery only after explicit confirmation.

Risk: Local scenes, schedules, and home metadata persist on disk, and music mode briefly opens a local listener.

Mitigation: Use the skill only on a trusted local network and approve persistent changes or music mode when needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yeelight/skills/yeelight-wifi-lan-control)
- [Yeelight WiFi Light Inter-Operation Specification](https://www.yeelight.com/download/Yeelight_Inter-Operation_Spec.pdf)
- [Local home organization](references/local-home.md)
- [Scenes and recovery](references/scenes.md)
- [Host scheduling](references/scheduling.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports per-device outcomes and next actions; physical changes require an explicit execution request.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
