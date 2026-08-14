## Description:

Control a real phone from OpenClaw through a local MCP relay to open apps, tap, input text, take screenshots, inspect device status, run mobile automation tasks, or query and abort phone agent tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mobileaiuse](https://clawhub.ai/user/mobileaiuse)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate a connected Android or iPhone device from OpenClaw, including read-only inspection and supervised mobile automation tasks. It is intended for workflows where the user can monitor and approve high-impact actions on a real device.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate a real phone and may send messages, make purchases, delete data, or change settings.

Mitigation: Use it only with an intended device connection, supervise first runs, and require explicit user approval before messages, payments, deletions, or settings changes.

Risk: Ambiguous goals can cause unintended device actions during multi-step automation.

Mitigation: Ask the user to confirm a precise task scope before invoking automation and prefer read-only screenshot or device-status checks before write actions.

Risk: A failed financial or irreversible action could be retried without enough context.

Mitigation: Do not retry financial transactions or irreversible tasks unless the user gives fresh explicit confirmation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mobileaiuse/skills/phone-agent)
- [Mobile AI Agent page](https://mobile-ai-use.com/mobileAi)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or invoke phone-control workflows that can modify real device state when connected through the configured MCP relay.]

## Skill Version(s):

0.1.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
