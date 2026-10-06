## Description:

Lets an OpenClaw agent query and control a user's Home Assistant devices, automations, and cameras through natural-language requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nj070574-gif](https://clawhub.ai/user/nj070574-gif)

### License/Terms of Use:

MIT-0

## Use Case:

Home Assistant owners use this skill to check device status and energy usage, control lights and climate, run automations, and view camera snapshots through an OpenClaw agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Device controls and automations can affect physical safety and security.

Mitigation: Use a dedicated least-privilege Home Assistant account, confirm changes before execution, and leave lock and alarm control disabled unless necessary.

Risk: Notifications can be sent without the confirmation gate used for other actions.

Mitigation: Require explicit user approval before sending a notification; do not assume the skill enforces confirmation for it.

Risk: Home Assistant tokens and camera snapshots expose sensitive household information.

Mitigation: Prefer HTTPS, keep tokens and snapshots private, and use plain HTTP only on a trusted LAN when explicitly necessary.

## Reference(s):

- [Home Assistant Integration on ClawHub](https://clawhub.ai/nj070574-gif/skills/home-assistant-skill)

## Skill Output:

**Output Type(s):** [Text, Images]

**Output Format:** [Plain text or Markdown responses; camera snapshots as image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may reveal sensitive home state, occupancy, or camera imagery.]

## Skill Version(s):

2.5.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
