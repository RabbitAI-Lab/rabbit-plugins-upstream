## Description:

Safely send, inspect, and diagnose personal iPhone notifications through Pushman MCP tools or the installed Pushman CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[whitekiwi](https://clawhub.ai/user/whitekiwi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to send intentional notifications to their own iPhone devices, inspect Pushman account state, review usage and history, and diagnose local Pushman MCP or CLI setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Notification sends are visible to the user and consume Pushman send allowance.

Mitigation: Require explicit send intent for each notification, preserve the requested scope, and do not retry ambiguous sends without a new user request.

Risk: Device, history, message, URL, and credential details are private user data.

Mitigation: Retrieve only the narrow state needed for the task and avoid exposing notification content, device nicknames, tokens, or credential values in summaries, logs, examples, or configuration.

Risk: Authorization, pairing, logout, and rename operations can change local Pushman account access.

Mitigation: Run credential or account mutations only when explicitly requested and verify resulting status after changes.

## Reference(s):

- [Pushman safety model](references/safety.md)
- [Pushman CLI installation guide](https://github.com/WhiteKiwi/pushman-cli/blob/main/docs/INSTALL.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with tool calls or inline shell commands when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report server acceptance IDs, target counts, usage facts, diagnostic results, and configuration steps while avoiding unnecessary disclosure of private notification content, device names, URLs, or credentials.]

## Skill Version(s):

0.5.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
