## Description:

Control a real phone from OpenClaw via a local MCP relay for app operation, screenshots, device status checks, and phone automation tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mobileaiuse](https://clawhub.ai/user/mobileaiuse)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent operate a connected Android or iPhone through a local relay, including opening apps, tapping, entering text, taking screenshots, checking device status, and managing phone automation tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can let an agent perform broad real-world actions on a connected phone.

Mitigation: Use it only with devices and apps the user is comfortable allowing an agent to operate, and require explicit confirmation before messages, purchases, account changes, settings changes, deletions, or other irreversible actions.

Risk: The referenced MCP server code is not included in the reviewed artifact.

Mitigation: Verify the MCP server implementation and dependencies before running it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mobileaiuse/skills/phone-agent)
- [Mobile AI Agent page](https://mobile-ai-use.com/mobileAi)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON-style configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include phone-control task guidance, tool names, setup steps, and troubleshooting instructions.]

## Skill Version(s):

0.1.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
