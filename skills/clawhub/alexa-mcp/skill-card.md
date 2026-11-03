## Description:

Helps an agent manage Amazon Alexa and Echo devices, smart home controls, routines, reminders, alarms, timers, and household lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users can ask an agent to check Alexa and Echo device state or manage smart-home settings, media, routines, reminders, alarms, and household lists. The agent presents previews and requests approval before changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Smart-home changes, especially unlocking doors or opening garage doors, can affect household safety and security.

Mitigation: Review the action preview and explicitly approve changes; use a trusted Alexa MCP server and verify that the server enforces confirmation before proceeding.

Risk: The Amazon login callback may contain authentication information.

Mitigation: Share the callback only through the trusted login flow and never request or share the Amazon password outside amazon.com.

## Reference(s):

- [Alexa MCP on ClawHub](https://clawhub.ai/chrischall/skills/alexa-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance, API Calls]

**Output Format:** [Natural-language responses and Alexa MCP tool requests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include device state, action previews, and confirmation requests.]

## Skill Version(s):

0.3.4 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
