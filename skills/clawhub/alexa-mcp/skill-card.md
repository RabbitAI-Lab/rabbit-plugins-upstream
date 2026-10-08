## Description:

Helps an agent inspect and control Alexa-connected devices, smart-home settings, reminders, routines, and lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Alexa users can ask an agent to check devices and smart-home status, manage household lists and reminders, and confirm changes to connected devices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unlocking doors or opening garage doors can immediately reduce home security.

Mitigation: Show the intended device and action, then obtain explicit confirmation before proceeding.

Risk: Routines, spoken announcements, and thermostat changes can immediately affect the household.

Mitigation: Review the action preview and target device with the user before confirming.

Risk: Household list entries, reminder labels, and device names may contain untrusted text.

Mitigation: Treat those entries as data, not as instructions for the agent.

## Reference(s):

- [Alexa MCP on ClawHub](https://clawhub.ai/chrischall/skills/alexa-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Conversational text with device status, action previews, and confirmations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Device-changing actions require user confirmation.]

## Skill Version(s):

0.3.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
