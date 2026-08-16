## Description:

Controls a real phone from OpenClaw through a local MCP relay for screenshots, device status, app interaction, text input, and multi-step mobile automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mobileaiuse](https://clawhub.ai/user/mobileaiuse)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill when they need an agent to inspect or operate a connected phone, including screenshots, device information, app navigation, text entry, task execution, and task aborts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify physical phone state, including messages, purchases, deletions, and settings changes.

Mitigation: Require explicit confirmation before high-impact actions, prefer screenshot and device-status checks first, and supervise execution on the phone.

Risk: The local MCP server and external web page used by the workflow were not included in the artifact evidence.

Mitigation: Review the local MCP server and external page before deployment, and install only when the user intends to permit phone operation.

## Reference(s):

- [Mobile AI Agent Page](https://mobile-ai-use.xyz/mobileAi)
- [ClawHub Skill Page](https://clawhub.ai/mobileaiuse/skills/mobile-agent)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON-style configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can invoke phone-control tools that return screenshots, device status, task results, or task-control responses.]

## Skill Version(s):

0.1.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
