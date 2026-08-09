## Description:

Control a real phone from OpenClaw via a local MCP relay for app actions, taps, text input, screenshots, device status checks, and phone automation tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mobileaiuse](https://clawhub.ai/user/mobileaiuse)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to connect OpenClaw to a local MCP relay and operate a connected Android or iPhone device through natural-language tasks, screenshots, device-status queries, and task result checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give an agent broad control over a connected phone and visibility into the current phone screen.

Mitigation: Use it only with a reviewed MCP server and website, avoid sensitive personal or work devices, and keep the phone screen visible while tasks run.

Risk: Phone automation could send messages, make purchases, change settings, or perform account actions if given an unsafe goal.

Mitigation: Require explicit human approval before messages, purchases, settings changes, or account actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mobileaiuse/skills/mobile-agent)
- [Mobile AI Agent page](https://mobile-ai-use.xyz/mobileAi)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON-style configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide MCP tool calls that return screenshots, device status, task status, and task results from a connected phone.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
