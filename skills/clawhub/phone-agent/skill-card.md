## Description:

Control a real phone from OpenClaw via a local MCP relay for phone operations, screenshots, device status checks, and running or aborting phone automation tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mobileaiuse](https://clawhub.ai/user/mobileaiuse)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an OpenClaw agent inspect and operate a connected Android or iPhone device through a local relay. It is intended for tasks such as opening apps, tapping, entering text, taking screenshots, checking device status, and managing running phone-agent tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate a real phone and may affect private data, accounts, settings, messages, purchases, app installs, or other sensitive actions.

Mitigation: Use it only with devices and accounts approved for agent control, review the current screen and intended action before sensitive operations, and require explicit human confirmation for messages, purchases, settings changes, account actions, app installs, or data exposure.

Risk: The local relay grants broad phone-control capability while it is connected.

Mitigation: Keep the relay local, expose only the required port, disconnect the device or stop the relay when work is complete, and avoid leaving unattended automation running.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mobileaiuse/skills/phone-agent)
- [Server-resolved GitHub provenance](https://github.com/MobileAiUse/skills/tree/main/phone-agent)
- [Mobile AI Agent page](https://mobile-ai-use.com/mobileAi)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON-style configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include phone screenshots or task-result summaries returned by the connected MCP tools.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
