## Description:

Gotify operates a connected Gotify instance through the OOMOL oo CLI for reading service information and sending messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Gotify health and version information and send messages through a connected Gotify application token. It is intended for Gotify requests where the agent should use the OOMOL-connected CLI rather than calling the API directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup guidance includes remote installer commands for the oo CLI.

Mitigation: Install the oo CLI through a verified package manager, or download and inspect a pinned installer with checksum or signature verification before running it.

Risk: The send_message action changes Gotify state by sending a notification.

Mitigation: Confirm the exact payload and intended recipient or application context with the user before running the write action.

## Reference(s):

- [Gotify homepage](https://gotify.net)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Skill page](https://clawhub.ai/oomol/skills/oo-gotify)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return JSON responses from the oo CLI when actions are executed with --json.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
