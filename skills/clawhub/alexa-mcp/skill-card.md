## Description:

Guides an agent in viewing and controlling Alexa-connected devices, smart-home equipment, reminders, routines, and lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Alexa users can ask an agent to check devices and smart-home status, change settings, manage reminders and lists, or run routines with confirmation before changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unlocking a door or opening a garage reduces home security.

Mitigation: Show the proposed action and obtain explicit user confirmation before proceeding.

Risk: An unauthorized login flow could expose Amazon credentials.

Mitigation: Use the Amazon sign-in flow only through amazon.com; never request the user's password.

## Reference(s):

- [Alexa MCP skill on ClawHub](https://clawhub.ai/chrischall/skills/alexa-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include device status and previews requiring user confirmation before changes.]

## Skill Version(s):

0.3.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
